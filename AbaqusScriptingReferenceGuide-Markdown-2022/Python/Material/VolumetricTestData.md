# VolumetricTestData object

The VolumetricTestData object provides volumetric test data.

## Access

```
import material
mdb.models[name].materials[name].hyperelastic.volumetricTestData
mdb.models[name].materials[name].hyperfoam.volumetricTestData
mdb.models[name].materials[name].viscoelastic.volumetricTestData
import odbMaterial
session.odbs[name].materials[name].hyperelastic.volumetricTestData
session.odbs[name].materials[name].hyperfoam.volumetricTestData
session.odbs[name].materials[name].viscoelastic.volumetricTestData
```

## VolumetricTestData(...)



This method creates a VolumetricTestData object.



### Path

```
mdb.models[name].materials[name].hyperelastic.VolumetricTestData
mdb.models[name].materials[name].hyperfoam.VolumetricTestData
mdb.models[name].materials[name].viscoelastic.VolumetricTestData
session.odbs[name].materials[name].hyperelastic.VolumetricTestData
session.odbs[name].materials[name].hyperfoam.VolumetricTestData
session.odbs[name].materials[name].viscoelastic.VolumetricTestData
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *volinf*

  None or a Float specifying a normalized volumetric value that depends on the value of the *time* member of the [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object. The default value is None.If *time*=RELAXATION_TEST_DATA, *volinf* specifies the value of the long-term, normalized volumetric modulus, kR⁢(∞). If *time*=CREEP_TEST_DATA, *volinf* specifies the value of the long-term, normalized volumetric compliance, K⁢(∞).This argument is valid only for a viscoelastic material model.

- *smoothing*

  None or an Int specifying the value for smoothing. If *smoothing*=None, no smoothing is employed. The default value is None.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

For a hyperelastic or hyperfoam material model, the table data specify the following:

- Pressure, p.
- Volume ratio, J (current volume/original volume).

For a viscoelastic material model, the values depend on the value of the *time* member of the [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object.

If *time*=RELAXATION_TEST_DATA, the table data specify the following:

- Normalized volumetric (bulk) modulus kR(t),(0≤kR(t)≤1).
- Time t (t>0).

If *time*=CREEP_TEST_DATA, the table data specify the following:

- Normalized volumetric (bulk) compliance jK(t),(jK(t)≥1).
- Time t (t>0).

### Return value

A VolumetricTestData object.

### Exceptions

None.



## setValues(...)



This method modifies the VolumetricTestData object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [VolumetricTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-volumetrictestdatapyc.htm?ContextScope=all#simaker-volumetrictestdatavolumetrictestdatapyc)method.

### Return value

None.

### Exceptions

None.



## Members

The VolumetricTestData object has members with the same names and descriptions as the arguments to the [VolumetricTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-volumetrictestdatapyc.htm?ContextScope=all#simaker-volumetrictestdatavolumetrictestdatapyc)method.



## Corresponding analysis keywords

- [VOLUMETRIC TEST DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-volumetrictestdata.htm?ContextScope=all#simakey-r-volumetrictestdata)