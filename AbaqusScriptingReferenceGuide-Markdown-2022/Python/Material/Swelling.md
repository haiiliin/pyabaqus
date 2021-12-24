# Swelling object

The Swelling object specifies time-dependent volumetric swelling for a material.

## Access

```
import material
mdb.models[name].materials[name].swelling
import odbMaterial
session.odbs[name].materials[name].swelling
```

## Swelling(...)



This method creates a Swelling object.



### Path

```
mdb.models[name].materials[name].Swelling
session.odbs[name].materials[name].Swelling
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.This argument is valid only when *law*=INPUT.

### Optional arguments

- *law*

  A SymbolicConstant specifying the type of data defining the swelling behavior. Possible values are INPUT and USER. The default value is INPUT.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- Volumetric swelling strain rate.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Swelling object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Swelling object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Swelling ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-swellingpyc.htm?ContextScope=all#simaker-swellingswellingpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Swelling object has members with the same names and descriptions as the arguments to the [Swelling ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-swellingpyc.htm?ContextScope=all#simaker-swellingswellingpyc)method.

In addition, the Swelling object can have the following member:

- *ratios*

  A [Ratios](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ratiospyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [SWELLING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-swelling.htm?ContextScope=all#simakey-r-swelling)