# FluidCavityPressure object

The FluidCavityPressure object stores the data for initial fluid cavity pressures. The base class*region* argument can not be specifed with this object.

The FluidCavityPressure object is derived from the [PredefinedField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].predefinedFields[name]
```

## FluidCavityPressure(...)



This method creates a FluidCavityPressure object.



### Path

```
mdb.models[name].FluidCavityPressure
```

### Required arguments

- *name*

  A String specifying the repository key.

- *fluidCavity*

  A String specifying the name of a Fluid Cavity Interaction.

- *fluidPressure*

  A Float specifying the initial fluid pressure.

### Optional arguments

None.

### Return value

A FluidCavityPressure object.

### Exceptions

None.



## setValues(...)



This method modifies the FluidCavityPressure object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FluidCavityPressure ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypressurepyc.htm?ContextScope=all#simaker-fluidcavitypressurefluidcavitypressurepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The FluidCavityPressure object has members with the same names and descriptions as the arguments to the [FluidCavityPressure ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypressurepyc.htm?ContextScope=all#simaker-fluidcavitypressurefluidcavitypressurepyc)method.

In addition, the FluidCavityPressure object can have the following member:

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object on which the *fluidCavity* interaction is specified.



## Corresponding analysis keywords

- [INITIAL CONDITIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-initialconditions.htm?ContextScope=all#simakey-r-initialconditions), TYPE=FLUID PRESSURE