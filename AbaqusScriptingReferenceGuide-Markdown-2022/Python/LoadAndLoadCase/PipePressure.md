# PipePressure object

The PipePressure object stores the data for a pressure applied to pipe or elbow elements.

The PipePressure object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## PipePressure(...)



This method creates a [Pressure](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepyc.htm?ContextScope=all) object.



### Path

```
mdb.models[name].PipePressure
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the pressure is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

- *magnitude*

  A Float specifying the pressure magnitude.Note:*magnitude* is optional if *distributionType*=USER_DEFINED.

- *diameter*

  A Float specifying the effective inner or outer diameter.

- *hZero*

  A Float specifying the height of the zero pressure level when *distributionType*=HYDROSTATIC.

- *hReference*

  A Float specifying the height of the reference pressure level when *distributionType*=HYDROSTATIC.

### Optional arguments

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *distributionType*

  A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM, HYDROSTATIC, USER_DEFINED, and FIELD. The default value is UNIFORM.

- *side*

  A SymbolicConstant specifying whether the pressure is applied internally or externally. Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.

### Return value

A PipePressure object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing PipePressure object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PipePressure ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pipepressurepyc.htm?ContextScope=all#simaker-pipepressurepipepressurepyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing PipePressure object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *magnitude*

  A Float specifying the pressure magnitude.

- *hZero*

  A Float specifying the height of the zero pressure level when *distributionType*=HYDROSTATIC.

- *hReference*

  A Float specifying the height of the reference pressure level when *distributionType*=HYDROSTATIC.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous static analysis step. FREED should be used if the load has no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The PipePressure object can have the following members:

- *name*

  A String specifying the load repository key.

- *distributionType*

  A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM, HYDROSTATIC, USER_DEFINED, and FIELD. The default value is UNIFORM.

- *side*

  A SymbolicConstant specifying whether the pressure is applied internally or externally. Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.

- *diameter*

  A Float specifying the effective inner or outer diameter.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.