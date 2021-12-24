# BoltLoadState object

The BoltLoadState object stores the propagating data of a bolt load in a step. One instance of this object is created internally by the [BoltLoad](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boltloadpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [BoltLoad](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boltloadpyc.htm?ContextScope=all) object.

The BoltLoadState object has no constructor or methods.

The BoltLoadState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The BoltLoadState object has the following members:

- *boltMethod*

  A SymbolicConstant specifying the type of bolt load. Possible values are APPLY_FORCE, ADJUST_LENGTH, and FIX_LENGTH.

- *boltMethodState*

  A SymbolicConstant specifying the propagation state of the bolt load type. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *magnitude*

  A Float specifying the bolt load magnitude.

- *magnitudeState*

  A SymbolicConstant specifying the propagation state of the bolt load magnitude. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

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

- [CLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cload.htm?ContextScope=all#simakey-r-cload) (when *boltMethod*=APPLY_FORCE)
- [BOUNDARY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-boundary.htm?ContextScope=all#simakey-r-boundary) (when *boltMethod*=ADJUST_LENGTH or FIX_LENGTH)