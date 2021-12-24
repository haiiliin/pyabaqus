# Hysteresis object

The Hysteresis object specifies the creep part of the material model for the hysteretic behavior of elastomers.

## Access

```
import material
mdb.models[name].materials[name].hyperelastic.hysteresis
import odbMaterial
session.odbs[name].materials[name].hyperelastic.hysteresis
```

## Hysteresis(...)



This method creates a Hysteresis object.



### Path

```
mdb.models[name].materials[name].hyperelastic.Hysteresis
session.odbs[name].materials[name].hyperelastic.Hysteresis
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

- Stress scaling factor.
- Creep parameter.
- Effective stress exponent.
- Creep strain exponent.

### Return value

A Hysteresis object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Hysteresis object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Hysteresis ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hysteresispyc.htm?ContextScope=all#simaker-hysteresishysteresispyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Hysteresis object has members with the same names and descriptions as the arguments to the [Hysteresis ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hysteresispyc.htm?ContextScope=all#simaker-hysteresishysteresispyc)method.



## Corresponding analysis keywords

- [HYSTERESIS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-hysteresis.htm?ContextScope=all#simakey-r-hysteresis)