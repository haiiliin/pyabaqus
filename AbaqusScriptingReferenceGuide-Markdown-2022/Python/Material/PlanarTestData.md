# PlanarTestData object

The PlanarTestData object specifies planar test (or pure shear) data (compression and/or tension).

## Access

```
import material
mdb.models[name].materials[name].hyperelastic.planarTestData
mdb.models[name].materials[name].hyperfoam.planarTestData
mdb.models[name].materials[name].mullinsEffect.planarTests[i]
import odbMaterial
session.odbs[name].materials[name].hyperelastic.planarTestData
session.odbs[name].materials[name].hyperfoam.planarTestData
session.odbs[name].materials[name].mullinsEffect.planarTests[i]
```

## PlanarTestData(...)



This method creates a PlanarTestData object.



### Path

```
mdb.models[name].materials[name].hyperelastic.PlanarTestData
mdb.models[name].materials[name].hyperfoam.PlanarTestData
mdb.models[name].materials[name].mullinsEffect.PlanarTestData
session.odbs[name].materials[name].hyperelastic.PlanarTestData
session.odbs[name].materials[name].hyperfoam.PlanarTestData
session.odbs[name].materials[name].mullinsEffect.PlanarTestData
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

- Nominal stress, TS.
- Nominal strain in the direction of loading, ϵS.

For a hyperfoam material model, the table data specify the following:

- Nominal stress, TL.
- Nominal strain in the direction of loading, ϵp.
- Nominal transverse strain, ϵ3. The default value is 0.

### Return value

A PlanarTestData object.

### Exceptions

None.



## setValues(...)



This method modifies the PlanarTestData object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PlanarTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-planartestdatapyc.htm?ContextScope=all#simaker-planartestdataplanartestdatapyc)method.

### Return value

None.

### Exceptions

None.



## Members

The PlanarTestData object has members with the same names and descriptions as the arguments to the [PlanarTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-planartestdatapyc.htm?ContextScope=all#simaker-planartestdataplanartestdatapyc)method.



## Corresponding analysis keywords

- [PLANAR TEST DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-planartestdata.htm?ContextScope=all#simakey-r-planartestdata)