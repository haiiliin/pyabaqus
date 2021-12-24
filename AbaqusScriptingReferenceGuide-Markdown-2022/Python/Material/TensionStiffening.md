# TensionStiffening object

The TensionStiffening object defines the retained tensile stress normal to a crack in a [Concrete](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretepyc.htm?ContextScope=all) model.

## Access

```
import material
mdb.models[name].materials[name].concrete.tensionStiffening
import odbMaterial
session.odbs[name].materials[name].concrete.tensionStiffening
```

## TensionStiffening(...)



This method creates a TensionStiffening object.



### Path

```
mdb.models[name].materials[name].concrete.TensionStiffening
session.odbs[name].materials[name].concrete.TensionStiffening
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying how the postcracking behavior is defined. Possible values are DISPLACEMENT and STRAIN. The default value is STRAIN.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=STRAIN, the table data specify the following:

- Fraction of remaining stress to stress at cracking.
- Absolute value of the direct strain minus the direct strain at cracking.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT, the table data specify the following:

- Displacement, u0u0, at which a linear loss of strength after cracking gives zero stress.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A TensionStiffening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the TensionStiffening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TensionStiffening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tensionstiffeningpyc.htm?ContextScope=all#simaker-tensionstiffeningtensionstiffeningpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The TensionStiffening object has members with the same names and descriptions as the arguments to the [TensionStiffening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tensionstiffeningpyc.htm?ContextScope=all#simaker-tensionstiffeningtensionstiffeningpyc)method.



## Corresponding analysis keywords

- [TENSION STIFFENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-tensionstiffening.htm?ContextScope=all#simakey-r-tensionstiffening)