# PorousMetalPlasticity object

The PorousMetalPlasticity object specifies a porous metal plasticity model.

## Access

```
import material
mdb.models[name].materials[name].porousMetalPlasticity
import odbMaterial
session.odbs[name].materials[name].porousMetalPlasticity
```

## PorousMetalPlasticity(...)



This method creates a PorousMetalPlasticity object.



### Path

```
mdb.models[name].materials[name].PorousMetalPlasticity
session.odbs[name].materials[name].PorousMetalPlasticity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *relativeDensity*

  None or a Float specifying the initial relative density of the material, r0. The default value is None.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- q1.
- q2.
- q3.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A PorousMetalPlasticity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the PorousMetalPlasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PorousMetalPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousmetalplasticitypyc.htm?ContextScope=all#simaker-porousmetalplasticityporousmetalplasticitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The PorousMetalPlasticity object has members with the same names and descriptions as the arguments to the [PorousMetalPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousmetalplasticitypyc.htm?ContextScope=all#simaker-porousmetalplasticityporousmetalplasticitypyc)method.

In addition, the PorousMetalPlasticity object can have the following members:

- *porousFailureCriteria*

  A [PorousFailureCriteria](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousfailurecriteriapyc.htm?ContextScope=all) object.

- *voidNucleation*

  A [VoidNucleation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-voidnucleationpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [POROUS METAL PLASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-porousmetalplasticity.htm?ContextScope=all#simakey-r-porousmetalplasticity)