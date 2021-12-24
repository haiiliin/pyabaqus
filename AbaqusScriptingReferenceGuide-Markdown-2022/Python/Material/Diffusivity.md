# Diffusivity object

The Diffusivity object specifies mass diffusivity.

## Access

```
import material
mdb.models[name].materials[name].diffusivity
import odbMaterial
session.odbs[name].materials[name].diffusivity
```

## Diffusivity(...)



This method creates a Diffusivity object.



### Path

```
mdb.models[name].materials[name].Diffusivity
session.odbs[name].materials[name].Diffusivity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of diffusivity. Possible values are ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.

- *law*

  A SymbolicConstant specifying the diffusion behavior. Possible values are GENERAL and FICK. The default value is GENERAL.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=ISOTROPIC, the table data specify the following:

- Diffusivity, D.
- Concentration, c.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ORTHOTROPIC, the table data specify the following:

- D11.
- D22.
- D33.
- Concentration, c.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ANISOTROPIC, the table data specify the following:

- D11.
- D12.
- D22.
- D13.
- D23.
- D33.
- Concentration, c.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Diffusivity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Diffusivity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Diffusivity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diffusivitypyc.htm?ContextScope=all#simaker-diffusivitydiffusivitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Diffusivity object has members with the same names and descriptions as the arguments to the [Diffusivity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diffusivitypyc.htm?ContextScope=all#simaker-diffusivitydiffusivitypyc)method.

In addition, the Diffusivity object can have the following members:

- *pressureEffect*

  A [PressureEffect](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressureeffectpyc.htm?ContextScope=all) object.

- *soretEffect*

  A [SoretEffect](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-soreteffectpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [DIFFUSIVITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-diffusivity.htm?ContextScope=all#simakey-r-diffusivity)