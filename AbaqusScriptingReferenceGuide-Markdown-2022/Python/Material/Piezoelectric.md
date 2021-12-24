# Piezoelectric object

The Piezoelectric object specifies piezoelectric material properties.

## Access

```
import material
mdb.models[name].materials[name].piezoelectric
import odbMaterial
session.odbs[name].materials[name].piezoelectric
```

## Piezoelectric(...)



This method creates a Piezoelectric object.



### Path

```
mdb.models[name].materials[name].Piezoelectric
session.odbs[name].materials[name].Piezoelectric
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of material coefficients for the piezoelectric property. Possible values are STRAIN and STRESS. The default value is STRESS.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=STRESS, the table data specify the following:

- e1 11φ.
- e1 22φ.
- e1 33φ.
- e1 12φ.
- e1 13φ.
- e1 23φ.
- e2 11φ.
- e2 22φ.
- e2 33φ.
- e2 12φ.
- e2 13φ.
- e2 23φ.
- e3 11φ.
- e3 22φ.
- e3 33φ.
- e3 12φ.
- e3 13φ.
- e3 23φ.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=STRAIN, the table data specify the following:

- d1 11φ.
- d1 22φ.
- d1 33φ.
- d1 12φ.
- d1 13φ.
- d1 23φ.
- d2 11φ.
- d2 22φ.
- d2 33φ.
- d2 12φ.
- d2 13φ.
- d2 23φ.
- d3 11φ.
- d3 22φ.
- d3 33φ.
- d3 13φ.
- d3 23φ.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A Piezoelectric object.

### Exceptions

None.



## setValues(...)



This method modifies the Piezoelectric object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Piezoelectric ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-piezoelectricpyc.htm?ContextScope=all#simaker-piezoelectricpiezoelectricpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The Piezoelectric object has members with the same names and descriptions as the arguments to the [Piezoelectric ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-piezoelectricpyc.htm?ContextScope=all#simaker-piezoelectricpiezoelectricpyc)method.



## Corresponding analysis keywords

- [PIEZOELECTRIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-piezoelectric.htm?ContextScope=all#simakey-r-piezoelectric)