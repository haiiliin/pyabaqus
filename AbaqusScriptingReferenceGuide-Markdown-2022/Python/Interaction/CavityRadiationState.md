# CavityRadiationState object

The CavityRadiationState object stores the propagating data for a [CavityRadiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cavityradiationpyc.htm?ContextScope=all) object. One instance of this object is created internally by the [CavityRadiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cavityradiationpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [CavityRadiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cavityradiationpyc.htm?ContextScope=all) object.

The CavityRadiationState object has no constructor or methods.

The CavityRadiationState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The CavityRadiationState object has the following members:

- *blocking*

  A SymbolicConstant specifying the blocking checks to be performed in the viewfactor calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING.

- *blockingState*

  A SymbolicConstant specifying the propagation state of the blocking member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *blockingSurfacesState*

  A SymbolicConstant specifying the propagation state of the *blockingSurfaces* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *rangeOfView*

  A Float specifying the distance beyond which factors need not be calculated because surfaces are judged to be too far apart to “see” each other (due to blocking by other surfaces).

- *rangeOfViewState*

  A SymbolicConstant specifying the propagation state of the *rangeOfView* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *surfaceReflection*

  A Boolean specifying whether reflection must be included in the cavity radiation calculations. The default value is ON.

- *surfaceReflectionState*

  A SymbolicConstant specifying the propagation state of the *surfaceReflection* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *viewfactorAccuracyTol*

  A Float specifying the acceptable tolerance for the viewfactor calculations.

- *viewfactorAccuracyTolState*

  A SymbolicConstant specifying the propagation state of the *viewfactorAccuracyTol* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *blockingSurfaces*

  A tuple of Strings specifying the surfaces that provide blocking inside the cavity.

- *status*

  A SymbolicConstant specifying the propagation state of the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEBUILT_INTO_BASE_STATE



## Corresponding analysis keywords

- [RADIATION VIEWFACTOR](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-radiationviewfactor.htm?ContextScope=all#simakey-r-radiationviewfactor)