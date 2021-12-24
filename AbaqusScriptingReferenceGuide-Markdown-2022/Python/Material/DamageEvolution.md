# DamageEvolution object

The DamageEvolution object specifies material properties to define the evolution of damage.

## Access

```
import material
mdb.models[name].materials[name].ductileDamageInitiation\
.damageEvolution
mdb.models[name].materials[name].fldDamageInitiation.damageEvolution
mdb.models[name].materials[name].flsdDamageInitiation.damageEvolution
mdb.models[name].materials[name].hashinDamageInitiation\
.damageEvolution
mdb.models[name].materials[name].johnsonCookDamageInitiation\
.damageEvolution
mdb.models[name].materials[name].maxeDamageInitiation.damageEvolution
mdb.models[name].materials[name].maxpeDamageInitiation.damageEvolution
mdb.models[name].materials[name].maxpsDamageInitiation.damageEvolution
mdb.models[name].materials[name].maxsDamageInitiation.damageEvolution
mdb.models[name].materials[name].mkDamageInitiation.damageEvolution
mdb.models[name].materials[name].msfldDamageInitiation.damageEvolution
mdb.models[name].materials[name].quadeDamageInitiation.damageEvolution
mdb.models[name].materials[name].quadsDamageInitiation.damageEvolution
mdb.models[name].materials[name].shearDamageInitiation.damageEvolution
import odbMaterial
session.odbs[name].materials[name].ductileDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].fldDamageInitiation.damageEvolution
session.odbs[name].materials[name].flsdDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].hashinDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].johnsonCookDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].maxeDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].maxpeDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].maxpsDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].maxsDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].mkDamageInitiation.damageEvolution
session.odbs[name].materials[name].msfldDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].quadeDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].quadsDamageInitiation\
.damageEvolution
session.odbs[name].materials[name].shearDamageInitiation\
.damageEvolution
```

## DamageEvolution(...)



This method creates a DamageEvolution object.



### Path

```
mdb.models[name].materials[name].ductileDamageInitiation\
.DamageEvolution
mdb.models[name].materials[name].fldDamageInitiation.DamageEvolution
mdb.models[name].materials[name].flsdDamageInitiation.DamageEvolution
mdb.models[name].materials[name].hashinDamageInitiation\
.DamageEvolution
mdb.models[name].materials[name].johnsonCookDamageInitiation\
.DamageEvolution
mdb.models[name].materials[name].maxeDamageInitiation.DamageEvolution
mdb.models[name].materials[name].maxpeDamageInitiation.DamageEvolution
mdb.models[name].materials[name].maxpsDamageInitiation.DamageEvolution
mdb.models[name].materials[name].maxsDamageInitiation.DamageEvolution
mdb.models[name].materials[name].mkDamageInitiation.DamageEvolution
mdb.models[name].materials[name].msfldDamageInitiation.DamageEvolution
mdb.models[name].materials[name].quadeDamageInitiation.DamageEvolution
mdb.models[name].materials[name].quadsDamageInitiation.DamageEvolution
mdb.models[name].materials[name].shearDamageInitiation.DamageEvolution
session.odbs[name].materials[name].ductileDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].fldDamageInitiation.DamageEvolution
session.odbs[name].materials[name].flsdDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].hashinDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].johnsonCookDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].maxeDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].maxpeDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].maxpsDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].maxsDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].mkDamageInitiation.DamageEvolution
session.odbs[name].materials[name].msfldDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].quadeDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].quadsDamageInitiation\
.DamageEvolution
session.odbs[name].materials[name].shearDamageInitiation\
.DamageEvolution
```

### Required arguments

- *type*

  A SymbolicConstant specifying the type of damage evolution. Possible values are DISPLACEMENT and ENERGY.

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *degradation*

  A SymbolicConstant specifying the degradation. Possible values are MAXIMUM and MULTIPLICATIVE. The default value is MAXIMUM.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *mixedModeBehavior*

  A SymbolicConstant specifying the mixed mode behavior. Possible values are MODE_INDEPENDENT, TABULAR, POWER_LAW, and BK. The default value is MODE_INDEPENDENT.

- *modeMixRatio*

  A SymbolicConstant specifying the mode mix ratio. Possible values are ENERGY and TRACTION. The default value is ENERGY.

- *power*

  None or a Float specifying the exponent in the power law or the Benzeggagh-Kenane criterion that defines the variation of fracture energy with mode mix for cohesive elements. The default value is None.

- *softening*

  A SymbolicConstant specifying the softening. Possible values are LINEAR, EXPONENTIAL, and TABULAR. The default value is LINEAR.

### Table data

If *type*=DISPLACEMENT, and *softening*=LINEAR, and *mixedModeBehavior*=MODE_INDEPENDENT, the table data specify the following:

- Equivalent total or plastic displacement at failure, measured from the time of damage initiation.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENERGY, and *softening*=LINEAR, and *mixedModeBehavior*=MODE_INDEPENDENT, the table data specify the following:

- Fracture energy.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT, and *softening*=LINEAR, and *mixedModeBehavior*=TABULAR, the table data specify the following:

- Total displacement at failure, measured from the time of damage initiation.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENERGY, and *softening*=LINEAR, and *mixedModeBehavior*=TABULAR, the table data specify the following:

- Fracture energy.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT, and *softening*=EXPONENTIAL, and *mixedModeBehavior*=MODE_INDEPENDENT, the table data specify the following:

- Equivalent total or plastic displacement at failure, measured from the time of damage initiation.
- Exponential law parameter.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENERGY, and *softening*=EXPONENTIAL, and *mixedModeBehavior*=MODE_INDEPENDENT, the table data specify the following:

- Fracture energy.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT, and *softening*=EXPONENTIAL, and *mixedModeBehavior*=TABULAR, the table data specify the following:

- Total displacement at failure, measured from the time of damage initiation.
- Exponential law parameter.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENERGY, and *softening*=EXPONENTIAL, and *mixedModeBehavior*=TABULAR, the table data specify the following:

- Fracture energy.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT, and *softening*=TABULAR, and *mixedModeBehavior*=MODE_INDEPENDENT, the table data specify the following:

- Damage variable.
- Equivalent total or plastic displacement, measured from the time of damage initiation.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT, and *softening*=TABULAR, and *mixedModeBehavior*=TABULAR, the table data specify the following:

- Damage variable.
- Equivalent total or plastic displacement, measured from the time of damage initiation.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three-dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENERGY, and *softening*=LINEAR or EXPONENTIAL, and *mixedModeBehavior*=POWER_LAW or BK, the table data specify the following:

- Normal mode fracture energy.
- Shear mode fracture energy for failure in the first shear direction.
- Shear mode fracture energy for failure in the second shear direction.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENERGY, *softening*=LINEAR and constructor for [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all)=HashinDamageInitiation the table data specify the following:

- Fiber tensile fracture energy.
- Fiber compressive fracture energy.
- Matrix tensile fracture energy.
- Matrix compressive fracture energy.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A DamageEvolution object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the DamageEvolution object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DamageEvolution ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageevolutionpyc.htm?ContextScope=all#simaker-damageevolutiondamageevolutionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The DamageEvolution object has members with the same names and descriptions as the arguments to the [DamageEvolution ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageevolutionpyc.htm?ContextScope=all#simaker-damageevolutiondamageevolutionpyc)method.



## Corresponding analysis keywords

- [DAMAGE EVOLUTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damageevolution.htm?ContextScope=all#simakey-r-damageevolution)