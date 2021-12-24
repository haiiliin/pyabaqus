# OptimizationConstraint object

The OptimizationConstraint object constrains an optimization from making changes to the topology of the model.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].optimizationConstraints[name]
      
```

## OptimizationConstraint(...)



This method creates an OptimizationConstraint object.



### Path

```
          mdb.models[name].optimizationTasks[name].OptimizationConstraint
        
```

### Required arguments

- *name*

  A String specifying the optimization constraint repository key.

- *designResponse*

  A String specifying the name of the design response to constrain.

- *restrictionValue*

  A Float specifying the value to which the design response should be constrained.

### Optional arguments

- *restrictionMethod*

  A SymbolicConstant specifying the method used to constrain the design response. Possible values are ABSOLUTE_EQUAL, ABSOLUTE_GREATER_THAN_EQUAL, ABSOLUTE_LESS_THAN_EQUAL, RELATIVE_EQUAL, RELATIVE_GREATER_THAN_EQUAL, and RELATIVE_LESS_THAN_EQUAL. The default value is ABSOLUTE_EQUAL.

### Return value

An OptimizationConstraint object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the OptimizationConstraint object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [OptimizationConstraint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationconstraintpyc.htm?ContextScope=all#simaker-optimizationconstraintoptimizationconstraintpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The OptimizationConstraint object has members with the same names and descriptions as the arguments to the [OptimizationConstraint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationconstraintpyc.htm?ContextScope=all#simaker-optimizationconstraintoptimizationconstraintpyc)method.