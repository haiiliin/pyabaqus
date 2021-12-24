# ShearTestData object

The ShearTestData object specifies the normalized shear creep compliance or relaxation modulus as a function of time.

## Access

```
import material
mdb.models[name].materials[name].viscoelastic.shearTestData
import odbMaterial
session.odbs[name].materials[name].viscoelastic.shearTestData
```

## ShearTestData(...)



This method creates a ShearTestData object.



### Path

```
mdb.models[name].materials[name].viscoelastic.ShearTestData
session.odbs[name].materials[name].viscoelastic.ShearTestData
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying values that depend on the *time* member of the [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object.

  If *time*=RELAXATION_TEST_DATA, the table data specify the following:

  - Normalized shear relaxation modulus gR⁢(t) (0≤gR⁢(t)≤1).
  - Time t. (t>0).

  If *time*=CREEP_TEST_DATA, the table data specify the following:

  - Normalized shear compliance jS⁢(t). (jS⁢(t)≥1).
  - Time t. (t>0).

### Optional arguments

- *shrinf*

  None or a Float specifying a normalized shear. The value of *shrinf* depends on the value of the *time* member of the [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object. The default value is None.If *time*=RELAXATION_TEST_DATA, *shrinf* specifies the value of the long-term, normalized shear modulus gR(∞).If *time*=CREEP_TEST_DATA, *shrinf* specifies the value of the long-term, normalized shear compliance jS(∞).

### Return value

A ShearTestData object.

### Exceptions

None.



## setValues(...)



This method modifies the ShearTestData object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ShearTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sheartestdatapyc.htm?ContextScope=all#simaker-sheartestdatasheartestdatapyc)method.

### Return value

None.

### Exceptions

None.



## Members

The ShearTestData object has members with the same names and descriptions as the arguments to the [ShearTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sheartestdatapyc.htm?ContextScope=all#simaker-sheartestdatasheartestdatapyc)method.



## Corresponding analysis keywords

- [SHEAR TEST DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-sheartestdata.htm?ContextScope=all#simakey-r-sheartestdata)