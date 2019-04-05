import numpy as np
from scipy.integrate import odeint


def cpg(k,mu,stance,swing,b,alpha,beta,x0,t):
    '''
    Centrl Pattern Generator
    Based on the paper: Pattern generators with sensory feedback for the control of quadruped locomotion
    '''
    def model(x_,t):   
        x = x_.reshape((4,2))
        dxdt = np.empty_like(x)
        for i in range(4):
            r2 = x[i,0]*x[i,0] + x[i,1]*x[i,1]
            w = swing/(np.exp(-b*x[i,1])+1.) + stance/(np.exp(b*x[i,1])+1.)
            dxdt[i,0] = alpha*(mu-r2)*x[i,0] - w*x[i,1]
            couple = 0.
            for j in range(4):
                couple += k[i,j]*x[j,1];
            dxdt[i,1] = beta*(mu-r2)*x[i,1] + w*x[i,0] + couple
        return dxdt.flatten()    
    xs = odeint(model,x0,t)
    return xs.reshape((-1,4,2))


if __name__ == '__main__':
    import matplotlib as mpl
    import platform
    if platform.system()=="Linux":
        mpl.use('TkAgg')
    import matplotlib.pyplot as plt
    import sys

    if len(sys.argv)!=5:
        print("python cpg.py <gait type> <stance freq> <swing freq> <time>")
        sys.exit(-1)
    
    # coupling matrix
    k = np.zeros((4,4))
    if sys.argv[1] == "pace":
        k[0,2] = k[1,3] = k[2,0] = k[3,1] = 1.
        k[0,1] = k[1,0] = k[1,2] = k[2,1] = k[2,3] = k[3,0] = k[3,2] = -1.
    elif sys.argv[1] == "bound":
        k[0,1] = k[1,0] = k[2,3] = k[3,2] = 1.
        k[0,2] = k[0,3] = k[1,2] = k[1,3] = k[2,0] = k[2,1] = k[3,0] = k[3,1] = -1.
    elif sys.argv[1] == "walk":
        k[0,2] = k[1,3] = k[2,1] = k[3,0] = 1.
        k[0,1] = k[0,3] = k[1,0] = k[1,2] = k[2,0] = k[2,3] = k[3,1] = k[3,2] = -1.
    else:  #trot
        k[0,3] = k[1,2] = k[2,1] = k[3,0] = 1.
        k[0,1] = k[0,2] = k[1,0] = k[1,3] = k[2,0] = k[2,3] = k[3,1] = k[3,2] = -1.
   
    print(k)

    mu = 1.
    stance = np.pi*float(sys.argv[2])
    swing = np.pi*float(sys.argv[3])
    b = 50.
    alpha = 5.
    beta = 50.
    x0 = np.random.normal(0.,0.1,(4,2))
   
    # calculate cpg trajectorues
    secs = 10.0 + float(sys.argv[4])
    fs = 200
    t = np.linspace(0.,secs,secs*fs)
    xs = cpg(k,mu,stance,swing,b,alpha,beta,x0.flatten(),t)

    # seek the first x0 zero position after 10 secs then drop
    x0 = xs[10*fs:,0,0]
    idx = np.nonzero(abs(x0)<0.05)
    hipPos = xs[(10*fs+idx[0][0]):,:,0]
    kneePos = np.sign(np.diff(hipPos,axis=0))
    hipPos = hipPos[:-1,:]
    t = t[-hipPos.shape[0]:]
   
    # output csv
    with open("cpgdata.csv","w") as csv:
        for step in range(hipPos.shape[0]):
            csv.write("%f,%f,%f,%f,%f,%f,%f,%f,\n"%(
                hipPos[step][0],kneePos[step][0],
                hipPos[step][1],kneePos[step][1],
                hipPos[step][2],kneePos[step][2],
                hipPos[step][3],kneePos[step][3]))

    # plot results
    plt.plot(t,hipPos[:,0]+7.5,label="LF")
    plt.plot(t,hipPos[:,1]+5,label="RF")
    plt.plot(t,hipPos[:,2]+2.5,label="LH")
    plt.plot(t,hipPos[:,3],label="RH")
    plt.title(sys.argv[1])
    plt.xlabel('time (sec)')
    plt.ylabel('position (deg)')
    plt.legend()
    frame = plt.gca()
    frame.axes.get_yaxis().set_ticks([])
    plt.show()
