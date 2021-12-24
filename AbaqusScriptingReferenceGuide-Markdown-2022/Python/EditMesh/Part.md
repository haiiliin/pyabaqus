# Part object

The following commands operate on Part objects. For more information about the Part object, see [Part object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all).

## Access

```
import meshEdit
```

## adjustMidsideNode(...)



This method is used to adjust the midside node of second-order elements of an orphan mesh part.



### Required arguments

- *cornerNodes*

  A sequence of Node objects specifying the nodes towards which connected midside nodes will be biased.

- *parameter*

  A Float specifying the normalized distance along the edge of the midside nodes. Possible values are 0.0 ≤≤ *parameter* ≤≤ 1.0, where 0.0 specifies the position of the corner node. The default value is 0.5.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## cleanMesh(...)



This method is used to collapse short element edges and delete collapsed elements, or grow short element edges, on an orphan mesh part composed of linear elements.



### Required arguments

- *mergeTolerance*

  A Float specifying the edge length tolerance. During the operation, edges shorter than the given tolerance will be collapsed, or grown to the specified length.

### Optional arguments

- *growEdges*

  A Boolean specifying whether short element edges will be grown to the specified tolerance. Default is False, meaning short edges will be collapsed.

- *elements*

  The elements to consider as the domain for the operation. By default all elements on the part are considered. The elements may be given as a [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all), a list of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects, a [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all), or a list of [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) objects.

- *refEdge*

  A [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) specifying a reference edge to indicate a topological direction in a structured mesh that will limit which edges within the element domain are considered. That is, only edges that are found to be topologically parallel to the given reference edge will be considered by the operation. By default all edges of the element domain are considered, unless *thicknessDir* is specified, in which case the operation will attempt to determine the topological edges from the thickness direction.

- *thicknessDir*

  A tuple of two or three Floats indicating a vector along which element edge lengths will be measured.

- *moveLayers*

  A Boolean indicating whether element edges will be all grown in the direction of the thickness vector specified by *thicknessDir*. This argument is ignored unless *growEdges* is True and *thicknessDir* is provided. When this argument is True the growth of any given element edge will no longer be constrained by short edges on neighboring elements, but elements could move from their original positions in cases where there are multiple adjacent layers of thin elements. The default value is False.

### Return value

None.

### Exceptions

None.



## collapseMeshEdge(...)



This method collapses an edge of a quadrilateral or triangular element of an orphan mesh part or part instance.



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



This method combines two triangular elements of an orphan mesh part or an Abaqus native mesh.



### Required arguments

