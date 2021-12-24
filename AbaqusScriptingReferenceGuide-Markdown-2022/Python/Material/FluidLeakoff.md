# FluidLeakoff object

The FluidLeakoff object specifies leak-off coefficients for pore pressure cohesive elements.

## Access

```
import material
mdb.models[name].materials[name].fluidLeakoff
import odbMaterial
session.odbs[name].materials[name].fluidLeakoff
```

## FluidLeakoff(...)



This method creates a FluidLeakoff object.



### Path

```
mdb.models[name].materials[name].FluidLeakoff
session.odbs[name].materials[name].FluidLeakoff
```

### Required arguments

None.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *type*

  A SymbolicConstant specifying the type of fluid leak-off. Possible values are COEFFICIENTS and USER. The default value is COEFFICIENTS.

- *table*

  A sequence of sequences of Floats specifying the items described below. The default value is an empty sequence.

### Table data

The table data specify the following:

- Fluid leak-off coefficient at top element surface.
- Fluid leak-off coefficient at bottom element surface.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A FluidLeakoff object.

### Exceptions

None.



## setValues(...)



This method modifies the FluidLeakoff object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FluidLeakoff ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidleakoffpyc.htm?ContextScope=all#simaker-fluidleakofffluidleakoffpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The FluidLeakoff object has members with the same names and descriptions as the arguments to the [FluidLeakoff ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidleakoffpyc.htm?ContextScope=all#simaker-fluidleakofffluidleakoffpyc)method.



## Corresponding analysis keywords

- [FLUID LEAKOFF](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-fluidleakoff.htm?ContextScope=all#simakey-r-fluidleakoff)