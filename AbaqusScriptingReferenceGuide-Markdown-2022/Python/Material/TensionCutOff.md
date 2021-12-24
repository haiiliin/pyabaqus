# TensionCutOff object

The TensionCutOff object specifies tension cutoff for different material models for example the Mohr-Coulomb plasticity model.

## Access

```
import material
mdb.models[name].materials[name].mohrCoulombPlasticity.tensionCutOff
import odbMaterial
session.odbs[name].materials[name].mohrCoulombPlasticity.tensionCutOff
```

## TensionCutOff(...)



This method creates a TensionCutOff object.



### Path

```
mdb.models[name].materials[name].mohrCoulombPlasticity.TensionCutOff
session.odbs[name].materials[name].mohrCoulombPlasticity.TensionCutOff
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

- Tension cutoff stress.
- The value of the corresponding tensile plastic strain.(The first tabular value entered must always be zero.)
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A TensionCutOff object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the TensionCutOff object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TensionCutOff ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tensioncutoffpyc.htm?ContextScope=all#simaker-tensioncutofftensioncutoffpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The TensionCutOff object has members with the same names and descriptions as the arguments to the [TensionCutOff ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tensioncutoffpyc.htm?ContextScope=all#simaker-tensioncutofftensioncutoffpyc)method.



## Corresponding analysis keywords

- [TENSION CUTOFF](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-tensioncutoff.htm?ContextScope=all#simakey-r-tensioncutoff)