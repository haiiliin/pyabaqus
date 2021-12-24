# Trs object

The Trs object defines the temperature-time shift for time history viscoelastic analysis.

## Access

```
import material
mdb.models[name].materials[name].viscoelastic.trs
mdb.models[name].materials[name].viscosity.trs
import odbMaterial
session.odbs[name].materials[name].viscoelastic.trs
session.odbs[name].materials[name].viscosity.trs
```

## Trs(...)



This method creates a Trs object.



### Path

```
mdb.models[name].materials[name].viscoelastic.Trs
mdb.models[name].materials[name].viscosity.Trs
session.odbs[name].materials[name].viscoelastic.Trs
session.odbs[name].materials[name].viscosity.Trs
```

### Required arguments

None.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the definition of the shift function. Possible values are WLF, ARRHENIUS, and USER. The default value is WLF.

- *table*

  A sequence of sequences of Floats specifying the items described below. The default value is an empty sequence.This argument is valid only when *definition*=WLF.

### Table data

- Reference temperature, θ0θ0.
- Calibration constant, C1C1.
- Calibration constant, C2C2.

### Return value

A Trs object.

### Exceptions

None.



## setValues(...)



This method modifies the Trs object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Trs ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-trspyc.htm?ContextScope=all#simaker-trstrspyc)method.

### Return value

None.

### Exceptions

None.



## Members

The Trs object has members with the same names and descriptions as the arguments to the [Trs ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-trspyc.htm?ContextScope=all#simaker-trstrspyc)method.



## Corresponding analysis keywords

- [TRS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-trs.htm?ContextScope=all#simakey-r-trs)