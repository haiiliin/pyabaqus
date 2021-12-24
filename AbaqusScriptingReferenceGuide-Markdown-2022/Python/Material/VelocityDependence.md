# VelocityDependence object

The VelocityDependence object specifies the dependence of the permeability of a material on the velocity of fluid flow.

## Access

```
import material
mdb.models[name].materials[name].permeability.velocityDependence
import odbMaterial
session.odbs[name].materials[name].permeability.velocityDependence
```

## VelocityDependence(...)



This method creates a VelocityDependence object.



### Path

```
mdb.models[name].materials[name].permeability.VelocityDependence
session.odbs[name].materials[name].permeability.VelocityDependence
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

- β. Only β> 0.0 is allowed.
- Void ratio, ee.

### Return value

A VelocityDependence object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the VelocityDependence object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [VelocityDependence ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitydependencepyc.htm?ContextScope=all#simaker-velocitydependencevelocitydependencepyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The VelocityDependence object has members with the same names and descriptions as the arguments to the [VelocityDependence ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitydependencepyc.htm?ContextScope=all#simaker-velocitydependencevelocitydependencepyc)method.



## Corresponding analysis keywords

- [PERMEABILITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-permeability.htm?ContextScope=all#simakey-r-permeability)