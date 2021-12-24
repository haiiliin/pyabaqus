# SizingTask object

The SizingTask object defines a Sizing task.

The SizingTask object is derived from the [OptimizationTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationtaskpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name]
      
```

## SizingTask(...)



This method creates a SizingTask object.



### Path

```
          mdb.models[name].SizingTask
        
```

### Required arguments

- *name*

  A String specifying the optimization task repository key.

### Optional arguments

- *abaqusSensitivities*

  A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities. The default value is True.

- *elementThicknessDeltaStopCriteria*

  A Float specifying the stop criteria based on the change in element thickness. The default value is 0.5 × 10–2.

- *freezeBoundaryConditionRegions*

  A Boolean specifying whether to exclude elements with boundary conditions from the optimization. The default value is OFF.

- *freezeLoadRegions*

  A Boolean specifying whether to exclude elements with loads and elements with loaded nodes from the optimization. The default value is ON.

- *modeTrackingRegion*

  The SymbolicConstatnt MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to use for mode tracking. The default value is MODEL.

- *numFulfilledStopCriteria*

  An Int specifying the number of stop criteria. The default value is 2.

- *numTrackedModes*

  An Int specifying the number of modes included in mode tracking. The default value is 5.

- *objectiveFunctionDeltaStopCriteria*

  A Float specifying the stop criteria based on the change in objective function. The default value is 0.001.

- *stopCriteriaDesignCycle*

  An Int specifying the first design cycle used to evaluate convergence criteria. The default value is 4.

- *thicknessMoveLimit*

  A Float specifying the maximum change in thickness per design cycle. The default value is 0.25.

- *thicknessUpdateStrategy*

  A SymbolicConstant specifying the strategy for how the thickness is updated in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.

- *groupOperator*

  A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities. The default value of False means that the existing algorithm will be used.

### Return value

A SizingTask object.

### Exceptions

None.



## setValues(...)



This method modifies the SizingTask object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SizingTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingtaskpyc.htm?ContextScope=all#simaker-sizingtasksizingtaskpyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The SizingTask object has members with the same names and descriptions as the arguments to the [SizingTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingtaskpyc.htm?ContextScope=all#simaker-sizingtasksizingtaskpyc) method.

In addition, the SizingTask object can have the following members:

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