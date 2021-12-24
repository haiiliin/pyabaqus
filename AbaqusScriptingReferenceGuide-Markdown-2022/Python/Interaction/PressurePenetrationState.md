# PressurePenetrationState object

The PressurePenetrationState object stores the propagating data of a [PressurePenetration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepenetrationpyc.htm?ContextScope=all) object in a step. One instance of this object is created internally by the [PressurePenetration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepenetrationpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [PressurePenetration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepenetrationpyc.htm?ContextScope=all) object.

The PressurePenetrationState object has no constructor or methods.

The PressurePenetrationState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The PressurePenetrationState object has the following members:

- *penetrationTime*

  A Float specifying the fraction of the current step time over which the fluid pressure on newly penetrated contact surface segments is ramped up to the current magnitude. The default value is 10–3.

- *penetrationTimeState*

  A SymbolicConstant specifying the propagation state of the *penetrationTime* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *criticalPressureState*

  A SymbolicConstant specifying the propagation state of the *criticalPressure* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *penetrationPressureState*

  A SymbolicConstant specifying the propagation state of the *penetrationPressure* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *penetrationPressure*

  A tuple of Floats specifying the fluid pressure magnitude. For steady state dynamic analyses, a tuple of Complexes specifying the fluid pressure magnitude.

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the load has no amplitude reference.

- *criticalPressure*

  A tuple of Floats specifying the critical contact pressure below which fluid penetration starts to occur.

- *status*

  A SymbolicConstant specifying the propagation state of the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - BUILT_INTO_BASE_STATE

## Corresponding analysis keywords

- [PRESSURE PENETRATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-pressurepenetration.htm?ContextScope=all#simakey-r-pressurepenetration)