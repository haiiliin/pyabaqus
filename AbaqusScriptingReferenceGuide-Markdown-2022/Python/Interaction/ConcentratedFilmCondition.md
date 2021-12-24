# ConcentratedFilmCondition object

The ConcentratedFilmCondition object defines concentrated film coefficients and associated sink temperatures.

The ConcentratedFilmCondition object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## ConcentratedFilmCondition(...)



This method creates a ConcentratedFilmCondition object.



### Path

```
mdb.models[name].ConcentratedFilmCondition
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the ConcentratedFilmCondition object is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the concentrated film condition interaction is applied. The interaction is applied to each node in the region.

- *definition*

  A SymbolicConstant specifying how the concentrated film condition is defined. Possible values are EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD.

### Optional arguments

- *nodalArea*

  A Float specifying the area associated with the node where the concentrated film condition is applied. The default value is 1.0.

- *explicitRegionType*

  A SymbolicConstant specifying how the concentrated film condition is applied to the boundary of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and EULERIAN. The default value is LAGRANGIAN. This argument applies only during an Abaqus/Explicit analysis.

- *interactionProperty*

  A String specifying the name of the [FilmConditionProp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionproppyc.htm?ContextScope=all) object associated with this interaction. The *interactionProperty* argument applies only when *definition*=PROPERTY_REF. The default value is an empty string.

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this interaction. The *field* argument applies only when *definition*=FIELD. The default value is an empty string.

- *sinkTemperature*

  A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0.

- *sinkAmplitude*

  A String specifying the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that gives the variation of the sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use None in an Abaqus/Standard analysis to specify that the reference sink temperature is applied immediately at the beginning of the step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that the reference sink temperature is applied throughout the step.

- *filmCoeff*

  A Float specifying the reference film coefficient value, hh. The *filmCoeff* argument applies when *definition*=EMBEDDED_COEFF, *definition*=USER_SUB, or *definition*=FIELD. The default value is 0.0.

- *filmCoeffAmplitude*

  A String specifying the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that gives the variation of the film coefficient, hh, with time. The default value is an empty string.Note:Use None in an Abaqus/Standard analysis to specify that the reference film coefficient is applied immediately at the beginning of the step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that the reference film coefficient is applied throughout the step.

- *sinkFieldName*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object associated with the sink temperature. The *sinkFieldName* argument applies only when *sinkDistributionType*=ANALYTICAL_FIELD or *sinkDistributionType*=DISCRETE_FIELD. The default value is an empty string.

- *sinkDistributionType*

  A SymbolicConstant specifying how the sink temperature is distributed. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

### Return value

A ConcentratedFilmCondition object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing ConcentratedFilmCondition object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConcentratedFilmCondition ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedfilmconditionpyc.htm?ContextScope=all#simaker-concentratedfilmconditionconcentratedfilmconditionpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data of an existing ConcentratedFilmCondition object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

The optional arguments to setValuesInStep are the same as the optional arguments to the ConcentratedFilmConditionState method.

### Return value

None.

### Exceptions

None.



## Members

The ConcentratedFilmCondition object has members with the same names and descriptions as the arguments to the [ConcentratedFilmCondition ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedfilmconditionpyc.htm?ContextScope=all#simaker-concentratedfilmconditionconcentratedfilmconditionpyc)method except the optional arguments to the [setValuesInStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedfilmconditionpyc.htm?ContextScope=all#simaker-concentratedfilmconditionsetvaluesinsteppyc) method.