# EquallySpacedAmplitude object

The EquallySpacedAmplitude object defines a list of amplitude values at fixed time intervals beginning at a specified value of time.

The EquallySpacedAmplitude object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## EquallySpacedAmplitude(...)



This method creates an EquallySpacedAmplitude object.



### Path

```
mdb.models[name].EquallySpacedAmplitude
session.odbs[name].EquallySpacedAmplitude
```

### Required arguments

- *name*

  A String specifying the repository key.

- *fixedInterval*

  A Float specifying the fixed time interval at which the amplitude data are given. Possible values are positive numbers.

- *data*

  A sequence of Floats specifying the amplitude values.

### Optional arguments

- *begin*

  A Float specifying the time at which the first amplitude data are given. Possible values are non-negative numbers. The default value is 0.0.

- *smooth*

  The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. Possible float values are 0 ≤≤ *smoothing* ≤≤ 0.5. If *smooth*=SOLVER_DEFAULT, the default degree of smoothing will be determined by the solver. The default value is SOLVER_DEFAULT.

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

### Return value

An EquallySpacedAmplitude object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the EquallySpacedAmplitude object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [EquallySpacedAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equallyspacedamplitudepyc.htm?ContextScope=all#simaker-equallyspacedamplitudeequallyspacedamplitudepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The EquallySpacedAmplitude object has members with the same names and descriptions as the arguments to the [EquallySpacedAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equallyspacedamplitudepyc.htm?ContextScope=all#simaker-equallyspacedamplitudeequallyspacedamplitudepyc)method.

In addition, the EquallySpacedAmplitude object can have the following member:

- *baselineCorrection*

  A [BaselineCorrection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baselinecorrectionpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [AMPLITUDE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-amplitude.htm?ContextScope=all#simakey-r-amplitude)