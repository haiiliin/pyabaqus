# BaselineCorrection object

The BaselineCorrection object modifies an acceleration history to minimize the overall drift of the displacement obtained from the time integration of the given acceleration.

## Access

```
import amplitude
mdb.models[name].amplitudes[name].baselineCorrection
import odbAmplitude
session.odbs[name].amplitudes[name].baselineCorrection
```

## BaselineCorrection(...)



This method creates a BaselineCorrection object.



### Path

```
mdb.models[name].amplitudes[name].BaselineCorrection
session.odbs[name].amplitudes[name].BaselineCorrection
```

### Required arguments

None.

### Optional arguments

- *intervals*

  A sequence of Floats specifying the correction time interval end points. Possible values are positive and monotonically increasing Floats. The default value is an empty sequence.

### Return value

A BaselineCorrection object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the BaselineCorrection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BaselineCorrection ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baselinecorrectionpyc.htm?ContextScope=all#simaker-baselinecorrectionbaselinecorrectionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The BaselineCorrection object has members with the same names and descriptions as the arguments to the [BaselineCorrection ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baselinecorrectionpyc.htm?ContextScope=all#simaker-baselinecorrectionbaselinecorrectionpyc)method.



## Corresponding analysis keywords

- [BASELINE CORRECTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-baselinecorrection.htm?ContextScope=all#simakey-r-baselinecorrection)