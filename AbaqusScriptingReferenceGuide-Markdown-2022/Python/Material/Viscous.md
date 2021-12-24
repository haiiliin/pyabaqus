# Viscous object

The Viscous object specifies the viscous properties for a two-layer viscoplastic material model.

## Access

```
import material
mdb.models[name].materials[name].viscous
import odbMaterial
session.odbs[name].materials[name].viscous
```

## Viscous(...)



This method creates a Viscous object.



### Path

```
mdb.models[name].materials[name].Viscous
session.odbs[name].materials[name].Viscous
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *law*

  A SymbolicConstant specifying the creep law. Possible values are STRAIN, TIME, USER, ANAND, DARVEAUX, DOUBLE_POWER, POWER_LAW, and TIME_POWER_LAW. The default value is STRAIN.

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
- f.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *law*=USER, the table data specify the following:

- f.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *law*=ANAND, the table data specify the following:

- s1.
- QR.
- A.
- ξ.
- m.
- A00.
- ˆs.
- n.
- a.
- S2.
- S3.
- A1.
- A2.
- A3.
- A4.
- f.

If *law*=DARVEAUX, the table data specify the following:

- Css.
- QR.
- α.
- n.
- ϵT.
- B.
- f.

If *law*=DOUBLE_POWER, the table data specify the following:

- A1.
- B1.
- C1.
- A2.
- B2.
- C2.
- σ0.
- f.

If *law*=POWER_LAW or *law*=TIME_POWER_LAW, the table data specify the following:

- q0.
- n.
- m.
- ∙ε0.⁢
- f.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Viscous object.

### Exceptions

None.



## setValues(...)



This method modifies the Viscous object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Viscous](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscouspyc.htm?ContextScope=all#simaker-viscousviscouspyc) method.

### Return value

None.

### Exceptions

None.



## Members

The Viscous object has members with the same names and descriptions as the arguments to the [Viscous](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscouspyc.htm?ContextScope=all#simaker-viscousviscouspyc) method.

In addition, the Viscous object can have the following member:

- *potential*

  A [Potential](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-potentialpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [VISCOUS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-viscous.htm?ContextScope=all#simakey-r-viscous)