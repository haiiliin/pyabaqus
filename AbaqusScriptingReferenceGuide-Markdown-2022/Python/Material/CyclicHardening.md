# CyclicHardening object

The CyclicHardening object defines the evolution of the elastic domain for the nonlinear isotropic/kinematic hardening model.

## Access

```
import material
mdb.models[name].materials[name].plastic.cyclicHardening
import odbMaterial
session.odbs[name].materials[name].plastic.cyclicHardening
```

## CyclicHardening(...)



This method creates a CyclicHardening object.



### Path

```
mdb.models[name].materials[name].plastic.CyclicHardening
session.odbs[name].materials[name].plastic.CyclicHardening
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *parameters*

  A Boolean specifying whether material parameters are to be input directly. The default value is OFF.

### Table data

- Equivalent stress.
- Q∞Q(only if *parameters*=ON).
- Hardening parameter (only if *parameters*=ON).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CyclicHardening object.

### Exceptions

None.



## setValues(...)



This method modifies the CyclicHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CyclicHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cyclichardeningpyc.htm?ContextScope=all#simaker-cyclichardeningcyclichardeningpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The CyclicHardening object has members with the same names and descriptions as the arguments to the [CyclicHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cyclichardeningpyc.htm?ContextScope=all#simaker-cyclichardeningcyclichardeningpyc)method.



## Corresponding analysis keywords

- [CYCLIC HARDENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cyclichardening.htm?ContextScope=all#simakey-r-cyclichardening)