# PsdDefinition object

The PsdDefinition object defines the cross-spectral density frequency function for random response loading.

The PsdDefinition object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import amplitude
mdb.models[name].amplitudes[name]
import odbAmplitude
session.odbs[name].amplitudes[name]
```

## PsdDefinition(...)



This method creates a PsdDefinition object.



### Path

```
mdb.models[name].PsdDefinition
session.odbs[name].PsdDefinition
```

### Required arguments

- *name*

  A String specifying the repository key.

- *data*

  A sequence of sequences of Floats specifying the real part of the frequency function, the imaginary part of the frequency function, and the frequency or frequency band number values, depending on the value of *unitType*.

### Optional arguments

- *unitType*

  A SymbolicConstant specifying the type of units for specifying the frequency function. FORCE implies power units. BASE implies gravity used to define base motion. DB implies decibel units. Possible values are FORCE, BASE, and DB. The default value is FORCE.

- *referenceGravityAcceleration*

  A Float specifying the reference gravity acceleration. This argument applies when *unitType* = BASE. The default value is 1.0.

- *referenecePower*

  A Float specifying the reference power value, in load units squared. This argument applies when *unitType* = DB. The default value is 0.0.

- *user*

  A Boolean specifying whether the frequency function is defined in user subroutine UPSD. If specified, then *data* is not applicable, and the *unitType* value must not be DB. The default value is OFF.

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.

- *amplitude*

  A String specifying the name of the amplitude that describes the dynamic event used to define the cross-spectral density frequency function. The default value is an empty string.

### Return value

A PsdDefinition object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the PsdDefinition object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PsdDefinition ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psddefinitionpyc.htm?ContextScope=all#simaker-psddefinitionpsddefinitionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The PsdDefinition object has members with the same names and descriptions as the arguments to the [PsdDefinition ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psddefinitionpyc.htm?ContextScope=all#simaker-psddefinitionpsddefinitionpyc)method.



## Corresponding analysis keywords

- [PSD-DEFINITION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-psd-definition.htm?ContextScope=all#simakey-r-psd-definition)