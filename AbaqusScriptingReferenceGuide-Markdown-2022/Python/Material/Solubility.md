# Solubility object

The Solubility object specifies solubility.

## Access

```
import material
mdb.models[name].materials[name].solubility
import odbMaterial
session.odbs[name].materials[name].solubility
```

## Solubility(...)



This method creates a Solubility object.



### Path

```
mdb.models[name].materials[name].Solubility
session.odbs[name].materials[name].Solubility
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

- Solubility.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Solubility object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Solubility object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Solubility ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solubilitypyc.htm?ContextScope=all#simaker-solubilitysolubilitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Solubility object has members with the same names and descriptions as the arguments to the [Solubility ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solubilitypyc.htm?ContextScope=all#simaker-solubilitysolubilitypyc)method.



## Corresponding analysis keywords

- [SOLUBILITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-solubility.htm?ContextScope=all#simakey-r-solubility)