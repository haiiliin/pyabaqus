# StdXplCosimulationState object

The StdXplCosimulationState object stores the propagating data for a [StdXplCosimulation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdxplcosimulationpyc.htm?ContextScope=all) object. One instance of this object is created internally by the [StdXplCosimulation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdxplcosimulationpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [StdXplCosimulation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdxplcosimulationpyc.htm?ContextScope=all) object.

The StdXplCosimulationState object has no constructor or methods.

The StdXplCosimulationState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The StdXplCosimulationState object has the following member:

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

- [CO-SIMULATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-co-simulation.htm?ContextScope=all#simakey-r-co-simulation),
- [CO-SIMULATION REGION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-co-simulationregion.htm?ContextScope=all#simakey-r-co-simulationregion),
- [CO-SIMULATION CONTROLS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-co-simulationcontrols.htm?ContextScope=all#simakey-r-co-simulationcontrols)