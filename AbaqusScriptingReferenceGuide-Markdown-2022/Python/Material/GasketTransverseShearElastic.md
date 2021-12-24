# GasketTransverseShearElastic object

The GasketTransverseShearElastic object defines the elastic parameters for the transverse shear behavior of a gasket.

## Access

```
import material
mdb.models[name].materials[name].gasketTransverseShearElastic
import odbMaterial
session.odbs[name].materials[name].gasketTransverseShearElastic
```

## GasketTransverseShearElastic(...)



This method creates a GasketTransverseShearElastic object.



### Path

```
mdb.models[name].materials[name].GasketTransverseShearElastic
session.odbs[name].materials[name].GasketTransverseShearElastic
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *variableUnits*

  A SymbolicConstant specifying the unit system in which the transverse shear behavior will be defined. Possible values are STRESS and FORCE. The default value is STRESS.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- Shear stiffness. (This value cannot be negative.)
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A GasketTransverseShearElastic object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the GasketTransverseShearElastic object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GasketTransverseShearElastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gaskettransverseshearelasticpyc.htm?ContextScope=all#simaker-gaskettransverseshearelasticgaskettransverseshearelpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The GasketTransverseShearElastic object has members with the same names and descriptions as the arguments to the [GasketTransverseShearElastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gaskettransverseshearelasticpyc.htm?ContextScope=all#simaker-gaskettransverseshearelasticgaskettransverseshearelpyc)method.



## Corresponding analysis keywords

- [GASKET ELASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gasketelasticity.htm?ContextScope=all#simakey-r-gasketelasticity)