# IncidentWaveProperty object

The IncidentWaveProperty object is an interaction property that defines the properties referred to by an [IncidentWave](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepyc.htm?ContextScope=all) object.

The IncidentWaveProperty object is derived from the [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactionProperties[name]
```

## IncidentWaveProperty(...)



This method creates an IncidentWaveProperty object.



### Path

```
mdb.models[name].IncidentWaveProperty
```

### Required arguments

- *name*

  A String specifying the interaction property repository key.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the type of wave to be defined. Possible values are PLANAR, SPHERICAL, DIFFUSE, AIR_BLAST, and SURFACE_BLAST. The default value is PLANAR.

- *propagationModel*

  A SymbolicConstant specifying the spherical propagation model. Possible values are ACOUSTIC, UNDEX_CHARGE, and GENERALIZED_DECAY. The default value is ACOUSTIC.This argument is valid only when *definition*=SPHERICAL.

- *soundSpeed*

  A Float specifying the speed of sound in the fluid.This argument is not valid when *definition*=AIR_BLAST or when *definition*=SURFACE_BLAST.

- *fluidDensity*

  A Float specifying the fluid mass density.This argument is not valid when *definition*=AIR_BLAST or when *definition*=SURFACE_BLAST.

- *specificHeatRatio*

  None or a Float specifying the ratio of specific heats for gas. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *gravity*

  None or a Float specifying the acceleration due to gravity. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *atmosphericPressure*

  None or a Float specifying the atmospheric pressure. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *dragCoefficient*

  None or a Float specifying the fluid drag coefficient. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *dragExponent*

  A Float specifying the fluid drag exponent. The default value is 2.0.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *waveEffects*

  A Boolean specifying whether or not to include wave effects in the fluid and gas. The default value is ON.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *chargeDensity*

  None or a Float specifying the density of the charge material. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *chargeMass*

  None or a Float specifying the mass of the charge material. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *constantK1*

  None or a Float specifying the charge material constant K. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *constantK2*

  None or a Float specifying the charge material constant k. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *constantA*

  None or a Float specifying the charge material constant A. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *constantB*

  None or a Float specifying the charge material constant B. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *constantKc*

  None or a Float specifying the charge material constant Kc. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *duration*

  None or a Float specifying the time duration for the bubble simulation. The default value is None.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *maximumSteps*

  An Int specifying the maximum number of time steps for the bubble simulation. The default value is 1500.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *relativeStepControl*

  A Float specifying the relative step size control parameter. The default value is 1×10–11.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *absoluteStepControl*

  A Float specifying the absolute step size control parameter. The default value is 1×10–11.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *stepControlExponent*

  A Float specifying the step size control exponent. The default value is 0.2.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE.

- *genDecayA*

  A Float specifying the constant A associated with the generalized decay propagation model. The default value is 0.0.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=GENERALIZED_DECAY.

- *genDecayB*

  A Float specifying the constant B associated with the generalized decay propagation model. The default value is 0.0.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=GENERALIZED_DECAY.

- *genDecayC*

  A Float specifying the constant C associated with the generalized decay propagation model. The default value is 0.0.This argument is valid only when *definition*=SPHERICAL and *propagationModel*=GENERALIZED_DECAY.

- *seedNumber*

  An Int specifying the seed number (N) for the diffuse source calculation. N2 sources will be used in the simulation.This argument is valid only when *definition*=DIFFUSE.

- *massTNT*

  A Float specifying the equivalent mass of TNT, in any preferred mass unit.This argument is valid only when *definition*=AIR_BLAST or *definition*=SURFACE_BLAST.

- *massFactor*

  A Float specifying the multiplication factor to convert from the preferred mass unit to kilograms. The default value is 1.0.This argument is valid only when *definition*=AIR_BLAST or *definition*=SURFACE_BLAST.

- *lengthFactor*

  A Float specifying the multiplication factor to convert from the analysis length unit to meters. The default value is 1.0.This argument is valid only when *definition*=AIR_BLAST or *definition*=SURFACE_BLAST.

- *timeFactor*

  A Float specifying the multiplication factor to convert from the analysis time unit to seconds. The default value is 1.0.This argument is valid only when *definition*=AIR_BLAST or *definition*=SURFACE_BLAST.

- *pressureFactor*

  A Float specifying the multiplication factor to convert from the analysis pressure unit to pascals. The default value is 1.0.This argument is valid only when *definition*=AIR_BLAST or *definition*=SURFACE_BLAST.

### Return value

An IncidentWaveProperty object.

### Exceptions

None.



## setValues(...)



This method modifies the IncidentWaveProperty object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [IncidentWaveProperty ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepropertypyc.htm?ContextScope=all#simaker-incidentwavepropertyincidentwavepropertypyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The IncidentWaveProperty object has members with the same names and descriptions as the arguments to the [IncidentWaveProperty ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-incidentwavepropertypyc.htm?ContextScope=all#simaker-incidentwavepropertyincidentwavepropertypyc)method.



## Corresponding analysis keywords

- [INCIDENT WAVE INTERACTION PROPERTY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-incidentwaveinteractionproperty.htm?ContextScope=all#simakey-r-incidentwaveinteractionproperty)
- [UNDEX CHARGE PROPERTY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-undexchargeproperty.htm?ContextScope=all#simakey-r-undexchargeproperty)
- [CONWEP CHARGE PROPERTY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-conwepchargeproperty.htm?ContextScope=all#simakey-r-conwepchargeproperty)