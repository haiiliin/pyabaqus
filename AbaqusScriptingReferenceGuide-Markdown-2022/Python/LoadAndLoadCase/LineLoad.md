# LineLoad object

The LineLoad object stores the data of an applied line load.

The LineLoad object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## LineLoad(...)



This method creates a LineLoad object.



### Path

```
mdb.models[name].LineLoad
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

### Optional arguments

- *distributionType*

  A SymbolicConstant specifying how the load is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *comp1*

  A Float or a Complex specifying the component of the load in the global or the beam local 1-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least one of them must be nonzero unless *distributionType*=USER_DEFINED.

- *comp2*

  A Float or a Complex specifying the component of the load in the global or the beam local 2-direction.

- *comp3*

  A Float or a Complex specifying the component of the load in the global 3-direction.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *system*

  A SymbolicConstant specifying whether the load is applied in a global or the beam local frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.

### Return value

A LineLoad object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing LineLoad object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [LineLoad ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lineloadpyc.htm?ContextScope=all#simaker-lineloadlineloadpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing LineLoad object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *comp1*

  A Float, a Complex, or a SymbolicConstant specifying the load component in the global or the beam local 1-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the load component is propagated from the previous static analysis step. Use FREED to remove a previously defined load component.

- *comp2*

  A Float, a Complex, or a SymbolicConstant specifying the load component in the global or the beam local 2-direction. For details see *comp1*.

- *comp3*

  A Float, a Complex, or a SymbolicConstant specifying the load component in the global 3-direction. For details see *comp1*.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous static analysis step. FREED should be used if the load is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The LineLoad object can have the following members:

- *name*

  A String specifying the load repository key.

- *distributionType*

  A SymbolicConstant specifying how the load is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

- *system*

  A SymbolicConstant specifying whether the load is applied in a global or the beam local frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.