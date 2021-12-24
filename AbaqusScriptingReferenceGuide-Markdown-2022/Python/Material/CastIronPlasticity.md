# CastIronPlasticity object

The CastIronPlasticity object specifies the Cast Iron plasticity model.

## Access

```
import material
mdb.models[name].materials[name].castIronPlasticity
import odbMaterial
session.odbs[name].materials[name].castIronPlasticity
```

## CastIronPlasticity(...)



This method creates a CastIronPlasticity object.



### Path

```
mdb.models[name].materials[name].CastIronPlasticity
session.odbs[name].materials[name].CastIronPlasticity
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

The table data specify the following:

- Plastic Poisson's ratio, νp⁢l (dimensionless).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CastIronPlasticity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the CastIronPlasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CastIronPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-castironplasticitypyc.htm?ContextScope=all#simaker-castironplasticitycastironplasticitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The CastIronPlasticity object has members with the same names and descriptions as the arguments to the [CastIronPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-castironplasticitypyc.htm?ContextScope=all#simaker-castironplasticitycastironplasticitypyc)method.

In addition, the CastIronPlasticity object can have the following members:

- *castIronTensionHardening*

  A [CastIronTensionHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-castirontensionhardeningpyc.htm?ContextScope=all) object.

- *castIronCompressionHardening*

  A [CastIronCompressionHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-castironcompressionhardeningpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [CAST IRON PLASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-castironplasticity.htm?ContextScope=all#simakey-r-castironplasticity)