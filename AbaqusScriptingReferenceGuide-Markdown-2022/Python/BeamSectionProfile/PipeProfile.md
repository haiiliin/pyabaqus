# PipeProfile object

The PipeProfile object defines the properties of a circular pipe profile.

The PipeProfile object is derived from the [Profile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## PipeProfile(...)



This method creates a PipeProfile object.



### Path

```
mdb.models[name].PipeProfile
session.odbs[name].PipeProfile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *r*

  A Float specifying the outer radius of the pipe. For more information, see [Beam cross-section library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

- *t*

  A Float specifying the wall thickness of the pipe.

### Optional arguments

None.

### Return value

A PipeProfile object.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the PipeProfile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PipeProfile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pipeprofilepyc.htm?ContextScope=all#simaker-pipeprofilepipeprofilepyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The PipeProfile object has members with the same names and descriptions as the arguments to the [PipeProfile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pipeprofilepyc.htm?ContextScope=all#simaker-pipeprofilepipeprofilepyc) method.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Corresponding analysis keywords

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=PIPE

- [BEAM SECTION](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection), SECTION=THICK PIPE