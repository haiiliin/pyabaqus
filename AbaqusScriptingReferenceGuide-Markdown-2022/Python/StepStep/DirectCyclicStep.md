# DirectCyclicStep object

The DirectCyclicStep object is used to provide a direct cyclic procedure for nonlinear, non-isothermal quasi-static analysis. It can also be used to predict progressive damage and failure for ductile bulk materials and/or to predict delamination/debonding growth at the interfaces in laminated composites in a low-cycle fatigue analysis.

The DirectCyclicStep object is derived from the [AnalysisStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analysissteppyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name]
```

## DirectCyclicStep(...)



This method creates a DirectCyclicStep object.



### Path

```
mdb.models[name].DirectCyclicStep
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

  A Float specifying the time of single loading cycle. The default value is 1.0.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are FIXED and AUTOMATIC. The default value is AUTOMATIC.

- *maxNumInc*

  An Int specifying the maximum number of increments in a step. The default value is 100.

- *initialInc*

  A Float specifying the initial time increment. The default value is the total time period for the step.

- *minInc*

  A Float specifying the minimum time increment allowed. The default value is the smaller of the suggested initial time increment or 10−5 times the total time period.

- *maxInc*

  A Float specifying the maximum time increment allowed. The default value is the total time period for the step.

- *maxNumIterations*

  An Int specifying the maximum number of iterations in a step. The default value is 200.

- *initialTerms*

  An Int specifying the initial number of terms in the Fourier series. The default value is 11.

- *maxTerms*

  An Int specifying the maximum number of terms in the Fourier series. The default value is 25.

- *termsIncrement*

  An Int specifying the increment in number of terms in the Fourier series. The default value is 5.

- *deltmx*

  A Float specifying the maximum temperature change to be allowed in an increment. The default value is 0.0.

- *cetol*

  A Float specifying the maximum difference in the creep strain increment calculated from the creep strain rates at the beginning and end of the increment. The default value is 0.0.

- *timePoints*

  None or a String specifying a String specifying the name of a time point object used to determine at which times the response of the structure will be evaluated. The default value is NONE.

- *fatigue*

  A Boolean specifying whether to include low-cycle fatigue analysis. The default value is OFF.

- *continueAnalysis*

  A Boolean specifying whether the displacement solution in the Fourier series obtained in the previous direct cyclic step is used as the starting values for the current step. The default value is OFF.

- *minCycleInc*

  An Int specifying the minimum number of cycles over which the damage is extrapolated forward. The default value is 100.

- *maxCycleInc*

  An Int specifying the maximum number of cycles over which the damage is extrapolated forward. The default value is 1000.

- *maxNumCycles*

  The SymbolicConstant DEFAULT or an Int specifying the maximum number of cycles allowed in a step or DEFAULT. A value of 1 plus half of the maximum number of cycles will be used if DEFAULT is specified. The default value is DEFAULT.

- *damageExtrapolationTolerance*

  A Float specifying the maximum extrapolated damage increment. The default value is 1.0.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *extrapolation*

  A SymbolicConstant specifying the type of extrapolation to use in determining the incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and PARABOLIC. The default value is LINEAR.

- *maintainAttributes*

  A Boolean specifying whether to retain attributes from an existing step with the same name. The default value is False.

- *convertSDI*

  A SymbolicConstant specifying whether to force a new iteration if severe discontinuities occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and CONVERT_SDI_ON. The default value is PROPAGATED.

### Return value

A DirectCyclicStep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the DirectCyclicStep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DirectCyclicStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-directcyclicsteppyc.htm?ContextScope=all#simaker-directcyclicstepdirectcyclicsteppyc)method, except for the *name*, *previous*, and *maintainAttributes* arguments.

### Return value

None.

### Exceptions

RangeError.



## Members

The DirectCyclicStep object can have the following members:

- *name*

  A String specifying the repository key.

- *timePeriod*

  A Float specifying the time of single loading cycle. The default value is 1.0.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are FIXED and AUTOMATIC. The default value is AUTOMATIC.

- *maxNumInc*

  An Int specifying the maximum number of increments in a step. The default value is 100.

- *initialInc*

  A Float specifying the initial time increment. The default value is the total time period for the step.

- *minInc*

  A Float specifying the minimum time increment allowed. The default value is the smaller of the suggested initial time increment or 10−5 times the total time period.

- *maxInc*

  A Float specifying the maximum time increment allowed. The default value is the total time period for the step.

- *maxNumIterations*

  An Int specifying the maximum number of iterations in a step. The default value is 200.

- *initialTerms*

  An Int specifying the initial number of terms in the Fourier series. The default value is 11.

- *maxTerms*

  An Int specifying the maximum number of terms in the Fourier series. The default value is 25.

- *termsIncrement*

  An Int specifying the increment in number of terms in the Fourier series. The default value is 5.

- *deltmx*

  A Float specifying the maximum temperature change to be allowed in an increment. The default value is 0.0.

- *cetol*

  A Float specifying the maximum difference in the creep strain increment calculated from the creep strain rates at the beginning and end of the increment. The default value is 0.0.

- *fatigue*

  A Boolean specifying whether to include low-cycle fatigue analysis. The default value is OFF.

- *continueAnalysis*

  A Boolean specifying whether the displacement solution in the Fourier series obtained in the previous direct cyclic step is used as the starting values for the current step. The default value is OFF.

- *minCycleInc*

  An Int specifying the minimum number of cycles over which the damage is extrapolated forward. The default value is 100.

- *maxCycleInc*

  An Int specifying the maximum number of cycles over which the damage is extrapolated forward. The default value is 1000.

- *maxNumCycles*

  The SymbolicConstant DEFAULT or an Int specifying the maximum number of cycles allowed in a step or DEFAULT. A value of 1 plus half of the maximum number of cycles will be used if DEFAULT is specified. The default value is DEFAULT.

- *damageExtrapolationTolerance*

  A Float specifying the maximum extrapolated damage increment. The default value is 1.0.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *extrapolation*

  A SymbolicConstant specifying the type of extrapolation to use in determining the incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and PARABOLIC. The default value is LINEAR.

- *convertSDI*

  A SymbolicConstant specifying whether to force a new iteration if severe discontinuities occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and CONVERT_SDI_ON. The default value is PROPAGATED.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *timePoints*

  None or a String specifying a String specifying the name of a time point object used to determine at which times the response of the structure will be evaluated. The default value is NONE.

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

- [DIRECT CYCLIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-directcyclic.htm?ContextScope=all#simakey-r-directcyclic)
- [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step)