# Dielectric object

The Dielectric object specifies dielectric material properties.

## Access

```
import material
mdb.models[name].materials[name].dielectric
import odbMaterial
session.odbs[name].materials[name].dielectric
```

## Dielectric(...)



This method creates a Dielectric object.



### Path

```
mdb.models[name].materials[name].Dielectric
session.odbs[name].materials[name].Dielectric
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the dielectric behavior. Possible values are ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.

- *frequencyDependency*

  A Boolean specifying whether the data depend on frequency. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=ISOTROPIC, the table data specify the following:

- Dielectric constant.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ORTHOTROPIC, the table data specify the following:

- Dφ11.
- Dφ2φ.
- Dφ3φ.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ANISOTROPIC, the table data specify the following:

- Dφ11.
- Dφ12.
- Dφ22.
- Dφ13.
- Dφ23.
- Dφ33.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Dielectric object.

### Exceptions

None.



## setValues(...)



This method modifies the Dielectric object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Dielectric ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dielectricpyc.htm?ContextScope=all#simaker-dielectricdielectricpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The Dielectric object has members with the same names and descriptions as the arguments to the [Dielectric ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dielectricpyc.htm?ContextScope=all#simaker-dielectricdielectricpyc)method.



## Corresponding analysis keywords

- [DIELECTRIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dielectric.htm?ContextScope=all#simakey-r-dielectric)