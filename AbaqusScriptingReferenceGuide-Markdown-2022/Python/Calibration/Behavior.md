# Behavior object

The Behavior object specifies the method used for calibrating a material.

## Access

```
        import calibration
        mdb.models[name].calibrations[name].behaviors[name]
      
```

## Behavior(...)



This method creates a Behavior object.



### Path

```
          mdb.models[name].calibrations[name].Behavior
        
```

### Required arguments

- *name*

  A String specifying the name of the new behavior.

- *typeName*

  A String specifying the type of the new Behavior. Values can be "ElasIsoBehavior", "ElasPlasIsoBehavior", "FeFpBehavior", or a user plug-in behavior type.

### Optional arguments

None.

### Return value

A Behavior object.

### Exceptions

InvalidNameError.



## setValues(...)



This method modifies the data for an existing behavior object.



### Required arguments

None.

### Optional arguments

- *E*

  Young's modulus. Only valid if the behavior type is ElasIsoBehavior.

- *nu*

  Poisson's ratio. Only valid if the behavior type is ElasIsoBehavior.

- *ds1Name*

  The name of the first data set. Only valid if the behavior type is ElasIsoBehavior or ElasPlasIsoBehavior

- *ds2Name*

  The name of the second data set. Only valid if the behavior type is ElasIsoBehavior or ElasPlasIsoBehavior

- *materialName*

  Material Name.

- *yieldPoint*

  Stress/strain value for the material yield point.Only valid if the behavior type is ElasPlasIsoBehavior

- *ultimatePoint*

  Stress/strain value for the material ultimate point.Only valid if the behavior type is ElasPlasIsoBehavior

- *plasticPoints*

  Stress/strain values for the plastic portion of material curve. Only valid if the behavior type is ElasPlasIsoBehavior

- *PoissonsRatio*

  Poisson's Ratio. Only valid if the behavior type is ElasPlasIsoBehavior

- *elasticModulus*

  Young's Modulus for the elastic portion of the material curve. Only valid if the behavior type is ElasPlasIsoBehavior

- *plasticPointsRange*

  Extent of the material plastic points. Only valid if the behavior type is ElasPlasIsoBehavior

- *name*

  Name of the behavior.

- *uniaxialName*

  Name of the uniaxial dataset. Only valid if the behavior type is FeFpBehavior

- *biaxialName*

  Name of the biaxial dataset. Only valid if the behavior type is FeFpBehavior

- *interpolation*

  'linear' specifies linear interpolation between data points, otherwise 'logarithmic'. Only valid if the behavior type is FeFpBehavior

- *uniWeight*

  Uniaxial weight factor, uniWeight + biWeight should equal 1.0. Only valid if the behavior type is FeFpBehavior

- *biWeight*

  Biaxial weight factor, uniWeight + biWeight should equal 1.0. Only valid if the behavior type is FeFpBehavior

- *uMullinsReload*

  A List of strings, specifying names of reloading DataSet objects obtained from uniaxial test data. Only valid if the behavior is of type FeFpBehavior

- *uMullinsUnload*

  A List of strings, specifying names of reloading DataSet objects obtained from uniaxial test data. Only valid if the behavior is of type FeFpBehavior

- *uPYieldPoint*

  A tuple specifying the coordinates of yield point of the permanent data set. Only valid if the behavior is of type FeFpBehavior

- *uPermSet*

  A List of strings, specifying names of permanent DataSet objects obtained from uniaxial test data. Only valid if the behavior is of type FeFpBehavior

- *uPrimary*

  A string specifying name of Primary DataSet object.Only valid if the behavior is of type FeFpBehavior

- *bMullinsReload*

  A List of strings, specifying names of reloading DataSet objects obtained from biaxial test data. Only valid if the behavior is of type FeFpBehavior

- *bMullinsUnload*

  A List of strings, specifying names of unloading DataSet objects obtained from biaxial test data. Only valid if the behavior is of type FeFpBehavior

- *bPYieldPoint*

  A tuple specifying the coordinates of yield point of the permanent data set. Only valid if the behavior is of type FeFpBehavior

- *bPermSet*

  A List of strings, specifying names of permanent DataSet objects obtained from biaxial test data. Only valid if the behavior is of type FeFpBehavior

