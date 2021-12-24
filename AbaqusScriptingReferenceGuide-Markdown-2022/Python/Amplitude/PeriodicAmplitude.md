# PeriodicAmplitude object

The PeriodicAmplitude object defines an amplitude curve using a Fourier series.

The PeriodicAmplitude object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## PeriodicAmplitude(...)



This method creates a PeriodicAmplitude object.



### Path

```
mdb.models[name].PeriodicAmplitude
session.odbs[name].PeriodicAmplitude
```

### Required arguments

- *name*

  A String specifying the repository key.

- *frequency*

  A Float specifying the circular frequency ωω. Possible values are positive numbers.

- *start*

  A Float specifying the starting time t0t0. Possible values are positive numbers.

- *a_0*

  A Float specifying the constant A0A0.

- *data*

  A sequence of pairs of Floats specifying AiAi and BiBi pairs.

### Optional arguments

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

### Return value

A PeriodicAmplitude object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the PeriodicAmplitude object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PeriodicAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-periodicamplitudepyc.htm?ContextScope=all#simaker-periodicamplitudeperiodicamplitudepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The PeriodicAmplitude object has members with the same names and descriptions as the arguments to the [PeriodicAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-periodicamplitudepyc.htm?ContextScope=all#simaker-periodicamplitudeperiodicamplitudepyc)method.



## Corresponding analysis keywords

- [AMPLITUDE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-amplitude.htm?ContextScope=all#simakey-r-amplitude)