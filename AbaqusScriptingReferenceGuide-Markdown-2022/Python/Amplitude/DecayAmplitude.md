# DecayAmplitude object

The DecayAmplitude object defines an amplitude curve using an exponential decay.

The DecayAmplitude object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## DecayAmplitude(...)



This method creates a DecayAmplitude object.



### Path

```
mdb.models[name].DecayAmplitude
session.odbs[name].DecayAmplitude
```

### Required arguments

- *name*

  A String specifying the repository key.

- *initial*

  A Float specifying the constant A0A0.

- *maximum*

  A Float specifying the coefficient AA.

- *start*

  A Float specifying the starting time t0t0. Possible values are non-negative numbers.

- *decayTime*

  A Float specifying the decay time tdtd. Possible values are non-negative numbers.

### Optional arguments

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

### Return value

A DecayAmplitude object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the DecayAmplitude object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DecayAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-decayamplitudepyc.htm?ContextScope=all#simaker-decayamplitudedecayamplitudepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The DecayAmplitude object has members with the same names and descriptions as the arguments to the [DecayAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-decayamplitudepyc.htm?ContextScope=all#simaker-decayamplitudedecayamplitudepyc)method.



## Corresponding analysis keywords

- [AMPLITUDE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-amplitude.htm?ContextScope=all#simakey-r-amplitude)