import vrep

emptyBuff = bytearray()

class cmdWrapper():
    def __init__(self, clientID, objectName, scriptType):
        self.clientID = clientID
        self.objectName = objectName
        self.scriptType = scriptType

    def createPureShape(self, primitiveType, options, sizes, mass):
        '''Creates a pure primitive shape.
        PARAMETERS
        primitiveType: 0 for a cuboid, 1 for a sphere, 2 for a cylinder and 3 for a cone
        options: Bit-coded: if bit0 is set (1), backfaces are culled. If bit1 is set (2), edges are visible. If bit2 is set (4), the shape appears smooth. If bit3 is set (8), the shape is respondable. If bit4 is set (16), the shape is static. If bit5 is set (32), the cylinder has open ends
        sizes: 3 values indicating the size of the shape
        mass: the mass of the shape
    
        RETURN
        -1 if operation was not successful, otherwise the handle of the newly created shape
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'createPureShape',
            [primitiveType, options], [*sizes, mass], [], emptyBuff, vrep.simx_opmode_blocking)
        return res, retInts[0]
    
    def setObjectName(self, objectHandle, objectName):
        '''Sets the name of an object based on its handle.
        PARAMETERS
        objectHandle: handle of the object. By adding sim.handleflag_altname to the object handle, the object alternative name can be set. By adding sim.handleflag_silenterror to the object handle, errors linked to the naming can be suppressed from output.
        objectName: name (or alternative name) of the object
    
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setObjectName',
            [objectHandle], [], [objectName], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def setObjectParent(self, objectHandle, parentObjectHandle, keepInPlace):
        '''Sets the name of an object based on its handle.
        PARAMETERS
        objectHandle: handle of the object that will become child of the parent object. Can be combined with sim_handleflag_assembly (simply add sim_handleflag_assembly to objectHandle), if the two objects can be assembled via a predefined assembly transformation (refer to the assembling option in the object common properties). In that case, parentObjectHandle can't be -1, and keepInPlace should be set to false.
        parentObjectHandle: handle of the object that will become parent, or -1 if the object should become parentless.
        keepInPlace: indicates whether the object's absolute position and orientation should stay same
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setObjectParent',
            [objectHandle, parentObjectHandle, keepInPlace], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def setObjectPosition(self, objectHandle, relativeToObjectHandle, position):
        '''Sets the position (x, y and z-coordinates) of an object.
        PARAMETERS
        objectHandle: handle of the object
        relativeToObjectHandle: indicates relative to which reference frame the position is specified. Specify -1 to set the absolute position, sim_handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified.
        position: coordinates of the object (x, y and z)
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setObjectPosition',
            [objectHandle, relativeToObjectHandle], [*position], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def setObjectOrientation(self, objectHandle, relativeToObjectHandle, orientation):
        '''Sets the orientation (Euler angles) of an object.
        PARAMETERS
        objectHandle: handle of the object
        relativeToObjectHandle: indicates relative to which reference frame the position is specified. Specify -1 to set the absolute position, sim_handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified.
        eulerAngles: Euler angles (alpha, beta and gamma)
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setObjectOrientation',
            [objectHandle, relativeToObjectHandle], [*orientation], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def setObjectQuaternion(self, objectHandle, relativeToObjectHandle, quaternion):
        '''Sets the quaternion (x,y,z,w) of an object.
        PARAMETERS
        objectHandle: handle of the object
        relativeToObjectHandle: indicates relative to which reference frame the position is specified. Specify -1 to set the absolute position, sim_handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified.
        quaternion: the quaternion (x,y,z,w)
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setObjectQuaternion',
            [objectHandle, relativeToObjectHandle], [*quaternion], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def setObjectInt32Parameter(self, objectHandle, parameterID, parameter):
        '''Sets an int32 parameter of a scene object or calculation object.
        PARAMETERS
        objectHandle: handle of the object
        parameterID: identifier of the parameter to retrieve. See the list of all possible object parameter identifiers
        parameter: parameter value
        RETURN
        -1 in case of an error, 0 if the parameter could not be set (e.g. because the parameterID doesn't exist, or because the specified object doesn't correspond to the correct type), or 1 if the operation was successful 
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setObjectInt32Parameter',
            [objectHandle, parameterID, parameter], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res

    def setObjectFloatParameter(self, objectHandle, parameterID, parameter):
        '''Sets an float parameter of a scene object or calculation object.
        PARAMETERS
        objectHandle: handle of the object
        parameterID: identifier of the parameter to retrieve. See the list of all possible object parameter identifiers
        parameter: parameter value
        RETURN
        -1 in case of an error, 0 if the parameter could not be set (e.g. because the parameterID doesn't exist, or because the specified object doesn't correspond to the correct type), or 1 if the operation was successful 
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setObjectFloatParameter',
            [objectHandle, parameterID], [parameter], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def getObjectFloatParameter(self, objectHandle, parameterID):
        '''Retrieves a floating point value.
        PARAMETERS
        objectHandle: handle of the object
        parameterID: identifier of the parameter to retrieve. See the list of all possible object parameter identifiers
        RETURN
        parameter value
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'getObjectFloatParameter',
            [objectHandle, parameterID], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res, retFloats[0]

    def resetDynamicObject(self, objectHandle):
        '''Dynamically resets an object that is dynamically simulated.
        PARAMETERS
        objectHandle: handle of the object or sim_handle_all (to reset all dynamic content in the scene). objectHandle can be combined with sim_handleflag_model, if you wish to reset all objects in a model (where objectHandle would be the model base).
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'resetDynamicObject',
            [objectHandle], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def createJoint(self, jointType, jointMode, options, sizes):
        '''Creates a pure primitive shape.
        PARAMETERS
        jointType: sim_joint_revolute_subtype, sim_joint_prismatic_subtype or sim_joint_spherical_subtype
        jointMode: a joint mode value
        options: bit-coded. For now only bit 0 is used (if set (1), the joint operates in hybrid mode)
        sizes: pointer to 2 values indicating the joint length and diameter. Can be NULL for default values
    
        RETURN
        -1 if operation was not successful, otherwise the handle of the joint
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'createJoint',
            [jointType, jointMode, options], [*sizes], [], emptyBuff, vrep.simx_opmode_blocking)
        return res, retInts[0]
    
    def createDummy(self, size):
        '''Creates a dummy. 
        PARAMETERS
        size: the dummy size
    
        RETURN
        -1 if operation was not successful, otherwise the handle of the dummy 
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'createDummy',
            [], [size], [], emptyBuff, vrep.simx_opmode_blocking)
        return res, retInts[0]
    
    def setLinkDummy(self, dummyHandle, linkedDummyHandle):
        '''Defines (or breaks) a dummy-dummy link pair. 
        PARAMETERS
        dummyHandle: handle of the first dummy in the dummy-dummy link pair.
        linkedDummyHandle: handle of the second dummy in the dummy-dummy link pair. Set to -1 to unlink the first dummy.
    
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setLinkDummy',
            [dummyHandle, linkedDummyHandle], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res

    def copyPasteObject(self, objectHandle, options):
        '''Copies and pastes an object
        PARAMETERS
        objectHandle: The handle of the object to copy and paste.
        options: bit-coded. If bit0 is set (i.e. 1), then whole models will be copied. In that case, all specified objects should be flagged as model base.. 
        RETURN
        -1 if operation was not successful, otherwise the handle of new object 
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'copyPasteObject',
            [objectHandle, options], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res, retInts[0]
    
    def getObjectHandle(self, objectName):
        '''Retrieves an object handle based on its name.
        PARAMETERS
        objectName: name of object
    
        RETURN
        handle of object or -1 if operation was not successful
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'getObjectHandle',
            [], [], [objectName], emptyBuff, vrep.simx_opmode_blocking)
        return res, retInts[0]

    def getObjectPosition(self, objectHandle, relativeToObjectHandle):
        '''Gets the position (x, y and z-coordinates) of an object.
        PARAMETERS
        objectHandle: handle of the object
        relativeToObjectHandle: indicates relative to which reference frame the position is specified. Specify -1 to set the absolute position, sim_handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified.
        RETURN
        position: coordinates of the object (x, y and z)
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'getObjectPosition',
            [objectHandle, relativeToObjectHandle], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res,retFloats
    
    def getObjectOrientation(self, objectHandle, relativeToObjectHandle):
        '''Retrieves the orientation (Euler angles) of an object.
        PARAMETERS
        objectHandle: handle of the object
        relativeToObjectHandle: indicates relative to which reference frame the position is specified. Specify -1 to set the absolute position, sim_handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified.
        RETURN
        eulerAngles: table of 3 values (Euler angles) or nil in case of an error
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'getObjectOrientation',
            [objectHandle, relativeToObjectHandle], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res,retFloats
    
    def getObjectQuaternion(self, objectHandle, relativeToObjectHandle):
        '''Retrieves the quaternion (x,y,z,w) of an object.
        PARAMETERS
        objectHandle: handle of the object
        relativeToObjectHandle: indicates relative to which reference frame the position is specified. Specify -1 to set the absolute position, sim_handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified.
        RETURN
        quaternion: the quaternion (x,y,z,w)
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'getObjectQuaternion',
            [objectHandle, relativeToObjectHandle], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res,retFloats
    
    def setJointPosition(self, objectHandle, position):
        '''Sets the intrinsic position of a joint.
        PARAMETERS
        objectHandle: handle of the object
        position: position of the joint (angular or linear value depending on the joint type)
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setJointPosition',
            [objectHandle], [position], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def setJointInterval(self, objectHandle, cyclic, interval):
        '''Sets the interval parameters of a joint (i.e. range values).
        PARAMETERS
        objectHandle: handle of the object
        cyclic: indicates whether the joint is cyclic. Only revolute joints with a pitch of 0 can be cyclic
        interval: interval of the joint. interval[0] is the joint minimum allowed value, interval[1] is the joint range (i.e. the maximum allowed value is interval[0]+interval[1])
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setJointInterval',
            [objectHandle, cyclic], interval, [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def groupShapes(self, shapeHandles):
        '''Groups (or merges) several shapes into a compound shape (or simple shape). 
        PARAMETERS
        shapeHandles: the handles of the shapes you wish to group
    
        RETURN
        -1 if operation was not successful. Otherwise the handle of the resulting compound shape.
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'groupShapes',
            shapeHandles, [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res, retInts[0]
    
    def setModelProperty(self, objectHandle, prop):
        '''Sets the properties of a model. 
        PARAMETERS
        objectHandle: handle of the object that serves as the model base
        prop: model property.
    
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setModelProperty',
            [objectHandle, prop], [], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
    
    def setMaterialFrict(self, objectHandle, frict):
        '''Sets the friction of a shape. 
        PARAMETERS
        objectHandle: handle of the object
        frict: friction value.
    
        RETURN
        -1 if operation was not successful. In a future release, a more differentiated return value might be available
        '''
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self.clientID, 
            self.objectName, vrep.sim_scripttype_customizationscript, 'setMaterialFrict',
            [objectHandle], [frict], [], emptyBuff, vrep.simx_opmode_blocking)
        return res
