# ModelChange object

The ModelChange object defines model change interactions for element removal and reactivation.

The ModelChange object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## ModelChange(...)



This method creates a ModelChange object.



### Path

```
mdb.models[name].ModelChange
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the ModelChange object is created.

### Optional arguments

- *isRestart*

  A Boolean specifying whether this interaction is being used solely to indicate that model change may be required in a subsequent restart analysis (either for elements or contact pairs). The default value is OFF.

- *regionType*

  A SymbolicConstant specifying the region selection type. This argument is valid only when *isRestart*=False. Possible values are GEOMETRY, SKINS, STRINGERS, and ELEMENTS. The default value is GEOMETRY.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the elements to be removed or reactivated. This argument is valid only when *isRestart*=False.

- *activeInStep*

  A Boolean specifying whether elements are being removed or reactivated. This argument is valid only when *isRestart*=False. The default value is OFF.

- *includeStrain*

  A Boolean specifying whether stress/displacement elements are reactivated with strain. This argument is valid only when *isRestart*=False and when *activeInStep*=True. The default value is OFF.

### Return value

A ModelChange object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing ModelChange object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ModelChange ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelchangepyc.htm?ContextScope=all#simaker-modelchangemodelchangepyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data of an existing ModelChange object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *activeInStep*

  A Boolean specifying whether elements are being removed or reactivated. This argument is valid only when *isRestart*=False. The default value is OFF.

- *includeStrain*

  A Boolean specifying whether stress/displacement elements are reactivated with strain. This argument is valid only when *isRestart*=False and when *activeInStep*=True. The default value is OFF.

### Return value

None.

### Exceptions

None.



## Members

The ModelChange object has members with the same names and descriptions as the arguments to the [ModelChange ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelchangepyc.htm?ContextScope=all#simaker-modelchangemodelchangepyc)method.



## Corresponding analysis keywords

- [MODEL CHANGE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-modelchange.htm?ContextScope=all#simakey-r-modelchange), TYPE=ELEMENT
- [MODEL CHANGE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-modelchange.htm?ContextScope=all#simakey-r-modelchange), ACTIVATE