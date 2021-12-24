# Edge object

Edges are one-dimensional regions of geometry.

## Access

```
import part
mdb.models[name].parts[name].allInternalSets[name].edges[i]
mdb.models[name].parts[name].allInternalSurfaces[name].edges[i]
mdb.models[name].parts[name].allSets[name].edges[i]
mdb.models[name].parts[name].allSurfaces[name].edges[i]
mdb.models[name].parts[name].edges[i]
mdb.models[name].parts[name].sets[name].edges[i]
mdb.models[name].parts[name].surfaces[name].edges[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].edges[i]
mdb.models[name].rootAssembly.allInstances[name].sets[name].edges[i]
mdb.models[name].rootAssembly.allInstances[name].surfaces[name].edges[i]
mdb.models[name].rootAssembly.allInternalSets[name].edges[i]
mdb.models[name].rootAssembly.allInternalSurfaces[name].edges[i]
mdb.models[name].rootAssembly.allSets[name].edges[i]
mdb.models[name].rootAssembly.allSurfaces[name].edges[i]
mdb.models[name].rootAssembly.edges[i]
mdb.models[name].rootAssembly.instances[name].edges[i]
mdb.models[name].rootAssembly.instances[name].sets[name].edges[i]
mdb.models[name].rootAssembly.instances[name].surfaces[name].edges[i]
mdb.models[name].rootAssembly.modelInstances[i].edges[i]
mdb.models[name].rootAssembly.modelInstances[i].sets[name].edges[i]
mdb.models[name].rootAssembly.modelInstances[i].surfaces[name]\
.edges[i]
mdb.models[name].rootAssembly.sets[name].edges[i]
mdb.models[name].rootAssembly.surfaces[name].edges[i]
```

## isTangentFlipped()



This method determines whether the tangent to the edge is flipped from its default direction by the use of the flipTangent method on a Part object.



### Arguments

None.

### Return value

A Boolean value of True if the tangent is flipped and False if not.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getCurvature(...)



This method returns curvature information at a location on the edge.



### Required arguments

- *parameter*

  A Float specifying the normalized parameter location on the edge where the curvature is to be computed. This argument is mutually exclusive with the argument *point*.

- *point*

  A tuple of *X*-, *Y*-, and *Z*-coordinates of a point at which the curvature is to be computed. If *point* does not lie on the edge an attempt is made to project it onto the edge and use the projected point.

### Optional arguments

None.

### Return value

A dictionary with keys 'evaluationPoint', 'curvature', 'radius', and 'tangent', where 'evaluationPoint' specifies the location at which the curvature was computed; 'curvature' specifies the curvature vector at that location; 'radius' is the radius of curvature; and 'tangent' specifies the tangent to the edge at that location.

### Exceptions

The given edge is straight.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getFaces()



This method returns a sequence consisting of the face ids of the faces which share this edge.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getAdjacentEdges()



This method returns an array of Edge objects that share at least one vertex of the edge.



### Arguments

None.

### Return value

An [EdgeArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object, which is a sequence of Edge objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getEdgesByEdgeAngle(...)



This method returns an array of Edge objects that are obtained by recursively finding adjacent edges that are at an angle of less than or equal to the specified face angle.



### Required arguments

- *angle*

  A float specifying the value of the face angle in degrees.

### Optional arguments

None.

### Return value

An [EdgeArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object, which is a sequence of Edgeobjects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getNodes()



This method returns an array of node objects that are associated with the edge.



### Arguments

None.

### Return value

A [MeshNodeArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object, which is a sequence of [MeshNode](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getElements()



This method returns an array of element objects that are associated with the edge.



### Arguments

None.

### Return value

A [MeshElementArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object which is a sequence of [MeshElement](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getRadius()



This method returns the radius of circular edges.



### Arguments

None.

### Return value

A Float specifying the radius.

### Exceptions

The given edges is not circular.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getSize(...)



This method returns a Float indicating the length of the edge.



### Required arguments

None.

### Optional arguments

- *printResults*

  A Bool specifying whether verbose output is printed. The default is True.

### Return value

A Float.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getVertices()



This method returns a sequence of indices of the vertices that bound this edge. The first index refers to the vertex where the normalized curve parameter = 0.0, and the second index refers to the vertex where the normalized curve parameter = 1.0. If the edge is a closed curve, only one vertex index is returned.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The Edge object has the following members:

- *index*

  An Int specifying the index of the edge in the EdgeArray.

- *isReferenceRep*

  A Boolean specifying whether the edge belongs to the reference representation of the Part or Instance.

- *pointOn*

  A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point located on the edge.

- *featureName*

  A tuple of Floats specifying the name of the feature that created this edge.

- *instanceName*

  A tuple of Floats specifying the name of the part instance for this edge (if applicable).