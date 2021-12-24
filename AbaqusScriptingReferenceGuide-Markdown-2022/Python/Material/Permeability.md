# Permeability object

The Permeability object defines permeability for pore fluid flow.

## Access

```
import material
mdb.models[name].materials[name].permeability
import odbMaterial
session.odbs[name].materials[name].permeability
```

## Permeability(...)



This method creates a Permeability object.



### Path

```
mdb.models[name].materials[name].Permeability
session.odbs[name].materials[name].Permeability
```

### Required arguments

- *specificWeight*

  A Float specifying the specific weight of the wetting liquid, γwγw.

- *inertialDragCoefficient*

  A Float specifying The inertial drag coefficient of the wetting liquid, γwγw.

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of permeability. Possible values are ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=ISOTROPIC, the table data specify the following:

- k.
- Void ratio, e.
- Temperature, if the data depend on temperature.

If *type*=ORTHOTROPIC, the table data specify the following:

- k11.
- k22.
- k33.
- Void ratio, e.
- Temperature, if the data depend on temperature.

If *type*=ANISOTROPIC, the table data specify the following:

- k11.
- k12.
- k22.
- k13.
- k23.
- k33.
- Void ratio, e.
- Temperature, if the data depend on temperature.

### Return value

A Permeability object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Permeability object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Permeability ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-permeabilitypyc.htm?ContextScope=all#simaker-permeabilitypermeabilitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Permeability object has members with the same names and descriptions as the arguments to the [Permeability ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-permeabilitypyc.htm?ContextScope=all#simaker-permeabilitypermeabilitypyc)method.

In addition, the Permeability object can have the following members:

- *saturationDependence*

  A [SaturationDependence](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-saturationdependencepyc.htm?ContextScope=all) object specifying the dependence of the permeability of a material on the saturation of the wetting liquid.

- *velocityDependence*

  A [VelocityDependence](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitydependencepyc.htm?ContextScope=all) object specifying the dependence of the permeability of a material on the velocity of fluid flow.



## Corresponding analysis keywords

- [PERMEABILITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-permeability.htm?ContextScope=all#simakey-r-permeability)