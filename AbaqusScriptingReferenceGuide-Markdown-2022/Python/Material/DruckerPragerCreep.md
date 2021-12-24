# DruckerPragerCreep object

The DruckerPragerCreep object specifies creep for Drucker-Prager plasticity models.

## Access

```
import material
mdb.models[name].materials[name].druckerPrager.druckerPragerCreep
import odbMaterial
session.odbs[name].materials[name].druckerPrager.druckerPragerCreep
```

## DruckerPragerCreep(...)



This method creates a DruckerPragerCreep object.



### Path

```
mdb.models[name].materials[name].druckerPrager.DruckerPragerCreep
session.odbs[name].materials[name].druckerPrager.DruckerPragerCreep
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *law*

  A SymbolicConstant specifying the type of data defining the creep law. Possible values are:STRAIN, specifying a strain-hardening power law.TIME, specifying a time-hardening power law.SINGHM, specifying a Singh-Mitchell type law.USER, specifying the creep law is input from user subroutine [CREEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-creep.htm?ContextScope=all#simasub-c-creep).The default value is STRAIN.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *law*=TIME or *law*=STRAIN, the table data specify the following:

- AA. (Units of F-nL2nT−1−m.)
- n.
- m.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *law*=SINGHM, the table data specify the following:

- A. (Units of T−1.)
- α. (Units of F−1L2.)
- m.
- t1. (Units of T.)
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A DruckerPragerCreep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the DruckerPragerCreep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DruckerPragerCreep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragercreeppyc.htm?ContextScope=all#simaker-druckerpragercreepdruckerpragercreeppyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The DruckerPragerCreep object has members with the same names and descriptions as the arguments to the [DruckerPragerCreep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragercreeppyc.htm?ContextScope=all#simaker-druckerpragercreepdruckerpragercreeppyc)method.



## Corresponding analysis keywords

- [DRUCKER PRAGER CREEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-druckerpragercreep.htm?ContextScope=all#simakey-r-druckerpragercreep)