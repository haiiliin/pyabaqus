# SubstructureLoad object

The SubstructureLoad object defines a substructure load.

The SubstructureLoad object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## SubstructureLoad(...)



This method creates a SubstructureLoad object.



### Path

```
mdb.models[name].SubstructureLoad
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the substructure load is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

- *loadCaseNames*

  A list of names of the load cases that should be activated by this substructure load.

- *magnitude*

  A Float specifying the multiplier for the load case magnitude.

### Optional arguments

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

A SubstructureLoad object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing SubstructureLoad object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SubstructureLoad ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructureloadpyc.htm?ContextScope=all#simaker-substructureloadsubstructureloadpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing SubstructureLoad object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *loadCaseNames*

  A list of names of the load cases that should be activated by this substructure load.

- *magnitude*

  A Float specifying the multiplier for the load case magnitude.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the load has no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The SubstructureLoad object can have the following members:

- *name*

  A String specifying the load repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.