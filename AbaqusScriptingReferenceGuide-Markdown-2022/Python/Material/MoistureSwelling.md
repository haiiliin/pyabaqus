# MoistureSwelling object

The MoistureSwelling object defines moisture-driven swelling.

## Access

```
import material
mdb.models[name].materials[name].moistureSwelling
import odbMaterial
session.odbs[name].materials[name].moistureSwelling
```

## MoistureSwelling(...)



This method creates a MoistureSwelling object.



### Path

```
mdb.models[name].materials[name].MoistureSwelling
session.odbs[name].materials[name].MoistureSwelling
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

- Volumetric moisture swelling strain, εm⁢s.
- Saturation, s. This value must lie in the range 0≤s≤1.0.

### Return value

A MoistureSwelling object.

### Exceptions

None.



## setValues(...)



This method modifies the MoistureSwelling object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MoistureSwelling ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-moistureswellingpyc.htm?ContextScope=all#simaker-moistureswellingmoistureswellingpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The MoistureSwelling object has members with the same names and descriptions as the arguments to the [MoistureSwelling ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-moistureswellingpyc.htm?ContextScope=all#simaker-moistureswellingmoistureswellingpyc)method.

In addition, the MoistureSwelling object can have the following member:

- *ratios*

  A [Ratios](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ratiospyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [MOISTURE SWELLING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-moistureswelling.htm?ContextScope=all#simakey-r-moistureswelling)