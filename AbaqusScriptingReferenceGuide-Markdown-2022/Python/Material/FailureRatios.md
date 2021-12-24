# FailureRatios object

The FailureRatios object specifies the shape of the failure surface for a [Concrete](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretepyc.htm?ContextScope=all) model.

## Access

```
import material
mdb.models[name].materials[name].concrete.failureRatios
import odbMaterial
session.odbs[name].materials[name].concrete.failureRatios
```

## FailureRatios(...)



This method creates a FailureRatios object.



### Path

```
mdb.models[name].materials[name].concrete.FailureRatios
session.odbs[name].materials[name].concrete.FailureRatios
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

- Ratio of the ultimate biaxial compressive stress to the uniaxial compressive ultimate stress. The default value is 1.16.
- Absolute value of the ratio of the uniaxial tensile stress at failure to the uniaxial compressive stress at failure. The default value is 0.09.
- Ratio of the magnitude of a principal component of plastic strain at ultimate stress in biaxial compression to the plastic strain at ultimate stress in uniaxial compression. The default value is 1.28.
- Ratio of the tensile principal stress value at shear in plane stress, when the other nonzero principal stress component is at the ultimate compressive stress value, to the tensile cracking stress under uniaxial tension. The default value is 1/3.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A FailureRatios object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the FailureRatios object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FailureRatios ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failureratiospyc.htm?ContextScope=all#simaker-failureratiosfailureratiospyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The FailureRatios object has members with the same names and descriptions as the arguments to the [FailureRatios ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failureratiospyc.htm?ContextScope=all#simaker-failureratiosfailureratiospyc)method.



## Corresponding analysis keywords

- [FAILURE RATIOS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-failureratios.htm?ContextScope=all#simakey-r-failureratios)