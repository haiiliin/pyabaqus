# Density object

The Density object specifies the material density.

## Access

```
import material
mdb.models[name].materials[name].density
import odbMaterial
session.odbs[name].materials[name].density
```

## Density(...)



This method creates a Density object.



### Path

```
mdb.models[name].materials[name].Density
session.odbs[name].materials[name].Density
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *distributionType*

  A SymbolicConstant specifying how the density is distributed spatially. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

- *fieldName*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object associated with this material option. The *fieldName* argument applies only when *distributionType*=ANALYTICAL_FIELD or *distributionType*=DISCRETE_FIELD. The default value is an empty string.

### Table data

- The mass density.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Density object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Density object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Density ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-densitypyc.htm?ContextScope=all#simaker-densitydensitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Density object has members with the same names and descriptions as the arguments to the [Density ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-densitypyc.htm?ContextScope=all#simaker-densitydensitypyc)method.



## Corresponding analysis keywords

- [DENSITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-density.htm?ContextScope=all#simakey-r-density)