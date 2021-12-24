# FluidExchange object

The FluidExchange object is used to define fluid exchange between two fluid cavities or between a fluid cavity and its environment.

The FluidExchange object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## FluidExchange(...)



This method creates an FluidExchange object.



### Path

```
mdb.models[name].FluidExchange
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the FluidExchange object is created.

- *firstCavity*

  A String specifying the first [FluidCavity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypyc.htm?ContextScope=all) object associated with this interaction. This will be the only cavity specified if *definition*=TO_ENVIRONMENT.

- *interactionProperty*

  A String specifying the [FluidExchangeProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidexchangepropertypyc.htm?ContextScope=all) object associated with this interaction.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the type of fluid exchange to be defined. Possible values are TO_ENVIRONMENT and BETWEEN_CAVITIES. The default value is TO_ENVIRONMENT.

- *secondCavity*

  A String specifying the second [FluidCavity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypyc.htm?ContextScope=all) object associated with this interaction. This argument is applicable only when *definition*=BETWEEN_CAVITIES.

- *exchangeArea*

  A Float specifying the effective exchange area. The default value is 1.0.

### Return value

A FluidExchange object.

### Exceptions

None.



## setValues(...)



This method modifies the FluidExchange object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FluidExchange ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidexchangepyc.htm?ContextScope=all#simaker-fluidexchangefluidexchangepyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## Members

The FluidExchange object has members with the same names and descriptions as the arguments to the [FluidExchange ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidexchangepyc.htm?ContextScope=all#simaker-fluidexchangefluidexchangepyc)method.



## Corresponding analysis keywords

- [FLUID EXCHANGE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-fluidexchange.htm?ContextScope=all#simakey-r-fluidexchange)