# BoxProfile object

The BoxProfile object defines the properties of a box profile.

The BoxProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## BoxProfile(...)



This method creates a BoxProfile object.



### Path

```
mdb.models[name].BoxProfile
session.odbs[name].BoxProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *a*

  A Float specifying the *a* dimension of the box profile. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

- *b*

  A Float specifying the *b* dimension of the box profile.

- *uniformThickness*

  A Boolean specifying whether the thickness is uniform.

- *t1*

  A Float specifying the uniform wall thickness if *uniformThickness*=ON, and the wall thickness of the first segment if *uniformThickness*=OFF.

### Optional arguments

- *t2*

  A Float specifying the wall thickness of the second segment. *t2* is required only when *uniformThickness*=OFF. The default value is 0.0.

- *t3*

  A Float specifying the wall thickness of the third segment. *t3* is required only when *uniformThickness*=OFF. The default value is 0.0.

- *t4*

  A Float specifying the wall thickness of the fourth segment. *t4* is required only when *uniformThickness*=OFF. The default value is 0.0.

### Return value

A BoxProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the BoxProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BoxProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boxprofilepyc.htm?ContextScope=all#simaker-boxprofileboxprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The BoxProfile object has members with the same names and descriptions as the arguments to the [BoxProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boxprofilepyc.htm?ContextScope=all#simaker-boxprofileboxprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=BOX