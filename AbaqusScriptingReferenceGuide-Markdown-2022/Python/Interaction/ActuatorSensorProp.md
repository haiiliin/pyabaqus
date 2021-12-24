# ActuatorSensorProp object

The ActuatorSensorProp object is an interaction property that defines the properties referred to by an [ActuatorSensor](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatorsensorpyc.htm?ContextScope=all) object.

The ActuatorSensorProp object is derived from the [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactionProperties[name]
```

## ActuatorSensorProp(...)



This method creates an ActuatorSensorProp object.



### Path

```
mdb.models[name].ActuatorSensorProp
```

### Required arguments

- *name*

  A String specifying the interaction property repository key.

### Optional arguments

- *realProperties*

  A sequence of Floats specifying the PROPS array used by user subroutine [UEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-uel.htm?ContextScope=all#simasub-c-uel). The default value is an empty sequence.

- *integerProperties*

  A sequence of Ints specifying the JPROPS array used by user subroutine [UEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-uel.htm?ContextScope=all#simasub-c-uel). The default value is an empty sequence.

### Return value

An ActuatorSensorProp object.

### Exceptions

None.



## setValues(...)



This method modifies the ActuatorSensorProp object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ActuatorSensorProp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatorsensorproppyc.htm?ContextScope=all#simaker-actuatorsensorpropactuatorsensorproppyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The ActuatorSensorProp object has members with the same names and descriptions as the arguments to the [ActuatorSensorProp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatorsensorproppyc.htm?ContextScope=all#simaker-actuatorsensorpropactuatorsensorproppyc)method.



## Corresponding analysis keywords

- [UEL PROPERTY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-uelproperty.htm?ContextScope=all#simakey-r-uelproperty)