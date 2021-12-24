# ObjectiveFunction object

The ObjectiveFunction object defines the objective of the optimization.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].objectiveFunctions[name]
      
```

## ObjectiveFunction(...)



This method creates an ObjectiveFunction object.



### Path

```
          mdb.models[name].optimizationTasks[name].ObjectiveFunction
        
```

### Required arguments

- *name*

  A String specifying the objective function repository key.

- *objectives*

  An [OptimizationObjectiveArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationobjectivepyc.htm?ContextScope=all) object.

### Optional arguments

- *target*

  A SymbolicConstant specifying the target of the objective function. Possible values are MINIMIZE, MAXIMIZE, and MINIMIZE_MAXIMUM. The default value is MINIMIZE.

### Return value

An ObjectiveFunction object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the ObjectiveFunction object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ObjectiveFunction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-objectivefunctionpyc.htm?ContextScope=all#simaker-objectivefunctionobjectivefunctionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The ObjectiveFunction object has members with the same names and descriptions as the arguments to the [ObjectiveFunction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-objectivefunctionpyc.htm?ContextScope=all#simaker-objectivefunctionobjectivefunctionpyc)method.