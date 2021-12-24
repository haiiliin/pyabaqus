# FluidInflator object

The FluidInflator object is used to define a fluid inflator to model deployment of an airbag.

The FluidInflator object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## FluidInflator(...)



This method creates a FluidInflator object.



### Path

```
mdb.models[name].FluidInflator
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the FluidInflator object is created.

- *cavity*

  A String specifying the first [FluidCavity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypyc.htm?ContextScope=all) object associated with this interaction.

- *interactionProperty*

  A String specifying the [FluidInflatorProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidinflatorpropertypyc.htm?ContextScope=all) object associated with this interaction.

### Optional arguments

- *inflationTimeAmplitude*

  A string specifying the name of the amplitude curve defining a mapping between the inflation time and the actual time.

- *massFlowAmplitude*

  A string specifying the name of the amplitude curve by which to modify the mass flow rate.

### Return value

A FluidInflator object.

### Exceptions

None.



## setValues(...)



This method modifies the FluidInflator object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FluidInflator ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidinflatorpyc.htm?ContextScope=all#simaker-fluidinflatorfluidinflatorpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## Members

The FluidInflator object has members with the same names and descriptions as the arguments to the [FluidInflator ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidinflatorpyc.htm?ContextScope=all#simaker-fluidinflatorfluidinflatorpyc)method.



## Corresponding analysis keywords

- [FLUID INFLATOR](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-fluidinflator.htm?ContextScope=all#simakey-r-fluidinflator)