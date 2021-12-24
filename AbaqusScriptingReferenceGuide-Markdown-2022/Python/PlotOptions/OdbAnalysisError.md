# OdbAnalysisError object

The OdbAnalysisError object stores the description of different errors encountered during the analysis.

## Access

```
        import visualization
        session.odbData[name].diagnosticData.analysisErrors[i]
      
```

## Members

The OdbAnalysisError object has the following members:

- *incrementNumber*

  An int specifying the increment number where the analysis was aborted. This attribute is read-only.

- *iterationNumber*

  An int specifying the iteration number where the analysis was aborted. This attribute is read-only.

- *attemptNumber*

  An int specifying the attempt number on which the analysis was aborted. This attribute is read-only.

- *category*

  String specifying the category of error. This attribute is read-only.

- *data*

  An [OdbAuxiliaryData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbauxilliarydatapyc.htm?ContextScope=all) object.

- *description*

  String specifying the cause of the error. This attribute is read-only.

- *detailStrings*

  String specifying the exact nature of the problem. This attribute is read-only.

- *knowledgeItem*

  String specifying the exact reason for the error encountered. This attribute is read-only.

- *numberOfVariations*

  An int specifying the number of variations. This attribute is read-only.

- *stepNumber*

  An int specifying the step number on which the error was encountered. This attribute is read-only.