# SelfContactExpState object

The SelfContactExpState object stores the propagating data for a [SelfContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-selfcontactexppyc.htm?ContextScope=all) object. One instance of this object is created internally by the [SelfContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-selfcontactexppyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [SelfContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-selfcontactexppyc.htm?ContextScope=all) object.

The SelfContactExpState object has no constructor or methods.

The SelfContactExpState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The SelfContactExpState object has the following members:

- *interactionPropertyState*

  A SymbolicConstant specifying the propagation state of the *interactionProperty* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *contactControlsState*

  A SymbolicConstant specifying the propagation state of the *contactControls* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *interactionProperty*

  A String specifying the name of the [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object associated with this interaction.

- *contactControls*

  A String specifying the name of the [ContactControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactcontrolpyc.htm?ContextScope=all) object associated with this interaction.

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
- [MODEL CHANGE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-modelchange.htm?ContextScope=all#simakey-r-modelchange), TYPE=CONTACT PAIR