# LineLoadState object

The LineLoadState object stores the propagating data of a line load in a step. One instance of this object is created internally by the [LineLoad](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lineloadpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [LineLoad](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lineloadpyc.htm?ContextScope=all) object.

The LineLoadState object has no constructor or methods.

The LineLoadState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The LineLoadState object has the following members:

- *comp1*

  A Float or a Complex specifying the load component in the global or the beam local 1-direction.

- *comp2*

  A Float or a Complex specifying the load component in the global or the beam local 2-direction.

- *comp3*

  A Float or a Complex specifying the load component in the global 3-direction.

- *comp1State*

  A SymbolicConstant specifying the propagation state of the load component in the global or the beam local 1-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *comp2State*

  A SymbolicConstant specifying the propagation state of the load component in the global or the beam local 2-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *comp3State*

  A SymbolicConstant specifying the propagation state of the load component in the global 3-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *status*

  A SymbolicConstant specifying the propagation state of the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - BUILT_INTO_BASE_STATE

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the load has no amplitude reference.



## Corresponding analysis keywords

- [DLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dload.htm?ContextScope=all#simakey-r-dload) (load type label: PX, PY, PZ for a global reference frame, and P1, P2 for a local reference frame)