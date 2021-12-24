# ArbitraryProfile object

The ArbitraryProfile object defines the properties of an arbitrary profile.

The ArbitraryProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## ArbitraryProfile(...)



This method creates a ArbitraryProfile object.



### Path

```
mdb.models[name].ArbitraryProfile
session.odbs[name].ArbitraryProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

None.

### Table data

The first sequence in the table specifies the following:

- 1-coordinate of the first point defining the profile.
- 2-coordinate of the first point defining the profile.

All other sequences in the table specify the following:

- 1–coordinate of the next point defining the profile.
- 2–coordinate of the next point defining the profile.
- The thickness of the segment ending at that point.

### Return value

An ArbitraryProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the ArbitraryProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ArbitraryProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-arbitraryprofilepyc.htm?ContextScope=all#simaker-arbitraryprofilearbitraryprofilepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The ArbitraryProfile object has members with the same names and descriptions as the arguments to the [ArbitraryProfile ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-arbitraryprofilepyc.htm?ContextScope=all#simaker-arbitraryprofilearbitraryprofilepyc)method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=ARBITRARY