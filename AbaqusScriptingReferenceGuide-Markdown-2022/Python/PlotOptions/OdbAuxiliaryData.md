# OdbAuxiliaryData object

The OdbAuxiliaryData object stores auxiliary data related to the steps in the analysis.

## Access

```
         import visualization
         session.odbData[name].diagnosticData.analysisErrors[i].data[i]
         session.odbData[name].diagnosticData.analysisWarnings[i].data[i]
         session.odbData[name].diagnosticData.steps[i].contactDiagnostics[i].data[i]
      
```

## Members

The OdbAuxiliaryData object has the following members:

- *elementInstanceNames*

  A tuple consisting of element instance names. This attribute is read-only.

- *elementLabels*

  A tuple consisting of element label names. This attribute is read-only.

- *hasValues*

  A boolean specifying whether the OdbAuxiliaryData object has values in it. This attribute is read-only.

- *nodeInstanceNames*

  A tuple consisting of node instance names. This attribute is read-only.

- *nodeLables*

  A tuple consisting of node label names. This attribute is read-only.