# LatentHeat object

The LatentHeat object specifies a material's latent heat.

## Access

```
import material
mdb.models[name].materials[name].latentHeat
import odbMaterial
session.odbs[name].materials[name].latentHeat
```

## LatentHeat(...)



This method creates a LatentHeat object.



### Path

```
mdb.models[name].materials[name].LatentHeat
session.odbs[name].materials[name].LatentHeat
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

- Latent heat per unit mass.
- Solidus temperature.
- Liquidus temperature.

### Return value

A LatentHeat object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the LatentHeat object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [LatentHeat ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-latentheatpyc.htm?ContextScope=all#simaker-latentheatlatentheatpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The LatentHeat object has members with the same names and descriptions as the arguments to the [LatentHeat ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-latentheatpyc.htm?ContextScope=all#simaker-latentheatlatentheatpyc)method.



## Corresponding analysis keywords

- [LATENT HEAT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-latentheat.htm?ContextScope=all#simakey-r-latentheat)