# MagneticPermeability object

The MagneticPermeability object specifies magnetic permeability.

## Access

```
import material
mdb.models[name].materials[name].magneticPermeability
import odbMaterial
session.odbs[name].materials[name].magneticPermeability
```

## MagneticPermeability(...)



This method creates a MagneticPermeability object.



### Path

```
mdb.models[name].materials[name].MagneticPermeability
session.odbs[name].materials[name].MagneticPermeability
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below in “Table data.” If *type*=ORTHOTROPIC and nonlinearBH=ON, the data specified in the *table* is for the first direction and *table2* and *table3* must be specified.

- *table2*

  A sequence of sequences of Floats specifying the items described below in “Table data” in the second direction. *table2* must be specified only if *type*=ORTHOTROPIC and nonlinearBH=ON.

- *table3*

  A sequence of sequences of Floats specifying the items described below in “Table data” in the third direction. *table3* must be specified only if *type*=ORTHOTROPIC and nonlinearBH=ON.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of magnetic permeability. Possible values are ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.

- *frequencyDependency*

  A Boolean specifying whether the data depend on frequency. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *nonlinearBH*

  A Boolean specifying whether the magnetic behavior is nonlinear and available in tabular form of magnetic flux density versus magnetic field values. The default value is OFF.

### Table data

If *type*=ISOTROPIC, the table data specify the following:

- Magnetic permeability.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ISOTROPIC, and *nonlinearBH*=TRUE, the table data specify the following:

- Magntitude of the magnetic flux density vector.
- Magnitude of the magnetic field vector.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ORTHOTROPIC, the table data specify the following:

- μ11E.
- μ22E.
- μ33E.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ORTHOTROPIC, and *nonlinearBH*=TRUE, the table data specify the following:

- Magntitude of the magnetic flux density vector in the first direction.
- Magnitude of the magnetic field vector in the second direction.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ANISOTROPIC, the table data specify the following:

- μ11E.
- μ12E.
- μ22E.
- μ13E.
- μ23E.
- μ33E.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A MagneticPermeability object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the MagneticPermeability object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MagneticPermeability ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-magneticpermeabilitypyc.htm?ContextScope=all#simaker-magneticpermeabilitymagneticpermeabilitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The MagneticPermeability object has members with the same names and descriptions as the arguments to the [MagneticPermeability ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-magneticpermeabilitypyc.htm?ContextScope=all#simaker-magneticpermeabilitymagneticpermeabilitypyc)method.



## Corresponding analysis keywords

- [MAGNETIC PERMEABILITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-magneticpermeability.htm?ContextScope=all#simakey-r-magneticpermeability)