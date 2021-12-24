# ElasticFoundationState object

The ElasticFoundationState object stores the propagating data for an [ElasticFoundation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticfoundationpyc.htm?ContextScope=all) object. One instance of this object is created internally by the [ElasticFoundation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticfoundationpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [ElasticFoundation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticfoundationpyc.htm?ContextScope=all) object.

The ElasticFoundationState object has no constructor or methods.

The ElasticFoundationState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The ElasticFoundationState object has the following members:

- *stiffness*

  A Float specifying the foundation stiffness per area.

- *stiffnessState*

  A SymbolicConstant specifying the propagation state of the stiffness member. Possible values are UNSET, SET, UNCHANGED, and FREED.

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