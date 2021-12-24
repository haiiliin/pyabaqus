# TensileFailure object

The TensileFailure object specifies the material tensile failure.

## Access

```
import material
mdb.models[name].materials[name].plastic.tensileFailure
mdb.models[name].materials[name].eos.tensileFailure
import odbMaterial
session.odbs[name].materials[name].plastic.tensileFailure
session.odbs[name].materials[name].eos.tensileFailure
```

## tensileFailure(...)



This method creates a tensileFailure object.



### Path

```
mdb.models[name].materials[name].plastic.TensileFailure
mdb.models[name].materials[name].eos.TensileFailure
session.odbs[name].materials[name].plastic.TensileFailure
session.odbs[name].materials[name].eos.TensileFailure
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *temperatureDependency*

  A boolean specifying whether the data depends on temperature. The default value is OFF.

- *elementDeletion*

  A boolean specifying whether element deletion is allowed. The default value is True.

- *pressure*

  A SymbolicConstant specifying the pressure stress. The Possible values are BRITTLE and DUCTILE.

- *shear*

  A SymbolicConstant specifying the deviatoric stress. Possible values are BRITTLE and DUCTILE.

### Table data

- The Hydrostatic cutoff stress (positive in tension).
- Temperature, if the data depend on temperature.
- Value of the first field variable if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

An TensileFailure object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the TensileFailure object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TensileFailure](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tensilefailurepyc.htm?ContextScope=all#simaker-tensilefailuretensilefailurepyc) method.

### Return value

None.

### Exceptions

RangeError.



## Members

The TensileFailure object has members with the same names and descriptions as the arguments to the [TensileFailure](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tensilefailurepyc.htm?ContextScope=all#simaker-tensilefailuretensilefailurepyc) method.



## Corresponding analysis keywords

- [TENSILE FAILURE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-tensilefailure.htm?ContextScope=all#simakey-r-tensilefailure)