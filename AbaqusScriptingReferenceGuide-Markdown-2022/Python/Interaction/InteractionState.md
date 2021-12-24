# InteractionState object

The InteractionState object is the abstract base type for other InteractionState objects. The InteractionState object has no explicit constructor. The members of the InteractionState object are common to all objects derived from InteractionState.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The InteractionState object has the following member:

- *status*

  A SymbolicConstant specifying the propagation state of the InteractionState object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - BUILT_INTO_BASE_STATE