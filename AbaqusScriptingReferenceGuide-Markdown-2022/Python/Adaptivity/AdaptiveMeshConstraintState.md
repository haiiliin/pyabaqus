# AdaptiveMeshConstraintState object

The AdaptiveMeshConstraintState object is the abstract base type for other Arbitrary Lagrangian Eularian (ALE) style AdaptiveMeshConstraintState objects. The AdaptiveMeshConstraintState object has no explicit constructor or methods. The members of the AdaptiveMeshConstraintState object are common to all objects derived from the AdaptiveMeshConstraintState object.

## Access

```
import step
mdb.models[name].steps[name].adaptiveMeshConstraintStates[name]
```

## Members

The AdaptiveMeshConstraintState object has the following members:

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - PROPAGATED_FROM_BASE_STATE
  - MODIFIED_FROM_BASE_STATE
  - DEACTIVATED_FROM_BASE_STATE
  - BUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the adaptive mesh constraint has no amplitude reference.