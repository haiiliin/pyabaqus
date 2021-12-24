# Regularization object

The Regularization object defines the tolerance to be used for regularizing material data.

## Access

```
import material
mdb.models[name].materials[name].regularization
import odbMaterial
session.odbs[name].materials[name].regularization
```

## Regularization(...)



This method creates a Regularization object.



### Path

```
mdb.models[name].materials[name].Regularization
session.odbs[name].materials[name].Regularization
```

### Required arguments

None.

### Optional arguments

- *rtol*

  A Float specifying the tolerance to be used for regularizing material data. The default value is 0.03.

- *strainRateRegularization*

  A SymbolicConstant specifying the form of regularization of strain-rate-dependent material data. Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC.

### Return value

A Regularization object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Regularization object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Regularization ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regularizationpyc.htm?ContextScope=all#simaker-regularizationregularizationpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Regularization object has members with the same names and descriptions as the arguments to the [Regularization ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regularizationpyc.htm?ContextScope=all#simaker-regularizationregularizationpyc)method.



## Corresponding analysis keywords

- [DASHPOT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dashpot.htm?ContextScope=all#simakey-r-dashpot)