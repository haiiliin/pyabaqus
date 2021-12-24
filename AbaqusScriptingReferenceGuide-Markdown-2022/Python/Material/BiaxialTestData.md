# BiaxialTestData object

The BiaxialTestData object provides equibiaxial test data (compression and/or tension).

## Access

```
import material
mdb.models[name].materials[name].hyperelastic.biaxialTestData
mdb.models[name].materials[name].hyperfoam.biaxialTestData
mdb.models[name].materials[name].mullinsEffect.biaxialTests[i]
import odbMaterial
session.odbs[name].materials[name].hyperelastic.biaxialTestData
session.odbs[name].materials[name].hyperfoam.biaxialTestData
session.odbs[name].materials[name].mullinsEffect.biaxialTests[i]
```

## BiaxialTestData(...)



This method creates a BiaxialTestData object.



### Path

```
mdb.models[name].materials[name].hyperelastic.BiaxialTestData
mdb.models[name].materials[name].hyperfoam.BiaxialTestData
mdb.models[name].materials[name].mullinsEffect.BiaxialTestData
session.odbs[name].materials[name].hyperelastic.BiaxialTestData
session.odbs[name].materials[name].hyperfoam.BiaxialTestData
session.odbs[name].materials[name].mullinsEffect.BiaxialTestData
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the following:

  - Nominal stress, TB.
  - Nominal strain, ϵB.

### Optional arguments

- *smoothing*

  None or an Int specifying the value for smoothing. If *smoothing*=None, no smoothing is employed. The default value is None.

- *lateralNominalStrain*

  A Boolean specifying whether to include lateral nominal strain. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Return value

A BiaxialTestData object.

### Exceptions

None.



## setValues(...)



This method modifies the BiaxialTestData object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BiaxialTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-biaxialtestdatapyc.htm?ContextScope=all#simaker-biaxialtestdatabiaxialtestdatapyc)method.

### Return value

None.

### Exceptions

None.



## Members

The BiaxialTestData object has members with the same names and descriptions as the arguments to the [BiaxialTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-biaxialtestdatapyc.htm?ContextScope=all#simaker-biaxialtestdatabiaxialtestdatapyc)method.



## Corresponding analysis keywords

- [BIAXIAL TEST DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-biaxialtestdata.htm?ContextScope=all#simakey-r-biaxialtestdata)