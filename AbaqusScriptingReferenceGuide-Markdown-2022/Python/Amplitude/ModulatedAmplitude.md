# ModulatedAmplitude object

The ModulatedAmplitude object defines a modulated amplitude curve.

The ModulatedAmplitude object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## ModulatedAmplitude(...)



This method creates a ModulatedAmplitude object.



### Path

```
mdb.models[name].ModulatedAmplitude
session.odbs[name].ModulatedAmplitude
```

### Required arguments

- *name*

  A String specifying the repository key.

- *initial*

  A Float specifying the constant A0A0.

- *magnitude*

  A Float specifying the coefficient AA.

- *start*

  A Float specifying the starting time t0t0. Possible values are non-negative numbers.

- *frequency1*

  A Float specifying the circular frequency 1 (ω1ω1). Possible values are positive numbers.

- *frequency2*

  A Float specifying the circular frequency 2 (ω2ω2). Possible values are positive numbers.

### Optional arguments

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

### Return value

A ModulatedAmplitude object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the ModulatedAmplitude object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ModulatedAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modulatedamplitudepyc.htm?ContextScope=all#simaker-modulatedamplitudemodulatedamplitudepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The ModulatedAmplitude object has members with the same names and descriptions as the arguments to the [ModulatedAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modulatedamplitudepyc.htm?ContextScope=all#simaker-modulatedamplitudemodulatedamplitudepyc)method.



## Corresponding analysis keywords

- [AMPLITUDE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-amplitude.htm?ContextScope=all#simakey-r-amplitude)