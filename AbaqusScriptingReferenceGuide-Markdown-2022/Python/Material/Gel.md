# Gel object

The Gel object defines a swelling gel.

## Access

```
import material
mdb.models[name].materials[name].gel
import odbMaterial
session.odbs[name].materials[name].gel
```

## Gel(...)



This method creates a Gel object.



### Path

```
mdb.models[name].materials[name].Gel
session.odbs[name].materials[name].Gel
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

- Radius of gel particles when completely dry, radry.
- Fully swollen radius of gel particles, raf.
- Number of gel particles per unit volume, ka.
- Relaxation time constant for long-term swelling of gel particles, τ1.

### Return value

A Gel object.

### Exceptions

None.



## setValues(...)



This method modifies the Gel object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Gel ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gelpyc.htm?ContextScope=all#simaker-gelgelpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The Gel object has members with the same names and descriptions as the arguments to the [Gel ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gelpyc.htm?ContextScope=all#simaker-gelgelpyc)method.



## Corresponding analysis keywords

- [GEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gel.htm?ContextScope=all#simakey-r-gel)