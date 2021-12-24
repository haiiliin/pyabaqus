# ElectricalConductivity object

The ElectricalConductivity object specifies electrical conductivity.

## Access

```
import material
mdb.models[name].materials[name].electricalConductivity
import odbMaterial
session.odbs[name].materials[name].electricalConductivity
```

## ElectricalConductivity(...)



This method creates an ElectricalConductivity object.



### Path

```
mdb.models[name].materials[name].ElectricalConductivity
session.odbs[name].materials[name].ElectricalConductivity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of electrical conductivity. Possible values are ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.

- *frequencyDependency*

  A Boolean specifying whether the data depend on frequency. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=ISOTROPIC, the table data specify the following:

- Electrical conductivity.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ORTHOTROPIC, the table data specify the following:

- σE1E.
- σE2E.
- σE3E.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ANISOTROPIC, the table data specify the following:

- σ11E.
- σ12E.
- σE2E.
- σE3E.
- σE3E.
- σE3E.
- Frequency, if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

An ElectricalConductivity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ElectricalConductivity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ElectricalConductivity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-electricalconductivitypyc.htm?ContextScope=all#simaker-electricalconductivityelectricalconductivitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ElectricalConductivity object has members with the same names and descriptions as the arguments to the [ElectricalConductivity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-electricalconductivitypyc.htm?ContextScope=all#simaker-electricalconductivityelectricalconductivitypyc)method.



## Corresponding analysis keywords

- [ELECTRICAL CONDUCTIVITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-electricalconductivity.htm?ContextScope=all#simakey-r-electricalconductivity)