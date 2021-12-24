# VoidNucleation object

The VoidNucleation object defines the nucleation of voids in a porous material.

## Access

```
import material
mdb.models[name].materials[name].porousMetalPlasticity.voidNucleation
import odbMaterial
session.odbs[name].materials[name].porousMetalPlasticity\
.voidNucleation
```

## VoidNucleation(...)



This method creates a VoidNucleation object.



### Path

```
mdb.models[name].materials[name].porousMetalPlasticity.VoidNucleation
session.odbs[name].materials[name].porousMetalPlasticity\
.VoidNucleation
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

- εN, the mean value of the nucleation-strain normal distribution.
- sN, the standard deviation of the nucleation-strain normal distribution.
- fN, the volume fraction of nucleating voids.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A VoidNucleation object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the VoidNucleation object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [VoidNucleation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-voidnucleationpyc.htm?ContextScope=all#simaker-voidnucleationvoidnucleationpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The VoidNucleation object has members with the same names and descriptions as the arguments to the [VoidNucleation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-voidnucleationpyc.htm?ContextScope=all#simaker-voidnucleationvoidnucleationpyc)method.



## Corresponding analysis keywords

- [VOID NUCLEATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-voidnucleation.htm?ContextScope=all#simakey-r-voidnucleation)