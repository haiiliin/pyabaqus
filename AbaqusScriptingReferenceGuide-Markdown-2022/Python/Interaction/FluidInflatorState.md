# FluidInflatorState object

The FluidInflatorState object stores the propagating data for a FluidInflator object. One instance of this object is created internally by the [FluidInflator](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidinflatorpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [FluidInflator](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidinflatorpyc.htm?ContextScope=all) object.

The FluidInflatorState object has no constructor or methods.

The FluidInflatorState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The FluidInflatorState object has the following member:

- *status*

  A *SymbolicConstant* specifying the propagation state of the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - BUILT_INTO_BASE_STATE