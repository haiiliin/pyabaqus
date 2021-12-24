# KinematicHardening object

The KinematicHardening object stores the data for initial equivalent plastic strains and, if relevant, the initial backstress tensor.

The KinematicHardening object is derived from the [PredefinedField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].predefinedFields[name]
```

## KinematicHardening(...)



This method creates a KinematicHardening object.



### Path

```
mdb.models[name].KinematicHardening
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the predefined field is applied.

### Optional arguments

- *numBackStress*

  An Int specifying the number of backstresses. The default value is 1.

- *equivPlasticStrain*

  A sequence of Floats specifying the initial equivalent plastic strain.

- *backStress*

  A sequence of sequences of Floats specifying the initial backstress tensor for kinematic hardening models. The default value is an empty sequence.

- *sectPtNum*

  A sequence of Ints specifying section point numbers. This argument is valid only when *definition*=SECTION_PTS.

- *definition*

  A SymbolicConstant specifying different types of kinematic hardening. Possible values are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The default value is KINEMATIC_HARDENING.

- *rebarLayerNames*

  A sequence of Strings specifying rebar layer names. This argument is valid only when *definition*=REBAR.

- *distributionType*

  A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE and ANALYTICAL_FIELD. The default value is MAGNITUDE.

### Return value

A KinematicHardening object.

### Exceptions

None.



## setValues(...)



This method modifies the KinematicHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [KinematicHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-kinematichardeningpyc.htm?ContextScope=all#simaker-kinematichardeningkinematichardeningpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The KinematicHardening object has members with the same names and descriptions as the arguments to the [KinematicHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-kinematichardeningpyc.htm?ContextScope=all#simaker-kinematichardeningkinematichardeningpyc)method.

In addition, the KinematicHardening object can have the following member:

- *field*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object associated with this predefined field. The *field* argument applies only when *distributionType*=ANALYTICAL_FIELD. The default value is an empty string.



## Corresponding analysis keywords

- [INITIAL CONDITIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-initialconditions.htm?ContextScope=all#simakey-r-initialconditions), TYPE=HARDENING