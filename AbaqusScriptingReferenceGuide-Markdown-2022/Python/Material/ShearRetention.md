# ShearRetention object

The ShearRetention object defines the reduction of the shear modulus associated with crack surfaces in a [Concrete](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretepyc.htm?ContextScope=all) model as a function of the tensile strain across the crack.

## Access

```
import material
mdb.models[name].materials[name].concrete.shearRetention
import odbMaterial
session.odbs[name].materials[name].concrete.shearRetention
```

## ShearRetention(...)



This method creates a ShearRetention object.



### Path

```
mdb.models[name].materials[name].concrete.ShearRetention
session.odbs[name].materials[name].concrete.ShearRetention
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

- ϱclose for dry concrete. The default value is 1.0.
- εmax for dry concrete. The default value is a very large number (full shear retention).
- ϱclose for wet concrete. The default value is 1.0.
- εmax for wet concrete. The default value is a very large number (full shear retention).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ShearRetention object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ShearRetention object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ShearRetention ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shearretentionpyc.htm?ContextScope=all#simaker-shearretentionshearretentionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ShearRetention object has members with the same names and descriptions as the arguments to the [ShearRetention ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shearretentionpyc.htm?ContextScope=all#simaker-shearretentionshearretentionpyc)method.



## Corresponding analysis keywords

- [SHEAR RETENTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shearretention.htm?ContextScope=all#simakey-r-shearretention)