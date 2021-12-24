# DataSet object

The DataSetobject specifies material test data.

## Access

```
        import calibration
        mdb.models[name].calibrations[name].dataSets[name]
      
```

## DataSet(...)



This method creates a DataSet object.



### Path

```
          mdb.models[name].calibrations[name].DataSet
        
```

### Required arguments

- *name*

  A String specifying the name of the new dataset.

### Optional arguments

- *data*

  A sequence of pairs of Floats specifying data set type pairs. Possible values are for stress/strain, force/displacement, or transverse strain/axial strain pairs.

- *type*

  A String specifying the type of the new dataset. Values can be "STRESS/STRAIN", "FORCE/DISPLACEMENT", or "AXIALSTRAIN/TRANSVERSESTRAIN". The default value is "STRESS/STRAIN".

- *form*

  A String specifying the form of the new dataset. Values can be "NOMINAL" or "TRUE". The default value is "NOMINAl".

### Return value

A DataSet object.

### Exceptions

InvalidNameError.



## setValues(...)



This method modifies the data for an existing DataSet object.



### Required arguments

None.

### Optional arguments

- *data*

  A sequence of pairs of Floats specifying data set type pairs.

### Return value

None.

### Exceptions

None.



## Members

The DataSet object has members with the same names and descriptions as the arguments to the [DataSet ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datasetpyc.htm?ContextScope=all#simaker-datasetdatasetpyc)method.