# MeanFieldInclusion object

The MeanFieldInclusion object specifies the inclusion type multiscale material property.

## Access

```
import material
mdb.models[name].materials[name].constituents[name]
import odbMaterial
session.odbs[name].materials[name].constituents[name]
```

## MeanFieldInclusion(...)



This method creates a MeanFieldInclusion object.



### Path

```
mdb.models[name].materials[name].meanFieldHomogenization.MeanFieldInclusion
session.odbs[name].materials[name].meanFieldHomogenization.MeanFieldInclusion
```

### Required arguments

- *name*

  A String specifying the constituent repository key.

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *material*

  A String specifying the name of the material.

- *isotropizationCoefficient*

  A Float specifying the factor used for scaling the plastic strain of the constituent when calculating the isotropic part of the tangent.

- *volumeFractionType*

  A SymbolicConstant specifying the type of volume fraction. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

- *volumeFractionFieldName*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object or [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object.

- *aspectRatioType*

  A SymbolicConstant specifying the type of aspect ratio. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

- *aspectRatioFieldName*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object or [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object.

- *orientationTensorType*

  A SymbolicConstant specifying the type of orientation tensor. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

- *orientationTensorFieldName*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object or [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object.

- *shape*

  A SymbolicConstant specifying the type of inclusion shapes. Possible values are SPHERE, PROLATE, OBLATE, CYLINDER, PENNY, and ELLIPTIC_CYLINDER. The default value is SPHERE.

- *direction*

  A SymbolicConstant specifying the type of inclusion direction. Possible values are FIXED, RANDOM3D, and ORIENTATION_TENSOR.

- *strainConcentrationTensor*

  A sequence of Floats defining the 36 components of the strain concentration tensor.

- *temperatureGradientConcentrationTensor*

  A sequence of Floats defining the 9 components of the temperature gradient concentration tensor.

### Table data

The table data specify the following:

- Volume fraction.
- Aspect ratio.
- Components of the direction vector defined in the local coordinate system when *direction*=FIXED. Components of the second-order orientation tensor in the local coordinate system when *direction*=ORIENTATION_TENSOR.
- Etc.

### Return value

A MeanFieldInclusion object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the MeanFieldInclusion object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MeanFieldInclusion(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meanfieldinclusionpyc.htm?ContextScope=all#simaker-meanfieldinclusionmeanfieldinclusionpyc) method.

### Return value

None.

### Exceptions

RangeError.



## Members

The MeanFieldInclusion object has members with the same names and descriptions as the arguments to the [MeanFieldInclusion(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meanfieldinclusionpyc.htm?ContextScope=all#simaker-meanfieldinclusionmeanfieldinclusionpyc) method.



## Corresponding analysis keywords

- [CONSTITUENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-constituent.htm?ContextScope=all#simakey-r-constituent)