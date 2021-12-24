# SurfaceToSurfaceStdState object

The SurfaceToSurfaceStdState object stores the propagating data for a [SurfaceToSurfaceContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactstdpyc.htm?ContextScope=all) object. One instance of this object is created internally by the [SurfaceToSurfaceContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactstdpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [SurfaceToSurfaceContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetosurfacecontactstdpyc.htm?ContextScope=all) object.

The SurfaceToSurfaceStdState object has no constructor or methods.

The SurfaceToSurfaceStdState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The SurfaceToSurfaceStdState object has the following members:

- *interactionPropertyState*

  A SymbolicConstant specifying the propagation state of the *interactionProperty* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *interferenceType*

  A SymbolicConstant specifying the interference type. Possible values are NONE, SHRINK_FIT, and UNIFORM.

- *interferenceTypeState*

  A SymbolicConstant specifying the propagation state of the *interferenceType* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *overclosure*

  A Float specifying the allowable overclosure.

- *overclosureState*

  A SymbolicConstant specifying the propagation state of the *overclosure* member. Possible values are COMPUTED and DIRECTION_COSINE.

- *interferenceDirectionType*

  A SymbolicConstant specifying the interference direction type. Possible values are COMPUTED and DIRECTION_COSINE.

- *interferenceDirectionTypeState*

  A SymbolicConstant specifying the propagation state of the *interferenceDirectionType* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *directionState*

  A SymbolicConstant specifying the propagation state of the *direction* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *contactControlsState*

  A SymbolicConstant specifying the propagation state of the *contactControls* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *interactionProperty*

  A String specifying the name of the [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object associated with this interaction.

- *amplitude*

  A String specifying the name of the Amplitude object that defines the magnitude of the prescribed interference during the step.

- *contactControls*

  A String specifying the name of the [ContactControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactcontrolpyc.htm?ContextScope=all) object associated with this interaction.

- *direction*

  A tuple of three Floats specifying the following:

  - X-direction cosine of the interference direction vector.
  - Y-direction cosine of the interference direction vector.
  - Z-direction cosine of the interference direction vector.

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

- [CONTACT CONTROLS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactcontrols.htm?ContextScope=all#simakey-r-contactcontrols)
- [CONTACT PAIR](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactpair.htm?ContextScope=all#simakey-r-contactpair)
- [CONTACT INTERFERENCE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactinterference.htm?ContextScope=all#simakey-r-contactinterference)