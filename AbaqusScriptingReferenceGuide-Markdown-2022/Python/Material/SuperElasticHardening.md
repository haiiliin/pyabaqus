# SuperElasticHardening object

The SuperElasticHardening object specifies the dependence of the yield stress on the total strain to define the piecewise linear hardening of a martensite material model.

## Access

```
import material
mdb.models[name].materials[name].superElasticity.SuperElasticHardening
import odbMaterial
session.odbs[name].materials[name].superElasticity.SuperElasticHardening
```

## SuperElasticHardening(...)



This method creates a SuperElasticHardening object.



### Path

```
mdb.models[name].materials[name].superElasticity.SuperElasticHardening
session.odbs[name].materials[name].superElasticity.SuperElasticHardening
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Table data

- Yield Stress.
- Total Strain.

### Return value

A SuperElasticHardening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the SuperElasticHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SuperElasticHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelastichardeningpyc.htm?ContextScope=all#simaker-superelastichardeningsuperelastichardeningpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The SuperElasticHardening object has members with the same names and descriptions as the arguments to the [SuperElasticHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelastichardeningpyc.htm?ContextScope=all#simaker-superelastichardeningsuperelastichardeningpyc)method.



## Corresponding analysis keywords

- [SUPERELASTIC HARDENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-superelastichardening.htm?ContextScope=all#simakey-r-superelastichardening)