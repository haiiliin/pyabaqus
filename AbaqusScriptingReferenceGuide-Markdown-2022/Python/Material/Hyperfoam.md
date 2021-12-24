# Hyperfoam object

The Hyperfoam object specifies elastic properties for a hyperelastic foam.

## Access

```
import material
mdb.models[name].materials[name].hyperfoam
import odbMaterial
session.odbs[name].materials[name].hyperfoam
```

## Hyperfoam(...)



This method creates a Hyperfoam object.



### Path

```
mdb.models[name].materials[name].Hyperfoam
session.odbs[name].materials[name].Hyperfoam
```

### Required arguments

None.

### Optional arguments

- *testData*

  A Boolean specifying whether test data are supplied. The default value is OFF.

- *poisson*

  None or a Float specifying the effective Poisson's ratio, νν, of the material. This argument is valid only when *testData*=ON. The default value is None.

- *n*

  An Int specifying the order of the strain energy potential. Possible values are 1 ≤n≤≤n≤ 6. The default value is 1.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *moduli*

  A SymbolicConstant specifying the time-dependence of the material constants. Possible values are INSTANTANEOUS and LONG_TERM. The default value is LONG_TERM.

- *table*

  A sequence of sequences of Floats specifying the items described below. This argument is valid only when *testData*=OFF. The default value is an empty sequence.

### Table data

The items in the table data specify the following for values of nn:

- μi and αi for i from 1 to n.
- νi.
- Temperature, if the data depend on temperature. Temperature dependence is not allowed for 4 ≤n≤ 6 in an Abaqus/Explicit analysis.

### Return value

A Hyperfoam object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Hyperfoam object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Hyperfoam ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hyperfoampyc.htm?ContextScope=all#simaker-hyperfoamhyperfoampyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Hyperfoam object has members with the same names and descriptions as the arguments to the [Hyperfoam ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hyperfoampyc.htm?ContextScope=all#simaker-hyperfoamhyperfoampyc)method.

In addition, the Hyperfoam object can have the following members:

- *biaxialTestData*

  A [BiaxialTestData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-biaxialtestdatapyc.htm?ContextScope=all) object.

- *volumetricTestData*

  A [VolumetricTestData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-volumetrictestdatapyc.htm?ContextScope=all) object.

- *planarTestData*

  A [PlanarTestData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-planartestdatapyc.htm?ContextScope=all) object.

- *simpleShearTestData*

  A [SimpleShearTestData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-simplesheartestdatapyc.htm?ContextScope=all) object.

- *uniaxialTestData*

  A [UniaxialTestData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-uniaxialtestdatapyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [HYPERFOAM](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-hyperfoam.htm?ContextScope=all#simakey-r-hyperfoam)