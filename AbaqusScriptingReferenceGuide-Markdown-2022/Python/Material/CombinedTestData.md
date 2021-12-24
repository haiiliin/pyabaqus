# CombinedTestData object

The CombinedTestData object specifies simultaneously the normalized shear and bulk compliances or relaxation moduli as functions of time.

## Access

```
import material
mdb.models[name].materials[name].viscoelastic.combinedTestData
import odbMaterial
session.odbs[name].materials[name].viscoelastic.combinedTestData
```

## CombinedTestData(...)



This method creates a CombinedTestData object.



### Path

```
mdb.models[name].materials[name].viscoelastic.CombinedTestData
session.odbs[name].materials[name].viscoelastic.CombinedTestData
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below. The values of the table data depend on the value of the *time* member of the [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object.

### Optional arguments

- *volinf*

  None or a Float specifying a normalized volume. The value of *volinf* depends on the value of the *time* member of the [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object. The default value is None.

  If *time*=RELAXATION_TEST_DATA, *volinf* specifies the value of the long-term normalized volumetric modulus, kR(∞).

  If *time*=CREEP_TEST_DATA, *volinf* specifies the value of the long-term normalized volumetric compliance, jK⁢(∞).

- *shrinf*

  None or a Float specifying a normalized shear. The value of *shrinf* depends on the value of the *time* member of the [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object. The default value is None.

  If *time*=RELAXATION_TEST_DATA, *shrinf* specifies the value of the long-term normalized shear modulus, gR(∞)

  If *time*=CREEP_TEST_DATA, *shrinf* specifies the value of the long-term normalized shear compliance, jS(∞).

### Table data

If *time*=RELAXATION_TEST_DATA, the table data specify the following:

- Normalized shear modulus, gR⁢(t) (0≤gR(t)≤1).
- Normalized volumetric (bulk) modulus, kR⁢(t) (0≤kR(t)≤1).
- Time t (t>0).

If *time*=CREEP_TEST_DATA, the table data specify the following:

- Normalized shear compliance, jS(t)(jS(t)≥1).
- Normalized volumetric (bulk) compliance, jK⁢(t) (jK(t)≥1)
- Time t (t>0)

### Return value

A CombinedTestData object.

### Exceptions

None.



## setValues(...)



This method modifies the CombinedTestData object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CombinedTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-combinedtestdatapyc.htm?ContextScope=all#simaker-combinedtestdatacombinedtestdatapyc)method.

### Return value

None.

### Exceptions

None.



## Members

The CombinedTestData object has members with the same names and descriptions as the arguments to the [CombinedTestData ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-combinedtestdatapyc.htm?ContextScope=all#simaker-combinedtestdatacombinedtestdatapyc)method.



## Corresponding analysis keywords

- [COMBINED TEST DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-combinedtestdata.htm?ContextScope=all#simakey-r-combinedtestdata)