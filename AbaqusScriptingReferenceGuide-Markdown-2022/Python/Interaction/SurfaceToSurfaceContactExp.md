# SurfaceToSurfaceContactExp object

The SurfaceToSurfaceContactExp object defines surface-to-surface contact during an Abaqus/Explicit analysis.

The SurfaceToSurfaceContactExp object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## SurfaceToSurfaceContactExp(...)



This method creates a SurfaceToSurfaceContactExp object.



### Path

```
mdb.models[name].SurfaceToSurfaceContactExp
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the SurfaceToSurfaceContactExp object is created.

- *main*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the main surface.

- *secondary*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the secondary surface.

- *sliding*

  A SymbolicConstant specifying the contact formulation. Possible values are FINITE and SMALL.

- *interactionProperty*

  A String specifying the name of the [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object associated with this interaction.

### Optional arguments

- *mechanicalConstraint*

  A SymbolicConstant specifying the mechanical constraint formulation. Possible values are KINEMATIC and PENALTY. The default value is KINEMATIC.

- *weightingFactorType*

  A SymbolicConstant specifying the weighting for node-to-face contact. Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.

- *weightingFactor*

  A Float specifying the weighting factor for the contact surfaces when *weightingFactorType*=SPECIFIED. The default value is 0.0.

- *contactControls*

  A String specifying the name of the [ContactControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactcontrolpyc.htm?ContextScope=all) object associated with this interaction. An empty string indicates that the default contact controls will be used. The default value is an empty string.

- *initialClearance*

  A SymbolicConstant or a Float specifying the initial clearance at regions of contact. Possible values are OMIT and COMPUTED. The default value is OMIT.

- *halfThreadAngle*

  None or a sequence of Floats specifying the half thread angle used for bolt clearance. The default value is None.

- *pitch*

  None or a sequence of Floats specifying the pitch used for bolt clearance. The default value is None.

- *majorBoltDiameter*

  The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used for bolt clearance. The default value is COMPUTED.

- *meanBoltDiameter*

  The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used for bolt clearance. The default value is COMPUTED.

- *datumAxis*

  A [DatumAxis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the orientation of the bolt hole when specifying bolt clearance.

- *useReverseDatumAxis*

  A Boolean specifying whether to reverse the bolt clearance direction given by the datum axis. The default value is OFF.

- *clearanceRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the contact region for which clearance is specified.

### Return value

A SurfaceToSurfaceContactExp object.

### Exceptions

None.



## swapSurfaces()



This method switches the main and secondary surfaces of a surface-to-surface contact pair. This command is valid only during the step in which the interaction is created.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing SurfaceToSurfaceContactExp object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SurfaceToSurfaceContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactexppyc.htm?ContextScope=all#simaker-surfacetosurfacecontactexpsurfacetosurfacecontactexpyc) method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing SurfaceToSurfaceContactExp object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *interactionProperty*

  A String specifying the name of the [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object associated with this interaction.

- *contactControls*

  A String specifying the name of the [ContactControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactcontrolpyc.htm?ContextScope=all) object associated with this interaction. An empty string indicates that the default contact controls will be used. The default value is an empty string.

### Return value

None.

### Exceptions

None.



## Members

The SurfaceToSurfaceContactExp object has members with the same names and descriptions as the arguments to the [SurfaceToSurfaceContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactexppyc.htm?ContextScope=all#simaker-surfacetosurfacecontactexpsurfacetosurfacecontactexpyc) method except the optional arguments to the [setValuesInStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactstdpyc.htm?ContextScope=all#simaker-surfacetosurfacecontactstdsetvaluesinsteppyc) method.