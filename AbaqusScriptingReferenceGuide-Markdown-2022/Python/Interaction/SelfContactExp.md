# SelfContactExp object

The SelfContactExp object defines self-contact during an Abaqus/Explicit analysis.

The SelfContactExp object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## SelfContactExp(...)



This method creates a SelfContactExp object.



### Path

```
mdb.models[name].SelfContactExp
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the SelfContactExp object is created.

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surface where self-contact is defined.

- *interactionProperty*

  A String specifying the name of the [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object associated with this interaction.

### Optional arguments

- *mechanicalConstraint*

  A SymbolicConstant specifying the mechanical constraint formulation. Possible values are KINEMATIC and PENALTY. The default value is KINEMATIC.

- *contactControls*

  A String specifying the name of the [ContactControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactcontrolpyc.htm?ContextScope=all) object associated with this interaction. An empty string indicates that the default contact controls will be used. The default value is an empty string.

### Return value

A SelfContactExp object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing SelfContactExp object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SelfContactExp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-selfcontactexppyc.htm?ContextScope=all#simaker-selfcontactexpselfcontactexppyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing SelfContactExp object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *interactionProperty*

  A String specifying the name of the [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object associated with this interaction.

- *contactControls*

  A String specifying the name of the [ContactControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactcontrolpyc.htm?ContextScope=all) object associated with this interaction. An empty string indicates that the default contact controls will be used. The default value is an empty string.

### Return value

None.

### Exceptions

None.



## Members

The SelfContactExp object has members with the same names and descriptions as the arguments to the [SelfContactExp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-selfcontactexppyc.htm?ContextScope=all#simaker-selfcontactexpselfcontactexppyc)method except the optional arguments to the [setValuesInStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-selfcontactexppyc.htm?ContextScope=all#simaker-selfcontactexpsetvaluesinsteppyc)method.