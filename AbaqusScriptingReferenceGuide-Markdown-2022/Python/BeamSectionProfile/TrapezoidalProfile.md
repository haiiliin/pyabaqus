# TrapezoidalProfile object

The TrapezoidalProfile object defines the properties of a trapezoidal profile.

The TrapezoidalProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## TrapezoidalProfile(...)



This method creates a TrapezoidalProfile object.



### Path

```
mdb.models[name].TrapezoidalProfile
session.odbs[name].TrapezoidalProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *a*

  A positive Float specifying the *a* dimension of the Trapezoidal profile. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

- *b*

  A positive Float specifying the *b* dimension of the Trapezoidal profile.

- *c*

  A positive Float specifying the *c* dimension of the Trapezoidal profile.

- *d*

  A Float specifying the *d* dimension of the Trapezoidal profile.

### Optional arguments

None.

### Return value

A TrapezoidalProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the TrapezoidalProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TrapezoidalProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-trapezoidalprofilepyc.htm?ContextScope=all#simaker-trapezoidalprofiletrapezoidalprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The TrapezoidalProfile object has members with the same names and descriptions as the arguments to the [TrapezoidalProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-trapezoidalprofilepyc.htm?ContextScope=all#simaker-trapezoidalprofiletrapezoidalprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=TRAPEZOID