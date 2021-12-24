# MomentState object

The MomentState object stores the propagating data for a moment in a step. One instance of this object is created internally by the [Moment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-momentpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [Moment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-momentpyc.htm?ContextScope=all) object.

The MomentState object has no constructor or methods.

The MomentState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The MomentState object has the following members:

- *cm1*

  A Float or a Complex specifying the load component in the 4-direction.

- *cm2*

  A Float or a Complex specifying the load component in the 5-direction.

- *cm3*

  A Float or a Complex specifying the load component in the 6-direction.

- *cm1State*

  A SymbolicConstant specifying the propagation state of the load component in the 4-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *cm2State*

  A SymbolicConstant specifying the propagation state of the load component in the 5-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *cm3State*

  A SymbolicConstant specifying the propagation state of the load component in the 6-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

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

- [CLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cload.htm?ContextScope=all#simakey-r-cload) (degree of freedom: 4, 5, or 6)