- *bPrimary*

  A string specifying name of Primary DataSet object. Only valid if the behavior is of type FeFpBehavior

### Return value

None.

### Exceptions

None.



## mapToMaterial(...)



This method appends the calibration data obtained from the DataSet object to an existing material object. In the case of ElasIsoBehavior, it appends the young's modulus and poisson's ratio. For ElasPlasIsoBehavior it appends the young's modulus, poisson's ratio and plastic points range and for FeFpBehavior it appends plastic points range and Mullins effect properties.



### Required arguments

- *materialName*

  A String specifying the name of the existing material

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## compute_E(...)



This method computes the value of young's modulus from the existing DataSet object. The method is only valid for ElasIsoBehavior type of behavior.



### Required arguments

- *dataSet*

  A [DataSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datasetpyc.htm?ContextScope=all) object.

### Optional arguments

None.

### Return value

A tuple consisting of a and b values of the regression line(y = ax + b), coefficient of determination(r-squared) value and the start and end-points of the line.

### Exceptions

None.



## compute_nu(...)



This method computes the value of Poisson's Ratio from the existing DataSet object. The method is only valid for ElasIsoBehavior and ElasPlasIsoBehavior type of behavior.



### Required arguments

- *dataSet*

  A [DataSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datasetpyc.htm?ContextScope=all) object.

### Optional arguments

None.

### Return value

A tuple consisting of a and b values of the regression line(y = ax + b), coefficient of determination(r-squared) value and the start and end-points of the line.

### Exceptions

None.



## compute_ultimatePoint(...)



This method computes the coordinates of the Ultimate point from the existing DataSet object. The method is only valid for ElasPlasIsoBehavior type of behavior.



### Required arguments

- *dataSet*

  A [DataSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datasetpyc.htm?ContextScope=all) object.

### Optional arguments

None.

### Return value

Coordinates of the ultimate point.

### Exceptions

None.



## compute_elasticModulus(...)



This method computes the value of the elastic modulus from the yieldpoint value. The method is only valid for ElasPlasIsoBehavior type of behavior.



### Required arguments

- *yieldPoint*

  A tuple consisting of coordinates of the yieldpoint.

### Optional arguments

None.

### Return value

A float specifying the value of elastic modulus.

### Exceptions

None.



## compute_plasticPoints(...)



This method extracts the coordinates of the plastic Points. The method is only valid for ElasPlasIsoBehavior type of behavior.



### Required arguments

- *dataSet*

  A [DataSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datasetpyc.htm?ContextScope=all) object.

- *slider_val*

  A float specifying the number of values to be taken.

- *start_index*

  A float specifying the lower limit of the range.

- *end_index*

  A float specifying the upper limit of the range.

### Optional arguments

- *yp*

  Coordinates of the yieldpoint. The default value is (0,0).

### Return value

A sequence of coordinates of the plastic points.

### Exceptions

None.



## xyDataDissect(...)



This method extracts primary, unload, reload and permanent DataSet objects from the existing DataSet object.The method is only valid for FeFpBehavior type of behavior.



### Required arguments

- *dsName*

  A string specifying the name of the uniaxial/biaxial test dataset.

- *modelName*

  A string specifying the name of the model to which the calibration behavior belongs.

- *calibrationName*

  A string specifying the name of the Calibration object to which the behavior belongs.

### Optional arguments

- *biaxial*

  A boolean specifying whether the test data is biaxial or uniaxial. The default value is True.

### Return value

A sequence of strings specifying names of the DataSet objects containing loading, unloading, reloading and primary datasets.

### Exceptions

None.



## Members

The Behavior object has members with the same names and descriptions as the arguments to the [Behavior ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-behaviorpyc.htm?ContextScope=all#simaker-behaviorbehaviorpyc)method and [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-behaviorpyc.htm?ContextScope=all#simaker-behaviorsetvaluespyc)method.

In addition, the Behavior object can have the following members:

- *modelName*

  A string specifying the name of the model to which the behavior belongs.

- *calibrationName*

  A string specifying the name of calibration to which the behavior belongs.

- *biAxialAllName*

  A String specifying the name of the dataset containing all the raw data in the test data file. Only valid if the behavior is of type FeFpBehavior

- *uniAxialAllName*

  A String specifying the name of the dataset containing all the raw data in the test data file. Only valid if the behavior is of type FeFpBehavior