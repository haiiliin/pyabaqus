# OptimizationTask object

The OptimizationTask object is the abstract base type for other OptimizationTask objects. The OptimizationTask object has no explicit constructor. The methods and members of the OptimizationTask object are common to all objects derived from OptimizationTask.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name]
      
```

## Members

The OptimizationTask object can have the following members:

- *name*

  A String specifying the optimization task repository key.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the optimization task is applied. The default value is MODEL.

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