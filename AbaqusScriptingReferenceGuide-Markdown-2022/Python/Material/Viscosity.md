# Viscosity object

The Viscosity object specifies mechanical viscosity.

## Access

```
import material
mdb.models[name].materials[name].viscosity
import odbMaterial
session.odbs[name].materials[name].viscosity
```

## Viscosity(...)



This method creates a Viscosity object.



### Path

```
mdb.models[name].materials[name].Viscosity
session.odbs[name].materials[name].Viscosity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of viscosity. The default value is NEWTONIAN.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=NEWTONIAN, the table data specify the following:

- Viscosity, k.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Viscosity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Viscosity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Viscosity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscositypyc.htm?ContextScope=all#simaker-viscosityviscositypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Viscosity object has members with the same names and descriptions as the arguments to the [Viscosity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscositypyc.htm?ContextScope=all#simaker-viscosityviscositypyc)method.

In addition, the Viscosity object can have the following member:

- *trs*

  A [Trs](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-trspyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [VISCOSITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-viscosity.htm?ContextScope=all#simakey-r-viscosity)