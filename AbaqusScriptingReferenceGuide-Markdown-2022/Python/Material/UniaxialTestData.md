# UniaxialTestData object

The UniaxialTestData object provides uniaxial test data (compression and/or tension).

## Access

```
import material
mdb.models[name].materials[name].hyperelastic.uniaxialTestData
mdb.models[name].materials[name].hyperfoam.uniaxialTestData
mdb.models[name].materials[name].lowDensityFoam\
.uniaxialCompressionTestData
mdb.models[name].materials[name].lowDensityFoam\
.uniaxialTensionTestData
mdb.models[name].materials[name].mullinsEffect.uniaxialTests[i]
import odbMaterial
session.odbs[name].materials[name].hyperelastic.uniaxialTestData
session.odbs[name].materials[name].hyperfoam.uniaxialTestData
session.odbs[name].materials[name].lowDensityFoam\
.uniaxialCompressionTestData
session.odbs[name].materials[name].lowDensityFoam\
.uniaxialTensionTestData
session.odbs[name].materials[name].mullinsEffect.uniaxialTests[i]
```

## UniaxialTestData(...)



This method creates a UniaxialTestData object.



### Path

```
mdb.models[name].materials[name].hyperelastic.UniaxialTestData
mdb.models[name].materials[name].hyperfoam.UniaxialTestData
mdb.models[name].materials[name].lowDensityFoam.UniaxialTestData
mdb.models[name].materials[name].mullinsEffect.UniaxialTestData
session.odbs[name].materials[name].hyperelastic.UniaxialTestData
session.odbs[name].materials[name].hyperfoam.UniaxialTestData
session.odbs[name].materials[name].lowDensityFoam.UniaxialTestData
session.odbs[name].materials[name].mullinsEffect.UniaxialTestData
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *smoothing*

  None or an Int specifying the value for smoothing. If *smoothing*=None, no smoothing is employed. The default value is None.

- *lateralNominalStrain*

  A Boolean specifying whether to include lateral nominal strain. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

For a hyperelastic material model, the table data specify the following:

- Nominal stress, TU.
- Nominal strain, ϵU.

For a hyperfoam material model, the table data specify the following:

- Nominal stress, TL.
- Nominal strain, ϵU.
- Nominal lateral strain, ϵ2=ϵ3. The default value is 0.

For a low-density foam material model, the table data specify the following:

- Nominal stress, TU.
- Nominal strain, ϵU.
- Nominal strain rate, ϵU˙.

### Return value

A UniaxialTestData object.

### Exceptions

None.



## setValues(...)



This method modifies the UniaxialTestData object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [UniaxialTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-uniaxialtestdatapyc.htm?ContextScope=all#simaker-uniaxialtestdatauniaxialtestdatapyc)method.

### Return value

None.

### Exceptions

None.



## Members

The UniaxialTestData object has members with the same names and descriptions as the arguments to the [UniaxialTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-uniaxialtestdatapyc.htm?ContextScope=all#simaker-uniaxialtestdatauniaxialtestdatapyc)method.



## Corresponding analysis keywords

- [UNIAXIAL TEST DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-uniaxialtestdata.htm?ContextScope=all#simakey-r-uniaxialtestdata)