# PorousElastic object

The PorousElastic object specifies elastic material properties for porous materials.

## Access

```
import material
mdb.models[name].materials[name].porousElastic
import odbMaterial
session.odbs[name].materials[name].porousElastic
```

## PorousElastic(...)



This method creates a PorousElastic object.



### Path

```
mdb.models[name].materials[name].PorousElastic
session.odbs[name].materials[name].PorousElastic
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *shear*

  A SymbolicConstant specifying the shear definition form. Possible values are G and POISSON. The default value is POISSON.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *shear*=G, the table data specify the following:

- The logarithmic bulk modulus, κ. (Dimensionless.)
- The shear modulus, G.
- The elastic tensile limit, peltpte⁢l. (This value cannot be negative.)
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *shear*=POISSON, the table data specify the following:

- The logarithmic bulk modulus, κ. (Dimensionless.)
- The Poisson's ratio, ν.
- The elastic tensile limit, peltpte⁢l. (This value cannot be negative.)
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A PorousElastic object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the PorousElastic object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PorousElastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porouselasticpyc.htm?ContextScope=all#simaker-porouselasticporouselasticpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The PorousElastic object has members with the same names and descriptions as the arguments to the [PorousElastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porouselasticpyc.htm?ContextScope=all#simaker-porouselasticporouselasticpyc)method.



## Corresponding analysis keywords

- [POROUS ELASTIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-porouselastic.htm?ContextScope=all#simakey-r-porouselastic)