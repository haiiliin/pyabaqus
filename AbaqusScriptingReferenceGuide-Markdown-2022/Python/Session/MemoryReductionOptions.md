# MemoryReductionOptions object

The MemoryReductionOptions object controls the default settings that Abaqus/CAE uses for running in reduced memory mode. The MemoryReductionOptions object has no constructor. Abaqus creates the *MemoryReductionOptions* member when a session is started.

## Access

```
session.memoryReductionOptions
```

## setValues(...)



This method modifies the MemoryReductionOptions object.



### Required arguments

None.

### Optional arguments

- *reducedMemoryMode*

  A Boolean specifying whether Abaqus/CAE should run in reduced memory mode. The default value is ON.

- *percentThreshold*

  A Float specifying the percent of *kernelMemoryLimit* at which the reduced memory mode starts. The default value is 75.0.

### Return value

None.

### Exceptions

None.



## Members

The MemoryReductionOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-memoryreductionoptionspyc.htm?ContextScope=all#simaker-memoryreductionoptionssetvaluespyc)method.