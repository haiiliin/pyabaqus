# AnnealTemperature object

The AnnealTemperature object specifies the material annealing temperature.

## Access

```
import material
mdb.models[name].materials[name].plastic.annealTemperature
import odbMaterial
session.odbs[name].materials[name].plastic.annealTemperature
```

## AnnealTemperature(...)



This method creates an AnnealTemperature object.



### Path

```
mdb.models[name].materials[name].plastic.AnnealTemperature
session.odbs[name].materials[name].plastic.AnnealTemperature
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- The annealing temperature, θθ.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

An AnnealTemperature object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the AnnealTemperature object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AnnealTemperature ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annealtemperaturepyc.htm?ContextScope=all#simaker-annealtemperatureannealtemperaturepyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The AnnealTemperature object has members with the same names and descriptions as the arguments to the [AnnealTemperature ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annealtemperaturepyc.htm?ContextScope=all#simaker-annealtemperatureannealtemperaturepyc)method.



## Corresponding analysis keywords

- [ANNEAL TEMPERATURE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-annealtemperature.htm?ContextScope=all#simakey-r-annealtemperature)