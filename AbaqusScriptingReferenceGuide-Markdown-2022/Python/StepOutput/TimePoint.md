# TimePoint object

The TimePoint object defines time points at which data are written to the output database or restart files.

## Access

```
import step
mdb.models[name].timePoints[name]
```

## TimePoint(...)



This method creates a TimePoint object.



### Path

```
mdb.models[name].TimePoint
```

### Required arguments

- *name*

  A String specifying the repository key.

- *points*

  A sequence of sequences of Floats specifying time points at which data are written to the output database or restart files.

### Optional arguments

None.

### Return value

A TimePoint object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the TimePoint object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TimePoint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-timepointpyc.htm?ContextScope=all#simaker-timepointtimepointpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The TimePoint object has members with the same names and descriptions as the arguments to the [TimePoint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-timepointpyc.htm?ContextScope=all#simaker-timepointtimepointpyc)method.



## Corresponding analysis keywords

- [TIME POINTS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-timepoints.htm?ContextScope=all#simakey-r-timepoints)