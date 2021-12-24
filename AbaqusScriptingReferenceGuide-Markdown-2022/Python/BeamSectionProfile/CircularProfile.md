# CircularProfile object

The CircularProfile object defines the properties of a solid circular profile.

The CircularProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## CircularProfile(...)



This method creates a CircularProfile object.



### Path

```
mdb.models[name].CircularProfile
session.odbs[name].CircularProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *r*

  A positive Float specifying the *r* dimension (outer radius) of the circular profile. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

### Optional arguments

None.

### Return value

A CircularProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the CircularProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CircularProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-circularprofilepyc.htm?ContextScope=all#simaker-circularprofilecircularprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The CircularProfile object has members with the same names and descriptions as the arguments to the [CircularProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-circularprofilepyc.htm?ContextScope=all#simaker-circularprofilecircularprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=CIRC