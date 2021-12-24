# FailStress object

The FailStress object defines parameters for stress-based failure measures.

## Access

```
import material
mdb.models[name].materials[name].elastic.failStress
import odbMaterial
session.odbs[name].materials[name].elastic.failStress
```

## FailStress(...)



This method creates a FailStress object.



### Path

```
mdb.models[name].materials[name].elastic.FailStress
session.odbs[name].materials[name].elastic.FailStress
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- Tensile stress limit in fiber direction, Xt.
- Compressive stress limit in fiber direction, Xc.
- Tensile stress limit in transverse direction, Yt.
- Compressive stress limit in transverse direction, Yc.
- Shear strength in the X–Y plane, S.
- Cross product term coefficient, *f* (-1.0≤f*≤1.0). The default value is zero.
- Biaxial stress limit, σb⁢i⁢a⁢x.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A FailStress object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the FailStress object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FailStress ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failstresspyc.htm?ContextScope=all#simaker-failstressfailstresspyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The FailStress object has members with the same names and descriptions as the arguments to the [FailStress ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failstresspyc.htm?ContextScope=all#simaker-failstressfailstresspyc)method.



## Corresponding analysis keywords

- [FAIL STRESS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-failstress.htm?ContextScope=all#simakey-r-failstress)