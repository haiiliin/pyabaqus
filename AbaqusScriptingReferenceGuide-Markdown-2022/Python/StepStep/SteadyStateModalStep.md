# SteadyStateModalStep object

he SteadyStateModalStep object is used to calculate the linearized steady-state response of the system to harmonic excitation.

The SteadyStateModalStep object is derived from the [AnalysisStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analysissteppyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name]
```

## SteadyStateModalStep(...)



This method creates a SteadyStateModalStep object.



### Path

```
mdb.models[name].SteadyStateModalStep
```

### Required arguments

- *name*

  A String specifying the repository key.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *frequencyRange*

  A [SteadyStateModalFrequencyArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steadystatemodalfrequencypyc.htm?ContextScope=all) object.

### Optional arguments

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *scale*

  A SymbolicConstant specifying whether a logarithmic or linear scale is used for output. Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.

- *directDamping*

  A [DirectDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-directdampingpyc.htm?ContextScope=all) object.

- *compositeDamping*

  A [CompositeDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositedampingpyc.htm?ContextScope=all) object.

- *rayleighDamping*

  A [RayleighDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rayleighdampingpyc.htm?ContextScope=all) object.

- *structuralDamping*

  A [StructuralDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-structuraldampingpyc.htm?ContextScope=all) object.

- *directDampingByFrequency*

  A [DirectDampingByFrequency](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-directdampingbyfrequencypyc.htm?ContextScope=all) object.

- *rayleighDampingByFrequency*

  A [RayleighDampingByFrequency](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rayleighdampingbyfrequencypyc.htm?ContextScope=all) object.

- *structuralDampingByFrequency*

  A [StructuralDampingByFrequency](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-structuraldampingbyfrequencypyc.htm?ContextScope=all) object.

- *maintainAttributes*

  A Boolean specifying whether to retain attributes from an existing step with the same name. The default value is False.

- *subdivideUsingEigenfrequencies*

  A Boolean specifying whether to subdivide each frequency range using the eigenfrequencies of the system. The default value is ON.

### Return value

A SteadyStateModalStep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the SteadyStateModalStep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SteadyStateModalStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steadystatemodalsteppyc.htm?ContextScope=all#simaker-steadystatemodalstepsteadystatemodalsteppyc)method, except for the *name*, *previous*, and *maintainAttributes* arguments.

### Return value

None.

### Exceptions

RangeError.



## Members

The SteadyStateModalStep object can have the following members:

- *name*

  A String specifying the repository key.

- *scale*

  A SymbolicConstant specifying whether a logarithmic or linear scale is used for output. Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.

- *subdivideUsingEigenfrequencies*

  A Boolean specifying whether to subdivide each frequency range using the eigenfrequencies of the system. The default value is ON.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *frequencyRange*

  A [SteadyStateModalFrequencyArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steadystatemodalfrequencypyc.htm?ContextScope=all) object.

- *directDamping*

  A [DirectDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-directdampingpyc.htm?ContextScope=all) object.

- *compositeDamping*

  A [CompositeDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositedampingpyc.htm?ContextScope=all) object.

- *rayleighDamping*

  A [RayleighDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rayleighdampingpyc.htm?ContextScope=all) object.

- *structuralDamping*

  A [StructuralDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-structuraldampingpyc.htm?ContextScope=all) object.

- *directDampingByFrequency*

  A [DirectDampingByFrequency](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-directdampingbyfrequencypyc.htm?ContextScope=all) object.

- *rayleighDampingByFrequency*

  A [RayleighDampingByFrequency](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rayleighdampingbyfrequencypyc.htm?ContextScope=all) object.

- *structuralDampingByFrequency*

  A [StructuralDampingByFrequency](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-structuraldampingbyfrequencypyc.htm?ContextScope=all) object.

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

- [DAMPING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damping.htm?ContextScope=all#simakey-r-damping)
- [MODAL DAMPING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-modaldamping.htm?ContextScope=all#simakey-r-modaldamping)
- [STEADY STATE DYNAMICS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-steadystatedynamics.htm?ContextScope=all#simakey-r-steadystatedynamics)
- [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step)