# ConcentratedForceState object

The ConcentratedForceState object stores the propagating data for a concentrated force in a step. One instance of this object is created internally by the [ConcentratedForce](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedforcepyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [ConcentratedForce](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedforcepyc.htm?ContextScope=all) object.

The ConcentratedForceState object has no constructor or methods.

The ConcentratedForceState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The ConcentratedForceState object has the following members:

- *cf1*

  A Float or a Complex specifying the concentrated force component in the 1-direction. Although *cf1*, *cf2*, and *cf3* are optional arguments, at least one of them must be nonzero.

- *cf2*

  A Float or a Complex specifying the concentrated force component in the 2-direction.

- *cf3*

  A Float or a Complex specifying the concentrated force component in the 3-direction.

- *cf1State*

  A SymbolicConstant specifying the propagation state of the concentrated force component in the 1-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *cf2State*

  A SymbolicConstant specifying the propagation state of the concentrated force component in the 2-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *cf3State*

  A SymbolicConstant specifying the propagation state of the concentrated force component in the 3-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *status*

  A SymbolicConstant specifying the propagation state of the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object. Possible values are:

  

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the load has no amplitude reference.

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

- [CLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cload.htm?ContextScope=all#simakey-r-cload) (degree of freedom: 1, 2, or 3)