# MeshFaceArray object

The MeshFaceArray is a sequence of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects.

## Access

```
import part
mdb.models[name].parts[name].elementFaces
import assembly
mdb.models[name].rootAssembly.allInstances[name].elementFaces
mdb.models[name].rootAssembly.instances[name].elementFaces
```

## MeshFaceArray(...)



This method creates a MeshFaceArray object.



### Path

mesh.MeshFaceArray

### Required arguments

- *elemFaces*

  A list of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects.

### Optional arguments

None.

### Return value

A MeshFaceArray object.

### Exceptions

None.



## getSequenceFromMask(...)



This method returns the objects in the MeshFaceArray identified using the specified *mask*. When large number of objects are involved, this method is highly efficient.



### Required arguments

- *mask*

  A String specifying the object or objects.

### Optional arguments

None.

### Return value

A MeshFaceArray object.

### Exceptions

- An exception occurs if the resulting sequence is empty.

  Error: The mask results in an empty sequence



## getMask()



This method returns a string specifying the object or objects.



### Arguments

None.

### Return value

A String specifying the object or objects.

### Exceptions

None.



## Members

The MeshFaceArray object has no members.