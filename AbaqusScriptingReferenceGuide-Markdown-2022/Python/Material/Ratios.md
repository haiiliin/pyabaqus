# Ratios object

The Ratios object specifies ratios that define anisotropic swelling.

## Access

```
import material
mdb.models[name].materials[name].moistureSwelling.ratios
mdb.models[name].materials[name].swelling.ratios
import odbMaterial
session.odbs[name].materials[name].moistureSwelling.ratios
session.odbs[name].materials[name].swelling.ratios
```

## Ratios(...)



This method creates a Ratios object.



### Path

```
mdb.models[name].materials[name].moistureSwelling.Ratios
mdb.models[name].materials[name].swelling.Ratios
session.odbs[name].materials[name].moistureSwelling.Ratios
session.odbs[name].materials[name].swelling.Ratios
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- r11.
- r22.
- r33.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Ratios object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Ratios object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Ratios ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ratiospyc.htm?ContextScope=all#simaker-ratiosratiospyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Ratios object has members with the same names and descriptions as the arguments to the [Ratios ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ratiospyc.htm?ContextScope=all#simaker-ratiosratiospyc)method.



## Corresponding analysis keywords

- [RATIOS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-ratios.htm?ContextScope=all#simakey-r-ratios)