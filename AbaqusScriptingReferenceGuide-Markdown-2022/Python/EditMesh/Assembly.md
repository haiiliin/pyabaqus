# Assembly object

The following commands operate on Assembly objects. For more information about the Assembly object, see [Assembly object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?ContextScope=all).

## Access

```
import meshEdit
```

## collapseMeshEdge(...)



This method collapses an edge of a quadrilateral or triangular element of a part instance.



### Required arguments

- *edge*

  A single [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object specifying the element edge to collapse.

- *collapseMethod*

  A SymbolicConstant specifying the method used to collapse the edge. Possible values are FORWARD, REVERSE, and AVERAGE.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## combineElement(...)



This method combines two triangular elements of a part instance.



### Required arguments

- *elements*

  A sequence of triangular [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the elements to combine.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## deleteElement(...)



This method deletes the given elements from a part instance. The elements must have been generated using the bottom-up meshing technique.



### Required arguments

- *elements*

  A sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects or a Set object containing elements.

### Optional arguments

- *deleteUnreferencedNodes*

  A Boolean specifying whether to delete all those associated nodes that become unreferenced after the given elements are deleted. The default value is OFF.

### Return value

None.

### Exceptions

None.



## projectNode(...)



This method projects the given nodes of a part instance onto a mesh entity, geometric entity, or a datum object.



### Required arguments

- *nodes*

  A sequence of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects to be projected.

- *projectionReference*

  An object specifying the target for the node projection operation. The *projectionReference* can be any one of the following objects: [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all), [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all), [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all), [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all), [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all), [DatumPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpointpyc.htm?ContextScope=all), [DatumAxis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all), or [DatumPlane](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumplanepyc.htm?ContextScope=all).

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## editNode(...)



This method changes the coordinates of the given nodes on a part instance.



### Required arguments

- *nodes*

  A sequence of MeshNode objects or a Set object containing nodes.

### Optional arguments

- *coordinate1*

  A Float specifying the value of the first coordinate. If *coordinate1* and *offset1* are unspecified, the existing value does not change.

- *coordinate2*

  A Float specifying the value of the second coordinate. If *coordinate2* and *offset2* are unspecified, the existing value does not change.

- *coordinate3*

  A Float specifying the value of the third coordinate. If *coordinate3* and *offset3* are unspecified, the existing value does not change.

- *coordinates*

  A sequence of three-dimensional coordinate tuples specifying the coordinates for each of the given nodes. When specified, the number of coordinate tuples must match the number of given nodes, and be ordered to correspond to the given nodes in *ascending order* according to index. Furthermore, *coordinate1*, *coordinate2*, *coordinate3*, *offset1*, *offset2*, or *offset3* may not be specified.

- *offset1*

  A Float specifying an offset to apply to the value of the first coordinate of the specified nodes.

- *offset2*

  A Float specifying an offset to apply to the value of the second coordinate of the specified nodes.

- *offset3*

  A Float specifying an offset to apply to the value of the third coordinate of the specified nodes.

- *localCsys*

  A DatumCsys object specifying the local coordinate system. If unspecified, the global coordinate system will be used.

- *projectToGeometry*

  A Boolean specifying whether to project nodes back to their original geometry. For example, if a node is on a face, this method first positions the node at the new location and then projects it back to the original face. The default value is ON.

### Return value

None.

### Exceptions

A coordinate and an offset may not both be specified for the same coordinate component.



## mergeNodes(...)



Merge the nodes of a part instance. The nodes must have been generated using the bottom-up meshing technique.



### Required arguments

- *nodes*

  A sequence of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects specifying the nodes to merge.

### Optional arguments

- *tolerance*

  A Float specifying the maximum distance between nodes that will be merged to a single node. The location of the new node is the average position of the merged nodes. The default value is 10–6.

- *removeDuplicateElements*

  A Boolean specifying whether elements with the same connectivity after the merge will merged into a single element. The default value is True.

### Return value

None.

### Exceptions

None.



## mergeNodes(...)



Merge two nodes of a part instance. At least one of the two nodes must have been generated using the bottom-up meshing technique.



### Required arguments

- *node1*

  A [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object specifying the first node to merge.

- *node2*

  A [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object specifying the second node to merge.

### Optional arguments

- *removeDuplicateElements*

  A Boolean specifying whether elements with the same connectivity after the merge will merged into a single element. The default value is True.

### Return value

None.

### Exceptions

None.



## splitElement(...)



This method splits quadrilateral elements into triangular elements.



### Required arguments

- *elements*

  A sequence of quadrilateral [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the elements to split. Each quadrilateral element is split into two triangular elements by the shorter diagonal.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## splitMeshEdge(...)



This method splits an edge of a quadrilateral or triangular element of a part instance.



### Required arguments

- *edge*

  A single [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object specifying the element edge to split.

### Optional arguments

- *parameter*

  A Float specifying the normalized distance along the *edge* at which to split. Possible values are 0.0 << *parameter* << 1.0. The default value is 0.5.

### Return value

None.

### Exceptions

None.



## swapMeshEdge(...)



This method swaps the diagonal of two adjacent triangular elements of a part instance.



### Required arguments

- *edge*

  A single [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object specifying the element edge to swap.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## generateMeshByOffset(...)



This method generates a solid or shell mesh from an orphan mesh surface by generating layers of elements that propagate out normal to the surface boundary.



### Required arguments

- *region*

  A Region object specifying the domain to be offset.

- *meshType*

  A Symbolic Constant specifying the type of mesh to be generated. Possible values are SOLID or SHELL.

- *totalThickness*

  A Float specifying the total thickness of the solid layers. This argument applies only when *meshType*=SOLID.

- *distanceBetweenLayers*

  A Float specifying the distance between shell layers. This argument applies only when *meshType*=SHELL.

- *numLayers*

  An Int specifying the number of element layers to be generated.

### Optional arguments

- *offsetDirection*

  A Symbolic Constant specifying the direction of the offset. This argument is required only when the given region relates to a shell mesh. Possible values are OUTWARD, INWARD, and BOTH. The default value is OUTWARD.

- *initialOffset*

  A Float specifying the magnitude of the initial offset. The default value is zero.

- *shareNodes*

  Boolean specifying whether the first layer of nodes should be shared with nodes on the base surface. The default value is False.

- *deleteBaseElements*

  A Boolean specifying whether to delete the shell elements after the offset layers are generated. The default value is False. This argument applies only when *meshType*=SHELL.

- *constantThicknessCorners*

  A Boolean specifying whether to use element-based thickness or nodal-based thickness. The default value is False.

- *extendElementSets*

  A Boolean specifying whether existing element sets that include base elements will be extended to include corresponding offset elements. The default value is False.

### Return value

None.

### Exceptions

None.



## redoMeshEdit()



This method executes the edit mesh or the bottom-up meshing operation most recently undone by the undoMeshEdit method on an assembly. A redo action must be currently available for the assembly. This implies that the user must have executed the undoMeshEdit method on the assembly and that the user has not subsequently executed any further edit mesh commands on the assembly. It also implies that the user provided a sufficient cache allowance to store the undo operation.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## undoMeshEdit()



This method undoes the most recent edit mesh or the bottom-up meshing operation on an assembly and restores the mesh on the affected part instance to its previous state. An edit mesh undo action must be available for the assembly. This implies that prior to executing an edit mesh command on the assembly, the user enabled edit mesh undo with a sufficient cache allowance to store the edit mesh operation.



### Arguments

None.

### Return value

None.

### Exceptions

None.