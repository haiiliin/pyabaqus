# OdbDiagnosticData object

The OdbDiagnosticData object.

## Access

```
        import visualization
        session.odbData[name].diagnosticData
      
```

## Members

The OdbDiagnosticData object has the following members:

- *analysisErrors*

  A repository of [OdbAnalysisError](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbanalysiserrorpyc.htm?ContextScope=all) objects.

- *analysisWarnings*

  A repository of [OdbAnalysisWarning](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbanalysiswarningpyc.htm?ContextScope=all) objects.

- *steps*

  A repository of [OdbDiagnosticStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdiagnosticsteppyc.htm?ContextScope=all) objects.

- *jobTime*

  An [OdbJobTime](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbjobtimepyc.htm?ContextScope=all) object.

- *numericalProblemSummary*

  An [OdbNumericalProblemSummary](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbnumericalproblemsummarypyc.htm?ContextScope=all) object.

- *isXplDoublePrecision*

  A boolean specifying whether or not double precision is used for the analysis. This attribute is read-only.

- *jobStatus*

  A String specifying the job status after the analysis. This attribute is read-only.

- *numDomains*

  An int specifying the number of domains. This attribute is read-only.

- *numberOfAnalysisErrors*

  An int specifying the number of analysis errors encountered. This attribute is read-only.

- *numberOfAnalysisWarnings*

  An int specifying the number of analysis warnings encountered. This attribute is read-only.

- *numberOfSteps*

  An int specifying the number of steps present in the analysis. This attribute is read-only.