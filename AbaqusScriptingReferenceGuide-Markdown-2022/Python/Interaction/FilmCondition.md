# FilmCondition object

The FilmCondition object defines film coefficients and associated sink temperatures for coupled temperature-displacement analyses.

The FilmCondition object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## FilmCondition(...)



This method creates a FilmCondition object.



### Path

```
mdb.models[name].FilmCondition
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the FilmCondition object is created.

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the name of the surface to which the film condition interaction is applied.

- *definition*

  A SymbolicConstant specifying how the film condition is defined. Possible values are EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD.

### Optional arguments

- *interactionProperty*

  A String specifying the name of the [FilmConditionProp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionproppyc.htm?ContextScope=all) object associated with this interaction. The *interactionProperty* argument applies only when *definition*=PROPERTY_REF. The default value is an empty string.

- *sinkTemperature*

  A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.

- *sinkAmplitude*

  A String specifying the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that gives the variation of the sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use empty string in an Abaqus/Standard analysis to specify that the reference sink temperature is applied immediately at the beginning of the step or linearly over the step. Use empty string in an Abaqus/Explicit analysis to specify that the reference sink temperature is applied throughout the step.

- *filmCoeff*

  A Float specifying the reference film coefficient value, hh. The *filmCoeff* argument applies when *definition*=EMBEDDED_COEFF, *definition*=USER_SUB, or *definition*=FIELD. The default value is 0.0.

- *filmCoeffAmplitude*

  A String specifying the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that gives the variation of the film coefficient, hh, with time. The default value is an empty string. Note: Use empty string in an Abaqus/Standard analysis to specify that the reference film coefficient is applied immediately at the beginning of the step or linearly over the step. Use empty string in an Abaqus/Explicit analysis to specify that the reference film coefficient is applied throughout the step.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this interaction. The *field* argument applies only when *definition*=FIELD. The default value is an empty string.

- *sinkFieldName*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object associated with the sink temperature. The *sinkFieldName* argument applies only when *sinkDistributionType*=ANALYTICAL_FIELD or *sinkDistributionType*=DISCRETE_FIELD. The default value is an empty string.

- *sinkDistributionType*

  A SymbolicConstant specifying how the sink temperature is distributed. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

### Return value

A FilmCondition object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing FilmCondition object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FilmCondition ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionpyc.htm?ContextScope=all#simaker-filmconditionfilmconditionpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data of an existing FilmCondition object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

The optional arguments to setValuesInStep are the same as the optional arguments to the FilmConditionState method.

### Return value

None.

### Exceptions

None.



## Members

The FilmCondition object has members with the same names and descriptions as the arguments to the [FilmCondition ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionpyc.htm?ContextScope=all#simaker-filmconditionfilmconditionpyc)method except the optional arguments to the [setValuesInStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionpyc.htm?ContextScope=all#simaker-filmconditionsetvaluesinsteppyc) method.