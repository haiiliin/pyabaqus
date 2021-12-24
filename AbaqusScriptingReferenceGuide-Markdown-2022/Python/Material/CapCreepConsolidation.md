# CapCreepConsolidation object

The CapCreepConsolidation object specifies a cap creep model and material properties.

## Access

```
import material
mdb.models[name].materials[name].capPlasticity.capCreepConsolidation
import odbMaterial
session.odbs[name].materials[name].capPlasticity.capCreepConsolidation
```

## CapCreepConsolidation(...)



This method creates a CapCreepConsolidation object.



### Path

```
mdb.models[name].materials[name].capPlasticity.CapCreepConsolidation
session.odbs[name].materials[name].capPlasticity.CapCreepConsolidation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *law*

  A SymbolicConstant specifying the cap creep law. Possible values are STRAIN, TIME, SINGHM, and USER. The default value is STRAIN.

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
- .ε0.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CapCreepConsolidation object.

### Exceptions

None.



## setValues(...)



This method modifies the CapCreepConsolidation object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CapCreepConsolidation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capcreepconsolidationpyc.htm?ContextScope=all#simaker-capcreepconsolidationcapcreepconsolidationpyc) method.

### Return value

None.

### Exceptions

None.



## Members

The CapCreepConsolidation object has members with the same names and descriptions as the arguments to the [CapCreepConsolidation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capcreepconsolidationpyc.htm?ContextScope=all#simaker-capcreepconsolidationcapcreepconsolidationpyc) method.



## Corresponding analysis keywords

- [CAP CREEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-capcreep.htm?ContextScope=all#simakey-r-capcreep)