# ClayHardening object

The ClayHardening object specifies hardening for the clay plasticity model.

## Access

```
import material
mdb.models[name].materials[name].clayPlasticity.clayHardening
import odbMaterial
session.odbs[name].materials[name].clayPlasticity.clayHardening
```

## ClayHardening(...)



This method creates a ClayHardening object.



### Path

```
mdb.models[name].materials[name].clayPlasticity.ClayHardening
session.odbs[name].materials[name].clayPlasticity.ClayHardening
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

- The hydrostatic pressure stress at yield, pc.
- The absolute value of the corresponding volumetric plastic strain.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ClayHardening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ClayHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ClayHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-clayhardeningpyc.htm?ContextScope=all#simaker-clayhardeningclayhardeningpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ClayHardening object has members with the same names and descriptions as the arguments to the [ClayHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-clayhardeningpyc.htm?ContextScope=all#simaker-clayhardeningclayhardeningpyc)method.



## Corresponding analysis keywords

- [CLAY HARDENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-clayhardening.htm?ContextScope=all#simakey-r-clayhardening)