# RadiationToAmbientState object

The RadiationToAmbientState object stores the propagating data for a [RadiationToAmbient](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationtoambientpyc.htm?ContextScope=all) object. One instance of this object is created internally by the [RadiationToAmbient](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationtoambientpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [RadiationToAmbient](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationtoambientpyc.htm?ContextScope=all) object.

The RadiationToAmbientState object has no constructor or methods.

The RadiationToAmbientState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The RadiationToAmbientState object has the following members:

- *ambientTemperature*

  A Float specifying the ambient temperature.

- *ambientTemperatureState*

  A SymbolicConstant specifying the propagation state of the *ambientTemperature* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *ambientTemperatureAmpState*

  A SymbolicConstant specifying the propagation state of the *ambientTemperatureAmp* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *emissivity*

  A Float specifying the emissivity.

- *emissivityState*

  A SymbolicConstant specifying the propagation state of the *emissivity* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *ambientTemperatureAmp*

  A String specifying the name of the Amplitude object that gives the variation of the ambient temperature with time.

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

- [SRADIATE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-sradiate.htm?ContextScope=all#simakey-r-sradiate)