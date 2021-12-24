# StdXplCosimulation object

The StdXplCosimulation object defines co-simulation behavior between Abaqus/Standard and Abaqus/Explicit.

The StdXplCosimulation object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## StdXplCosimulation(...)



This method creates a StdXplCosimulation object.



### Path

```
mdb.models[name].StdXplCosimulation
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the StdXplCosimulation object is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the import and export region upon which the co-simulation exchanges data with the coupled analysis program.

### Optional arguments

- *incrementation*

  A SymbolicConstant specifying whether the analysis programs use the same time increments or one is allowed to use more time increments than the other before exchanging data. Possible values are ALLOW_SUBCYCLING and LOCKSTEP. The default value is ALLOW_SUBCYCLING.

- *stepSize*

  A Float specifying the size of the increments to be used by Abaqus/Standard and Abaqus/Explicit. The default value is 0.0.

- *stepSizeDefinition*

  A SymbolicConstant specifying whether the increment size is the analysis default or a supplied variable. Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.

### Return value

A StdXplCosimulation object.

### Exceptions

None.



## setValues(...)



This method modifies the StdXplCosimulation object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [StdXplCosimulation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdxplcosimulationpyc.htm?ContextScope=all#simaker-stdxplcosimulationstdxplcosimulationpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## Members

The StdXplCosimulation object has members with the same names and descriptions as the arguments to the [StdXplCosimulation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdxplcosimulationpyc.htm?ContextScope=all#simaker-stdxplcosimulationstdxplcosimulationpyc)method.