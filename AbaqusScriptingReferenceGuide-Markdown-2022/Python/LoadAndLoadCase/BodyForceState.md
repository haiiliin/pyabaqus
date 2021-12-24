# BodyForceState object

The BodyForceState object stores the propagating data of a body force in a step. One instance of this object is created internally by the [BodyForce](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyforcepyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [BodyForce](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyforcepyc.htm?ContextScope=all) object.

The BodyForceState object has no constructor or methods.

The BodyForceState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The BodyForceState object has the following members:

- *comp1*

  A Float or a Complex specifying the body force component in the 1-direction.

- *comp2*

  A Float or a Complex specifying the body force component in the 2-direction.

- *comp3*

  A Float or a Complex specifying the body force component in the 3-direction.

- *comp1State*

  A SymbolicConstant specifying the propagation state of the body force component in the 1-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *comp2State*

  A SymbolicConstant specifying the propagation state of the body force component in the 2-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *comp3State*

  A SymbolicConstant specifying the propagation state of the body force component in the 3-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

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

- [DLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dload.htm?ContextScope=all#simakey-r-dload) (load type label: BX, BY, BZ, BR, BXNU, BYNU, BZNU, or BRNU)