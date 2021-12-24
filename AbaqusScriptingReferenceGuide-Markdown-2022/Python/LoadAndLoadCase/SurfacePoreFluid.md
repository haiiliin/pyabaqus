# SurfacePoreFluid object

The SurfacePoreFluid object defines surface pore fluid flow from a region or into a region.

The SurfacePoreFluid object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## SurfacePoreFluid(...)



This method creates a SurfacePoreFluid object.



### Path

```
mdb.models[name].SurfacePoreFluid
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

- *magnitude*

  A Float specifying the surface pore fluid flow magnitude. *magnitude* is optional if *distributionType*=USER_DEFINED.

### Optional arguments

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *distributionType*

  A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

A SurfacePoreFluid object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing SurfacePoreFluid object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SurfacePoreFluid ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceporefluidpyc.htm?ContextScope=all#simaker-surfaceporefluidsurfaceporefluidpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing SurfacePoreFluid object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the surface pore fluid flow is modified.

### Optional arguments

- *magnitude*

  A Float specifying the surface pore fluid flow magnitude.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the load has no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The SurfacePoreFluid object can have the following members:

- *name*

  A String specifying the load repository key.

- *distributionType*

  A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.