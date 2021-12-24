# Moment object

The Moment object stores the data for a moment.

The Moment object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## Moment(...)



This method creates a Moment object.



### Path

```
mdb.models[name].Moment
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

### Optional arguments

- *cm1*

  A Float or a Complex specifying the load component in the 4-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least one of them must be nonzero.

- *cm2*

  A Float or a Complex specifying the load component in the 5- direction.

- *cm3*

  A Float or a Complex specifying the load component in the 6-direction.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *follower*

  A Boolean specifying whether the direction of the force rotates with the rotation of the node. You should provide the *follower* argument only if it is valid for the specified step. The default value is OFF.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the ID of the Datum coordinate system used as the local coordinate system of the load. If *localCsys*=None, the load is defined in the global coordinate system. When this member is queried, it returns an Int. The default value is None.

- *distributionType*

  A SymbolicConstant specifying how the load is distributed spatially. Possible values are UNIFORM and FIELD. The default value is UNIFORM.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

### Return value

A Moment object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing Moment object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Moment ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-momentpyc.htm?ContextScope=all#simaker-momentmomentpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing Moment object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *comp1*

  A Float, a Complex, or a SymbolicConstant specifying the load component in the 4-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the load component is propagated from the previous static analysis step. Use FREED to remove a previously defined load component.

- *comp2*

  A Float, a Complex, or a SymbolicConstant specifying the load component in the 5-direction. For details see *comp1*.

- *comp3*

  A Float, a Complex, or a SymbolicConstant specifying the load component in the 6-direction. For details see *comp1*.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous static analysis step. FREED should be used if the load is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The Moment object can have the following members:

- *name*

  A String specifying the load repository key.

- *distributionType*

  A SymbolicConstant specifying how the load is distributed spatially. Possible values are UNIFORM and FIELD. The default value is UNIFORM.

- *follower*

  A Boolean specifying whether the direction of the force rotates with the rotation of the node. You should provide the *follower* argument only if it is valid for the specified step. The default value is OFF.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the ID of the Datum coordinate system used as the local coordinate system of the load. If *localCsys*=None, the load is defined in the global coordinate system. When this member is queried, it returns an Int. The default value is None.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.