# OdbPart object

The OdbPart object is similar to the kernel Part object and contains nodes and elements, but not geometry.

## Access

```
import odbAccess
session.odbs[name].parts[name]
```

## Part(...)



This method creates an OdbPart object. Nodes and elements are added to this object at a later stage.



### Path

```
session.odbs[name].Part
```

### Required arguments

- *name*

  A String specifying the part name.

- *embeddedSpace*

  A SymbolicConstant specifying the dimensionality of the [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object. Possible values are THREE_D, TWO_D_PLANAR, and AXISYMMETRIC.

- *type*

  A SymbolicConstant specifying the type of the [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object. Possible values are DEFORMABLE_BODY and ANALYTIC_RIGID_SURFACE.

### Optional arguments

None.

### Return value

An OdbPart object.

### Exceptions

None.



## addElements(...)



This method adds elements to an OdbPart object using element labels and nodal connectivity.

Warning:Adding elements not in ascending order of their labels may cause Abaqus/Viewer to plot contours incorrectly.





### Required arguments

- *labels*

  A sequence of Ints specifying the element labels.

- *connectivity*

  A sequence of sequences of Ints specifying the nodal connectivity.

- *type*

  A String specifying the element type.

### Optional arguments

- *elementSetName*

  A String specifying a name for this element set. The default value is the empty string.

- *sectionCategory*

  A [SectionCategory](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectioncategorypyc.htm?ContextScope=all) object for this element set.

### Return value

None.

### Exceptions

None.



## addElements(...)



This method adds elements to an OdbPart object using a sequence of element labels and nodal connectivity.

Warning:Adding elements not in ascending order of their labels may cause Abaqus/Viewer to plot contours incorrectly.





### Required arguments

- *elementData*

  A sequence of sequences of Ints specifying the element labels and nodal connectivity, in the form ((*label*, *c1*, *c2*, *c3*, *c4*), (*label*, *c1*, *c2*, *c3*, *c4*), ...).

- *type*

  A String specifying the element type. The value can be user defined.

### Optional arguments

- *elementSetName*

  A String specifying a name for this element set. The default value is None.

- *sectionCategory*

  A [SectionCategory](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectioncategorypyc.htm?ContextScope=all) object for this element set.

### Return value

None.

### Exceptions

None.



## addNodes(...)



This method adds nodes to an OdbPart object using node labels and coordinates.

Warning:Adding nodes not in ascending order of their labels may cause Abaqus/Viewer to plot contours incorrectly.





### Required arguments

- *labels*

  A sequence of Ints specifying the node labels.

- *coordinates*

  A sequence of sequences of Floats specifying the nodal coordinates.

### Optional arguments

- *nodeSetName*

  A String specifying a name for this node set. The default value is None.

### Return value

None.

### Exceptions

None.



## addNodes(...)



This method adds nodes to an OdbPart object using a sequence of node labels and coordinates.

Warning:Adding nodes not in ascending order of their labels may cause Abaqus/Viewer to plot contours incorrectly.





### Required arguments

- *nodeData*

  A sequence of tuples specifying the node labels and coordinates, in the form ((*label*, *x*, *y*, *z*), (*label*, *x*, *y*, *z*), ...).

### Optional arguments

- *nodeSetName*

  A String specifying a name for this node set. The default value is None.

### Return value

None.

### Exceptions

None.



## assignBeamOrientation(...)



This method assigns a beam section orientation to a region of a part instance.



### Required arguments

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying a region on an instance.

- *method*

  A SymbolicConstant specifying the assignment method. Only a value of N1_COSINES is currently supported.

- *vector*

  A sequence of three Floats specifying the approximate local  n1n1 -direction of the beam cross-section.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## assignMaterialOrientation(...)



This method assigns a material orientation to a region of a part instance.



### Required arguments

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying a region on an instance.

- *localCSys*

  An [OdbDatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system or None, indicating the global coordinate system.

### Optional arguments

- *axis*

  A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied. For shells this axis is also the shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle*

  A Float specifying the angle of the additional rotation. The default value is 0.0.

- *stackDirection*

  A SymbolicConstant specifying the stack or thickness direction of the material. Possible values are STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is STACK_3.

### Return value

None.

### Exceptions

None.



## assignRebarOrientation(...)



This method assigns a rebar reference orientation to a region of a part instance.



### Required arguments

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying a region on an instance.

- *localCsys*

  An [OdbDatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system or None, indicating the global coordinate system.

### Optional arguments

- *axis*

  A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied. For shells this axis is also the shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle*

  A Float specifying the angle of the additional rotation. The default value is 0.0.

### Return value

None.

### Exceptions

None.



## getElementFromLabel(...)



This method is used to retrieved an element with a specific label from a part object.



### Required arguments

- *label*

  An Int specifying the element label.

### Optional arguments

None.

### Return value

An [OdbMeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) object.

### Exceptions

- If no element with the specified label exists:

  OdbError: Invalid element label



## getNodeFromLabel(...)



This method is used to retrieved a node with a specific label from a part object.



### Required arguments

- *label*

  An Int specifying the node label.

### Optional arguments

None.

### Return value

An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object.

### Exceptions

- If no node with the specified label exists:

  OdbError: Invalid node label



## AnalyticRigidSurf2DPlanar(...)



This method is used to define a two-dimensional [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) object on the part object.



### Required arguments

- *name*

  The name of the analytic surface.

- *profile*

  A sequence of [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) objects or an [OdbSequenceAnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsequenceanalyticsurfacesegmentpyc.htm?ContextScope=all) object.

### Optional arguments

- *filletRadius*

  A Double specifying the radius of curvature to smooth discontinuities between adjoining segments. The default value is 0.0.

### Return value

None.

### Exceptions

- If OdbPart is of type THREE_D:

  OdbError: 2D-Planar Analytic Rigid Surface can be defined only if the part is of type TWO_D_PLANAR or AXISYMMETRIC.



## AnalyticRigidSurfExtrude(...)



This method is used to define a three-dimensional cylindrical [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) on the part object.



### Required arguments

- *name*

  The name of the analytic surface.

- *profile*

  A sequence of [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) objects or an [OdbSequenceAnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsequenceanalyticsurfacesegmentpyc.htm?ContextScope=all) object.

### Optional arguments

- *filletRadius*

  A Double specifying the radius of curvature to smooth discontinuities between adjoining segments. The default value is 0.0.

### Return value

None.

### Exceptions

- If OdbPart is not of type THREE_D:

  OdbError: Analytic Rigid Surface of type CYLINDER can be defined only if the part is of type THREE_D.



## AnalyticRigidSurfRevolve(...)



This method is used to define a three-dimensional [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) of revolution on the part object.



### Required arguments

- *name*

  The name of the analytic surface.

- *profile*

  A sequence of [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) objects or an [OdbSequenceAnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsequenceanalyticsurfacesegmentpyc.htm?ContextScope=all) object.

### Optional arguments

- *filletRadius*

  A Double specifying the radius of curvature to smooth discontinuities between adjoining segments. The default value is 0.0.

### Return value

None.

### Exceptions

- If OdbPart is not of type THREE_D:

  OdbError: Analytic Rigid Surface of type REVOLUTION can be defined only if the part is of type THREE_D.



## RigidBody(...)



This method defines an [OdbRigidBody](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbrigidbodypyc.htm?ContextScope=all) on the part object.



### Required arguments

- *referenceNode*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying the reference node assigned to the rigid body.

### Optional arguments

- *position*

  A symbolic constant specify if the location of the reference node is to be defined by the user. Possible values are INPUT and CENTER_OF_MASS. The default value is INPUT.

- *isothermal*

  A Boolean specifying an isothermal rigid body. The default value is OFF. This parameter is used only for a fully-coupled thermal stress analysis.

- *elset*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying an element set assigned to the rigid body.

- *pinNodes*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying pin-type nodes assigned to the rigid body.

- *tieNodes*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying tie-type nodes assigned to the rigid body.

- *analyticSurface*

  An [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying the Analytic Rigid Surface assigned to the rigid body.

### Return value

None.

### Exceptions

- If *referenceNode* is not a node set:

  OdbError: Rigid body definition requires a node set.



## Members

The OdbPart object has members with the same names and descriptions as the arguments to the [Part ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpartpyc.htm?ContextScope=all#simaker-odbpartpartpyc)method.

In addition, the OdbPart object can have the following members:

- *nodes*

  An [OdbMeshNodeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object.

- *elements*

  An [OdbMeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) object.

- *nodeSets*

  A repository of [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) objects specifying node sets.

- *elementSets*

  A repository of [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) objects specifying element sets.

- *surfaces*

  A repository of [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) objects specifying surfaces.

- *sectionAssignments*

  A [SectionAssignmentArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionassignmentpyc.htm?ContextScope=all) object.

- *beamOrientations*

  A [BeamOrientationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beamorientationpyc.htm?ContextScope=all) object.

- *materialOrientations*

  A [MaterialOrientationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialorientationpyc.htm?ContextScope=all) object.

- *rebarOrientations*

  A [RebarOrientationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarorientationpyc.htm?ContextScope=all) object.

- *rigidBodies*

  An [OdbRigidBodyArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbrigidbodypyc.htm?ContextScope=all) object.

- *analyticSurface*

  An [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) object specifying analytic Surface defined on the instance.