# BoundaryConditionState object

The BoundaryConditionState object is the abstract base type for other BoundaryConditionState objects. The BoundaryConditionState object has no explicit constructor or methods. The members of the BoundaryConditionState object are common to all objects derived from the BoundaryConditionState object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The BoundaryConditionState object has the following members:

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.