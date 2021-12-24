# AccelerationBaseMotionBC object

The AccelerationBaseMotionBC object stores the data for an acceleration base motion boundary condition.

The AccelerationBaseMotionBC object is derived from the [BoundaryCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].boundaryConditions[name]
```

## AccelerationBaseMotionBC(...)



This method creates a AccelerationBaseMotionBC object.



### Path

```
mdb.models[name].AccelerationBaseMotionBC
```

### Required arguments

- *name*

  A String specifying the boundary condition repository key.

- *createStepName*

  A String specifying the name of the step in which the boundary condition is created.

- *dof*

  A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1.

### Optional arguments

- *amplitudeScaleFactor*

  A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

- *centerOfRotation*

  A [ModelDot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying a tuple containing one center of rotation. The default value is the global origin. This argument applies only when *dof*=UR1, UR2, or UR3.

- *correlation*

  A [CorrelationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-correlationpyc.htm?ContextScope=all) object.

- *secondaryBase*

  A String specifying the name of the [SecondaryBaseBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-secondarybasebcpyc.htm?ContextScope=all) object associated with this boundary condition. The default value is an empty string.

- *useComplex*

  A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base motion record given by amplitude definition. The default value is OFF.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

An AccelerationBaseMotionBC object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing AccelerationBaseMotionBC object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AccelerationBaseMotionBC ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbasemotionbcpyc.htm?ContextScope=all#simaker-accelerationbasemotionbcaccelerationbasemotionbcpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing AccelerationBaseMotionBC object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the boundary condition is modified.

### Optional arguments

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the boundary condition is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The AccelerationBaseMotionBC object can have the following members:

- *name*

  A String specifying the boundary condition repository key.

- *amplitudeScaleFactor*

  A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

- *useComplex*

  A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base motion record given by amplitude definition. The default value is OFF.

- *centerOfRotation*

  A [ModelDot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying a tuple containing one center of rotation. The default value is the global origin. This argument applies only when *dof*=UR1, UR2, or UR3.

- *correlation*

  A [CorrelationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-correlationpyc.htm?ContextScope=all) object.

- *secondaryBase*

  A String specifying the name of the [SecondaryBaseBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-secondarybasebcpyc.htm?ContextScope=all) object associated with this boundary condition. The default value is an empty string.

- *category*

  A SymbolicConstant specifying the category of the boundary condition. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the boundary condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.