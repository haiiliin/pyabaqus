# MeanFieldHomogenization object

The MeanFieldHomogenization object specifies the multiscale material definition.

## Access

```
import material
mdb.models[name].materials[name].meanFieldHomogenization
import odbMaterial
session.odbs[name].materials[name].meanFieldHomogenization
```

## MeanFieldHomogenization(...)



This method creates a MeanFieldHomogenization object.



### Path

```
mdb.models[name].materials[name].MeanFieldHomogenization
session.odbs[name].materials[name].MeanFieldHomogenization
```

### Required arguments

None.

### Optional arguments

- *angleSubdivision*

  An Int specifying the number of angle increments used for the discretization of the orientation space.

- *formulation*

  A SymbolicConstant specifying the type of homogenization model. Possible values are MT, REUSS, VOIGT, INVERSED_MT, BALANCED, and UNSPECIFIED. The default value is MT.

- *isotropization*

  A SymbolicConstant specifying the type of isotropization method. Possible values are ALLISO, EISO, and PISO. The default value is ALLISO.

- *uniformMatrixStrain*

  A SymbolicConstant specifying whether the average strain in the matrix is uniform across all pseudo-grains. Possible values are NO and YES. The default value is NO.

### Return value

A MeanFieldHomogenization object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the MeanFieldHomogenization object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MeanFieldHomogenization(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meanfieldhomogenizationpyc.htm?ContextScope=all#simaker-meanfieldhomogenizationmeanfieldhomogenizationpyc) method.

### Return value

None.

### Exceptions

RangeError.



## Members

The MeanFieldHomogenization object has members with the same names and descriptions as the arguments to the [MeanFieldHomogenization(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meanfieldhomogenizationpyc.htm?ContextScope=all#simaker-meanfieldhomogenizationmeanfieldhomogenizationpyc) method.



## Corresponding analysis keywords

- [MEAN FIELD HOMOGENIZATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-meanfieldhomogenization.htm?ContextScope=all#simakey-r-meanfieldhomogenization)