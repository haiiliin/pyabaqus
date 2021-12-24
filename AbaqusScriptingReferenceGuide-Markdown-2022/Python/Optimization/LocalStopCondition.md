# LocalStopCondition object

The LocalStopCondition object defines a local stop condition.

The LocalStopCondition object is derived from the [StopCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stopconditionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].stopConditions[name]
      
```

## LocalStopCondition(...)



This method creates a LocalStopCondition object.



### Path

```
          mdb.models[name].optimizationTasks[name].LocalStopCondition
        
```

### Required arguments

- *name*

  A String specifying the stop condition repository key.

- *referenceFactor*

  A Float specifying the factor used to modify the reference value.

### Optional arguments

- *comparisonOperation*

  A SymbolicConstant specifying the operation used to compare the selected value to the reference value. Possible values are LESS_THAN, LESS_THAN_EQUAL, EQUAL, GREATER_THAN_EQUAL, and GREATER_THAN. The default value is LESS_THAN.

- *identifier*

  A SymbolicConstant specifying the variable identifier of the compared value. Possible values are:

  - ABSOLUTE_GROWTH_MOVEMENT
  - ABSOLUTE_SHRINK_MOVEMENT
  - GROWTH_MOVEMENT
  - SHRINK_MOVEMENT
  - MOVEMENT
  - TOTAL_ABSOLUTE_MOVEMENT
  - EQUIV_STRESS
  - FREE_TASK_REGION_EQUIV_STRESS
  - RESTRICTED_TASK_REGION_EQUIV_STRESS
  - SURFACE_POINT_EQUIV_STRESS
  - TASK_REGION_EQUIV_STRESS

  The default value is MOVEMENT.

- *identifierOperation*

  A SymbolicConstant specifying the operation used to evaluate values in the region. Possible values are MAXIMUM, MINIMUM, and SUM. The default value is MAXIMUM.

- *referenceDesignCycle*

  A SymbolicConstant specifying the iteration from which a value is compared to the reference value. Possible values are FIRST and PREVIOUS. The default value is PREVIOUS.

- *referenceOperation*

  A SymbolicConstant specifying the operation used to modify the reference value by the reference factor. Possible values are ADD, DIVIDE, MULTIPLY, and SUBTRACT. The default value is ADD.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the stop condition is applied. The default value is MODEL.

### Return value

A LocalStopCondition object.

### Exceptions

None.



## setValues(...)



This method modifies the LocalStopCondition object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [LocalStopCondition ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-localstopconditionpyc.htm?ContextScope=all#simaker-localstopconditionlocalstopconditionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The LocalStopCondition object has members with the same names and descriptions as the arguments to the [LocalStopCondition ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-localstopconditionpyc.htm?ContextScope=all#simaker-localstopconditionlocalstopconditionpyc)method.