# RotationalBodyForce object

The RotationalBodyForce object stores the data for a rotational body force.

The RotationalBodyForce object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## RotationalBodyForce(...)



This method creates a RotationalBodyForce object.



### Path

```
mdb.models[name].RotationalBodyForce
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created. This must be the first analysis step name.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

- *magnitude*

  A Float specifying the load magnitude.

- *point1*

  A sequence of Floats specifying the first point on the axis of rotation for the load.

- *point2*

  A sequence of Floats specifying the second point on the axis of rotation for the load.

### Optional arguments

- *distributionType*

  A SymbolicConstant specifying how the load is distributed spatially. Possible values are UNIFORM and FIELD. The default value is UNIFORM.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *centrifugal*

  A Boolean specifying whether or not the effect of the load is centrifugal. The default value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be specified and only one must have the value ON.

- *rotaryAcceleration*

  A Boolean specifying whether or not the effect of the load is rotary acceleration. The default value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be specified and only one must have the value ON.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

A RotationalBodyForce object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing RotationalBodyForce object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [RotationalBodyForce ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rotationalbodyforcepyc.htm?ContextScope=all#simaker-rotationalbodyforcerotationalbodyforcepyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing RotationalBodyForce object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *magnitude*

  A Float specifying the load magnitude.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous static analysis step. FREED should be used if the load is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The RotationalBodyForce object can have the following members:

- *name*

  A String specifying the load repository key.

- *distributionType*

  A SymbolicConstant specifying how the load is distributed spatially. Possible values are UNIFORM and FIELD. The default value is UNIFORM.

- *centrifugal*

  A Boolean specifying whether or not the effect of the load is centrifugal. The default value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be specified and only one must have the value ON.

- *rotaryAcceleration*

  A Boolean specifying whether or not the effect of the load is rotary acceleration. The default value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be specified and only one must have the value ON.

- *point1*

  A tuple of Floats specifying the first point on the axis of rotation for the load.

- *point2*

  A tuple of Floats specifying the second point on the axis of rotation for the load.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.