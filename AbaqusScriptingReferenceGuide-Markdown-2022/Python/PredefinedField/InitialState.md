# InitialState object

The InitialState object stores the data for an initial state predefined field.

The InitialState object is derived from the [PredefinedField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].predefinedFields[name]
```

## InitialState(...)



This method creates an InitialState predefined field object.



### Path

```
mdb.models[name].InitialState
```

### Required arguments

- *name*

  A String specifying the repository key.

- *instances*

  A [PartInstanceArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object specifying the instances to which the predefined field is applied.

- *fileName*

  A String specifying the name of the job that generated the initial state data.

### Optional arguments

- *endStep*

  The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial state values are to be read or the SymbolicConstant LAST_STEP. The default value is LAST_STEP.

- *endIncrement*

  The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration of the step set in *endStep* or the SymbolicConstant STEP_END. The default value is STEP_END.

- *updateReferenceConfiguration*

  A Boolean specifying whether to update the reference configuration based on the import data. The default value is OFF.

### Return value

An InitialState object.

### Exceptions

None.



## setValues(...)



This method modifies the InitialState object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [InitialState ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-initialstatepyc.htm?ContextScope=all#simaker-initialstateinitialstatepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The InitialState object has members with the same names and descriptions as the arguments to the [InitialState ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-initialstatepyc.htm?ContextScope=all#simaker-initialstateinitialstatepyc)method.



## Corresponding analysis keywords

- [INSTANCE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-instance.htm?ContextScope=all#simakey-r-instance)