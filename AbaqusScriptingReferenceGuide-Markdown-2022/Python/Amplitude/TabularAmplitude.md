# TabularAmplitude object

The TabularAmplitude object defines an amplitude curve as a table of values at convenient points on the time scale.

The TabularAmplitude object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## TabularAmplitude(...)



This method creates a TabularAmplitude object.



### Path

```
mdb.models[name].TabularAmplitude
session.odbs[name].TabularAmplitude
```

### Required arguments

- *name*

  A String specifying the repository key.

- *data*

  A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible values for time/frequency are positive numbers.

### Optional arguments

- *smooth*

  The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. Possible float values are between 0 and 0.5. If *smooth*=SOLVER_DEFAULT, the default degree of smoothing will be determined by the solver. The default value is SOLVER_DEFAULT.

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

### Return value

A TabularAmplitude object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the TabularAmplitude object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TabularAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tabularamplitudepyc.htm?ContextScope=all#simaker-tabularamplitudetabularamplitudepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The TabularAmplitude object has members with the same names and descriptions as the arguments to the [TabularAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tabularamplitudepyc.htm?ContextScope=all#simaker-tabularamplitudetabularamplitudepyc)method.

In addition, the TabularAmplitude object can have the following member:

- *baselineCorrection*

  A [BaselineCorrection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baselinecorrectionpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [AMPLITUDE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-amplitude.htm?ContextScope=all#simakey-r-amplitude)