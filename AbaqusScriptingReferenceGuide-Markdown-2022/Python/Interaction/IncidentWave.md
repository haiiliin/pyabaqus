# IncidentWave object

The IncidentWave object defines incident wave interactions for acoustic and coupled acoustic-structural analyses.

The IncidentWave object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## IncidentWave(...)



This method creates an IncidentWave object.



### Path

```
mdb.models[name].IncidentWave
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the IncidentWave object is created.

- *sourcePoint*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the incident wave source point.

- *standoffPoint*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the incident wave standoff point.This argument is not valid when *definition*=CONWEP.

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surface defining the incident wave interaction. In problems involving fluid/surface boundaries, both the fluid surface and the solid surface comprising the boundary must have an incident wave interaction specified.

- *interactionProperty*

  A String specifying the [IncidentWaveProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepropertypyc.htm?ContextScope=all) object associated with this interaction.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the type of incident wave to be defined. The value must be PRESSURE for linear perturbation steps. An Explicit step is required when the value is set to CONWEP. Possible values are PRESSURE, ACCELERATION, UNDEX, and CONWEP. The default value is PRESSURE.

- *amplitude*

  A String specifying the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that defines the fluid pressure time history at the standoff point, if *definition*=PRESSURE. If *definition*=ACCELERATION, then this string specifies the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that defines the fluid particle acceleration time history at the standoff point. This member can be specified only if *definition*=PRESSURE or ACCELERATION. The default value is an empty string.

- *imaginaryAmplitude*

  A String specifying the name of the [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) object that defines the imaginary component of the fluid pressure time history at the standoff point. This member is applicable only for linear perturbation steps and if *definition*=PRESSURE. The default value is an empty string.

- *surfaceNormal*

  A sequence of three Floats specifying the X, Y, and Z components of the direction cosine of the fluid surface normal.This argument is valid only when *definition*=UNDEX.

- *initialDepth*

  None or a Float specifying the initial depth of the UNDEX bubble. The default value is None.This argument is valid only when *definition*=UNDEX.

- *referenceMagnitude*

  A Float specifying the reference magnitude.This argument is not valid when *definition*=CONWEP.

- *detonationTime*

  A Float specifying the time of detonation, given in total time.This argument is valid only when *definition*=CONWEP.

- *magnitudeFactor*

  A Float specifying the magnitude scale factor. The default value is 1.0.This argument is valid only when *definition*=CONWEP.

### Return value

An IncidentWave object.

### Exceptions

None.



## setValues(...)



This method modifies the IncidentWave object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [IncidentWave ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepyc.htm?ContextScope=all#simaker-incidentwaveincidentwavepyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## Members

The IncidentWave object has members with the same names and descriptions as the arguments to the [IncidentWave ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepyc.htm?ContextScope=all#simaker-incidentwaveincidentwavepyc)method.



## Corresponding analysis keywords

- [INCIDENT WAVE INTERACTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-incidentwaveinteraction.htm?ContextScope=all#simakey-r-incidentwaveinteraction)