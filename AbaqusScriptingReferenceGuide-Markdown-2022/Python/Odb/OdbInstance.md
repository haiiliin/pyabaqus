# OdbInstance object

A part instance is the usage of a part within an assembly.

## Access

```
import odbAccess
session.odbs[name].rootAssembly.instances[name]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance
```

## Instance(...)



This method creates an OdbInstance object from an [OdbPart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpartpyc.htm?ContextScope=all) object.



### Path

session.odbs[*name*].rootAssembly.Instance

### Required arguments

- *name*

  A String specifying the instance name.

- *object*

  An [OdbPart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpartpyc.htm?ContextScope=all) object.

### Optional arguments

- *localCoordSystem*

  A sequence of sequences of three Floats specifying the rotation and translation of the part instance in the global Cartesian coordinate system. The first three sequences specify the new local coordinate system with its center at the origin.The first sequence specifies a point on the 1-axis.The second sequence specifies a point on the 2-axis.The third sequence specifies a point on the 3-axis.The fourth sequence specifies the translation of the local coordinate system from the origin to its intended location.For example, the following sequence moves a part 10 units in the *X*-direction with no rotation:`localCoordSystem = ((1, 0, 0), (0, 1, 0),                                 (0, 0, 1), (10, 0, 0))`The following sequence moves a part 5 units in the *X*-direction with rotation:`localCoordSystem = ((0, 1, 0), (1, 0, 0),                                 (0, 0, 1), (5, 0, 0))`transforms a part containing the two points`                                 Pt1= (1,0,0)                                  Pt2= (2,0,0)                                 `to`                                 Pt1 = (0, 6, 0)                                  Pt2 = (0, 7, 0)                                                      `

### Return value

An OdbInstance object.

### Exceptions

InvalidNameError.



## assignBeamOrientation(...)



This method assigns a beam section orientation to a region of a part instance.



### Required arguments

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying a region on an instance.

- *method*

  A SymbolicConstant specifying the assignment method. Only a value of N1_COSINES is currently supported.

- *vector*

  A sequence of three Floats specifying the approximate local n1n1-direction of the beam cross-section.

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

- *localCsys*

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



This method is used to retrieved an element with a specific label from an instance object.



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



This method is used to retrieved a node with a specific label from an instance object.



### Required arguments

- *label*

  An Int specifying the node label.

### Optional arguments

None.

### Return value

An[OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object.

### Exceptions

- If no node with the specified label exists:

  OdbError: Invalid node label



## assignSection(...)



This method is used to assign a section to a region on an instance.



### Required arguments

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying a region on an instance.

- *section*

  A [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

### Optional arguments

None.

### Return value

None.

### Exceptions

- If *region* is not an element set:

  OdbError: Section assignment requires element set.

- If the element set is not from the current instance:

  OdbError: Section assignment requires element set from this part instance.



## AnalyticRigidSurf2DPlanar(...)



This method is used to define a two-dimensional [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) object on the instance.



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

- If [OdbPart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpartpyc.htm?ContextScope=all) associated with the part instance is of type THREE_D:

  OdbError: 2D-Planar Analytic Rigid Surface can be defined only if the instance is of type TWO_D_PLANAR or AXISYMMETRIC.



## AnalyticRigidSurfExtrude(...)



This method is used to define a three-dimensional cylindrical [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) on the instance.



### Required arguments

- *name*

  The name of the analytic surface.

- *profile*

  A sequence of [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) objects or an [OdbSequenceAnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsequenceanalyticsurfacesegmentpyc.htm?ContextScope=all) object.

### Optional arguments

- *filletRadius*

  A Double specifying the radius of curvature to smooth discontinuities between adjoining segments. The default value is 0.0.

- *localCoordData*

  A sequence of sequences of Floats specifying the global coordinates of points used to define the local coordinate system.

### Return value

None.

### Exceptions

- If [OdbPart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpartpyc.htm?ContextScope=all) associated with the part instance is not of type THREE_D:

  OdbError: Analytic Rigid Surface of type CYLINDER can be defined only if the instance is of type THREE_D.



## AnalyticRigidSurfRevolve(...)



This method is used to define a three-dimensional [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) of revolution on the instance.



### Required arguments

- *name*

  The name of the analytic surface.

- *profile*

  A sequence of [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) objects or an [OdbSequenceAnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsequenceanalyticsurfacesegmentpyc.htm?ContextScope=all) object.

### Optional arguments

- *filletRadius*

  A Double specifying the radius of curvature to smooth discontinuities between adjoining segments. The default value is 0.0.

- *localCoordData*

  A sequence of sequences of Floats specifying the global coordinates of points used to define the local coordinate system.

### Return value

None.

### Exceptions

- If [OdbPart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpartpyc.htm?ContextScope=all) associated with the part instance is not of type THREE_D:

  OdbError: Analytic Rigid Surface of type REVOLUTION can be defined only if the instance is of type THREE_D.



## RigidBody(...)



This method defines an [OdbRigidBody](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbrigidbodypyc.htm?ContextScope=all) on the instance.



### Required arguments

- *referenceNode*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying the reference node assigned to the rigid body.

### Optional arguments

- *position*

  A symbolic constant specify if the location of the reference node is to be defined by the user. Possible values are INPUT, and CENTER_OF_MASS. The default value is INPUT.

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



## getNodeFromLabel(...)



This method is used to retrieved a node with a specific label from an instance object.



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



## getNodeFromLabel(...)



This method is used to retrieved a node with a specific label from an instance object.



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



## Members

The OdbInstance object can have the following members:

- *name*

  A String specifying the instance name.

- *type*

  A SymbolicConstant specifying the type of the [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object. Only a value of DEFORMABLE_BODY is currently supported.

- *embeddedSpace*

  A SymbolicConstant specifying the dimensionality of the [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object. Possible values are THREE_D, TWO_D_PLANAR, AXISYMMETRIC, and UNKNOWN_DIMENSION.

- *resultState*

  A SymbolicConstant specifying the state of the Instance as modified by the analysis. This member is only present if the Instance is part of the RootAssemblyState tree. Possible values are:PROPAGATED, specifying that the value is the same as the previous frame or the original rootAssembly.MODIFIED, specifying that the geometry of the instance has been changed at this frame.The default value is PROPAGATED.

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

- *rigidBodies*

  An [OdbRigidBodyArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbrigidbodypyc.htm?ContextScope=all) object.

- *beamOrientations*

  A [BeamOrientationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beamorientationpyc.htm?ContextScope=all) object.

- *materialOrientations*

  A [MaterialOrientationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialorientationpyc.htm?ContextScope=all) object.

- *rebarOrientations*

  A [RebarOrientationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarorientationpyc.htm?ContextScope=all) object.

- *analyticSurface*

  An [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) object specifying analytic Surface defined on the instance.