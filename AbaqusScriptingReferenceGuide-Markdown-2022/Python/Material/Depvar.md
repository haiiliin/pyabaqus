# Depvar object

The Depvar object specifies solution-dependent state variables.

## Access

```
import material
mdb.models[name].materials[name].depvar
import odbMaterial
session.odbs[name].materials[name].depvar
```

## Depvar(...)



This method creates a Depvar object.



### Path

```
mdb.models[name].materials[name].Depvar
session.odbs[name].materials[name].Depvar
```

### Required arguments

None.

### Optional arguments

- *deleteVar*

  An Int specifying the state variable number controlling the element deletion flag. The default value is 0.This argument applies only to Abaqus/Explicit analyses.

- *n*

  An Int specifying the number of solution-dependent state variables required at each integration point. The default value is 0.

### Return value

A Depvar object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Depvar object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Depvar ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-depvarpyc.htm?ContextScope=all#simaker-depvardepvarpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Depvar object has members with the same names and descriptions as the arguments to the [Depvar ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-depvarpyc.htm?ContextScope=all#simaker-depvardepvarpyc)method.



## Corresponding analysis keywords

- [DEPVAR](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-depvar.htm?ContextScope=all#simakey-r-depvar)