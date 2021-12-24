# BodyConcentrationFlux object

The BodyConcentrationFlux object defines body concentration flux from a region or into a region.

The BodyConcentrationFlux object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## BodyConcentrationFlux(...)



This method creates a BodyConcentrationFlux object.



### Path

```
mdb.models[name].BodyConcentrationFlux
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

- *magnitude*

  A Float specifying the body concentration flux magnitude. *magnitude* is optional if *distributionType*=USER_DEFINED.

### Optional arguments

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *distributionType*

  A SymbolicConstant specifying how the body concentration flux is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

A BodyConcentrationFlux object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing BodyConcentrationFlux object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BodyConcentrationFlux ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyconcentrationfluxpyc.htm?ContextScope=all#simaker-bodyconcentrationfluxbodyconcentrationfluxpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing BodyConcentrationFlux object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the Body heat flux is modified.

### Optional arguments

- *magnitude*

  A Float specifying the Body concentration flux magnitude.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the load has no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The BodyConcentrationFlux object can have the following members:

- *name*

  A String specifying the load repository key.

- *distributionType*

  A SymbolicConstant specifying how the body concentration flux is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this load. The *field* argument applies only when *distributionType*=FIELD. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.