# DamageStabilization object

The DamageStabilization object specifies the viscosity coefficients for the damage model for fiber-reinforced materials.

## Access

```
import material
mdb.models[name].materials[name].ductileDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].fldDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].flsdDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].hashinDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].johnsonCookDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].maxeDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].maxpeDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].maxpsDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].maxsDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].mkDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].msfldDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].quadeDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].quadsDamageInitiation\
.damageStabilization
mdb.models[name].materials[name].shearDamageInitiation\
.damageStabilization
import odbMaterial
session.odbs[name].materials[name].ductileDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].fldDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].flsdDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].hashinDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].johnsonCookDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].maxeDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].maxpeDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].maxpsDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].maxsDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].mkDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].msfldDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].quadeDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].quadsDamageInitiation\
.damageStabilization
session.odbs[name].materials[name].shearDamageInitiation\
.damageStabilization
```

## DamageStabilization(...)



This method creates a DamageStabilization object.



### Path

```
mdb.models[name].materials[name].ductileDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].fldDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].flsdDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].hashinDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].johnsonCookDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].maxeDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].maxpeDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].maxpsDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].maxsDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].mkDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].msfldDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].quadeDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].quadsDamageInitiation\
.DamageStabilization
mdb.models[name].materials[name].shearDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].ductileDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].fldDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].flsdDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].hashinDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].johnsonCookDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].maxeDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].maxpeDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].maxpsDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].maxsDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].mkDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].msfldDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].quadeDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].quadsDamageInitiation\
.DamageStabilization
session.odbs[name].materials[name].shearDamageInitiation\
.DamageStabilization
```

### Required arguments

- *fiberTensileCoeff*

  A Float specifying the viscosity coefficient for the fiber tensile failure mode.

- *fiberCompressiveCoeff*

  A Float specifying the viscosity coefficient for the fiber compressive failure mode.

- *matrixTensileCoeff*

  A Float specifying the viscosity coefficient for the matrix tensile failure mode.

- *matrixCompressiveCoeff*

  A Float specifying the viscosity coefficient for the matrix compressive failure mode.

### Optional arguments

None.

### Return value

A DamageStabilization object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the DamageStabilization object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DamageStabilization ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damagestabilizationpyc.htm?ContextScope=all#simaker-damagestabilizationdamagestabilizationpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The DamageStabilization object has members with the same names and descriptions as the arguments to the [DamageStabilization ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damagestabilizationpyc.htm?ContextScope=all#simaker-damagestabilizationdamagestabilizationpyc)method.



## Corresponding analysis keywords

- [DAMAGE STABILIZATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damagestabilization.htm?ContextScope=all#simakey-r-damagestabilization)