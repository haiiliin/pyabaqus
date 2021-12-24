# MeshFace object

The MeshFace object refers to an element face. It has no constructor or members. A MeshFace object can be accessed via a [MeshFaceArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) or a repository on a part or part instance.

## Access

```
import part
mdb.models[name].parts[name].elementFaces[i]
mdb.models[name].parts[name].elemFaces[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].elementFaces[i]
mdb.models[name].rootAssembly.allInstances[name].elemFaces[i]
mdb.models[name].rootAssembly.instances[name].elementFaces[i]
mdb.models[name].rootAssembly.instances[name].elemFaces[i]
```

## getElemEdges()



This method returns a tuple of unique element edges on the element face.



### Arguments

None.

### Return value

A tuple of [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getElements()



This method returns a tuple of elements that share the element face.



### Arguments

None.

### Return value

A tuple of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getNodes()



This method returns a tuple of nodes on the element face.



### Arguments

None.

### Return value

A tuple of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getNodesByFaceAngle(...)



This method returns an array of mesh node objects that are obtained by recursively finding adjacent element faces that are at an angle of less than or equal to the specified angle.



### Required arguments

- *angle*

  A float specifying the value of the face angle.

### Optional arguments

None.

### Return value

A [MeshNodeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object, which is a sequence of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getNormal(...)



This method returns the normal direction for the element face.



### Required arguments

None.

### Optional arguments

None.

### Return value

A tuple of 3 floats representing the unit normal vector. If the element face is collapsed such that a normal cannot be computed, a zero-length vector is returned.

### Exceptions

None.



## getElemFacesByFaceAngle(...)



This method returns an array of element face objects that are obtained by recursively finding adjacent element faces that are at an angle of less than or equal to the specified angle.



### Required arguments

- *angle*

  A float specifying the value of the face angle.

### Optional arguments

None.

### Return value

A [MeshFaceArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object, which is a sequence of MeshFace objects.

### Exceptions

None.



## getElemEdgesByFaceAngle(...)



This method returns an array of element edge objects that are obtained by recursively finding adjacent element edges that are at an angle of less than or equal to the specified face angle.



### Required arguments

- *angle*

  A float specifying the value of the face angle in degrees.

### Optional arguments

None.

### Return value

A [MeshEdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object, which is a sequence of [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getElementsByFaceAngle(...)



This method returns an array of mesh Element objects that are obtained by recursively finding adjacent element faces that are at an angle of less than or equal to the specified angle.



### Required arguments

- *angle*

  A float specifying the value of the face angle.

### Optional arguments

None.

### Return value

A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object, which is a sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getElemFacesByLimitingAngle(...)



This method returns an array of element edge objects that are obtained by recursively finding adjacent element faces that are at an angle of less than or equal to the specified face angle with the seed face.



### Required arguments

- *angle*

  A float specifying the value of the face angle in degrees.

### Optional arguments

None.

### Return value

A [MeshFaceArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object, which is a sequence of MeshFace objects.

### Exceptions

None.



## getElementsViaTopology()



This method returns an array of mesh Element objects that are obtained by recursively finding adjacent elements via topology.



### Arguments

None.

### Return value

A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object, which is a sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getElemFacesByLayer()



This method returns an array of element face objects, obtained by traversing shell elements or the exterior of a solid mesh, and recursively finding adjacent element faces by layer.



### Required arguments

- *numLayers*

  A int specifying the value of the number of layers.

### Optional arguments

None.

### Return value

A [MeshFaceArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object, which is a sequence of MeshFace objects.

### Exceptions

None.



## Members

The MeshFace object has the following members:

- *label*

  An Int specifying an Int specifying the element label.

- *face*

  An Int specifying a symbolic constant specifying the side of the element.