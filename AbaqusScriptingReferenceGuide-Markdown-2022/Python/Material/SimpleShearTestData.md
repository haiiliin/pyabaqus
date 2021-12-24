# SimpleShearTestData object

The SimpleShearTestData object provides simple shear test data.

## Access

```
import material
mdb.models[name].materials[name].hyperfoam.simpleShearTestData
import odbMaterial
session.odbs[name].materials[name].hyperfoam.simpleShearTestData
```

## SimpleShearTestData(...)



This method creates a SimpleShearTestData object.



### Path

```
mdb.models[name].materials[name].hyperfoam.SimpleShearTestData
session.odbs[name].materials[name].hyperfoam.SimpleShearTestData
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

- Nominal shear stress, TS.
- Nominal shear strain, γ.
- Nominal transverse stress, TT (normal to edge with shear stress). This stress value is optional.

### Return value

A SimpleShearTestData object.

### Exceptions

None.



## setValues(...)



This method modifies the SimpleShearTestData object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SimpleShearTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-simplesheartestdatapyc.htm?ContextScope=all#simaker-simplesheartestdatasimplesheartestdatapyc)method.

### Return value

None.

### Exceptions

None.



## Members

The SimpleShearTestData object has members with the same names and descriptions as the arguments to the [SimpleShearTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-simplesheartestdatapyc.htm?ContextScope=all#simaker-simplesheartestdatasimplesheartestdatapyc)method.



## Corresponding analysis keywords

- [SIMPLE SHEAR TEST DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-simplesheartestdata.htm?ContextScope=all#simakey-r-simplesheartestdata)