# StaticRiksStep object

The StaticRiksStep object is used to indicate that the step should be analyzed as a static load step using the modified Riks method for proportional loading cases.

The StaticRiksStep object is derived from the [AnalysisStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analysissteppyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name]
```

## StaticRiksStep(...)



This method creates a StaticRiksStep object.



### Path

```
mdb.models[name].StaticRiksStep
```

### Required arguments

- *name*

  A String specifying the repository key.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

### Optional arguments

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *nlgeom*

  A Boolean specifying whether to allow for geometric nonlinearity. The default value is OFF.

- *adiabatic*

  A Boolean specifying whether to perform an adiabatic stress analysis. The default value is OFF.

- *maxLPF*

  None or a Float specifying the maximum value of the load proportionality factor. The default value is None.

- *nodeOn*

  A Boolean specifying whether to monitor the finishing displacement value at a node. The default value is OFF.

- *maximumDisplacement*

  A Float specifying the value of the total displacement (or rotation) at the node and degree of freedom that, if crossed during an increment, ends the step at the current increment. This argument is required when *nodeOn*=ON. The default value is 0.0.

- *dof*

  An Int specifying the degree of freedom being monitored. This argument is required when *nodeOn*=ON. The default value is 0.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the vertex at which the finishing displacement value is being monitored. This argument is required when *nodeOn*=ON.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are FIXED and AUTOMATIC. The default value is AUTOMATIC.

- *maxNumInc*

  An Int specifying the maximum number of increments in a step. The default value is 100.

- *totalArcLength*

  A Float specifying the total load proportionality factor associated with the load in this step. The default value is 1.0.

- *initialArcInc*

  A Float specifying the initial load proportionality factor. The default value is the total load proportionality factor for the step.

- *minArcInc*

  A Float specifying the minimum arc length increment allowed. The default value is the smaller of the suggested initial load proportionality factor or 10−5 times the total load proportionality factor for the step.

- *maxArcInc*

  A Float specifying the maximum arc length increment allowed. The default value is the total load proportionality factor for the step.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *extrapolation*

  A SymbolicConstant specifying the type of extrapolation to use in determining the incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and PARABOLIC. The default value is LINEAR.

- *fullyPlastic*

  A String specifying the name of the region being monitored for fully plastic behavior. The default value is an empty string.

- *noStop*

  A Boolean specifying whether to accept the solution to an increment after the maximum number of iterations allowed have been completed, even if the equilibrium tolerances are not satisfied. The default value is OFF.Warning:You should set *noStop*=ON only in special cases when you have a thorough understanding of how to interpret the results.

- *maintainAttributes*

  A Boolean specifying whether to retain attributes from an existing step with the same name. The default value is False.

- *useLongTermSolution*

  A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with time-domain viscoelasticity or the long-term elastic-plastic solution for two-layer viscoplasticity. The default value is OFF.

- *convertSDI*

  A SymbolicConstant specifying whether to force a new iteration if severe discontinuities occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and CONVERT_SDI_ON. The default value is PROPAGATED.

### Return value

A StaticRiksStep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the StaticRiksStep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [StaticRiksStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-staticrikssteppyc.htm?ContextScope=all#simaker-staticriksstepstaticrikssteppyc)method, except for the *name*, *previous*, and *maintainAttributes* arguments.

### Return value

None.

### Exceptions

RangeError.



## Members

The StaticRiksStep object can have the following members:

- *name*

  A String specifying the repository key.

- *nlgeom*

  A Boolean specifying whether to allow for geometric nonlinearity. The default value is OFF.

- *adiabatic*

  A Boolean specifying whether to perform an adiabatic stress analysis. The default value is OFF.

- *maxLPF*

  None or a Float specifying the maximum value of the load proportionality factor. The default value is None.

- *nodeOn*

  A Boolean specifying whether to monitor the finishing displacement value at a node. The default value is OFF.

- *maximumDisplacement*

  A Float specifying the value of the total displacement (or rotation) at the node and degree of freedom that, if crossed during an increment, ends the step at the current increment. This argument is required when *nodeOn*=ON. The default value is 0.0.

- *dof*

  An Int specifying the degree of freedom being monitored. This argument is required when *nodeOn*=ON. The default value is 0.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are FIXED and AUTOMATIC. The default value is AUTOMATIC.

- *maxNumInc*

  An Int specifying the maximum number of increments in a step. The default value is 100.

- *totalArcLength*

  A Float specifying the total load proportionality factor associated with the load in this step. The default value is 1.0.

- *initialArcInc*

  A Float specifying the initial load proportionality factor. The default value is the total load proportionality factor for the step.

- *minArcInc*

  A Float specifying the minimum arc length increment allowed. The default value is the smaller of the suggested initial load proportionality factor or 10−5 times the total load proportionality factor for the step.

- *maxArcInc*

  A Float specifying the maximum arc length increment allowed. The default value is the total load proportionality factor for the step.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *extrapolation*

  A SymbolicConstant specifying the type of extrapolation to use in determining the incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and PARABOLIC. The default value is LINEAR.

- *noStop*

  A Boolean specifying whether to accept the solution to an increment after the maximum number of iterations allowed have been completed, even if the equilibrium tolerances are not satisfied. The default value is OFF.Warning:You should set *noStop*=ON only in special cases when you have a thorough understanding of how to interpret the results.

- *useLongTermSolution*

  A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with time-domain viscoelasticity or the long-term elastic-plastic solution for two-layer viscoplasticity. The default value is OFF.

- *convertSDI*

  A SymbolicConstant specifying whether to force a new iteration if severe discontinuities occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and CONVERT_SDI_ON. The default value is PROPAGATED.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *fullyPlastic*

  A String specifying the name of the region being monitored for fully plastic behavior. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the vertex at which the finishing displacement value is being monitored. This argument is required when *nodeOn*=ON.

- *explicit*

  A SymbolicConstant specifying whether the step has an explicit procedure type (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).

- *perturbation*

  A Boolean specifying whether the step has a perturbation procedure type.

- *nonmechanical*

  A Boolean specifying whether the step has a mechanical procedure type.

- *procedureType*

  A SymbolicConstant specifying the Abaqus procedure. Possible values are:

  - ANNEAL
  - BUCKLE
  - COMPLEX_FREQUENCY
  - COUPLED_TEMP_DISPLACEMENT
  - COUPLED_THERMAL_ELECTRIC
  - DIRECT_CYCLIC
  - DYNAMIC_IMPLICIT
  - DYNAMIC_EXPLICIT
  - DYNAMIC_SUBSPACE
  - DYNAMIC_TEMP_DISPLACEMENT
  - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
  - FREQUENCY
  - GEOSTATIC
  - HEAT_TRANSFER
  - MASS_DIFFUSION
  - MODAL_DYNAMICS
  - RANDOM_RESPONSE
  - RESPONSE_SPECTRUM
  - SOILS
  - STATIC_GENERAL
  - STATIC_LINEAR_PERTURBATION
  - STATIC_RIKS
  - STEADY_STATE_DIRECT
  - STEADY_STATE_MODAL
  - STEADY_STATE_SUBSPACE
  - VISCO

- *suppressed*

  A Boolean specifying whether the step is suppressed or not. The default value is OFF.

- *fieldOutputRequestState*

  A repository of [FieldOutputRequestState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequeststatepyc.htm?ContextScope=all) objects.

- *historyOutputRequestState*

  A repository of [HistoryOutputRequestState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequeststatepyc.htm?ContextScope=all) objects.

- *diagnosticPrint*

  A [DiagnosticPrint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diagnosticprintpyc.htm?ContextScope=all) object.

- *monitor*

  A [Monitor](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-monitorpyc.htm?ContextScope=all) object.

- *restart*

  A [Restart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-restartpyc.htm?ContextScope=all) object.

- *adaptiveMeshConstraintStates*

  A repository of [AdaptiveMeshConstraintState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshconstraintstatepyc.htm?ContextScope=all) objects.

- *adaptiveMeshDomains*

  A repository of [AdaptiveMeshDomain](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshdomainpyc.htm?ContextScope=all) objects.

- *control*

  A [Control](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-controlpyc.htm?ContextScope=all) object.

- *solverControl*

  A [SolverControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solvercontrolpyc.htm?ContextScope=all) object.

- *boundaryConditionStates*

  A repository of [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) objects.

- *interactionStates*

  A repository of [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) objects.

- *loadStates*

  A repository of [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) objects.

- *loadCases*

  A repository of [LoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadcasepyc.htm?ContextScope=all) objects.

- *predefinedFieldStates*

  A repository of [PredefinedFieldState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldstatepyc.htm?ContextScope=all) objects.



## Corresponding analysis keywords

- [STATIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-static.htm?ContextScope=all#simakey-r-static)
- [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step)