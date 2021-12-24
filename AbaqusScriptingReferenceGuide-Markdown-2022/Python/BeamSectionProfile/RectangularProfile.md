# RectangularProfile object

The RectangularProfile object defines the properties of a solid rectangular profile.

The RectangularProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## RectangularProfile(...)



This method creates a RectangularProfile object.



### Path

```
mdb.models[name].RectangularProfile
session.odbs[name].RectangularProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *a*

  A positive Float specifying the *a* dimension of the rectangular profile. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

- *b*

  A positive Float specifying the *b* dimension of the rectangular profile.

### Optional arguments

None.

### Return value

A RectangularProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the RectangularProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [RectangularProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rectangularprofilepyc.htm?ContextScope=all#simaker-rectangularprofilerectangularprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The RectangularProfile object has members with the same names and descriptions as the arguments to the [RectangularProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rectangularprofilepyc.htm?ContextScope=all#simaker-rectangularprofilerectangularprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=RECT