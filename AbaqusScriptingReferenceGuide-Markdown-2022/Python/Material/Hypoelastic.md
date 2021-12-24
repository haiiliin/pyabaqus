# Hypoelastic object

The Hypoelastic object specifies hypoelastic material properties.

## Access

```
import material
mdb.models[name].materials[name].hypoelastic
import odbMaterial
session.odbs[name].materials[name].hypoelastic
```

## Hypoelastic(...)



This method creates a Hypoelastic object.



### Path

```
mdb.models[name].materials[name].Hypoelastic
session.odbs[name].materials[name].Hypoelastic
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *user*

  A Boolean specifying that hypoelasticity is defined by user subroutine [UHYPEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-uhypel.htm?ContextScope=all#simasub-c-uhypel). The default value is OFF.

### Table data

- Instantaneous Young's modulus, E.
- Instantaneous Poisson's ratio, ν.
- First strain invariant, I1.
- Second strain invariant, I2.
- Third strain invariant, I3.

### Return value

A Hypoelastic object.

### Exceptions

None.



## setValues(...)



This method modifies the Hypoelastic object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Hypoelastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hypoelasticpyc.htm?ContextScope=all#simaker-hypoelastichypoelasticpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The Hypoelastic object has members with the same names and descriptions as the arguments to the [Hypoelastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hypoelasticpyc.htm?ContextScope=all#simaker-hypoelastichypoelasticpyc)method.



## Corresponding analysis keywords

- [HYPOELASTIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-hypoelastic.htm?ContextScope=all#simakey-r-hypoelastic)