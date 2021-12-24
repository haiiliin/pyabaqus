# IncidentWaveState object

The IncidentWaveState object stores the propagating data of an [IncidentWave](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepyc.htm?ContextScope=all) object in a step. One instance of this object is created internally by the [IncidentWave](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [IncidentWave](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepyc.htm?ContextScope=all) object.

The IncidentWaveState object has no constructor or methods.

The IncidentWaveState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The IncidentWaveState object has the following member:

- *status*

  A SymbolicConstant specifying the propagation state of the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEBUILT_INTO_BASE_STATE



## Corresponding analysis keywords

- [INCIDENT WAVE INTERACTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-incidentwaveinteraction.htm?ContextScope=all#simakey-r-incidentwaveinteraction)