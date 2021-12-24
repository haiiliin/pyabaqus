# DruckerPragerHardening object

The DruckerPragerHardening object specifies hardening for Drucker-Prager plasticity models.

## Access

```
import material
mdb.models[name].materials[name].druckerPrager.druckerPragerHardening
import odbMaterial
session.odbs[name].materials[name].druckerPrager\
.druckerPragerHardening
```

## DruckerPragerHardening(...)



This method creates a DruckerPragerHardening object.



### Path

```
mdb.models[name].materials[name].druckerPrager.DruckerPragerHardening
session.odbs[name].materials[name].druckerPrager\
.DruckerPragerHardening
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of data defining the hardening behavior. Possible values are COMPRESSION, TENSION, and SHEAR. The default value is COMPRESSION.

- *rate*

  A Boolean specifying whether the data depend on rate. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- Yield stress.
- Absolute value of the corresponding plastic strain. (The first tabular value entered must always be zero.)
- Equivalent plastic strain rate, ˙¯εpl, for which this hardening curve applies.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A DruckerPragerHardening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the DruckerPragerHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DruckerPragerHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragerhardeningpyc.htm?ContextScope=all#simaker-druckerpragerhardeningdruckerpragerhardeningpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The DruckerPragerHardening object has members with the same names and descriptions as the arguments to the [DruckerPragerHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragerhardeningpyc.htm?ContextScope=all#simaker-druckerpragerhardeningdruckerpragerhardeningpyc)method.



## Corresponding analysis keywords

- [DRUCKER PRAGER HARDENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-druckerpragerhardening.htm?ContextScope=all#simakey-r-druckerpragerhardening)