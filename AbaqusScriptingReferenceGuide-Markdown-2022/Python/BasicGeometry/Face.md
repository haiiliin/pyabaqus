# Face object

Faces are two-dimensional regions of geometry.

## Access

```
import part
mdb.models[name].parts[name].allInternalSets[name].faces[i]
mdb.models[name].parts[name].allInternalSurfaces[name].faces[i]
mdb.models[name].parts[name].allSets[name].faces[i]
mdb.models[name].parts[name].allSurfaces[name].faces[i]
mdb.models[name].parts[name].faces[i]
mdb.models[name].parts[name].sets[name].faces[i]
mdb.models[name].parts[name].surfaces[name].faces[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].faces[i]
mdb.models[name].rootAssembly.allInstances[name].sets[name].faces[i]
mdb.models[name].rootAssembly.allInstances[name].surfaces[name].faces[i]
mdb.models[name].rootAssembly.allInternalSets[name].faces[i]
mdb.models[name].rootAssembly.allInternalSurfaces[name].faces[i]
mdb.models[name].rootAssembly.allSets[name].faces[i]
mdb.models[name].rootAssembly.allSurfaces[name].faces[i]
mdb.models[name].rootAssembly.instances[name].faces[i]
mdb.models[name].rootAssembly.instances[name].sets[name].faces[i]
mdb.models[name].rootAssembly.instances[name].surfaces[name].faces[i]
mdb.models[name].rootAssembly.modelInstances[i].sets[name].faces[i]
mdb.models[name].rootAssembly.modelInstances[i].surfaces[name]\
.faces[i]
mdb.models[name].rootAssembly.sets[name].faces[i]
mdb.models[name].rootAssembly.surfaces[name].faces[i]
```

## getCentroid()



This method returns the centroid of a face.



### Arguments

None.

### Return value

A sequence of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the centroid of the face.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getCurvature(...)



This method returns information about the curvature at a location on the face.



### Required arguments

- *point*

  A tuple specifying the *X*-, *Y*-, and *Z* coordinates of the point where the curvature is desired. If the *point* does not lie on the face it will be projected onto the face. This argument and *uParam* and *vParam* are mutually exclusive.

- *uParam*

  A Float specifying the normalized *U* parameter value at which the curvature is to be computed. This value must lie between (0,1). *vParam* must also be specified. This argument is mutually exclusive with *point*.

- *vParam*

  A Float specifying the normalized *V* parameter value at which the curvature is to be computed. This value must lie between (0,1).

### Optional arguments

None.

### Return value

A dictionary with keys 'evaluationPoint', 'principalAxis1', 'principalAxis2', 'curvature1', 'curvature2' and 'gaussianCurvature'. Where the evaluationPoint specifies the location at which the curvature was evaluated. 'principalAxis1' and 'principalAxis2' refer to the vectors specifying the two principal axes of the face. 'curvature1' and 'curvature2' specify the curvatures along the two principal axes.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getElements()



This method returns an array of element objects that are associated with the face.



### Arguments

None.

### Return value

A [MeshElementArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object which is a sequence of [MeshElement](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getElementFaces(...)



This method returns an array of mesh face objects. Each mesh face object contains the element label and the side of the element that lies on the geometric face.



### Required arguments

None.

### Optional arguments

- *faceSide*

  A symbolic constant specifying the side of the geometric face of a solid from which the element faces should be retrieved. Possible values are *SIDE1*, *SIDE2*, and *BOTH_SIDES*. The default value is *BOTH_SIDES*. For shell faces this option is ignored.

### Return value

A [MeshFaceArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object which is a sequence of [MeshFace](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getNodes(...)



This method returns an array of mesh node objects. Each mesh node object contains the label of the node that lies on the geometric face.



### Required arguments

None.

### Optional arguments

- *faceSide*

  A symbolic constant specifying the side of the geometric face of a solid from which the nodes should be retrieved. Possible values are xo*SIDE1*, *SIDE2*, and *BOTH_SIDES*. The default value is *BOTH_SIDES*. For shell faces and for faces with compatible meshes on either sides this option is ignored. Otherwise, the nodes on the specified side(s) of the face are output.

### Return value

A [MeshNodeArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object which is a sequence of [MeshNode](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getNormal(...)



This method returns the normal to a face at the location specified by the *pointOn* member. The normal at a different location on the face can be obtained by specifying the optional *point* argument.



### Required arguments

None.

### Optional arguments

- *point*

  A tuple specifying the *X*-, *Y*-, and *Z* coordinates of the point where the normal to the face is desired. If the *point* does not lie on the face it will be projected onto the face.

### Return value

A sequence of Floats specifying the *X*-, *Y*-, and *Z*-components of the normal to the face.

### Exceptions

An exception is raised if the optional argument *point* is provided but the point cannot be projected onto the face.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getSize(...)



This method returns a Float indicating the area of the face.



### Required arguments

None.

### Optional arguments

- *printResults*

  A Bool specifying whether verbose output is printed. The default value is True.

### Return value

A Float.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getEdges()



This method returns a sequence consisting of the edge ids of the edges on the face.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getVertices()



This method returns a sequence consisting of the vertex ids of the vertices of the face.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getCells()



This method returns a sequence consisting of the cell ids of the cells to which this face belongs.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getAdjacentFaces()



This method returns an array of face objects that share at least one edge of the face.



### Arguments

None.

### Return value

A [FaceArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object which is a sequence of Face objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getFacesByFaceAngle(...)



This method returns an array of Face objects that are obtained by recursively finding adjacent faces that are at an angle of less than or equal to the specified angle.



### Required arguments

- *angle*

  A float specifying the value of the face angle.

### Optional arguments

None.

### Return value

A [FaceArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object, which is a sequence of Face objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getFacesByCurvature()



This method returns an array of Face objects that are obtained by recursively finding adjacent faces that share the same curvature.



### Arguments

None.

### Return value

A [FaceArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object, which is a sequence of Face objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## isNormalFlipped()



This method determines whether the normal to the face is flipped from its default direction by the use of the flipNormal method on a Part object.



### Arguments

None.

### Return value

A Boolean value of True if the normal is flipped and False if not.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getCADAttributes(...)



This method returns an array of CAD attribute strings associated with the Face when the part was created from CAD data.



### Arguments

None.

### Return value

An array of String

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The Face object has the following members:

- *index*

  An Int specifying the index of the face in the FaceArray.

- *isReferenceRep*

  A Boolean specifying whether the face belongs to the reference representation of the Part or Instance.

- *pointOn*

  A tuple of tuples of Floats specifying the coordinates. For a face of a shell *pointOn* specifies the *X*-, *Y*-, and *Z*-coordinates of a point located on the face and the *X*-, *Y*-, and *Z*-components of the normal to the face.For a face of a solid *pointOn* specifies the *X*-, *Y*-, and *Z*-coordinates of a point located on the face.

- *featureName*

  A tuple of Floats specifying the name of the feature that created this face.

- *instanceName*

  A tuple of Floats specifying the name of the part instance for this face (if applicable).