# OdbDiagnosticStep object

The OdbDiagnosticStep object stores step data.

## Access

```
        import visualization
        session.odbData[name].diagnosticData.steps[i]
      
```

## extractData(...)



This method creates a temporary [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) object, with increments on the x-axis and requested output on the y-axis.



### Required arguments

- *incrementStatistics*

  An enum specifying the requested output variable for the data table. Possible enum values are NUM_ATTEMPTS (the number of attempts), NUM_SDI (the number of severe discontinuity iterations), NUM_EQI (the number of equivalent iterations), NUM_ITERS (the number of iterations), STEP_TIME (the cumulative step time until that increment) or INC_SIZE (the step time for each increment).

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The OdbDiagnosticStep object has the following members:

- *activeXplStatus*

  A Tuple of the status values. This attribute is read-only.

- *characteristicElementLength*

  A float specifying the characteristic element length for the step. This attribute is read-only.

- *contactDiagnostics*

  A repository of [OdbContactDiagnostic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbcontactdiagnosticspyc.htm?ContextScope=all) objects.

- *explicitIncrementStatus*

  A sequence of string specifying the explicit increment status. This attribute is read-only.

- *extrapolation*

  A String specifying the method (Linear or logarithmic) used for extrapolation. This attribute is read-only.

- *incrementationScheme*

  A String specifying the method of incrementation (Auto or fixed). This attribute is read-only.

- *incrementsCompleted*

  An int specifying the number of completed increments. This attribute is read-only.

- *increments*

  A repository of [OdbDiagnosticIncrement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdiagnosticincrementpyc.htm?ContextScope=all) objects.

- *initialTimeIncrement*

  A float specifying the initial increment size for the step. This attribute is read-only.

- *isNlgeom*

  A boolean specifying whether or not the effects of geometric nonlinearities are considered. This attribute is read-only.

- *isPerturbation*

  A boolean specifying whether or not the step is a perturbation step. This attribute is read-only.

- *isStabilized*

  A boolean specifying whether or not stabilization for the system in any form is considered. This attribute is read-only.

- *isRiks*

  A boolean specifying whether the step is static riks. This attribute is read-only.

- *isUnsymm*

  A boolean specifying whether the matrix storage is unsymmetric. This attribute is read-only.

- *matrixSolver*

  A string specifying the method of solving (Direct or Iterative). This attribute is read-only.

- *maximumNumberOfIncrements*

  An int specifying the maximum number of allowed increments in the step. This attribute is read-only.

- *maximumTimeIncrement*

  A float specifying the size of the allowed maximum time increment in the step. This attribute is read-only.

- *minimumTimeIncrement*

  A float specifying the size of the allowed minimum time increment in the step. This attribute is read-only.

- *name*

  A string specifying the name of the step. This attribute is read-only.

- *number*

  An int specifying the step number. This attribute is read-only.

- *numberOfContactDiagnostics*

  An int specifying the number of contact diagnostics encountered. This attribute is read-only.

- *numberOfIncrements*

  An int specifying the number of increments taken in the step to complete the solution. This attribute is read-only.

- *numberOfXplStatus*

  An int specifying the number of the explicit status. This attribute is read-only.

- *stabilizeFactor*

  A float specifying the stabilize factor. This attribute is read-only.

- *stepTimeCompleted*

  A float specifying the time taken for the completion of the step. This attribute is read-only.

- *timePeriod*

  A float specifying the duration for the step. This attribute is read-only.