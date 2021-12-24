# TProfile object

The TProfile object defines the properties of a T profile.

The TProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## TProfile(...)



This method creates a TProfile object.



### Path

```
mdb.models[name].TProfile
session.odbs[name].TProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *b*

  A positive Float specifying the *b* dimension (flange width) of the T profile. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

- *h*

  A positive Float specifying the *h* dimension (height) of the T profile.

- *l*

  A positive Float specifying the *l* dimension (offset of 1–axis from the edge of web) of the T profile.

- *tf*

  A positive Float specifying the *tf* dimension (flange thickness) of the T profile (*tf < h*).

- *tw*

  A positive Float specifying the *tw* dimension (web thickness) of the T profile (*tw< b*).

### Optional arguments

None.

### Return value

A TProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the TProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tprofilepyc.htm?ContextScope=all#simaker-tprofiletprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The TProfile object has members with the same names and descriptions as the arguments to the [TProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tprofilepyc.htm?ContextScope=all#simaker-tprofiletprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=I