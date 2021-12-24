# OdbDiagnosticAttempt object

The OdbDiagnosticAttempt object.

## Access

```
         import visualization
         session.odbData[name].diagnosticData.steps[i].increments[i].attempts[i]
      
```

## Members

The OdbDiagnosticAttempt object has the following members:

- *autoStabilize*

  A boolean specifying the state of Auto-stablilization. This attribute is read-only.

- *isConverged*

  A boolean specifying the state of convergence for the attempt. This attribute is read-only.

- *isCutBack*

  A boolean specifying the state of cutback. This attribute is read-only.

- *needsReordering*

  A boolean specifying whether or not reordering is needed. This attribute is read-only.

- *numberOfCutbackDiagnostics*

  An int specifying the number of cutback diagnostics. This attribute is read-only.

- *numberOfIterations*

  An int specifying the number of iterations for the particular attempt. This attribute is read-only.

- *numberOfSevereDiscontinuityIterations*

  An int specifying the number of iterations with severe discontinuities This attribute is read-only.

- *size*

  A float specifying the size of the increment of the particular attempt. This attribute is read-only.