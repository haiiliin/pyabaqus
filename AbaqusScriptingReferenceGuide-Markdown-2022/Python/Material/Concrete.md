# Concrete object

The Concrete object defines concrete properties beyond the elastic range.

## Access

```
import material
mdb.models[name].materials[name].concrete
import odbMaterial
session.odbs[name].materials[name].concrete
```

## Concrete(...)



This method creates a Concrete object.



### Path

```
mdb.models[name].materials[name].Concrete
session.odbs[name].materials[name].Concrete
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

- Absolute value of compressive stress.
- Absolute value of plastic strain.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Concrete object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Concrete object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Concrete ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretepyc.htm?ContextScope=all#simaker-concreteconcretepyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Concrete object has members with the same names and descriptions as the arguments to the [Concrete ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretepyc.htm?ContextScope=all#simaker-concreteconcretepyc)method.

In addition, the Concrete object can have the following members:

- *failureRatios*

  A [FailureRatios](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failureratiospyc.htm?ContextScope=all) object.

- *shearRetention*

  A [ShearRetention](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shearretentionpyc.htm?ContextScope=all) object.

- *tensionStiffening*

  A [TensionStiffening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tensionstiffeningpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [CONCRETE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-concrete.htm?ContextScope=all#simakey-r-concrete)