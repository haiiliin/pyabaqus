# BodyHeatFluxState object

The BodyHeatFluxState object stores the propagating data for a Body [BodyHeatFlux](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyheatfluxpyc.htm?ContextScope=all) object in a step. One instance of this object is created internally by the [BodyHeatFlux](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyheatfluxpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [BodyHeatFlux](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyheatfluxpyc.htm?ContextScope=all) object.

The BodyHeatFluxState object has no constructor or methods.

The BodyHeatFluxState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The BodyHeatFluxState object has the following members:

- *magnitude*

  A Float specifying the Body heat flux magnitude.

- *magnitudeState*

  A SymbolicConstant specifying the propagation state of the Body heat flux magnitude. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

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

- [DFLUX](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dflux.htm?ContextScope=all#simakey-r-dflux)