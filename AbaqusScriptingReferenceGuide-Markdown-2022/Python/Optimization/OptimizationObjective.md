# OptimizationObjective object

An OptimizationObjective is an object used to define objectives in an objective function.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].objectiveFunctions[name]\
        .objectives[i]
      
```

## Members

The OptimizationObjective object has the following members:

- *suppress*

  A Boolean specifying whether the objective is suppressed or not. The default value is OFF.

- *weight*

  A Float specifying the weight applied to the design response value. The default value is 1.0.

- *referenceValue*

  The SymbolicConstant DEFAULT or a Float specifying the reference value used in evaluating a design response. For topology optimization, DEFAULT> indicates the reference value is 0. For shape optimization, DEFAULT indicates the reference value is the nodal average. The default value is DEFAULT.

- *designResponse*

  A String specifying the name of the design response.