# SurfaceCurrentDensity object

The SurfaceCurrentDensity object stores the data for a surface current.

The SurfaceCurrentDensity object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## SurfaceCurrentDensity(...)



This method creates a SurfaceCurrentDensity object.



### Path

```
mdb.models[name].SurfaceCurrentDensity
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created. This must be the first analysis step name.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

- *comp1*

  A Complex specifying the first component of the load.

- *comp2*

  A Complex specifying the second component of the load.

- *comp3*

  A Complex specifying the third component of the load.

### Optional arguments

- *distributionType*

  A SymbolicConstant specifying how the load is distributed spatially. Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

A SurfaceCurrentDensity object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing SurfaceCurrentDensity object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SurfaceCurrentDensity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentdensitypyc.htm?ContextScope=all#simaker-surfacecurrentdensitysurfacecurrentdensitypyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing SurfaceCurrentDensity object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *comp1*

  A Complex specifying the first component of the load.

- *comp2*

  A Complex specifying the second component of the load.

- *comp3*

  A Complex specifying the third component of the load.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous static analysis step. FREED should be used if the load is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The SurfaceCurrentDensity object can have the following members:

- *name*

  A String specifying the load repository key.

- *distributionType*

  A SymbolicConstant specifying how the load is distributed spatially. Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.