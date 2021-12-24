# PressureEffect object

The PressureEffect object defines equivalent pressure stress driven mass diffusion.

## Access

```
import material
mdb.models[name].materials[name].diffusivity.pressureEffect
import odbMaterial
session.odbs[name].materials[name].diffusivity.pressureEffect
```

## PressureEffect(...)



This method creates a PressureEffect object.



### Path

```
mdb.models[name].materials[name].diffusivity.PressureEffect
session.odbs[name].materials[name].diffusivity.PressureEffect
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

- Pressure stress factor, κpκp.
- Concentration.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A PressureEffect object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the PressureEffect object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PressureEffect ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressureeffectpyc.htm?ContextScope=all#simaker-pressureeffectpressureeffectpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The PressureEffect object has members with the same names and descriptions as the arguments to the [PressureEffect ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressureeffectpyc.htm?ContextScope=all#simaker-pressureeffectpressureeffectpyc)method.



## Corresponding analysis keywords

- [KAPPA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-kappa.htm?ContextScope=all#simakey-r-kappa)