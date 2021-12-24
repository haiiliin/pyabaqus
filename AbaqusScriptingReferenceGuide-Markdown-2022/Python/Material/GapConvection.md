# GapConvection object

The GapConvection object specifies the Nusselt number (Nu) to calculate the convective coefficient for heat transfer between the gap flow and both the top and bottom surfaces of a coupled temperature-pore pressure cohesive element.

## Access

```
import material
mdb.models[name].materials[name].gapConvection
import odbMaterial
session.odbs[name].materials[name].gapConvection
```

## GapConvection(...)



This method creates a GapConvection object.



### Path

```
mdb.models[name].materials[name].GapConvection
session.odbs[name].materials[name].GapConvection
```

### Required arguments

- *type*

  An odb_String specifying the type of gap convection. Possible values are FLUX, TEMPERATURE, and TABULAR. The default value is FLUX.

### Optional arguments

If *type*=TABULAR, the following optional arguments can be used:

- *table*

  A sequence of sequences of Floats specifying the items described below.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

For *type*=TABULAR the table data specify the following:

- Nusselt number (Nu)
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A GapConvection object.

### Exceptions

None.



## setValues(...)



This method modifies the GapConvection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GapConvection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapconvectionpyc.htm?ContextScope=all#simaker-gapconvectiongapconvectionpyc) method.

### Return value

None.



## Members

The GapConvection object has members with the same names and descriptions as the arguments to the [GapConvection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapflowpyc.htm?ContextScope=all#simaker-gapflowgapflowpyc) method.



## Corresponding analysis keywords

- [GAP CONVECTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gapconvection.htm?ContextScope=all#simakey-r-gapconvection)