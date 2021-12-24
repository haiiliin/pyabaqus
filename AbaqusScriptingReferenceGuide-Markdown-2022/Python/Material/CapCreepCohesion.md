# CapCreepCohesion object

The CapCreepCohesion object specifies a cap creep model and material properties.

## Access

```
import material
mdb.models[name].materials[name].capPlasticity.capCreepCohesion
import odbMaterial
session.odbs[name].materials[name].capPlasticity.capCreepCohesion
```

## CapCreepCohesion(...)



This method creates a CapCreepCohesion object.



### Path

```
mdb.models[name].materials[name].capPlasticity.CapCreepCohesion
session.odbs[name].materials[name].capPlasticity.CapCreepCohesion
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *law*

  A SymbolicConstant specifying the cap creep law. Possible values are STRAIN, TIME, SINGHM, USER, POWER_LAW, and TIME_POWER_LAW. The default value is STRAIN.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *time*

  A SymbolicConstant specifying the time increment for the relevant laws. Possible values are CREEP and TOTAL. The default value is TOTAL.

### Table data

If *law*=STRAIN or *law*=TIME, the table data specify the following:

- A.
- n.
- m.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *law*=SINGHM, the table data specify the following:

- A.
- α.
- m.
- t1.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *law*=POWER_LAW or *law*=TIME_POWER_LAW, the table data specify the following:

- q0.
- n.
- m.
- ε0.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CapCreepCohesion object.

### Exceptions

None.



## setValues(...)



This method modifies the CapCreepCohesion object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CapCreepCohesion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capcreepcohesionpyc.htm?ContextScope=all#simaker-capcreepcohesioncapcreepcohesionpyc) method.

### Return value

None.

### Exceptions

None.



## Members

The CapCreepCohesion object has members with the same names and descriptions as the arguments to the [CapCreepCohesion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capcreepcohesionpyc.htm?ContextScope=all#simaker-capcreepcohesioncapcreepcohesionpyc) method.



## Corresponding analysis keywords

- [CAP CREEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-capcreep.htm?ContextScope=all#simakey-r-capcreep)