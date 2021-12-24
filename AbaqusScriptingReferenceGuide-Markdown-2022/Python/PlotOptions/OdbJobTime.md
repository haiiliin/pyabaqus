# OdbJobTime object

The OdbJobTime object stores the analysis time of a job.

## Access

```
        import visualization
        session.odbData[name].diagnosticData.jobTime
      
```

## Members

The OdbJobTime object has the following members:

- *systemTime*

  A float specifying the systemtime for the analysis. This attribute is read-only.

- *userTime*

  A float specifying the usertime for the analysis. This attribute is read-only.

- *wallclockTime*

  A float specifying the wallclocktime for the analysis. This attribute is read-only.