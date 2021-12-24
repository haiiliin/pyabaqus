# SolutionDependentAmplitude object

The SolutionDependentAmplitude object defines a solution-dependent amplitude for superplastic forming analysis.

The SolutionDependentAmplitude object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## SolutionDependentAmplitude(...)



This method creates a SolutionDependentAmplitude object.



### Path

```
mdb.models[name].SolutionDependentAmplitude
session.odbs[name].SolutionDependentAmplitude
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *initial*

  A Float specifying the initial amplitude value. Possible values are those between *minimum* and *maximum*. The default value is 1.0.

- *minimum*

  A Float specifying the minimum amplitude value. Possible values are those smaller than *maximum* and *initial*. The default value is 0.1.

- *maximum*

  A Float specifying the maximum amplitude value. Possible values are those larger than *minimum* and *initial*. The default value is 1000.0.

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

### Return value

A SolutionDependentAmplitude object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the SolutionDependentAmplitude object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SolutionDependentAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solutiondependentamplitudepyc.htm?ContextScope=all#simaker-solutiondependentamplitudesolutiondependentamplitudpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The SolutionDependentAmplitude object has members with the same names and descriptions as the arguments to the [SolutionDependentAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solutiondependentamplitudepyc.htm?ContextScope=all#simaker-solutiondependentamplitudesolutiondependentamplitudpyc)method.



## Corresponding analysis keywords

- [AMPLITUDE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-amplitude.htm?ContextScope=all#simakey-r-amplitude)