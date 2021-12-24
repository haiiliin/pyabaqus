# CapHardening object

The CapHardening object specifies Drucker-Prager/Cap plasticity hardening.

## Access

```
import material
mdb.models[name].materials[name].capPlasticity.capHardening
import odbMaterial
session.odbs[name].materials[name].capPlasticity.capHardening
```

## CapHardening(...)



This method creates a CapHardening object.



### Path

```
mdb.models[name].materials[name].capPlasticity.CapHardening
session.odbs[name].materials[name].capPlasticity.CapHardening
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

- Hydrostatic pressure yield stress.
- Absolute value of the corresponding volumetric inelastic strain.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CapHardening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the CapHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CapHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-caphardeningpyc.htm?ContextScope=all#simaker-caphardeningcaphardeningpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The CapHardening object has members with the same names and descriptions as the arguments to the [CapHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-caphardeningpyc.htm?ContextScope=all#simaker-caphardeningcaphardeningpyc)method.



## Corresponding analysis keywords

- [CAP HARDENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-caphardening.htm?ContextScope=all#simakey-r-caphardening)