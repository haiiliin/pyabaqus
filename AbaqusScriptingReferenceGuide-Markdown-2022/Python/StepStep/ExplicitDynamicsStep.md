# ExplicitDynamicsStep object

The ExplicitDynamicsStep object is used to perform a dynamic stress/displacement analysis using explicit integration in Abaqus/Explicit.

The ExplicitDynamicsStep object is derived from the [AnalysisStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analysissteppyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name]
```

## ExplicitDynamicsStep(...)



This method creates an ExplicitDynamicsStep object.



### Path

```
mdb.models[name].ExplicitDynamicsStep
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

  A Float specifying the total time period for the step. The default value is 1.0.

- *nlgeom*

  A Boolean specifying whether geometric nonlinearities should be accounted for during the step. The default value is ON.

- *adiabatic*

  A Boolean specifying that an adiabatic stress analysis is to be performed. The default value is OFF.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default value is AUTOMATIC_GLOBAL.

- *maxIncrement*

  None or a Float specifying the maximum time increment. If there is no upper limit, *maxIncrement*=None. This argument is required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.

- *scaleFactor*

  A Float specifying the factor that is used to scale the time increment. This argument is required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or FIXED_EBE. The default value is 1.0.

- *massScaling*

  A [MassScalingArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-massscalingpyc.htm?ContextScope=all) object specifying mass scaling controls. The default value is PREVIOUS_STEP.

- *linearBulkViscosity*

  A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.

- *quadBulkViscosity*

  A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is 1.2.

- *userDefinedInc*

  None or a Float specifying the user-defined time increment. This argument is required only when *timeIncrementationMethod*=FIXED_USER_DEFINED_INC. The default value is None.

- *maintainAttributes*

  A Boolean specifying whether to retain attributes from an existing step with the same name. The default value is False.

- *improvedDtMethod*

  A Boolean specifying whether to use the "improved" (*improvedDtMethod*=ON) or "conservative" (*improvedDtMethod*=OFF) method to estimate the element stable time increment for three-dimensional continuum elements and elements with plane stress formulations (shell, membrane, and two-dimensional plane stress elements). The default value is ON.

### Return value

An ExplicitDynamicsStep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ExplicitDynamicsStep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ExplicitDynamicsStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-explicitdynamicssteppyc.htm?ContextScope=all#simaker-explicitdynamicsstepexplicitdynamicssteppyc)method, except for the *name*, *previous*, and *maintainAttributes* arguments.

### Return value

None.

### Exceptions

RangeError.



## Members

The ExplicitDynamicsStep object can have the following members:

- *name*

  A String specifying the repository key.

- *timePeriod*

  A Float specifying the total time period for the step. The default value is 1.0.

- *nlgeom*

  A Boolean specifying whether geometric nonlinearities should be accounted for during the step. The default value is ON.

- *adiabatic*

  A Boolean specifying that an adiabatic stress analysis is to be performed. The default value is OFF.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default value is AUTOMATIC_GLOBAL.

- *maxIncrement*

  None or a Float specifying the maximum time increment. If there is no upper limit, *maxIncrement*=None. This argument is required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.

- *scaleFactor*

  A Float specifying the factor that is used to scale the time increment. This argument is required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or FIXED_EBE. The default value is 1.0.

- *linearBulkViscosity*

  A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.

- *quadBulkViscosity*

  A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is 1.2.

- *userDefinedInc*

  None or a Float specifying the user-defined time increment. This argument is required only when *timeIncrementationMethod*=FIXED_USER_DEFINED_INC. The default value is None.

- *improvedDtMethod*

  A Boolean specifying whether to use the "improved" (*improvedDtMethod*=ON) or "conservative" (*improvedDtMethod*=OFF) method to estimate the element stable time increment for three-dimensional continuum elements and elements with plane stress formulations (shell, membrane, and two-dimensional plane stress elements). The default value is ON.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *massScaling*

  A [MassScalingArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-massscalingpyc.htm?ContextScope=all) object specifying mass scaling controls. The default value is PREVIOUS_STEP.

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

- [BULK VISCOSITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-bulkviscosity.htm?ContextScope=all#simakey-r-bulkviscosity)
- [DYNAMIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dynamic.htm?ContextScope=all#simakey-r-dynamic)
- [FIXED MASS SCALING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-fixedmassscaling.htm?ContextScope=all#simakey-r-fixedmassscaling)
- [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step)
- [VARIABLE MASS SCALING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-variablemassscaling.htm?ContextScope=all#simakey-r-variablemassscaling)