- *elements*

  A sequence of triangular [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the elements to combine.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## convertSolidMeshToShell()



This method removes all solid elements from an orphan mesh part and creates triangular or quadrilateral shell elements along their outer faces.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## deleteElement(...)



This method deletes the given elements from an orphan mesh part or an Abaqus native mesh. If the elements belong to an Abaqus native mesh then the elements must have been generated using the bottom-up meshing technique.



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



## deleteNode(...)



This method deletes the given nodes from an orphan mesh part.



### Required arguments

- *nodes*

  A sequence of MeshNode objects or a Set object containing nodes.

### Optional arguments

- *deleteUnreferencedNodes*

  A Boolean specifying whether to delete all those associated nodes that become unreferenced after the given nodes and the connected elements are deleted. The default value is OFF.

### Return value

None.

### Exceptions

None.



## editNode(...)



This method changes the coordinates of the given nodes on an orphan mesh part or on an Abaqus native mesh.



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



## projectNode(...)



This method projects the given nodes onto a mesh entity, geometric entity, or a datum object. The nodes may belong to an orphan mesh part or to an Abaqus native mesh.



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



## generateMesh(...)



This method generates a new mesh on an orphan mesh part based on the original mesh.



### Required arguments

None.

### Optional arguments

- *elemShape*

  A SymbolicConstant specifying the element shape to be used for meshing. Possible values are:TRIRefine a planar triangular mesh and replace it with a new one. If no element sizes are attached, the new mesh will be governed by the sizes of the boundary edges in the old mesh.TETCreate a tetrahedral mesh from a closed shell of triangular elements.

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



## mergeNodes(...)



Merge the nodes of an orphan mesh part, or nodes that were generated using the bottom-up meshing technique.



### Required arguments

- *nodes*

  A sequence of Node objects specifying the nodes to merge.

### Optional arguments

- *tolerance*

  A Float specifying the maximum distance between nodes that will be merged to a single node. The location of the new node is the average position of the merged nodes. The default value is 10–6.

- *removeDuplicateElements*

  A Boolean specifying whether elements with the same connectivity after the merge will merged into a single element. The default value is True.

- *keepHighLabels*

  A Boolean specifying which node labels will remain after nodes are merged. If True then the highest node labels are kept; when False the lowest node labels are kept. The default value is False. This argument applies only to merging of orphan mesh nodes.

### Return value

None.

### Exceptions

None.



## mergeElement(...)



Merge a selection of elements arranged in layers on an orphan mesh part into a single layer.



### Required arguments

- *edge*

  A [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) of one of the specified elements that serves as a reference edge to indicate the topological direction for merging elements. All specified elements must be reachable by topological navigation from this element edge, and the topological direction must be unambiguous.

- *elements*

  A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all), a list of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects, a [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all), or a list of [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) objects containing the elements to be included in the merge operation.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## mergeNodes(...)



Merge two nodes of an orphan mesh part or an Abaqus native mesh. If the nodes belong to an Abaqus native mesh then at least one of the two nodes must have been generated using the bottom-up meshing technique.



### Required arguments

