# HexagonalProfile object

The HexagonalProfile object defines the properties of a hexagonal profile.

The HexagonalProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## HexagonalProfile(...)



This method creates a HexagonalProfile object.



### Path

```
mdb.models[name].HexagonalProfile
session.odbs[name].HexagonalProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *r*

  A positive Float specifying the *r* dimension (outer radius) of the hexagonal profile. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

- *t*

  A positive Float specifying the *t* dimension (wall thickness) of the hexagonal profile, *t < (sqrt(3)/2)r*.

### Optional arguments

None.

### Return value

A HexagonalProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the HexagonalProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [HexagonalProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hexagonalprofilepyc.htm?ContextScope=all#simaker-hexagonalprofilehexagonalprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The HexagonalProfile object has members with the same names and descriptions as the arguments to the [HexagonalProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hexagonalprofilepyc.htm?ContextScope=all#simaker-hexagonalprofilehexagonalprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=HEX