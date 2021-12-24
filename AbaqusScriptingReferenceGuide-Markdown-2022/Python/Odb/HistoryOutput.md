# HistoryOutput object

The HistoryOutput object contains the history output at a point for the specified variable.

## Access

```
import odbAccess
session.odbs[name].steps[name].historyRegions[name]\
.historyOutputs[name]
```

## HistoryOutput(...)



This method creates a HistoryOutput object.



### Path

```
session.odbs[name].steps[name].historyRegions[name].HistoryOutput
```

### Required arguments

- *name*

  A String specifying the output variable name.

- *description*

  A String specifying the output variable.

- *type*

  A SymbolicConstant specifying the output type. Only SCALAR is currently supported.

### Optional arguments

- *validInvariants*

  A sequence of SymbolicConstants specifying which invariants should be calculated for this field. Possible values are MAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL, MID_PRINCIPAL, and MIN_PRINCIPAL. The default value is an empty sequence.

### Return value

A HistoryOutput object.

### Exceptions

None.



## addData(...)



This method adds data to the *data* member of the HistoryOutput object.



### Required arguments

- *frame*

  A Double specifying the frame value. *frame* can be specified in step time, frequency, or mode number.

- *value*

  A Double specifying the value of the variable at the frame value specified in *frame*.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## addData(...)



This method adds data to the *data* member of the HistoryOutput object.



### Required arguments

- *frame*

  A sequence of Floats specifying the frame values. *frame* can be specified in step time, frequency, or mode number.

- *value*

  A sequence of Floats specifying the value of the variable at the frame values specified in *frame*.

### Optional arguments

None.

### Return value

None.

### Exceptions

If the length of *frame* is not the same as the length of *value* a ValueError is raised.



## addData(...)



This method adds data to the *data* member of the HistoryOutput object.



### Required arguments

- *data*

  A sequence of pairs of Floats specifying the pairs (*frameValue*, *value*) where *frameValue* is either time, frequency, or mode and *value* is the value of the specified variable at *frameValue*. (This value depends on the type of the variable.)

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The HistoryOutput object has members with the same names and descriptions as the arguments to the [HistoryOutput ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputpyc.htm?ContextScope=all#simaker-historyoutputhistoryoutputpyc)method.

In addition, the HistoryOutput object has the following members:

- *data*

  A tuple of pairs of Floats specifying the pairs (*frameValue*, *value*) where *frameValue* is either time, frequency, or mode and *value* is the value of the specified variable at *frameValue*. (This value depends on the type of the variable.)

- *conjugateData*

  A tuple of pairs of Floats specifying the imaginary portion of a specified complex variable at each frame value (time, frequency, or mode). The pairs have the form (*frameValue*, *value*).