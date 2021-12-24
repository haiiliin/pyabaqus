# IProfile object

The IProfile object defines the properties of an I profile.

The IProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## IProfile(...)



This method creates an IProfile object.



### Path

```
mdb.models[name].IProfile
session.odbs[name].IProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *l*

  A Float specifying the *l* dimension (offset of 1–axis from the bottom flange surface) of the I profile. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

- *h*

  A Float specifying the *h* dimension (height) of the I profile.

- *b1*

  A Float specifying the *b1* dimension (bottom flange width) of the I profile.

- *b2*

  A Float specifying the *b2* dimension (top flange width) of the I profile.

- *t1*

  A Float specifying the *t1* dimension (bottom flange thickness) of the I profile.

- *t2*

  A Float specifying the *t2* dimension (top flange thickness) of the I profile.

- *t3*

  A Float specifying the *t3* dimension (web thickness) of the I profile.

### Optional arguments

None.

### Return value

An IProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the IProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [IProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-iprofilepyc.htm?ContextScope=all#simaker-iprofileiprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The IProfile object has members with the same names and descriptions as the arguments to the [IProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-iprofilepyc.htm?ContextScope=all#simaker-iprofileiprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=I