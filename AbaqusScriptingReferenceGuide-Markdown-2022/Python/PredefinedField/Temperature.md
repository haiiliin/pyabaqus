# Temperature object

The Temperature object stores the data for temperature predefined fields.

The Temperature object is derived from the [PredefinedField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].predefinedFields[name]
```

## Temperature(...)



This method creates a Temperature object.



### Path

```
mdb.models[name].Temperature
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the predefined field is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the predefined field is applied. *Region* is ignored if the predefined field has a *distributionType* member available, and *distributionType*=FROM_FILE .

### Optional arguments

- *distributionType*

  A SymbolicConstant specifying how the predefined field varies spatially. Possible values are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and DISCRETE_FIELD. The default value is UNIFORM.

- *crossSectionDistribution*

  A SymbolicConstant specifying how the predefined field is distributed over the cross section of the region. Possible values are

  - CONSTANT_THROUGH_THICKNESS
  - GRADIENTS_THROUGH_SHELL_CS
  - GRADIENTS_THROUGH_BEAM_CS
  - POINTS_THROUGH_SECTION

  The default value is CONSTANT_THROUGH_THICKNESS.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object associated with this predefined field. The *field* argument applies only when *distributionType*=FIELD or *distributionType*=DISCRETE_FIELD. The default value is an empty string.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the predefined field has no amplitude reference. The default value is UNSET.Note:*amplitude* should be given only if it is valid for the specified step.

- *fileName*

  A String specifying the name of the file from which the temperature values are to be read when *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED.

- *beginStep*

  An Int specifying the first step from which temperature values are to be read or the SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The default value is None.

- *beginIncrement*

  An Int specifying the first increment of the step set in *beginStep* or the SymbolicConstants STEP_START or STEP_END. This argument is valid only when *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The default value is None.

- *endStep*

  An Int specifying the last step from which temperature values are to be read or the SymbolicConstants FIRST_STEP and LAST_STEP. This argument is valid only when *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The default value is None.

- *endIncrement*

  An Int specifying the last increment of the step set in *endStep* or the SymbolicConstants STEP_START and STEP_END. This argument is valid only when *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The default value is None.

- *interpolate*

  A SymbolicConstant specifying whether to interpolate a field read from an output database or results file. Possible values are OFF, ON or MIDSIDE_ONLY. The default value is OFF.

- *magnitudes*

  A Sequence of Doubles specifying the temperature values when *distributionType*=UNIFORM or FIELD. The value of the *magnitudes* argument is a function of the *crossSectionDistribution* argument, as shown in the following list:

  - If *crossSectionDistribution*=CONSTANT_THROUGH_THICKNESS then *magnitudes* is a Double specifying the temperature.
  - If *crossSectionDistribution*=GRADIENTS_THROUGH_SHELL_CS then *magnitudes* is a sequence of Doubles specifying the mean value and the gradient in the thickness direction.
  - If *crossSectionDistribution*=GRADIENTS_THROUGH_BEAM_CS then *magnitudes* is a sequence of Doubles specifying the mean value, the gradient in the N1 direction, and the gradient in the N2 direction.
  - If *crossSectionDistribution*=POINTS_THROUGH_SECTION then *magnitudes* is a sequence of Doubles specifying the temperature at each point.

- *absoluteExteriorTolerance*

  A Float specifying the absolute value by which a driven node of the field can lie outside the region of the elements of the global model. The default value is 0.0. This argument cannot be used with *midside*.

- *exteriorTolerance*

  A Float specifying the fraction of the average element size in the global model by which a driven node of the field can lie outside the region of the elements of the global model. The default value is 0.0. This argument cannot be used with *midside*.

### Return value

A Temperature object.

### Exceptions

None.



## move(...)



This method moves the [TemperatureState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturestatepyc.htm?ContextScope=all) object from one step to a different step.



### Required arguments

- *fromStepName*

  A String specifying the name of the step from which the [PredefinedFieldState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldstatepyc.htm?ContextScope=all) is moved.

- *toStepName*

  A String specifying the name of the step to which the [PredefinedFieldState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldstatepyc.htm?ContextScope=all) is moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## setValues(...)



This method modifies the data for an existing Temperature object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Temperature ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturepyc.htm?ContextScope=all#simaker-temperaturetemperaturepyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing Temperature object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the predefined field is modified.

### Optional arguments

The optional arguments to setValuesInStep are the same as the optional arguments to the [Temperature ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturepyc.htm?ContextScope=all#simaker-temperaturetemperaturepyc)method, except for the *distributionType* and *crossSectionDistribution* arguments.

### Return value

None.

### Exceptions

None.



## Members

The Temperature object can have the following members:

- *name*

  A String specifying the repository key.

- *distributionType*

  A SymbolicConstant specifying how the predefined field varies spatially. Possible values are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and DISCRETE_FIELD. The default value is UNIFORM.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object associated with this predefined field. The *field* argument applies only when *distributionType*=FIELD or *distributionType*=DISCRETE_FIELD. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the predefined field is applied. *Region* is ignored if the predefined field has an *instances* member available. *Region* is also ignored if the predefined field has a *distributionType* member available, and *distributionType*=FROM_FILE or FROM_FILE_AND_USER_DEFINED.



## Corresponding analysis keywords

- [INITIAL CONDITIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-initialconditions.htm?ContextScope=all#simakey-r-initialconditions), TYPE=TEMPERATURE
- [TEMPERATURE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-temperature.htm?ContextScope=all#simakey-r-temperature)