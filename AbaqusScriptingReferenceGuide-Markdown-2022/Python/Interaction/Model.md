# Model object

The following commands operate on Model objects. For more information about the Model object, see [Model object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?ContextScope=all).

## Access

```
import interaction
```

## contactDetection(...)



This method uses contact detection to create [SurfaceToSurfaceContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactstdpyc.htm?ContextScope=all), [SurfaceToSurfaceContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactexppyc.htm?ContextScope=all), and [Tie](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tiepyc.htm?ContextScope=all) objects.



### Required arguments

None.

### Optional arguments

- *name*

  A String specifying the prefix used to generate repository keys. The default value is "CP-"

- *createStepName*

  A String specifying the name of the step in which the [SurfaceToSurfaceContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactstdpyc.htm?ContextScope=all), [SurfaceToSurfaceContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactexppyc.htm?ContextScope=all), and [Tie](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tiepyc.htm?ContextScope=all) objects are created. The default value is "Initial."

- *searchDomain*

  A SymbolicConstant MODEL or a sequence of Strings specifying the names of instances to search. MODEL indicates the whole model is searched. The default value is MODEL.

- *defaultType*

  A SymbolicConstant specifying the default type of object to create. Possible values are CONTACT, CONTACT_STANDARD, CONTACT_EXPLICIT, and TIE. If CONTACT is used, the behavior is determined by the type of [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) in the model. If an [ExplicitDynamicsStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-explicitdynamicssteppyc.htm?ContextScope=all) or [TempDisplacementDynamicsStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tempdisplacementdynamicssteppyc.htm?ContextScope=all) exists, then [SurfaceToSurfaceContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactexppyc.htm?ContextScope=all) is created by default. Otherwise [SurfaceToSurfaceContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactstdpyc.htm?ContextScope=all) is created by default. The default value is CONTACT.

- *interactionProperty*

  A String specifying the name of the [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object associated with any interactions created.

- *separationTolerance*

  A Float specifying the maximum separation for considering two surfaces to be candidates for contact, where separation is the maximum distance between the points of closest approach on the two surfaces. The default value is a function of the model.

- *extendByAngle*

  None or a Float specifying the angle for extending surface definitions to include adjacent faces. The default value is 20.

- *mergeWithinAngle*

  None or a Float specifying the angle for merging adjacent contact pairs that lie within the angle. The default value is 20.

- *searchSingleInstances*

  A Boolean specifying whether to include surface pairs within a single instance. The default value is OFF.

- *nameEachSurfaceFound*

  A Boolean specifying whether to assign a name to each surface found. The default value is ON.

- *createUnionOfMainSurfaces*

  A Boolean specifying whether to create a surface that is the union of all main surfaces found. The default value is OFF.

- *createUnionOfSecondarySurfaces*

  A Boolean specifying whether to create a surface that is the union of all secondary surfaces found. The default value is OFF.

- *createUnionOfMainSecondarySurfaces*

  A Boolean specifying whether to create a surface that is the union of all main and secondary surfaces found. The default value is OFF.

- *includePlanar*

  A Boolean specifying whether to include planar geometry. The default value is ON.

- *includeCylindricalSphericalToric*

  A Boolean specifying whether to include cylindrical, spherical, and toric geometry. The default value is ON.

- *includeSplineBased*

  A Boolean specifying whether to include spline-based geometry. The default value is ON.

- *includeMeshSolid*

  A Boolean specifying whether to include solid mesh entities. The default value is ON.

- *includeMeshShell*

  A Boolean specifying whether to include shell mesh entities. The default value is ON.

- *includeMeshMembrane*

  A Boolean specifying whether to include mesh membrane entities. The default value is OFF.

- *includeOverclosed*

  A Boolean specifying whether to include overclosed pairs. The default value is ON.

- *includeNonOverlapping*

  A Boolean specifying whether to include opposing geometry surfaces that do not overlap. The default value is OFF.

- *meshedGeometrySearchTechnique*

  A SymbolicConstant USE_GEOMETRY or USE_MESH specifying whether to locate pairs in meshed geometry using the geometric entities or mesh entities. The default value is USE_GEOMETRY.

- *useShellThickness*

  A Boolean specifying whether to account for shell thickness and offset during contact detection. The default value is ON.

- *surfaceSmoothing*

  A SymbolicConstant specifying whether to use surface smoothing for geometric surfaces in [SurfaceToSurfaceContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactstdpyc.htm?ContextScope=all) interactions. Possible values are NONE and AUTOMATIC. The default value isAUTOMATIC.

### Return value

None

### Exceptions

None.



## getSurfaceSeparation(...)



This method returns a list of all possible contacts that can be created using the [ContactDetection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelitnpyc.htm?ContextScope=all#simaker-modelcontactdetectionpyc) method.



### Required arguments

None.

### Optional arguments

The optional arguments to getSurfaceSeparation are the same as the arguments to the [ContactDetection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelitnpyc.htm?ContextScope=all#simaker-modelcontactdetectionpyc) method, with the exception of the *createStepName*, *defaultType*, *interactionProperty*, and *nameEachSurfaceFound* arguments.

### Return value

Tuple of tuples, where each tuple holds information, to be used in contact creation as follows:

A string specifying the name of the main surface used in contact.

A string specifying the name of the secondary surface used in contact.

A float specifying the separation distance between the main surface and the secondary surface.

A boolean specifying whether or not contact surfaces are overclosed.

### Exceptions

None.