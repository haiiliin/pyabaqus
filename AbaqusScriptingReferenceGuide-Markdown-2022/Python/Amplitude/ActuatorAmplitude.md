# ActuatorAmplitude object

The ActuatorAmplitude object defines an actuator amplitude curve.

The ActuatorAmplitude object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## ActuatorAmplitude(...)



This method creates a ActuatorAmplitude object.



### Path

```
mdb.models[name].ActuatorAmplitude
session.odbs[name].ActuatorAmplitude
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

### Return value

An ActuatorAmplitude object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the ActuatorAmplitude object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ActuatorAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatoramplitudepyc.htm?ContextScope=all#simaker-actuatoramplitudeactuatoramplitudepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The ActuatorAmplitude object has members with the same names and descriptions as the arguments to the [ActuatorAmplitude ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatoramplitudepyc.htm?ContextScope=all#simaker-actuatoramplitudeactuatoramplitudepyc)method.



## Corresponding analysis keywords

- [AMPLITUDE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-amplitude.htm?ContextScope=all#simakey-r-amplitude)