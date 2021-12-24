# StdStabilization object

The StdStabilization object is used in conjunction with [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) in Abaqus/Standard analyses to specify contact stabilization.

The StdStabilization object is derived from the [ContactStabilization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstabilizationpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].contactStabilizations[name]
```

## StdStabilization(...)



This method creates a StdStabilization object.



### Path

```
mdb.models[name].StdStabilization
```

### Required arguments

- *name*

  A String specifying the contact stabilization repository key.

### Optional arguments

- *zeroDistance*

  None or a Float specifying the clearance distance at which the stabilization becomes zero. The default value is None.

- *reductionFactor*

  A Float specifying the factor by which the analysis will reduce the contact stabilization coefficient per increment. The default value is 0.1.

- *scaleFactor*

  A Float specifying the factor by which the analysis will scale the contact stabilization coefficient. The default value is 1.0.

- *tangentialFactor*

  A Float specifying the factor that scales the contact stabilization coefficient in the tangential direction. The default value is 0.0.

- *amplitude*

  A String specifying the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that defines a time-dependent scale factor for contact stabilization over the step. The default value is an empty string.

- *reset*

  A Boolean specifying whether to cancel carryover effects from contact stabilization specifications involving nondefault amplitudes that appeared in previous steps. The default value is OFF.

### Return value

A StdStabilization object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the StdStabilization object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [StdStabilization ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdstabilizationpyc.htm?ContextScope=all#simaker-stdstabilizationstdstabilizationpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The StdStabilization object has members with the same names and descriptions as the arguments to the [StdStabilization ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdstabilizationpyc.htm?ContextScope=all#simaker-stdstabilizationstdstabilizationpyc)method.



## Corresponding analysis keywords

- [CONTACT STABILIZATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactstabilization.htm?ContextScope=all#simakey-r-contactstabilization)