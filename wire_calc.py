import vrep
from cmdWrapper import cmdWrapper
import datetime
import time
import numpy as np
from scipy.spatial.transform import Rotation as R

if __name__ == '__main__':

    print('Program started')
    
    vrep.simxFinish(-1) # just in case, close all opened connections
    clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to V-REP
    if clientID!=-1:
        print('Connected to remote API server')
        vrep.simxAddStatusbarMessage(clientID,'Hello V-REP!  '+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            vrep.simx_opmode_blocking)
        
        cmd = cmdWrapper(clientID,'remoteApiServer', vrep.sim_scripttype_customizationscript)
        for d in ["lf","lh","rf","rh"]:
            _,h1 = cmd.getObjectHandle(d+'_wire_joint')
            _,h2 = cmd.getObjectHandle(d+'_wire_dummy')
            _,h3 = cmd.getObjectHandle(d+'_wire_dummy2')
            _,pos1 = cmd.getObjectPosition(h1,-1)
            pos1 = np.array(pos1).reshape((3,1))
            _,pos2 = cmd.getObjectPosition(h2,-1)
            pos2 = np.array(pos2).reshape((3,1))
            vec2 = pos2-pos1
            vec2 = vec2/np.linalg.norm(vec2)
            vec1 = np.array([0.,0.,1.]).reshape((3,1))
            dcm = 2*np.matmul((vec1+vec2),np.transpose(vec1+vec2))/np.matmul(np.transpose(vec1+vec2),(vec1+vec2))-np.eye(3)
            r = R.from_dcm(dcm)
            cmd.setObjectQuaternion(h1,-1,r.as_quat())
            cmd.setObjectQuaternion(h2,-1,r.as_quat())
            cmd.setObjectQuaternion(h3,-1,r.as_quat())
        
        # Now close the connection to V-REP:
        vrep.simxFinish(clientID)
    else:
        print ('Failed connecting to remote API server')
    
    print('Program ended')
