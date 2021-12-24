# LProfile object

The LProfile object defines the properties of a L profile.

The LProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## LProfile(...)



This method creates a LProfile object.



### Path

```
mdb.models[name].LProfile
session.odbs[name].LProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *a*

  A positive Float specifying the *a* dimension (flange length) of the L profile. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

- *b*

  A positive Float specifying the *b* dimension (flange length) of the L profile.

- *t1*

  A positive Float specifying the *t1* dimension (flange thickness) of the L profile (*t1 < b*).

- *t2*

  A positive Float specifying the *t2* dimension (flange thickness) of the L profile (*t2< a*).

### Optional arguments

None.

### Return value

A LProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the LProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [LProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lprofilepyc.htm?ContextScope=all#simaker-lprofilelprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The LProfile object has members with the same names and descriptions as the arguments to the [LProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lprofilepyc.htm?ContextScope=all#simaker-lprofilelprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=L