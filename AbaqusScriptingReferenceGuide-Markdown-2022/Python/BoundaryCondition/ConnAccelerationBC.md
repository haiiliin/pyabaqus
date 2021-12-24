# ConnAccelerationBC object

The ConnAccelerationBC object stores the data for a connector acceleration boundary condition.

The ConnAccelerationBC object is derived from the [BoundaryCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].boundaryConditions[name]
```

## ConnAccelerationBC(...)



This method creates an ConnAccelerationBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.



### Path

```
mdb.models[name].ConnAccelerationBC
```

### Required arguments

- *name*

  A String specifying the boundary condition repository key.

- *createStepName*

  A String specifying the name of the step in which the boundary condition is created.

### Optional arguments

- *region*

  The wire region to which the boundary condition is applied. This argument is not valid when *fastenerName* and *fastenerSetName* are specified.

- *fastenerName*

  A String specifying the name of the assembled fastener to which the boundary condition will be applied. This argument is not valid when *region* is specified. When this argument is specified, *fastenerSetName* must also be specified. The default value is an empty string.

- *fastenerSetName*

  A String specifying the assembled fastener template model set to which the boundary condition will be applied. This argument is not valid when *region* is specified. When this argument is specified, *fastenerName* must also be specified. The default value is an empty string.

- *a1*

  A Float or a SymbolicConstant specifying the acceleration component in the connector's local 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.Note:Although *a1*, *a2*, *a3*, *ar1*, *ar2*, and *ar3* are optional arguments, at least one of them must be specified.

- *a2*

  A Float or a SymbolicConstant specifying the acceleration component in the connector's local 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *a3*

  A Float or a SymbolicConstant specifying the acceleration component in the connector's local 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *ar1*

  A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *ar2*

  A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *ar3*

  A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *distributionType*

  A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

### Return value

A ConnAccelerationBC object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing ConnAccelerationBC object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnAccelerationBC ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connaccelerationbcpyc.htm?ContextScope=all#simaker-connaccelerationbcconnaccelerationbcpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing ConnAccelerationBC object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the boundary condition is modified.

### Optional arguments

- *a1*

  A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *a2*

  A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *a3*

  A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *ar1*

  A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 4-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *ar2*

  A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 5-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *ar3*

  A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 6-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the boundary condition is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The ConnAccelerationBC object can have the following members:

- *name*

  A String specifying the boundary condition repository key.

- *distributionType*

  A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

- *fastenerName*

  A String specifying the name of the assembled fastener to which the boundary condition will be applied. This argument is not valid when *region* is specified. When this argument is specified, *fastenerSetName* must also be specified. The default value is an empty string.

- *fastenerSetName*

  A String specifying the assembled fastener template model set to which the boundary condition will be applied. This argument is not valid when *region* is specified. When this argument is specified, *fastenerName* must also be specified. The default value is an empty string.

- *category*

  A SymbolicConstant specifying the category of the boundary condition. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the boundary condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.