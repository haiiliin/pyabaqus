# Creep object

The Creep object defines a creep law.

## Access

```
import material
mdb.models[name].materials[name].creep
import odbMaterial
session.odbs[name].materials[name].creep
```

## Creep(...)



This method creates a Creep object.



### Path

```
mdb.models[name].materials[name].Creep
session.odbs[name].materials[name].Creep
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *law*

  A SymbolicConstant specifying the strain-hardening law. Possible values are STRAIN, TIME, HYPERBOLIC_SINE, USER, ANAND, DARVEAUX,DOUBLE_POWER, POWER_LAW, and TIME_POWER_LAW. The default value is STRAIN.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *time*

  A SymbolicConstant specifying the time interval for relevant laws. Possible values are CREEP and TOTAL. The default value is TOTAL.

### Table data

If *law*=STRAIN or *law*=TIME, the table data specify the following:

- A.
- n.
- m.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *law*=HYPERBOLIC_SINE, the table data specify the following:

- A.
- B.
- n.
- △⁢H, if the data depend on temperature.
- R.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *law*=ANAND, the table data specify the following:

- s1.

- QR.

  A.

- ξ.

- m.

- A0.

- ˆS.

- n.

- a.

- S2.

- S3.

- A1.

- A2.

- A3.

- A4.

If *law*=DARVEAUX, the table data specify the following:

- Css.
- QR.
- α.
- n.
- ϵT.
- B.

If *law*=DOUBLE_POWER, the table data specify the following:

- A1.
- B1.
- C1.
- A2.
- B2.
- C2.
- σ0.

If *law*=POWER_LAW or *law*=TIME_POWER_LAW, the table data specify the following:

- q0.
- n.
- m.
- ∙ε0•.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Creep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Creep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Creep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-creeppyc.htm?ContextScope=all#simaker-creepcreeppyc) method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Creep object has members with the same names and descriptions as the arguments to the [Creep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-creeppyc.htm?ContextScope=all#simaker-creepcreeppyc) method.

In addition, the Creep object can have the following members:

- *ornl*

  An [Ornl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ornlpyc.htm?ContextScope=all) object.

- *potential*

  A [Potential](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-potentialpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [CREEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-creep.htm?ContextScope=all#simakey-r-creep)