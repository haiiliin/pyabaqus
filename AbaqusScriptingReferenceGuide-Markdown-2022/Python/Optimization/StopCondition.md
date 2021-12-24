# StopCondition object

The StopCondition object is the abstract base type for other StopCondition objects. The StopCondition object has no explicit constructor. The methods and members of the StopCondition object are common to all objects derived from StopCondition.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].stopConditions[name]
      
```

## Members

The StopCondition object can have the following members:

- *name*

  A String specifying the stop condition repository key.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the stop condition is applied. The default value is MODEL.