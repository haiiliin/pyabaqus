# AcousticImpedanceState object

The AcousticImpedanceState object stores the propagating data of an [AcousticImpedance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedancepyc.htm?ContextScope=all) object in a step. One instance of this object is created internally by the [AcousticImpedance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedancepyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [AcousticImpedance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedancepyc.htm?ContextScope=all) object.

The AcousticImpedanceState object has no constructor or methods.

The AcousticImpedanceState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The AcousticImpedanceState object has the following members:

- *interactionPropertyState*

  A SymbolicConstant specifying the propagation state of the *interactionProperty* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *interactionProperty*

  A String specifying the name of the [AcousticImpedanceProp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedanceproppyc.htm?ContextScope=all) object associated with this interaction.

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

- [SIMPEDANCE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-simpedance.htm?ContextScope=all#simakey-r-simpedance)