# ImplicitDynamicsStep object

The ImplicitDynamicsStep object is used to provide direct integration of a dynamic stress/displacement response in Abaqus/Standard analyses and is generally used for nonlinear cases.

The ImplicitDynamicsStep object is derived from the [AnalysisStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analysissteppyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name]
```

## ImplicitDynamicsStep(...)



This method creates an ImplicitDynamicsStep object.



### Path

```
mdb.models[name].ImplicitDynamicsStep
```

### Required arguments

- *name*

  A String specifying the repository key.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

### Optional arguments

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *timePeriod*

  A Float specifying the total time period of the step. The default value is 1.0.

- *nlgeom*

  A Boolean specifying whether geometric nonlinearities should be accounted for during the step. The default value is based on the previous step.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *application*

  A SymbolicConstant specifying the application type of the step. Possible values are ANALYSIS_PRODUCT_DEFAULT, TRANSIENT_FIDELITY, MODERATE_DISSIPATION, and QUASI_STATIC. The default value is ANALYSIS_PRODUCT_DEFAULT.

- *adiabatic*

  A Boolean specifying whether an adiabatic stress analysis is to be performed. The default value is OFF.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are FIXED and AUTOMATIC. The default value is AUTOMATIC.

- *maxNumInc*

  An Int specifying the maximum number of increments in a step. The default value is 100.

- *initialInc*

  A Float specifying the initial time increment. The default value is the total time period for the step.

- *minInc*

  A Float specifying the minimum time increment allowed. The default value is the smaller of the suggested initial time increment or 10−5 times the total time period.

- *maxInc*

  The SymbolicConstant DEFAULT or a Float specifying the maximum time increment allowed.

- *hafTolMethod*

  A SymbolicConstant specifying the way of specifying half-increment residual tolerance with the automatic time incrementation scheme. Possible values are ANALYSIS_PRODUCT_DEFAULT, VALUE, and SCALE. The default value is VALUE.

- *haftol*

  None or a Float specifying the half-increment residual tolerance to be used with the automatic time incrementation scheme. The default value is None.

- *halfIncScaleFactor*

  None or a Float specifying the half-increment residual tolerance scale factor to be used with the automatic time incrementation scheme. The default value is None.

- *nohaf*

  A Boolean specifying whether to suppress calculation of the half-increment residual. The default value is OFF.

- *amplitude*

  A SymbolicConstant specifying the amplitude variation for loading magnitudes during the step. Possible values are STEP and RAMP. The default value is STEP.

- *alpha*

  The SymbolicConstant DEFAULT or a Float specifying the nondefault value of the numerical (artificial) damping control parameter, αα, in the implicit operator. Possible values are −.333 <α<<α< 0. The default value is DEFAULT.

- *initialConditions*

  A SymbolicConstant specifying whether accelerations should be calculated or recalculated at the beginning of the step. Possible values are DEFAULT, BYPASS, and ALLOW. The default value is DEFAULT.

- *extrapolation*

  A SymbolicConstant specifying the type of extrapolation to use in determining the incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, PARABOLIC, VELOCITY_PARABOLIC, and ANALYSIS_PRODUCT_DEFAULT. The default value is ANALYSIS_PRODUCT_DEFAULT.

- *noStop*

  A Boolean specifying whether to accept the solution to an increment after the maximum number of iterations allowed have been completed, even if the equilibrium tolerances are not satisfied. The default value is OFF.Warning:You should set *noStop*=OFF only in special cases when you have a thorough understanding of how to interpret the results.

- *maintainAttributes*

  A Boolean specifying whether to retain attributes from an existing step with the same name. The default value is False.

- *solutionTechnique*

  A SymbolicConstant specifying the technique used to for solving nonlinear equations. Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.

- *reformKernel*

  An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix is reformed.. The default value is 8.

- *convertSDI*

  A SymbolicConstant specifying whether to force a new iteration if severe discontinuities occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and CONVERT_SDI_ON. The default value is PROPAGATED.

### Return value

An ImplicitDynamicsStep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ImplicitDynamicsStep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ImplicitDynamicsStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-implicitdynamicssteppyc.htm?ContextScope=all#simaker-implicitdynamicsstepimplicitdynamicssteppyc)method, except for the *name*, *previous*, and *maintainAttributes* arguments.

### Return value

None.

### Exceptions

RangeError.



## Members

The ImplicitDynamicsStep object can have the following members:

- *name*

  A String specifying the repository key.

- *timePeriod*

  A Float specifying the total time period of the step. The default value is 1.0.

- *nlgeom*

  A Boolean specifying whether geometric nonlinearities should be accounted for during the step. The default value is based on the previous step.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *application*

  A SymbolicConstant specifying the application type of the step. Possible values are ANALYSIS_PRODUCT_DEFAULT, TRANSIENT_FIDELITY, MODERATE_DISSIPATION, and QUASI_STATIC. The default value is ANALYSIS_PRODUCT_DEFAULT.

- *adiabatic*

  A Boolean specifying whether an adiabatic stress analysis is to be performed. The default value is OFF.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are FIXED and AUTOMATIC. The default value is AUTOMATIC.

- *maxNumInc*

  An Int specifying the maximum number of increments in a step. The default value is 100.

- *initialInc*

  A Float specifying the initial time increment. The default value is the total time period for the step.

- *minInc*

  A Float specifying the minimum time increment allowed. The default value is the smaller of the suggested initial time increment or 10−5 times the total time period.

- *maxInc*

  The SymbolicConstant DEFAULT or a Float specifying the maximum time increment allowed.

- *hafTolMethod*

  A SymbolicConstant specifying the way of specifying half-increment residual tolerance with the automatic time incrementation scheme. Possible values are ANALYSIS_PRODUCT_DEFAULT, VALUE, and SCALE. The default value is VALUE.

- *haftol*

  None or a Float specifying the half-increment residual tolerance to be used with the automatic time incrementation scheme. The default value is None.

- *halfIncScaleFactor*

  None or a Float specifying the half-increment residual tolerance scale factor to be used with the automatic time incrementation scheme. The default value is None.

- *nohaf*

  A Boolean specifying whether to suppress calculation of the half-increment residual. The default value is OFF.

- *amplitude*

  A SymbolicConstant specifying the amplitude variation for loading magnitudes during the step. Possible values are STEP and RAMP. The default value is STEP.

- *alpha*

  The SymbolicConstant DEFAULT or a Float specifying the nondefault value of the numerical (artificial) damping control parameter, αα, in the implicit operator. Possible values are −.333 <α<<α< 0. The default value is DEFAULT.

- *initialConditions*

  A SymbolicConstant specifying whether accelerations should be calculated or recalculated at the beginning of the step. Possible values are DEFAULT, BYPASS, and ALLOW. The default value is DEFAULT.

- *extrapolation*

  A SymbolicConstant specifying the type of extrapolation to use in determining the incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, PARABOLIC, VELOCITY_PARABOLIC, and ANALYSIS_PRODUCT_DEFAULT. The default value is ANALYSIS_PRODUCT_DEFAULT.

- *noStop*

  A Boolean specifying whether to accept the solution to an increment after the maximum number of iterations allowed have been completed, even if the equilibrium tolerances are not satisfied. The default value is OFF.Warning:You should set *noStop*=OFF only in special cases when you have a thorough understanding of how to interpret the results.

- *solutionTechnique*

  A SymbolicConstant specifying the technique used to for solving nonlinear equations. Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.

- *reformKernel*

  An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix is reformed.. The default value is 8.

- *convertSDI*

  A SymbolicConstant specifying whether to force a new iteration if severe discontinuities occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and CONVERT_SDI_ON. The default value is PROPAGATED.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

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

- [DYNAMIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dynamic.htm?ContextScope=all#simakey-r-dynamic)
- [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step)