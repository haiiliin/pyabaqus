# GeneralizedProfile object

The GeneralizedProfile object defines the properties of a profile via its area, moment of inertia, etc.

The GeneralizedProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## GeneralizedProfile(...)



This method creates a GeneralizedProfile object.



### Path

```
mdb.models[name].GeneralizedProfile
session.odbs[name].GeneralizedProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *area*

  A Float specifying the cross-sectional area for the profile.

- *i11*

  A Float specifying the moment of inertia for bending about the 1-axis, I11I11.

- *i12*

  A Float specifying the moment of inertia for cross bending, I12I12.

- *i22*

  A Float specifying the moment of inertia for bending about the 2-axis, I22I22.

- *j*

  A Float specifying the torsional constant, JJ.

- *gammaO*

  A Float specifying the sectorial moment, Γ0Γ0.

- *gammaW*

  A Float specifying the warping constant, ΓWΓW.

### Optional arguments

None.

### Return value

A GeneralizedProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the GeneralizedProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GeneralizedProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-generalizedprofilepyc.htm?ContextScope=all#simaker-generalizedprofilegeneralizedprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The GeneralizedProfile object has members with the same names and descriptions as the arguments to the [GeneralizedProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-generalizedprofilepyc.htm?ContextScope=all#simaker-generalizedprofilegeneralizedprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM GENERAL SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamgeneralsection.htm?ContextScope=all#simakey-r-beamgeneralsection), SECTION=GENERAL or NONLINEAR GENERAL