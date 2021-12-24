# XFEMCrackGrowthState object

The XFEMCrackGrowthState object stores the propagating data of an [XFEMCrackGrowth](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackgrowthpyc.htm?ContextScope=all) object in a step. One instance of this object is created internally by the [XFEMCrackGrowth](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackgrowthpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [XFEMCrackGrowth](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackgrowthpyc.htm?ContextScope=all) object.

The XFEMCrackGrowthState object has no constructor or methods.

The XFEMCrackGrowthState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The XFEMCrackGrowthState object has the following members:

- *allowGrowth*

  A Boolean specifying whether the crack is allowed to grow (propagate) during this analysis step. The default value is ON.

- *allowGrowthState*

  A SymbolicConstant specifying the propagation state of the *allowGrowth* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

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

- [ENRICHMENT ACTIVATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-enrichmentactivation.htm?ContextScope=all#simakey-r-enrichmentactivation)