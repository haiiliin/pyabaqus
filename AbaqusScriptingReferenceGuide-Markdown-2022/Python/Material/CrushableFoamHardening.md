# CrushableFoamHardening object

The CrushableFoamHardening object specifies hardening for the crushable foam plasticity model.

## Access

```
import material
mdb.models[name].materials[name].crushableFoam.crushableFoamHardening
import odbMaterial
session.odbs[name].materials[name].crushableFoam\
.crushableFoamHardening
```

## CrushableFoamHardening(...)



This method creates a CrushableFoamHardening object.



### Path

```
mdb.models[name].materials[name].crushableFoam.CrushableFoamHardening
session.odbs[name].materials[name].crushableFoam\
.CrushableFoamHardening
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

- The yield stress in uniaxial compression, σcσc.
- The absolute value of the corresponding plastic strain.(The first tabular value entered must always be zero.)
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CrushableFoamHardening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the CrushableFoamHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CrushableFoamHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-crushablefoamhardeningpyc.htm?ContextScope=all#simaker-crushablefoamhardeningcrushablefoamhardeningpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The CrushableFoamHardening object has members with the same names and descriptions as the arguments to the [CrushableFoamHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-crushablefoamhardeningpyc.htm?ContextScope=all#simaker-crushablefoamhardeningcrushablefoamhardeningpyc)method.



## Corresponding analysis keywords

- [CRUSHABLE FOAM HARDENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-crushablefoamhardening.htm?ContextScope=all#simakey-r-crushablefoamhardening)