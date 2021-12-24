# ClayPlasticity object

The ClayPlasticity object specifies the extended Cam-clay plasticity model.

## Access

```
import material
mdb.models[name].materials[name].clayPlasticity
import odbMaterial
session.odbs[name].materials[name].clayPlasticity
```

## ClayPlasticity(...)



This method creates a ClayPlasticity object.



### Path

```
mdb.models[name].materials[name].ClayPlasticity
session.odbs[name].materials[name].ClayPlasticity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *intercept*

  None or a Float specifying e1e1, the intercept of the virgin consolidation line with the void ratio axis in a plot of void ratio versus the logarithm of pressure stress. The default value is None.This argument is valid only if *hardening*=EXPONENTIAL.

- *hardening*

  A SymbolicConstant specifying the type of hardening/softening definition. Possible values are EXPONENTIAL and TABULAR. The default value is EXPONENTIAL.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *hardening*=EXPONENTIAL, the table data specify the following:

- Logarithmic plastic bulk modulus, λ (dimensionless).
- Stress ratio at critical state, M.
- The initial yield surface size, a0.
- ββ, the parameter defining the size of the yield surface on the “wet” side of critical state.
- KK, the ratio of the flow stress in triaxial tension to the flow stress in triaxial compression. 0.778≤K≤1.0. If the default value of 0.0 is accepted, a value of 1.0 is assumed.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *hardening*=TABULAR, the table data specify the following:

- Stress ratio at critical state, M.
- The initial volumetric plastic strain, ε_vol^pl∣0, corresponding to pc|0according to the [ClayHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-clayhardeningpyc.htm?ContextScope=all) definition.
- ββ, the parameter defining the size of the yield surface on the “wet” side of critical state.
- KK, the ratio of the flow stress in triaxial tension to the flow stress in triaxial compression. 0.778≤K≤1.0.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ClayPlasticity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ClayPlasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ClayPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-clayplasticitypyc.htm?ContextScope=all#simaker-clayplasticityclayplasticitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ClayPlasticity object has members with the same names and descriptions as the arguments to the [ClayPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-clayplasticitypyc.htm?ContextScope=all#simaker-clayplasticityclayplasticitypyc)method.

In addition, the ClayPlasticity object can have the following member:

- *clayHardening*

  A [ClayHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-clayhardeningpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [CLAY PLASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-clayplasticity.htm?ContextScope=all#simakey-r-clayplasticity)