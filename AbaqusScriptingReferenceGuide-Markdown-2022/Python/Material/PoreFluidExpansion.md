# PoreFluidExpansion object

The PoreFluidExpansion object specifies the thermal expansion coefficient for a hydraulic fluid.

## Access

```
import material
mdb.models[name].materials[name].poreFluidExpansion
import odbMaterial
session.odbs[name].materials[name].poreFluidExpansion
```

## PoreFluidExpansion(...)



This method creates a PoreFluidExpansion object.



### Path

```
mdb.models[name].materials[name].PoreFluidExpansion
session.odbs[name].materials[name].PoreFluidExpansion
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *zero*

  A Float specifying the value of θ0. The default value is 0.0.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- Mean coefficient of thermal expansion, α.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A PoreFluidExpansion object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the PoreFluidExpansion object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PoreFluidExpansion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porefluidexpansionpyc.htm?ContextScope=all#simaker-porefluidexpansionporefluidexpansionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The PoreFluidExpansion object has members with the same names and descriptions as the arguments to the [PoreFluidExpansion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porefluidexpansionpyc.htm?ContextScope=all#simaker-porefluidexpansionporefluidexpansionpyc)method.



## Corresponding analysis keywords

- [EXPANSION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-expansion.htm?ContextScope=all#simakey-r-expansion)