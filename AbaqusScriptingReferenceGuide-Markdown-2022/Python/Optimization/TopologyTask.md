# TopologyTask object

The TopologyTask object defines a topology task.

The TopologyTask object is derived from the [OptimizationTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationtaskpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name]
      
```

## TopologyTask(...)



This method creates a TopologyTask object.



### Path

```
          mdb.models[name].TopologyTask
        
```

### Required arguments

- *name*

  A String specifying the optimization task repository key.

### Optional arguments

- *abaqusSensitivities*

  A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities. The default value is True.

- *algorithm*

  A SymbolicConstant specifying the optimization task algorithm. Possible values are GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is GENERAL_OPTIMIZATION.

- *densityMoveLimit*

  A Float specifying the maximum density change per design cycle. The default value is 0.25.

- *densityUpdateStrategy*

  A SymbolicConstant specifying the strategy for how the densities are updated in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.

- *elementDensityDeltaStopCriteria*

  A Float specifying the stop criteria based upon the change in element densities. The default value is 0.5×10–2.

- *filterRadius*

  None or a Float specifying the mesh filter radius for mesh independence and minimum size. The default value is None.

- *firstCycleDeletedVolume*

  A Float specifying the volume that can be removed immediately in the first design cycle. The default value is 5.0.

- *firstCycleDeletedVolumeTechnique*

  A SymbolicConstant specifying the method of quantifying volume that can be removed immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and ABSOLUTE. The default value is OFF.

- *freezeBoundaryConditionRegions*

  A Boolean specifying whether to exclude elements with boundary conditions from the optimization. The default value is OFF.

- *freezeLoadRegions*

  A Boolean specifying whether to exclude elements with loads and elements with loaded nodes from the optimization. The default value is ON.

- *frequencySpectrumWeight*

  A Float specifying the weighting factor for frequency spectrum peaks. The default value is 6.0.

- *initialDensity*

  A SymbolicConstant specifying the Optimization product default or a float specifying the initial density. The default value is DEFAULT.

- *materialInterpolationPenalty*

  A Float specifying the penalty factor for the material interpolation technique. The default value is 3.0.

- *materialInterpolationTechnique*

  A SymbolicConstant specifying the material interpolation technique: optimization product default, solid isotropic material with penalization, or rational approximation of material properties. Possible values are DEFAULT, SIMP, and RAMP. The default value is DEFAULT.

- *maxDensity*

  A Float specifying the maximum density in the density update. The default value is 1.0.

- *minDensity*

  A Float specifying the minimum density in the density update. The default value is 10–3.

- *modeTrackingRegion*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to use for mode tracking. The default value is MODEL.

- *numDesignCycles*

  An Int specifying the number of design cycles permitted when *stepSize* is DYNAMIC. The default value is 15.

- *numFulfilledStopCriteria*

  An Int specifying the number of stop criteria. The default value is 2.

- *numTrackedModes*

  An Int specifying the number of modes included in mode tracking. The default value is 5.

- *objectiveFunctionDeltaStopCriteria*

  A Float specifying the stop criteria based on the change in objective function. The default value is 10–3.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the optimization task is applied. The default value is MODEL.

- *softDeletionMethod*

  A SymbolicConstant specifying the method used when *softDeletionRegion* is specified. The STANDARD method avoids creating disconnected regions. The AGGRESSIVE method only considers the *softDeletionThreshold*. The MAX_SHEAR_STRAIN, MAX_ELASTOPLASTIC_STRAIN and VOLUME_COMPRESSION methods do not need the *softDeletionRadius*. Possible values are STANDARD, AGGRESSIVE, MAX_SHEAR_STRAIN, MIN_PRINCIPAL_STRAIN, MAX_ELASTOPLASTIC_STRAIN and VOLUME_COMPRESSION. The default value is STANDARD.

- *softDeletionRadius*

  A Float specifying the radius to use when considering neighboring soft elements to delete. The default value is 0.0.

- *softDeletionRegion*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region in which the soft elements should be deleted during optimization. The default value is None.

- *softDeletionThreshold*

  A Float specifying the relative material density value used to identify soft elements. Those with values below the threshold are considered for removal. For STANDARD and AGGRESSIVE methods positive values are accepted and the default value is 0.05. For MAX_SHEAR_STRAIN and MAX_ELASTOPLASTIC_STRAIN methods positive values are accepted whereas for MIN_PRINCIPAL_STRAIN and VOLUME_COMPRESSION methods negative values are accepted.

- *stepSize*

  A SymbolicConstant specifying the size of the increment for volume modification. Possible values are DYNAMIC, VERY_SMALL, SMALL, MODERATE, MEDIUM, and LARGE. The default value is MEDIUM.

- *stiffnessMassDamping*

  The SymbolicConstant AVERAGE_EDGE_LENGTH or a Float specifying the stiffness mass damping for the task region. The default value is AVERAGE_EDGE_LENGTH.

- *stopCriteriaDesignCycle*

  An Int specifying the first design cycle used to evaluate convergence criteria. The default value is 4.

- *structuralMassDamping*

  None or a Float specifying the structural mass damping for the task region. The default value is None.

- *viscousMassDamping*

  None or a Float specifying the viscous mass damping for the task region. The default value is None.

- *viscousStiffnessDamping*

  None or a Float specifying the viscous stiffness damping for the task region. The default value is None.

- *groupOperator*

  A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities. The default value of False means that the existing algorithm will be used.

### Return value

A TopologyTask object.

### Exceptions

None.



## setValues(...)



This method modifies the TopologyTask object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all#simaker-topologytasktopologytaskpyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The TopologyTask object has members with the same names and descriptions as the arguments to the [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all#simaker-topologytasktopologytaskpyc) method.

In addition, the TopologyTask object can have the following members:

- *designResponses*

  A repository of [DesignResponse](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designresponsepyc.htm?ContextScope=all) objects.

- *objectiveFunctions*

  A repository of [ObjectiveFunction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-objectivefunctionpyc.htm?ContextScope=all) objects.

- *optimizationConstraints*

  A repository of [OptimizationConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationconstraintpyc.htm?ContextScope=all) objects.

- *geometricRestrictions*

  A repository of [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) objects.

- *stopConditions*

  A repository of [StopCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stopconditionpyc.htm?ContextScope=all) objects.