# MohrCoulombHardening object

The MohrCoulombHardening object specifies hardening for the Mohr-Coulomb plasticity model.

## Access

```
import material
mdb.models[name].materials[name].mohrCoulombPlasticity\
.mohrCoulombHardening
import odbMaterial
session.odbs[name].materials[name].mohrCoulombPlasticity\
.mohrCoulombHardening
```

## MohrCoulombHardening(...)



This method creates a MohrCoulombHardening object.



### Path

```
mdb.models[name].materials[name].mohrCoulombPlasticity\
.MohrCoulombHardening
session.odbs[name].materials[name].mohrCoulombPlasticity\
.MohrCoulombHardening
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

- Cohesion yield stress.
- The absolute value of the corresponding plastic strain.(The first tabular value entered must always be zero.)
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A MohrCoulombHardening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the MohrCoulombHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MohrCoulombHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mohrcoulombhardeningpyc.htm?ContextScope=all#simaker-mohrcoulombhardeningmohrcoulombhardeningpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The MohrCoulombHardening object has members with the same names and descriptions as the arguments to the [MohrCoulombHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mohrcoulombhardeningpyc.htm?ContextScope=all#simaker-mohrcoulombhardeningmohrcoulombhardeningpyc)method.



## Corresponding analysis keywords

- [MOHR COULOMB HARDENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-mohrcoulombhardening.htm?ContextScope=all#simakey-r-mohrcoulombhardening)