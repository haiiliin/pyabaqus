# SaturationDependence object

The SaturationDependence object specifies the dependence of the permeability of a material on the saturation of the wetting liquid.

## Access

```
import material
mdb.models[name].materials[name].permeability.saturationDependence
import odbMaterial
session.odbs[name].materials[name].permeability.saturationDependence
```

## SaturationDependence(...)



This method creates a SaturationDependence object.



### Path

```
mdb.models[name].materials[name].permeability.SaturationDependence
session.odbs[name].materials[name].permeability.SaturationDependence
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

- ks. (Dimensionless.)
- Saturation, s. (Dimensionless.)

### Return value

A SaturationDependence object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the SaturationDependence object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SaturationDependence ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-saturationdependencepyc.htm?ContextScope=all#simaker-saturationdependencesaturationdependencepyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The SaturationDependence object has members with the same names and descriptions as the arguments to the [SaturationDependence ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-saturationdependencepyc.htm?ContextScope=all#simaker-saturationdependencesaturationdependencepyc)method.



## Corresponding analysis keywords

- [PERMEABILITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-permeability.htm?ContextScope=all#simakey-r-permeability)