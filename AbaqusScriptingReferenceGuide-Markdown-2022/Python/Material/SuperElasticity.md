# SuperElasticity object

The SuperElasticity object specifies a superelastic material model.

## Access

```
import material
mdb.models[name].materials[name].superElasticity
import odbMaterial
session.odbs[name].materials[name].superElasticity
```

## SuperElasticity(...)



This method creates a SuperElasticity object.



### Path

```
mdb.models[name].materials[name].SuperElasticity
session.odbs[name].materials[name].SuperElasticity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *nonassociated*

  None or a Float specifying the volumetric transformation strain. If *nonassociated*=None, the value of the volumetric transformation strain is equal to the uniaxial transformation strain. The default value is None.

### Table data

- Young's Modulus (Martensite).
- Poisson's Ratio (Martensite).
- Transformation Strain.
- Start of Transformation (Loading).
- End of Transformation (Loading).
- Start of Transformation (Unloading).
- End of Transformation (Unloading).
- Start of Transformation in Compression (Loading).
- Reference Temperature.
- Loading.
- Unloading.

### Return value

A SuperElasticity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the SuperElasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SuperElasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelasticitypyc.htm?ContextScope=all#simaker-superelasticitysuperelasticitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The SuperElasticity object has members with the same names and descriptions as the arguments to the [SuperElasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelasticitypyc.htm?ContextScope=all#simaker-superelasticitysuperelasticitypyc)method.

In addition, the SuperElasticity object can have the following members:

- *superElasticHardening*

  A [SuperElasticHardening object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelastichardeningpyc.htm?ContextScope=all#simaker-c-superelastichardeningpyc).

- *superElasticHardeningModifications*

  A [SuperElasticHardeningModifications object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelastichardeningmodificationpyc.htm?ContextScope=all#simaker-c-superelastichardeningmodificationpyc).



## Corresponding analysis keywords

- [SUPERELASTIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-superelastic.htm?ContextScope=all#simakey-r-superelastic)