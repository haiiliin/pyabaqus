# Expansion object

The Expansion object specifies thermal expansion.

## Access

```
import material
mdb.models[name].materials[name].expansion
import odbMaterial
session.odbs[name].materials[name].expansion
```

## Expansion(...)



This method creates an Expansion object.



### Path

```
mdb.models[name].materials[name].Expansion
session.odbs[name].materials[name].Expansion
```

### Required arguments

None.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of expansion. Possible values are ISOTROPIC, ORTHOTROPIC, ANISOTROPIC, and SHORT_FIBER. The default value is ISOTROPIC.

- *userSubroutine*

  A Boolean specifying whether a user subroutine is used to define the increments of thermal strain. The default value is OFF.

- *zero*

  A Float specifying the value of θ0 if the thermal expansion is temperature-dependent or field-variable-dependent. The default value is 0.0.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *table*

  A sequence of sequences of Floats specifying the items described below. The default value is an empty sequence.This argument is required only if *type* is not USER.

### Table data

If *type*=ISOTROPIC, the table data specify the following:

- α in Abaqus/Standard or Abaqus/Explicit analysis.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ORTHOTROPIC, the table data specify the following:

- α11.
- α22.
- α33.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ANISOTROPIC, the table data specify the following:

- α11.
- α22.
- α33. (Not used for plane stress case.)
- α12.
- α13.
- α23.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=SHORT_FIBER, there is no table data.

### Return value

An Expansion object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Expansion object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Expansion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expansionpyc.htm?ContextScope=all#simaker-expansionexpansionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Expansion object has members with the same names and descriptions as the arguments to the [Expansion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expansionpyc.htm?ContextScope=all#simaker-expansionexpansionpyc)method.



## Corresponding analysis keywords

- [EXPANSION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-expansion.htm?ContextScope=all#simakey-r-expansion)