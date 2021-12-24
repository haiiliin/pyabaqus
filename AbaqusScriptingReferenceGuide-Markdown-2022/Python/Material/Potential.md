# Potential object

The Potential object defines an anisotropic yield/creep model.

## Access

```
import material
mdb.models[name].materials[name].creep.potential
mdb.models[name].materials[name].plastic.potential
mdb.models[name].materials[name].viscous.potential
import odbMaterial
session.odbs[name].materials[name].creep.potential
session.odbs[name].materials[name].plastic.potential
session.odbs[name].materials[name].viscous.potential
```

## Potential(...)



This method creates a Potential object.



### Path

```
mdb.models[name].materials[name].creep.Potential
mdb.models[name].materials[name].plastic.Potential
mdb.models[name].materials[name].viscous.Potential
session.odbs[name].materials[name].creep.Potential
session.odbs[name].materials[name].plastic.Potential
session.odbs[name].materials[name].viscous.Potential
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

- R11.
- R22.
- R33.
- R12.
- R13.
- R23.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Potential object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Potential object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Potential ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-potentialpyc.htm?ContextScope=all#simaker-potentialpotentialpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Potential object has members with the same names and descriptions as the arguments to the [Potential ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-potentialpyc.htm?ContextScope=all#simaker-potentialpotentialpyc)method.



## Corresponding analysis keywords

- [POTENTIAL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-potential.htm?ContextScope=all#simakey-r-potential)