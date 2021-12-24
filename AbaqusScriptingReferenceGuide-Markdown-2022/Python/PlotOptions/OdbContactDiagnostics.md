# OdbContactDiagnostics object

The OdbDiagnosticContact object.

## Access

```
        import visualization
        session.odbData[name].diagnosticData.steps[i].contactDiagnostics[i]
      
```

## Members

The OdbContactDiagnostic object has the following members:

- *data*

  A repository of [OdbAuxiliaryData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbauxilliarydatapyc.htm?ContextScope=all) objects. This attribute is read-only.

- *description*

  A string specifying the opening/overclosure status of the contact. This attribute is read-only.

- *detailStrings*

  A sequence of strings specifying the nature of each of the contact pair. This attribute is read-only.

- *type*

  A string specifying the type of contact initialization. This attribute is read-only.

- *defaultFormats*

  A string specifying the default format value. This attribute is read-only.

- *elementDescriptions*

  A string specifying the element description. This attribute is read-only.

- *nodeDescriptions*

  A string specifying the node description. This attribute is read-only.