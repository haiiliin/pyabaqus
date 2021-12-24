# Calibration object

A Calibration object is the object used to specify a material calibration. The Calibration object stores the data that is used for specifying materials from test data.

## Access

```
        import calibration
        mdb.models[name].calibrations[name]
      
```

## Calibration(...)



This method creates a Calibration object.



### Path

```
          mdb.models[name].Calibration
        
```

### Required arguments

- *name*

  A String specifying the name of the new calibration.

### Optional arguments

None.

### Return value

A Calibration object.

### Exceptions

InvalidNameError.



## Members

The Calibration object has members with the same names and descriptions as the arguments to the [Calibration ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-calibrationpyc.htm?ContextScope=all#simaker-calibrationcalibrationpyc)method.

In addition, the Calibration object can have the following members:

- *dataSets*

  A [DataSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datasetpyc.htm?ContextScope=all) object.

- *behaviors*

  A [Behavior](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-behaviorpyc.htm?ContextScope=all) object.