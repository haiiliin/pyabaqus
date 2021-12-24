# FilmConditionState object

The FilmConditionState object stores the propagating data for a [FilmCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionpyc.htm?ContextScope=all) object. One instance of this object is created internally by the [FilmCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [FilmCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionpyc.htm?ContextScope=all) object.

The FilmConditionState object has no constructor or methods.

The FilmConditionState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The FilmConditionState object has the following members:

- *interactionPropertyState*

  A SymbolicConstant specifying the propagation state of the *interactionProperty* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *sinkTemperature*

  A Float specifying the sink temperature.

- *sinkTemperatureState*

  A SymbolicConstant specifying the propagation state of the *sinkTemperature* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *sinkAmplitudeState*

  A SymbolicConstant specifying the propagation state of the *sinkAmplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *filmCoeff*

  A Float specifying the film coefficient.

- *filmCoeffState*

  A SymbolicConstant specifying the propagation state of the *filmCoeff* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *filmCoeffAmplitudeState*

  A SymbolicConstant specifying the propagation state of the *filmCoeffAmplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *interactionProperty*

  A String specifying the [FilmConditionProp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionproppyc.htm?ContextScope=all) object associated with this interaction.

- *sinkAmplitude*

  A String specifying the name of the Amplitude object that gives the variation of the sink temperature.

- *filmCoeffAmplitude*

  A String specifying the name of the Amplitude object that gives the variation of the film coefficient.

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

- [SFILM](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-sfilm.htm?ContextScope=all#simakey-r-sfilm)
- [FILM](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-film.htm?ContextScope=all#simakey-r-film)