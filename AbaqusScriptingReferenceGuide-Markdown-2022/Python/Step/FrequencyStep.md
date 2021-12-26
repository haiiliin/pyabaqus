# FrequencyStep object

The FrequencyStep object is used to perform eigenvalue extraction to calculate the natural frequencies and corresponding mode shapes of a system.

The FrequencyStep object is derived from the [AnalysisStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analysissteppyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name]
```

## FrequencyStep(...)



This method creates a FrequencyStep object.



### Path

```
mdb.models[name].FrequencyStep
```

### Required arguments

- *name*

  A String specifying the repository key.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *eigensolver*

  A SymbolicConstant specifying the eigensolver. Possible values are LANCZOS, SUBSPACE, and AMS.The following optional arguments are ignored unless *eigensolver*=LANCZOS: *blockSize*, *maxBlocks*, *normalization*, *propertyEvaluationFrequency*.The following optional arguments are ignored unless *eigensolver*=LANCZOS or AMS: *minEigen*, *maxEigen*, and *acousticCoupling*.The following optional arguments are ignored unless *eigensolver*=AMS: *projectDamping*, *acousticRangeFactor*, *substructureCutoffMultiplier*, *firstCutoffMultiplier*, *secondCutoffMultiplier*, *residualModeRegion*, *regionalModeDof*, and *limitSavedEigenvectorRegion*.

### Optional arguments

- *numEigen*

  The SymbolicConstant ALL or an Int specifying the number of eigenvalues to be calculated or ALL. The default value is ALL.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *shift*

  A Float specifying the shift point in cycles per time. The default value is 0.0.

- *minEigen*

  None or a Float specifying the minimum frequency of interest in cycles per time. The default value is None.

- *maxEigen*

  None or a Float specifying the maximum frequency of interest in cycles per time. The default value is None.

- *vectors*

  None or an Int specifying the number of vectors used in the iteration. The default is the minimum of (2*n*, *n* + 8), where *n* is the number of eigenvalues requested. The default value is None.

- *maxIterations*

  An Int specifying the maximum number of iterations. The default value is 30.

- *blockSize*

  A SymbolicConstant specifying the size of the Lanczos block steps. The default value is DEFAULT.

- *maxBlocks*

  A SymbolicConstant specifying the maximum number of Lanczos block steps within each Lanczos run. The default value is DEFAULT.

- *normalization*

  A SymbolicConstant specifying the method for normalizing eigenvectors. Possible values are DISPLACEMENT and MASS. The default value is DISPLACEMENT.A value of DISPLACEMENT indicates normalizing the eigenvectors so that the largest displacement entry in each vector is unity. A value of MASS indicates normalizing the eigenvectors with respect to the structure's mass matrix, which results in scaling the eigenvectors so that the generalized mass for each vector is unity.

- *propertyEvaluationFrequency*

  None or a Float specifying the frequency at which to evaluate frequency-dependent properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. If the value is None, the analysis product will evaluate the stiffness associated with frequency-dependent springs and dashpots at zero frequency and will not consider the stiffness contributions from frequency-domain viscoelasticity in the step. The default value is None.

- *projectDamping*

  A Boolean specifying whether to include projection of viscous and structural damping operators during *AMS* eigenvalue extraction. Valid only when *eigenSolver*=AMS. The default value is ON.

- *acousticCoupling*

  A SymbolicConstant specifying the type of acoustic-structural coupling in models with acoustic and structural elements coupled using the [TIE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-tie.htm?ContextScope=all#simakey-r-tie) option or in models with ASI-type elements. Possible values are AC_ON, AC_OFF, and AC_PROJECTION. The default value is AC_ON.

- *acousticRangeFactor*

  A Float specifying the ratio of the maximum acoustic frequency to the maximum structural frequency. The default value is 1.0.

- *frictionDamping*

  A Boolean specifying whether to add to the damping matrix contributions due to friction effects. The default value is OFF.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *maintainAttributes*

  A Boolean specifying whether to retain attributes from an existing step with the same name. The default value is False.

- *simLinearDynamics*

  A Boolean specifying whether to activate the SIM-based linear dynamics procedures. The default value is OFF.

- *residualModes*

  A Boolean specifying whether to include residual modes from an immediately preceding Static, Linear Perturbation step. The default value is OFF.

- *substructureCutoffMultiplier*

  A Float specifying the cutoff frequency for substructure eigenproblems, defined as a multiplier of the maximum frequency of interest. The default value is 5.0.

- *firstCutoffMultiplier*

  A Float specifying the first cutoff frequency for a reduced eigenproblem, defined as a multiplier of the maximum frequency of interest. The default value is 1.7.

- *secondCutoffMultiplier*

  A Float specifying the second cutoff frequency for a reduced eigenproblem defined as a multiplier of the maximum frequency of interest. The default value is 1.1.

- *residualModeRegion*

  None or a sequence of Strings specifying the name of a region for which residual modes are requested. The default value is None.

- *residualModeDof*

  None or a sequence of Ints specifying the degree of freedom for which residual modes are requested. The default value is None.

- *limitSavedEigenvectorRegion*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying a region for which eigenvectors should be saved or the SymbolicConstant None representing the whole model. The default value is None.

### Return value

A FrequencyStep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the FrequencyStep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FrequencyStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-frequencysteppyc.htm?ContextScope=all#simaker-frequencystepfrequencysteppyc)method, except for the *name*, *previous*, and *maintainAttributes* arguments.

### Return value

None.

### Exceptions

RangeError.



## Members

The FrequencyStep object can have the following members:

- *name*

  A String specifying the repository key.

- *eigensolver*

  A SymbolicConstant specifying the eigensolver. Possible values are LANCZOS, SUBSPACE, and AMS.The following optional arguments are ignored unless *eigensolver*=LANCZOS: *blockSize*, *maxBlocks*, *normalization*, *propertyEvaluationFrequency*.The following optional arguments are ignored unless *eigensolver*=LANCZOS or AMS: *minEigen*, *maxEigen*, and *acousticCoupling*.The following optional arguments are ignored unless *eigensolver*=AMS: *projectDamping*, *acousticRangeFactor*, *substructureCutoffMultiplier*, *firstCutoffMultiplier*, *secondCutoffMultiplier*, *residualModeRegion*, *regionalModeDof*, and *limitSavedEigenvectorRegion*.

- *numEigen*

  The SymbolicConstant ALL or an Int specifying the number of eigenvalues to be calculated or ALL. The default value is ALL.

- *shift*

  A Float specifying the shift point in cycles per time. The default value is 0.0.

- *minEigen*

  None or a Float specifying the minimum frequency of interest in cycles per time. The default value is None.

- *maxEigen*

  None or a Float specifying the maximum frequency of interest in cycles per time. The default value is None.

- *vectors*

  None or an Int specifying the number of vectors used in the iteration. The default is the minimum of (2*n*, *n* + 8), where *n* is the number of eigenvalues requested. The default value is None.

- *maxIterations*

  An Int specifying the maximum number of iterations. The default value is 30.

- *blockSize*

  A SymbolicConstant specifying the size of the Lanczos block steps. The default value is DEFAULT.

- *maxBlocks*

  A SymbolicConstant specifying the maximum number of Lanczos block steps within each Lanczos run. The default value is DEFAULT.

- *normalization*

  A SymbolicConstant specifying the method for normalizing eigenvectors. Possible values are DISPLACEMENT and MASS. The default value is DISPLACEMENT.A value of DISPLACEMENT indicates normalizing the eigenvectors so that the largest displacement entry in each vector is unity. A value of MASS indicates normalizing the eigenvectors with respect to the structure's mass matrix, which results in scaling the eigenvectors so that the generalized mass for each vector is unity.

- *propertyEvaluationFrequency*

  None or a Float specifying the frequency at which to evaluate frequency-dependent properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. If the value is None, the analysis product will evaluate the stiffness associated with frequency-dependent springs and dashpots at zero frequency and will not consider the stiffness contributions from frequency-domain viscoelasticity in the step. The default value is None.

- *projectDamping*

  A Boolean specifying whether to include projection of viscous and structural damping operators during *AMS* eigenvalue extraction. Valid only when *eigenSolver*=AMS. The default value is ON.

- *acousticCoupling*

  A SymbolicConstant specifying the type of acoustic-structural coupling in models with acoustic and structural elements coupled using the [TIE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-tie.htm?ContextScope=all#simakey-r-tie) option or in models with ASI-type elements. Possible values are AC_ON, AC_OFF, and AC_PROJECTION. The default value is AC_ON.

- *acousticRangeFactor*

  A Float specifying the ratio of the maximum acoustic frequency to the maximum structural frequency. The default value is 1.0.

- *frictionDamping*

  A Boolean specifying whether to add to the damping matrix contributions due to friction effects. The default value is OFF.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *simLinearDynamics*

  A Boolean specifying whether to activate the SIM-based linear dynamics procedures. The default value is OFF.

- *residualModes*

  A Boolean specifying whether to include residual modes from an immediately preceding Static, Linear Perturbation step. The default value is OFF.

- *substructureCutoffMultiplier*

  A Float specifying the cutoff frequency for substructure eigenproblems, defined as a multiplier of the maximum frequency of interest. The default value is 5.0.

- *firstCutoffMultiplier*

  A Float specifying the first cutoff frequency for a reduced eigenproblem, defined as a multiplier of the maximum frequency of interest. The default value is 1.7.

- *secondCutoffMultiplier*

  A Float specifying the second cutoff frequency for a reduced eigenproblem defined as a multiplier of the maximum frequency of interest. The default value is 1.1.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *residualModeRegion*

  None or a tuple of Strings specifying the name of a region for which residual modes are requested. The default value is None.

- *residualModeDof*

  None or a tuple of Ints specifying the degree of freedom for which residual modes are requested. The default value is None.

- *limitSavedEigenvectorRegion*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying a region for which eigenvectors should be saved or the SymbolicConstant None representing the whole model. The default value is None.

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

- [FREQUENCY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-frequency.htm?ContextScope=all#simakey-r-frequency)
- [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step)