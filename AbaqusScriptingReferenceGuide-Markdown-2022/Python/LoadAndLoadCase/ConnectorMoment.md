# ConnectorMoment object

The ConnectorMoment object stores the data for a connector moment.

The ConnectorMoment object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## ConnectorMoment(...)



This method creates a ConnectorMoment object on a wire region. Alternatively, the load may also be applied to a wire set referenced from an assembled fastener template model.



### Path

```
mdb.models[name].ConnectorMoment
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created.

### Optional arguments

- *region*

  The wire region to which the load is applied. This argument is not valid when *fastenerName* and *fastenerSetName* are specified.

- *fastenerName*

  A String specifying the name of the assembled fastener to which the load will be applied. This argument is not valid when *region* is specified. When this argument is specified, *fastenerSetName* must also be specified. The default value is an empty string.

- *fastenerSetName*

  A String specifying the assembled fastener template model set to which the load will be applied. This argument is not valid when *region* is specified. When this argument is specified, *fastenerName* must also be specified. The default value is an empty string.

- *m1*

  A Float or a Complex specifying the moment component in the connector's local 4-direction.

- *m2*

  A Float or a Complex specifying the moment component in the connector's local 5-direction.

- *m3*

  A Float or a Complex specifying the moment component in the connector's local 6-direction.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

A ConnectorMoment object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing ConnectorMoment object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorMoment ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectormomentpyc.htm?ContextScope=all#simaker-connectormomentconnectormomentpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing ConnectorMoment object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *m1*

  A Float, a Complex, or a SymbolicConstant specifying the moment component in the connector's local 4-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the load component is propagated from the previous static analysis step. Use FREED to remove a previously defined load component.

- *m2*

  A Float, a Complex, or a SymbolicConstant specifying the moment component in the connector's local 5-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the load component is propagated from the previous static analysis step. Use FREED to remove a previously defined load component.

- *m3*

  A Float, a Complex, or a SymbolicConstant specifying the moment component in the connector's local 6-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the load component is propagated from the previous static analysis step. Use FREED to remove a previously defined load component.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous static analysis step. FREED should be used if the load is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The ConnectorMoment object can have the following members:

- *name*

  A String specifying the load repository key.

- *fastenerName*

  A String specifying the name of the assembled fastener to which the load will be applied. This argument is not valid when *region* is specified. When this argument is specified, *fastenerSetName* must also be specified. The default value is an empty string.

- *fastenerSetName*

  A String specifying the assembled fastener template model set to which the load will be applied. This argument is not valid when *region* is specified. When this argument is specified, *fastenerName* must also be specified. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.