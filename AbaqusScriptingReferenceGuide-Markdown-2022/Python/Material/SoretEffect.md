# SoretEffect object

The SoretEffect object defines temperature gradient driven mass diffusion.

## Access

```
import material
mdb.models[name].materials[name].diffusivity.soretEffect
import odbMaterial
session.odbs[name].materials[name].diffusivity.soretEffect
```

## SoretEffect(...)



This method creates a SoretEffect object.



### Path

```
mdb.models[name].materials[name].diffusivity.SoretEffect
session.odbs[name].materials[name].diffusivity.SoretEffect
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

- Soret effect factor, κs.
- Concentration.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A SoretEffect object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the SoretEffect object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SoretEffect ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-soreteffectpyc.htm?ContextScope=all#simaker-soreteffectsoreteffectpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The SoretEffect object has members with the same names and descriptions as the arguments to the [SoretEffect ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-soreteffectpyc.htm?ContextScope=all#simaker-soreteffectsoreteffectpyc)method.



## Corresponding analysis keywords

- [KAPPA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-kappa.htm?ContextScope=all#simakey-r-kappa)