# SmoothStepAmplitude object

The SmoothStepAmplitude object defines an amplitude that ramps up or down smoothly from one data point to another.

The SmoothStepAmplitude object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## SmoothStepAmplitude(...)



This method creates a SmoothStepAmplitude object.



### Path

```
mdb.models[name].SmoothStepAmplitude
session.odbs[name].SmoothStepAmplitude
```

### Required arguments

- *name*

  A String specifying the repository key.

- *data*

  A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible values for time/frequency are positive numbers.

### Optional arguments

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

### Return value

A SmoothStepAmplitude object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the SmoothStepAmplitude object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SmoothStepAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothstepamplitudepyc.htm?ContextScope=all#simaker-smoothstepamplitudesmoothstepamplitudepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The SmoothStepAmplitude object has members with the same names and descriptions as the arguments to the [SmoothStepAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothstepamplitudepyc.htm?ContextScope=all#simaker-smoothstepamplitudesmoothstepamplitudepyc)method.



## Corresponding analysis keywords

- [AMPLITUDE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-amplitude.htm?ContextScope=all#simakey-r-amplitude)