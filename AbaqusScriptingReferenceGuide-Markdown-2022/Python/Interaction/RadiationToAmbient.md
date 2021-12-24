# RadiationToAmbient object

The RadiationToAmbient object defines radiant heat transfer between a surface and its environment.

The RadiationToAmbient object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## RadiationToAmbient(...)



This method creates a RadiationToAmbient object.



### Path

```
mdb.models[name].RadiationToAmbient
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the RadiationToAmbient object is created.

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surface to which the radiation interaction is applied.

- *emissivity*

  A Float specifying the emissivity, ϵϵ.

### Optional arguments

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this interaction. The *field* argument applies only when *distributionType*=ANALYTICAL_FIELD. The default value is an empty string.

- *distributionType*

  A SymbolicConstant specifying how the radiation is distributed. This argument applies only when *radiationType*=AMBIENT. Possible values are UNIFORM and ANALYTICAL_FIELD. The default value is UNIFORM.

- *radiationType*

  A SymbolicConstant specifying whether to use the default surface radiation behavior, or the cavity radiation approximation. Possible values are AMBIENT and CAVITY. The default value is AMBIENT.

- *ambientTemperature*

  A Float specifying the reference ambient temperature, θ0θ0. This argument applies only when *radiationType*=AMBIENT. The default value is 0.0.

- *ambientTemperatureAmp*

  A String specifying the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that gives the variation of the ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify that the reference ambient temperature is applied immediately at the beginning of the step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that the reference ambient temperature is applied throughout the step. This argument applies only when *radiationType*=AMBIENT.

### Return value

A RadiationToAmbient object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing RadiationToAmbient object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [RadiationToAmbient ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationtoambientpyc.htm?ContextScope=all#simaker-radiationtoambientradiationtoambientpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data of an existing RadiationToAmbient object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

The optional arguments to setValuesInStep are *emissivity*, *ambientTemperature*, and *ambientTemperatureAmp* arguments.

### Return value

None.

### Exceptions

None.



## Members

The RadiationToAmbient object has members with the same names and descriptions as the arguments to the [RadiationToAmbient ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationtoambientpyc.htm?ContextScope=all#simaker-radiationtoambientradiationtoambientpyc)method except the optional arguments to the [setValuesInStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationtoambientpyc.htm?ContextScope=all#simaker-radiationtoambientsetvaluesinsteppyc) method.