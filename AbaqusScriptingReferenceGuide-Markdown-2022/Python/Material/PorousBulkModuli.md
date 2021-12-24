# PorousBulkModuli object

The PorousBulkModuli object defines bulk moduli for soils and rocks.

## Access

```
import material
mdb.models[name].materials[name].porousBulkModuli
import odbMaterial
session.odbs[name].materials[name].porousBulkModuli
```

## PorousBulkModuli(...)



This method creates a PorousBulkModuli object.



### Path

```
mdb.models[name].materials[name].PorousBulkModuli
session.odbs[name].materials[name].PorousBulkModuli
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

### Table data

- Bulk modulus of solid grains.
- Bulk modulus of permeating fluid.
- Temperature, if the data depend on temperature.

### Return value

A PorousBulkModuli object.

### Exceptions

None.



## setValues(...)



This method modifies the PorousBulkModuli object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PorousBulkModuli ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousbulkmodulipyc.htm?ContextScope=all#simaker-porousbulkmoduliporousbulkmodulipyc)method.

### Return value

None.

### Exceptions

None.



## Members

The PorousBulkModuli object has members with the same names and descriptions as the arguments to the [PorousBulkModuli ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousbulkmodulipyc.htm?ContextScope=all#simaker-porousbulkmoduliporousbulkmodulipyc)method.



## Corresponding analysis keywords

- [POROUS BULK MODULI](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-porousbulkmoduli.htm?ContextScope=all#simakey-r-porousbulkmoduli)