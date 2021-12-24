# PressurePenetration object

The PressurePenetration object defines pressure penetration loading simulated with surface-to-surface contact.

The PressurePenetration object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## PressurePenetration(...)



This method creates a PressurePenetration object.



### Path

```
mdb.models[name].PressurePenetration
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the PressurePenetration object is created.

- *contactInteraction*

  A String specifying the name of the Surface-to-surface contact (Standard) interaction.

- *mainPoints*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the points on the main surface that are exposed to the fluid.

- *secondaryPoints*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the points on the secondary surface that are exposed to the fluid.

- *penetrationPressure*

  A tuple of Floats specifying the fluid pressure magnitude. For steady state dynamic analyses, a tuple of Complexes specifying the fluid pressure magnitude.

- *criticalPressure*

  A tuple of Floats specifying the critical contact pressure below which fluid penetration starts to occur.

### Optional arguments

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *penetrationTime*

  A Float specifying the fraction of the current step time over which the fluid pressure on newly penetrated contact surface segments is ramped up to the current magnitude. The default value is 0.001.

### Return value

A PressurePenetration object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing PressurePenetration object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PressurePenetration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepenetrationpyc.htm?ContextScope=all#simaker-pressurepenetrationpressurepenetrationpyc) method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing PressurePenetration object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *penetrationPressure*

  A tuple of Floats specifying the fluid pressure magnitude. For steady state dynamic analyses, a tuple of Complexes specifying the fluid pressure magnitude.

- *criticalPressure*

  A tuple of Floats specifying the critical contact pressure below which fluid penetration starts to occur.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the load is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

- *penetrationTime*

  A Float specifying the fraction of the current step time over which the fluid pressure on newly penetrated contact surface segments is ramped up to the current magnitude. The default value is 0.001.

### Return value

None.

### Exceptions

None.



## Members

The PressurePenetration object has the following members:

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the PressurePenetration object is created.

- *contactInteraction*

  A String specifying the name of the Surface-to-surface contact (Standard) interaction.

- *mainPoints*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the points on the main surface that are exposed to the fluid.

- *secondaryPoints*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the points on the secondary surface that are exposed to the fluid.



## Corresponding analysis keywords

- [PRESSURE PENETRATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-pressurepenetration.htm?ContextScope=all#simakey-r-pressurepenetration)