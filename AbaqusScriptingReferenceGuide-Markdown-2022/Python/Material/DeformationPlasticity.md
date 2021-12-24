# DeformationPlasticity object

The DeformationPlasticity object specifies the deformation plasticity model.

## Access

```
import material
mdb.models[name].materials[name].deformationPlasticity
import odbMaterial
session.odbs[name].materials[name].deformationPlasticity
```

## DeformationPlasticity(...)



This method creates a DeformationPlasticity object.



### Path

```
mdb.models[name].materials[name].DeformationPlasticity
session.odbs[name].materials[name].DeformationPlasticity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

### Table data

- Young's modulus, E.
- Poisson's ratio, ν.
- Yield stress, σ0.
- Exponent, n.
- Yield offset, α.
- Temperature, if the data depend on temperature.

### Return value

A DeformationPlasticity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the DeformationPlasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DeformationPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-deformationplasticitypyc.htm?ContextScope=all#simaker-deformationplasticitydeformationplasticitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The DeformationPlasticity object has members with the same names and descriptions as the arguments to the [DeformationPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-deformationplasticitypyc.htm?ContextScope=all#simaker-deformationplasticitydeformationplasticitypyc)method.



## Corresponding analysis keywords

- [DEFORMATION PLASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-deformationplasticity.htm?ContextScope=all#simakey-r-deformationplasticity)