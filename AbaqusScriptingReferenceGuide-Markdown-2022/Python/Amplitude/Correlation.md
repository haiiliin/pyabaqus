# Correlation object

A Correlation is an object used to define the cross-correlation as part of the definition of random loading.

The Correlation object is derived from the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].boundaryConditions[name].correlation[i]
```

## Members

The Correlation object has the following members:

- *name*

  A String specifying the repository key.

- *approach*

  A SymbolicConstant specifying the approach used in the correlation data representation. Possible values are CORRELATED, MOVING_NOISE, UNCORRELATED, and USER. The default value is CORRELATED.

- *data*

  A tuple of tuples of Floats specifying the real and imaginary part of the scaling factor. If *approach*=MOVING_NOISE, then *data* represents the noise velocity components 1, 2, and 3.

- *timeSpan*

  A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP and TOTAL. The default value is STEP.