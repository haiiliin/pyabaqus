# PEGLoadState object

The PEGLoadState object stores the propagating data for a concentrated force in a step. One instance of this object is created internally by the [PEGLoad](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegloadpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [PEGLoad](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegloadpyc.htm?ContextScope=all) object.

The PEGLoadState object has no constructor or methods.

The PEGLoadState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The PEGLoadState object has the following members:

- *comp1*

  A Float or a Complex specifying the load component at dof 1 of reference node 1.

- *comp2*

  A Float or a Complex specifying the load component at dof 1 of reference node 2.

- *comp3*

  A Float or a Complex specifying the load component at dof 2 of reference node 2.

- *comp1State*

  A SymbolicConstant specifying the propagation state of the load component at dof 1 of reference node 1. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *comp2State*

  A SymbolicConstant specifying the propagation state of the load component at dof 1 of reference node 2. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *comp3State*

  A SymbolicConstant specifying the propagation state of the load component at dof 2 of reference node 2. Possible values are UNSET, SET, UNCHANGED, and FREED.

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

- [CLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cload.htm?ContextScope=all#simakey-r-cload) (degree of freedom: 1 or 2)