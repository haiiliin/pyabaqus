# Velocity object

The Velocity object stores the data for an initial velocity predefined field.

The Velocity object is derived from the [PredefinedField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].predefinedFields[name]
```

## Velocity(...)



This method creates a Velocity predefined field object.



### Path

```
mdb.models[name].Velocity
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the predefined field is applied.

- *velocity1*

  A Float specifying the first component of the velocity.

- *velocity2*

  A Float specifying the second component of the velocity.

- *velocity3*

  A Float specifying the third component of the velocity.

- *omega*

  A Float specifying the angular velocity.

- *axisBegin*

  A sequence of Floats specifying the *X-*, *Y-*, and *Z*- coordinates of the starting point of the axis about which *omega* is defined.

- *axisEnd*

  A sequence of Floats specifying the *X-*, *Y-*, and *Z*- coordinates of the end point of the axis about which *omega* is defined.

### Optional arguments

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this predefined field. The *field* argument applies only when *distributionType*=FIELD_ANALYTICAL. The default value is an empty string.

- *distributionType*

  A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE and FIELD_ANALYTICAL. The default value is MAGNITUDE.

### Return value

A Velocity object.

### Exceptions

None.



## setValues(...)



This method modifies the Velocity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Velocity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitypyc.htm?ContextScope=all#simaker-velocityvelocitypyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The Velocity object has members with the same names and descriptions as the arguments to the [Velocity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitypyc.htm?ContextScope=all#simaker-velocityvelocitypyc)method.



## Corresponding analysis keywords

- [INITIAL CONDITIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-initialconditions.htm?ContextScope=all#simakey-r-initialconditions), TYPE=VELOCITY
- [INITIAL CONDITIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-initialconditions.htm?ContextScope=all#simakey-r-initialconditions), TYPE=ROTATING VELOCITY