# SubstructureGenerateStep object

TheSubstructureGenerateStep object is used to generate a substructure.

The SubstructureGenerateStep object is derived from the [AnalysisStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analysissteppyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name]
```

## SubstructureGenerateStep(...)



This method creates a SubstructureGenerateStep object.



### Path

```
mdb.models[name].SubstructureGenerateStep
```

### Required arguments

- *name*

  A String specifying the repository key.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *substructureIdentifier*

  An Integer specifying a unique identifier for the substructure.

### Optional arguments

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *recoveryMatrix*

  A SymbolicConstant specifying the subtructure recovery to be computed. Possible values are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL.

- *recoveryRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region for substructure recovery. This argument is required when *recoveryMatrix*=REGION.

- *computeGravityLoadVectors*

  A Boolean specifying whether to compute the gravity load vectors. The default value is False.

- *computeReducedMassMatrix*

  A Boolean specifying whether to compute the reduced mass matrix. The default value is False.

- *computeReducedStructuralDampingMatrix*

  A Boolean specifying whether to compute the reduced structural damping matrix. The default value is False.

- *computeReducedViscousDampingMatrix*

  A Boolean specifying whether to compute the reduced viscous damping matrix. The default value is False.

- *evaluateFrequencyDependentProperties*

  A Boolean specifying whether to evaluate the frequency dependent properties. The default value is False.

- *frequency*

  A Float specifying the frequency at which to evaluate the frequency dependent properties. The default value is 0.0.

- *retainedEigenmodesMethod*

  A SymbolicConstant specifying the eigenmodes to be retained. Possible values are MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE.

- *modeRange*

  A [SubstructureGenerateModesArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructuregeneratemodespyc.htm?ContextScope=all) object.

- *frequencyRange*

  A [SubstructureGenerateFrequencyArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructuregeneratefrequencypyc.htm?ContextScope=all) object.

- *globalDampingField*

  A SymbolicConstant specifying the field to which the global damping factors should be applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is NONE.

- *alphaDampingRatio*

  A Float specifying the factor to create global Rayleigh mass proportional damping. The default value is 0.0.

- *betaDampingRatio*

  A Float specifying the factor to create global Rayleigh stiffness proportional damping. The default value is 0.0.

- *structuralDampingRatio*

  A Float specifying the factor to create frequency-independent stiffness proportional structural damping. The default value is 0.0.

- *viscousDampingControl*

  A SymbolicConstant specifying the damping control to include the viscous damping matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE.

- *structuralDampingControl*

  A SymbolicConstant specifying the damping control to include the structural damping matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE.

### Return value

A SubstructureGenerateStep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the SubstructureGenerateStep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SubstructureGenerateStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructuregeneratesteppyc.htm?ContextScope=all#simaker-substructuregeneratestepsubstructuregeneratesteppyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The SubstructureGenerateStep object can have the following members:

- *name*

  A String specifying the repository key.

- *recoveryMatrix*

  A SymbolicConstant specifying the subtructure recovery to be computed. Possible values are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL.

- *frequency*

  A Float specifying the frequency at which to evaluate the frequency dependent properties. The default value is 0.0.

- *retainedEigenmodesMethod*

  A SymbolicConstant specifying the eigenmodes to be retained. Possible values are MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE.

- *globalDampingField*

  A SymbolicConstant specifying the field to which the global damping factors should be applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is NONE.

- *alphaDampingRatio*

  A Float specifying the factor to create global Rayleigh mass proportional damping. The default value is 0.0.

- *betaDampingRatio*

  A Float specifying the factor to create global Rayleigh stiffness proportional damping. The default value is 0.0.

- *structuralDampingRatio*

  A Float specifying the factor to create frequency-independent stiffness proportional structural damping. The default value is 0.0.

- *viscousDampingControl*

  A SymbolicConstant specifying the damping control to include the viscous damping matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE.

- *structuralDampingControl*

  A SymbolicConstant specifying the damping control to include the structural damping matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *substructureIdentifier*

  A String specifying a unique identifier for the substructure. The default value is an empty string.

- *recoveryRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region for substructure recovery. This argument is required when *recoveryMatrix*=REGION.

- *frequencyRange*

  A [SubstructureGenerateFrequencyArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructuregeneratefrequencypyc.htm?ContextScope=all) object.

- *modeRange*

  A [SubstructureGenerateModesArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructuregeneratemodespyc.htm?ContextScope=all) object.

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

- [SUBSTRUCTURE GENERATE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-substructuregenerate.htm?ContextScope=all#simakey-r-substructuregenerate)
- [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step)