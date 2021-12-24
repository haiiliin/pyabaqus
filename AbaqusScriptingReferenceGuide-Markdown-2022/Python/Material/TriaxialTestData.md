# TriaxialTestData object

The TriaxialTestData object provides triaxial test data.

## Access

```
import material
mdb.models[name].materials[name].druckerPrager.triaxialTestData
import odbMaterial
session.odbs[name].materials[name].druckerPrager.triaxialTestData
```

## TriaxialTestData(...)



This method creates a TriaxialTestData object.



### Path

```
mdb.models[name].materials[name].druckerPrager.TriaxialTestData
session.odbs[name].materials[name].druckerPrager.TriaxialTestData
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *a*

  None or a Float specifying the value of the material constant aa. None is used when the value is unknown or it is not held fixed at the input value. The default value is None.

- *b*

  None or a Float specifying the value of the material constant bb. None is used when the value is unknown or it is not held fixed at the input value. The default value is None.

- *pt*

  None or a Float specifying the value of the material constant pt. None is used when the value is unknown or it is not held fixed at the input value. The default value is None.

### Table data

- Sign and magnitude of confining stress, σ1=σ2.
- Sign and magnitude of the stress in loading direction, σ3.

### Return value

A TriaxialTestData object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the TriaxialTestData object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TriaxialTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-triaxialtestdatapyc.htm?ContextScope=all#simaker-triaxialtestdatatriaxialtestdatapyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The TriaxialTestData object has members with the same names and descriptions as the arguments to the [TriaxialTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-triaxialtestdatapyc.htm?ContextScope=all#simaker-triaxialtestdatatriaxialtestdatapyc)method.



## Corresponding analysis keywords

- [TRIAXIAL TEST DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-triaxialtestdata.htm?ContextScope=all#simakey-r-triaxialtestdata)