# Conductivity object

The Conductivity object specifies thermal conductivity.

## Access

```
import material
mdb.models[name].materials[name].conductivity
import odbMaterial
session.odbs[name].materials[name].conductivity
```

## Conductivity(...)



This method creates a Conductivity object.



### Path

```
mdb.models[name].materials[name].Conductivity
session.odbs[name].materials[name].Conductivity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of conductivity. Possible values are ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=ISOTROPIC, the table data specify the following:

- Conductivity, k.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ORTHOTROPIC, the table data specify the following:

- k11.
- k22.
- k33.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ANISOTROPIC, the table data specify the following:

- k11.
- k12.
- k22.
- k13.
- k23.
- k33.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Conductivity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Conductivity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Conductivity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conductivitypyc.htm?ContextScope=all#simaker-conductivityconductivitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Conductivity object has members with the same names and descriptions as the arguments to the [Conductivity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conductivitypyc.htm?ContextScope=all#simaker-conductivityconductivitypyc)method.



## Corresponding analysis keywords

- [CONDUCTIVITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-conductivity.htm?ContextScope=all#simakey-r-conductivity)