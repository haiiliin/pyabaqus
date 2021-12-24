# SuperElasticHardeningModifications object

The SuperElasticHardeningModifications object specifies the variation of the transformation stress levels of a material model.

## Access

```
import material
mdb.models[name].materials[name].superElasticity.SuperElasticHardening
import odbMaterial
session.odbs[name].materials[name].superElasticity.SuperElasticHardening
```

## SuperElasticHardeningModifications(...)



This method creates a SuperElasticHardeningModifications object.



### Path

```
mdb.models[name].materials[name].superElasticity.SuperElasticHardeningModifications
session.odbs[name].materials[name].superElasticity.SuperElasticHardeningModifications
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below or user-defined data if the dependence of the transformation stress levels on plastic strain is specified in a user subroutine.

### Table data

- Start of Transformation (Loading).
- End of Transformation (Loading).
- Start of Transformation (Unloading).
- End of Transformation (Unloading).
- Plastic Strain.

### Return value

A SuperElasticHardeningModifications object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the SuperElasticHardeningModifications object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SuperElasticHardeningModifications ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelastichardeningmodificationpyc.htm?ContextScope=all#simaker-superelastichardeningmodificationssuperelastichardeningmodificationspyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The SuperElasticHardeningModifications object has members with the same names and descriptions as the arguments to the [SuperElasticHardeningModifications ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelastichardeningmodificationpyc.htm?ContextScope=all#simaker-superelastichardeningmodificationssuperelastichardeningmodificationspyc)method.



## Corresponding analysis keywords

- [SUPERELASTIC HARDENING MODIFICATIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-superelastichardeningmodifications.htm?ContextScope=all#simakey-r-superelastichardeningmodifications)