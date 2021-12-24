# OdbDiagnosticIncrement object

The OdbDiagnosticIncrement object.

## Access

```
        import visualization
        session.odbData[name].diagnosticData.steps[i].increments[i]
      
```

## Members

The OdbDiagnosticIncrement object has the following members:

- *attempts*

  A repository of [OdbDiagnosticAttempt](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdiagnosticattemptpyc.htm?ContextScope=all) objects.

- *initialSize*

  A float specifying the size of the initial increment. This attribute is read-only.

- *isConverged*

  A boolean specifying whether the solution converged for the particular increment. This attribute is read-only.

- *numberOfAttempts*

  An int specifying the number of attempts for the particular increment. This attribute is read-only.

- *numberOfElementDiagnostics*

  An int specifying the number of element diagnostics encountered for the particular increment. This attribute is read-only.

- *size*

  A float specifying the size of the particular increment. This attribute is read-only.

- *stepTimeCompleted*

  A float specifying the amount of step time completed in the particular increment. This attribute is read-only.