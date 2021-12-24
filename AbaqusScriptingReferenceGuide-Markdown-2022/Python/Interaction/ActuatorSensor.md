# ActuatorSensor object

The ActuatorSensor object defines a single point actuator where the actuation is determined by a user subroutine ([UEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-uel.htm?ContextScope=all#simasub-c-uel)). The subroutine senses the data at the same point as the actuator.

The ActuatorSensor object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## ActuatorSensor(...)



This method creates an ActuatorSensor object.



### Path

```
mdb.models[name].ActuatorSensor
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the actuator/sensor interaction is created. *createStepName* must be set to 'Initial'.

- *point*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the point at which the constraint is applied.

- *interactionProperty*

  A String specifying the [ActuatorSensorProp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatorsensorproppyc.htm?ContextScope=all) object associated with this interaction.

- *noCoordComponents*

  An Int specifying the number of coordinate components supplied to the user subroutine ([UEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-uel.htm?ContextScope=all#simasub-c-uel)).

- *unsymm*

  A Boolean specifying whether the element matrices are symmetric (ON) or unsymmetric (OFF). The default value is OFF.

- *noSolutionDepVar*

  An Int specifying the number of solution-dependent variables. The default value is 0.

- *userSubUel*

  A String specifying the name of the user subroutine ([UEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-uel.htm?ContextScope=all#simasub-c-uel)) that defines the user element.

- *dof*

  A String specifying the degrees of freedom, separated by commas.

- *solutionDepVars*

  A sequence of Floats specifying the initial values of the solution-dependent variables.

### Optional arguments

None.

### Return value

An ActuatorSensor object.

### Exceptions

None.



## setValues(...)



This method modifies the ActuatorSensor object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ActuatorSensor ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatorsensorpyc.htm?ContextScope=all#simaker-actuatorsensoractuatorsensorpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## Members

The ActuatorSensor object has members with the same names and descriptions as the arguments to the [ActuatorSensor ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatorsensorpyc.htm?ContextScope=all#simaker-actuatorsensoractuatorsensorpyc)method.



## Corresponding analysis keywords

- [ELEMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-element.htm?ContextScope=all#simakey-r-element)
- [USER ELEMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-userelement.htm?ContextScope=all#simakey-r-userelement)
- [INITIAL CONDITIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-initialconditions.htm?ContextScope=all#simakey-r-initialconditions), TYPE=SOLUTION