# AcousticImpedance object

The AcousticImpedance object defines surface impedance information or nonreflecting boundaries for acoustic and coupled acoustic-structural analyses.

The AcousticImpedance object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## AcousticImpedance(...)



This method creates an AcousticImpedance object.



### Path

```
mdb.models[name].AcousticImpedance
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the AcousticImpedance object is created.

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the acoustic boundary surface.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the type of acoustic impedance to be defined. Possible values are TABULAR and NONREFLECTING. The default value is TABULAR.

- *interactionProperty*

  A String specifying the [AcousticImpedanceProp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedanceproppyc.htm?ContextScope=all) object associated with this interaction.

- *nonreflectingType*

  A SymbolicConstant specifying the type of nonreflecting geometry to be defined. Possible values are PLANE, IMPROVED, CIRCULAR, SPHERICAL, ELLIPTICAL, and PROLATE. The default value is PLANE.This argument is valid only when *definition*=NONREFLECTING.

- *radius*

  A Float specifying the radius of the circle or sphere defining the boundary surface. The default value is 1.0.This argument is valid only when *definition*=NONREFLECTING, and *nonreflectingType*=CIRCULAR or SPHERICAL.

- *semimajorAxis*

  A Float specifying the semimajor axis length of the ellipse or prolate spheroid defining the boundary surface. The default value is 1.0.This argument is valid only when *definition*=NONREFLECTING, and *nonreflectingType*=ELLIPTICAL or PROLATE.

- *eccentricity*

  A Float specifying the eccentricity of the ellipse or prolate spheroid defining the boundary surface. The default value is 0.0.This argument is valid only when *definition*=NONREFLECTING, and *nonreflectingType*=ELLIPTICAL or PROLATE.

- *centerCoordinates*

  A sequence of three Floats specifying the X, Y, and Z coordinates of the center of the ellipse or prolate spheroid defining the boundary surface. The default value is (0, 0, 0).This argument is valid only when *definition*=NONREFLECTING, and *nonreflectingType*=ELLIPTICAL or PROLATE.

- *directionCosine*

  A sequence of three Floats specifying the X, Y, and Z components of the direction cosine of the major axis of the ellipse or prolate spheroid defining the boundary surface. The default value is (0, 0, 1).This argument is valid only when *definition*=NONREFLECTING, and *nonreflectingType*=ELLIPTICAL or PROLATE.

### Return value

An AcousticImpedance object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing AcousticImpedance object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AcousticImpedance ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedancepyc.htm?ContextScope=all#simaker-acousticimpedanceacousticimpedancepyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing AcousticImpedance object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *interactionProperty*

  A String specifying the [AcousticImpedanceProp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedanceproppyc.htm?ContextScope=all) object associated with this interaction.

### Return value

None.

### Exceptions

None.



## Members

The AcousticImpedance object has members with the same names and descriptions as the arguments to the [AcousticImpedance ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedancepyc.htm?ContextScope=all#simaker-acousticimpedanceacousticimpedancepyc)method except the optional arguments to the [setValuesInStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedancepyc.htm?ContextScope=all#simaker-acousticimpedancesetvaluesinsteppyc)method.



## Corresponding analysis keywords

- [SIMPEDANCE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-simpedance.htm?ContextScope=all#simakey-r-simpedance)