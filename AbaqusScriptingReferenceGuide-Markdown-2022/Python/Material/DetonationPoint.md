# DetonationPoint object

A DetonationPoint object specifies a suboption of the Eos object. The DetonationPoint object defines either isotropic linear elastic shear or linear viscous shear behavior for a hydrodynamic material.

## Access

```
import material
mdb.models[name].materials[name].eos.detonationPoint
import odbMaterial
session.odbs[name].materials[name].eos.detonationPoint
```

## DetonationPoint(...)



This method creates a DetonationPoint object.



### Path

```
mdb.models[name].materials[name].eos.DetonationPoint
session.odbs[name].materials[name].eos.DetonationPoint
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

- X value for coordinate of detonation point.
- Y value for coordinate of detonation point.
- Z value for coordinate of detonation point.
- Detonation delay time.

### Return value

A DetonationPoint object.

### Exceptions

None.



## setValues(...)



This method modifies the DetonationPoint object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DetonationPoint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-detonationpointpyc.htm?ContextScope=all#simaker-detonationpointdetonationpointpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The DetonationPoint object has members with the same names and descriptions as the arguments to the [DetonationPoint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-detonationpointpyc.htm?ContextScope=all#simaker-detonationpointdetonationpointpyc)method.



## Corresponding analysis keywords

- [DETONATION POINT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-detonationpoint.htm?ContextScope=all#simakey-r-detonationpoint)