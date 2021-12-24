# BoltLoad object

The BoltLoad object defines a bolt load.

The BoltLoad object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## BoltLoad(...)



This method creates a BoltLoad object.



### Path

```
mdb.models[name].BoltLoad
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created. This must be the first analysis step name.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

- *magnitude*

  A Float specifying the bolt load magnitude.

### Optional arguments

- *boltMethod*

  A SymbolicConstant specifying the method of applying the bolt load. Possible values are APPLY_FORCE and ADJUST_LENGTH. The default value is APPLY_FORCE.

- *datumAxis*

  A [DatumAxis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the orientation of the pre-tension section normal.Note: *datumAxis* is applicable only for Solid and Shell regions; it has no meaning for Wire regions.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *preTenSecPartLevel*

  A Boolean specifying whether the pre-tension section is to be defined at the part level. The default value is False. You should provide the *preTenSecPartLevel* argument only if the selected region belongs to a dependent part instance. A pre-tension section cannot be defined at the part level for independent and model instances.

### Return value

A BoltLoad object.

### Exceptions

TextError.



## setValues(...)



This method modifies the data for an existing BoltLoad object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BoltLoad ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boltloadpyc.htm?ContextScope=all#simaker-boltloadboltloadpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing BoltLoad object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *boltMethod*

  A SymbolicConstant specifying the type of bolt load. Possible values are APPLY_FORCE, ADJUST_LENGTH, and FIX_LENGTH. The default is APPLY_FORCE.

- *magnitude*

  A Float specifying the bolt load magnitude.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the load is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The BoltLoad object can have the following members:

- *name*

  A String specifying the load repository key.

- *datumAxis*

  A [DatumAxis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the orientation of the pre-tension section normal.Note:*datumAxis* is required only for Solid and Shell regions; it has no meaning for Wire regions.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.



## Corresponding analysis keywords

- [PRE-TENSION SECTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-pre-tensionsection.htm?ContextScope=all#simakey-r-pre-tensionsection)
- [NODE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-node.htm?ContextScope=all#simakey-r-node) (for the reference node)
- [NSET](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-nset.htm?ContextScope=all#simakey-r-nset) (for the reference node)