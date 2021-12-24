# VelocityAdaptiveMeshConstraint object

The VelocityAdaptiveMeshConstraint object stores the data for an Arbitrary Lagrangian Eularian (ALE) style velocity adaptive mesh constraint.

The VelocityAdaptiveMeshConstraint object is derived from the [AdaptiveMeshConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshconstraintpyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].adaptiveMeshConstraints[name]
```

## VelocityAdaptiveMeshConstraint(...)



This method creates a VelocityAdaptiveMeshConstraint object.



### Path

```
mdb.models[name].VelocityAdaptiveMeshConstraint
```

### Required arguments

- *name*

  A String specifying the adaptive mesh constraint repository key.

- *createStepName*

  A String specifying the name of the step in which the adaptive mesh constraint is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the adaptive mesh constraint is applied.

### Optional arguments

- *v1*

  A Float or a SymbolicConstant specifying the velocity component in the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.Note:Although *v1*, *v2*, *v3*, *vr1*, *vr2*, and *vr3* are optional arguments, at least one of them must be specified.

- *v2*

  A Float or a SymbolicConstant specifying the velocity component in the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *v3*

  A Float or a SymbolicConstant specifying the velocity component in the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *vr1*

  A Float or a SymbolicConstant specifying the rotational velocity component about the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *vr2*

  A Float or a SymbolicConstant specifying the rotational velocity component about the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *vr3*

  A Float or a SymbolicConstant specifying the rotational velocity component about the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the adaptive mesh constraint has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the adaptive mesh constraint's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.

- *motionType*

  A SymbolicConstant specifying the mesh motion in relation to the underlying material. Possible values are INDEPENDENT, FOLLOW and USER_DEFINED. The default value is INDEPENDENT.

### Return value

A VelocityAdaptiveMeshConstraint object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing VelocityAdaptiveMeshConstraint object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [VelocityAdaptiveMeshConstraint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocityadaptivemeshconstraintpyc.htm?ContextScope=all#simaker-velocityadaptivemeshconstraintvelocityadaptivemeshcpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing VelocityAdaptiveMeshConstraint object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the adaptive mesh constraint is modified.

### Optional arguments

- *v1*

  A Float or a SymbolicConstant specifying the velocity component in the 1-direction. Possible values for the SymbolicConstant are SET and FREED.

- *v2*

  A Float or a SymbolicConstant specifying the velocity component in the 2-direction. Possible values for the SymbolicConstant are SET and FREED.

- *v3*

  A Float or a SymbolicConstant specifying the velocity component in the 3-direction. Possible values for the SymbolicConstant are SET and FREED.

- *vr1*

  A Float or a SymbolicConstant specifying the rotational velocity component about the 1-direction. Possible values for the SymbolicConstant are SET and FREED.

- *vr2*

  A Float or a SymbolicConstant specifying the rotational velocity component about the 2-direction. Possible values for the SymbolicConstant are SET and FREED.

- *vr3*

  A Float or a SymbolicConstant specifying the rotational velocity component about the 3-direction. Possible values for the SymbolicConstant are SET and FREED.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the adaptive mesh constraint is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The VelocityAdaptiveMeshConstraint object can have the following members:

- *name*

  A String specifying the adaptive mesh constraint repository key.

- *category*

  A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the adaptive mesh constraint is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the adaptive mesh constraint's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.