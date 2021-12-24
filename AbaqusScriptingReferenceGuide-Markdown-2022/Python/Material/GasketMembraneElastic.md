# GasketMembraneElastic object

The GasketMembraneElastic object defines the elastic parameters for the membrane shear behavior of a gasket.

## Access

```
import material
mdb.models[name].materials[name].gasketMembraneElastic
import odbMaterial
session.odbs[name].materials[name].gasketMembraneElastic
```

## GasketMembraneElastic(...)



This method creates a GasketMembraneElastic object.



### Path

```
mdb.models[name].materials[name].GasketMembraneElastic
session.odbs[name].materials[name].GasketMembraneElastic
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

- Young's modulus, E.
- Poisson's ratio, ν.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A GasketMembraneElastic object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the GasketMembraneElastic object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GasketMembraneElastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gasketmembraneelasticpyc.htm?ContextScope=all#simaker-gasketmembraneelasticgasketmembraneelasticpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The GasketMembraneElastic object has members with the same names and descriptions as the arguments to the [GasketMembraneElastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gasketmembraneelasticpyc.htm?ContextScope=all#simaker-gasketmembraneelasticgasketmembraneelasticpyc)method.



## Corresponding analysis keywords

- [GASKET ELASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gasketelasticity.htm?ContextScope=all#simakey-r-gasketelasticity)