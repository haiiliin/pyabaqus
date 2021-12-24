# SubmodelBCState object

The SubmodelBCState object stores the propagating data for a Submodel boundary condition in a step. One instance of this object is created internally by the [SubmodelBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelbcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [SubmodelBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelbcpyc.htm?ContextScope=all) object.

The SubmodelBCState object has no constructor or methods.

The SubmodelBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The SubmodelBCState object has the following members:

- *dofState*

  A SymbolicConstant specifying the propagation state of the *dof* member. Possible values are SET and UNCHANGED.

- *globalStepState*

  A SymbolicConstant specifying the propagation state of the *globalStep* member. Possible values are SET and UNCHANGED.

- *globalIncrement*

  An Int specifying the increment number in the global model step at which the solution will be used to specify the values of the driven variables. This argument is applicable only for linear perturbation steps.

- *globalIncrementState*

  A SymbolicConstant specifying the propagation state of the *globalIncrement* member. Possible values are SET and UNCHANGED.

- *centerZoneSize*

  None or a Float specifying the thickness of the center zone size around the shell midsurface. The default value is None.

- *centerZoneSizefState*

  A SymbolicConstant specifying the propagation state of the *centerZoneSize* member. Possible values are SET and UNCHANGED.

- *scale*

  None or a Float specifying a scaling value applied to the applied displacements at the interface. The default value is 1.0.

- *scaleState*

  A SymbolicConstant specifying the propagation state of the *scale* member. Possible values are SET and UNCHANGED.

- *globalStep*

  A String specifying the step in the global model from which Abaqus reads the values of the variables that will drive the submodel analysis. The String indicates the position of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates the first step.

- *dof*

  A tuple of Ints specifying the degrees of freedom to which the boundary condition is applied.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [SUBMODEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-submodel.htm?ContextScope=all#simakey-r-submodel)
- [BOUNDARY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-boundary.htm?ContextScope=all#simakey-r-boundary), SUBMODEL