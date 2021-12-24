# FluidCavity object

The FluidCavity object defines a surface-based cavity.

The FluidCavity object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## FluidCavity(...)



This method creates an FluidCavity object.



### Path

```
mdb.models[name].FluidCavity
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the FluidCavity object is created.

- *cavityPoint*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the fluid cavity reference point.

- *cavitySurface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surface forming the boundary of the fluid cavity.

- *interactionProperty*

  A String specifying the [FluidCavityProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypropertypyc.htm?ContextScope=all) object associated with this interaction.

### Optional arguments

- *ambientPressure*

  A Float specifying the magnitude of the ambient pressure. The default value is 0.0.

- *thickness*

  A Float specifying the out-of-plane thickness of the surface for two-dimensional models. This argument is valid only when using two-dimensional models. The default value is 1.0.

- *useAdiabatic*

  A Boolean specifying whether adiabatic behavior is assumed for the ideal gas. This argument is valid only when *interactionProperty* specifies a pneumatic definition. The default value is OFF.

- *checkNormals*

  A Boolean specifying whether the analysis will check the consistency of the surface normals. The default value is ON.

### Return value

A FluidCavity object.

### Exceptions

None.



## setValues(...)



This method modifies the FluidCavity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FluidCavity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypyc.htm?ContextScope=all#simaker-fluidcavityfluidcavitypyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## Members

The FluidCavity object has members with the same names and descriptions as the arguments to the [FluidCavity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypyc.htm?ContextScope=all#simaker-fluidcavityfluidcavitypyc)method.



## Corresponding analysis keywords

- [FLUID CAVITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-fluidcavity.htm?ContextScope=all#simakey-r-fluidcavity)