- *node1*

  A [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object specifying the first node to merge.

- *node2*

  A [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object specifying the second node to merge.

### Optional arguments

- *removeDuplicateElements*

  A Boolean specifying whether elements with the same connectivity after the merge will merged into a single element. The default value is True.

- *keepHighLabels*

  A Boolean specifying which node label will remain after nodes are merged. If True then the higher node label is kept; when False the lower node label is kept. The default value is False. This argument applies only to merging of orphan mesh nodes.

### Return value

None.

### Exceptions

None.



## orientElements(...)



This method orients the stack direction of elements in a continuum shell or gasket mesh.



### Required arguments

- *pickedElements*

  A sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the elements to orient.

- *referenceRegion*

  A [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object specifying a reference top face that indicates the desired orientation.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## removeElementSize()



This method removes the global element size from an orphan mesh part.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## renumberElement(...)



This method assigns new labels to orphan mesh elements.



### Required arguments

None.

### Optional arguments

Either *startLabel* and *increment*, or *offset*, or *labels* must be specified.

- *elements*

  A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) or a tuple or list of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects, or a [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) containing elements to be renumbered. If unspecified, all elements in the part will be renumbered.

- *startLabel*

  A positive Int specifying the new label for the first element in *elements*.

- *increment*

  A positive Int specifying the increment used for computation of new labels for all consecutive elements in *elements*.

- *offset*

  An Int by which existing labels of the specified elements will be offset.

- *labels*

  A list of labels for the specified elements. The length of this list must match the number of specified elements.

### Return value

None.

### Exceptions

- Renumbering is attempted on a native part:

  Error: Renumbering can be applied to orphan mesh parts only

- Renumbering data is specified incorrectly:

  Error: Either startLabel and increment or offset must be specified

- Renumbering will result in invalid labels:

  Error: Specified data will result in invalid labels

- Renumbering will result in conflicting labels:

  Error: Specified data will result in conflicting labels



## renumberNode(...)



This method assigns new labels to orphan mesh nodes.



### Required arguments

None.

### Optional arguments

Either *startLabel* and *increment*, or *offset*, or *labels* must be specified.

- *nodes*

  A [MeshNodeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) or a tuple or list of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects, or a [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) containing nodes to be renumbered. If unspecified, all nodes in the part will be renumbered.

- *startLabel*

  A positive Int specifying the new label for the first node in *nodes*.

- *increment*

  A positive Int specifying the increment used for computation of new labels for all consecutive nodes in *nodes*.

- *offset*

  An Int by which existing labels of the specified nodes will be offset.

- *labels*

  A list of labels for the specified nodes. The length of this list must match the number of specified nodes.

### Return value

None.

### Exceptions

- Renumbering is attempted on a native part:

  Error: Renumbering can be applied to orphan mesh parts only

- Renumbering data is specified incorrectly:

  Error: Either startLabel and increment or offset must be specified

- Renumbering will result in invalid labels:

  Error: Specified data will result in invalid labels

- Renumbering will result in conflicting labels:

  Error: Specified data will result in conflicting labels



## setElementSize(...)



This method sets the global element size for an orphan mesh part.



### Required arguments

- *size*

  A Float specifying the desired element size.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## splitElement(...)



This method splits quadrilateral elements of an orphan mesh part or a Abaqus native mesh into triangular elements.



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



This method splits an edge of a quadrilateral or triangular element of an orphan mesh part or an Abaqus native mesh.



### Required arguments

- *edge*

  A single [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object specifying the element edge to split.

### Optional arguments

- *parameter*

  A Float specifying the normalized distance along *edge* at which to split. Possible values are 0.0 << *parameter* << 1.0. The default value is 0.5.

### Return value

None.

### Exceptions

None.



## subdivideElement(...)



Subdivide a selection of elements on an orphan mesh part in one or more directions.



### Required arguments

None.

### Optional arguments

- *elements*

  A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all), a list of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects, a [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all), or a list of [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) objects containing the elements to be subdivided. By default all the elements of the part are subdivided.

- *divisionNumber*

  An Int specifying the number of resulting elements for each input element in each direction of the subdivision. If *face* or *edge* are not specified, elements will be subdivided according to this number in all possible directions. Must be greater than one. Default is 2.

- *face*

  A [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object that serves as a reference for indicating two topological directions for the subdivision operation. Must be a face of one of the specified elements, and all specified elements must be reachable by topological navigation from this element face. May not be combined with *edge*.

- *edge*

  A [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object that serves as a reference for indicating a single topological direction for the subdivision operation. Must be an edge of one of the specified elements, and all specified elements must be reachable by topological navigation from this element edge. May not be combined with *face*.

### Return value

None.

### Exceptions

None.



## swapMeshEdge(...)



This method swaps the diagonal of two adjacent triangular elements of an orphan mesh part or an Abaqus native mesh.



### Required arguments

- *edge*

  A single [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object specifying the element edge to swap.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## wrapMesh(...)



This method wraps a planar orphan mesh part about the *Z*-axis.



### Required arguments

- *radius*

  A Float specifying the radius of the cylinder about which the part is to be wrapped. The wrapping procedure will relocate a node at point (xx, yy) on the planar mesh to (x,θ,zx,θ,z), where rr is the specified radius, θθ = xrxr, and zz=yy.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## redoMeshEdit()



This method executes the edit mesh or the bottom-up meshing operation most recently undone by the undoMeshEdit method on an part. A redo action must be currently available for the part. This implies that the user must have executed the undoMeshEdit method on the part and that the user has not subsequently executed any further edit mesh commands on the assembly. It also implies that the user provided a sufficient cache allowance to store the undo operation.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## undoMeshEdit()



This method undoes the most recent edit mesh or the bottom-up meshing operation on a part and restores the mesh to its previous state. An edit mesh undo action must be available for the part. This implies that prior to executing an edit mesh command on the part, the user enabled edit mesh undo with a sufficient cache allowance to store the edit mesh operation.



### Arguments

None.

### Return value

None.

### Exceptions

None.