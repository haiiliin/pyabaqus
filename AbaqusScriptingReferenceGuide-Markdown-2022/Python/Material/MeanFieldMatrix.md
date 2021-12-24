# MeanFieldMatrix object

The MeanFieldMatrix object specifies the matrix property.

## Access

```
import material
mdb.models[name].materials[name].constituents[name]
import odbMaterial
session.odbs[name].materials[name].constituents[name]
```

## MeanFieldMatrix(...)



This method creates a MeanFieldMatrix object.



### Path

```
mdb.models[name].materials[name].meanFieldHomogenization.MeanFieldMatrix
session.odbs[name].materials[name].meanFieldHomogenization.MeanFieldMatrix
```

### Required arguments

- *name*

  A String specifying the constituent repository key.

### Optional arguments

- *material*

  A String specifying the name of the material.

- *isotropizationCoefficient*

  A Float specifying the factor used for scaling the plastic strain of the constituent when calculating the isotropic part of the tangent.

### Return value

A MeanFieldMatrix object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the MeanFieldMatrix object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MeanFieldMatrix(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meanfieldmatrixpyc.htm?ContextScope=all#simaker-meanfieldmatrixmeanfieldmatrixpyc) method.

### Return value

None.

### Exceptions

RangeError.



## Members

The MeanFieldMatrix object has members with the same names and descriptions as the arguments to the [MeanFieldMatrix(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meanfieldmatrixpyc.htm?ContextScope=all#simaker-meanfieldmatrixmeanfieldmatrixpyc) method.



## Corresponding analysis keywords

- [CONSTITUENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-constituent.htm?ContextScope=all#simakey-r-constituent)