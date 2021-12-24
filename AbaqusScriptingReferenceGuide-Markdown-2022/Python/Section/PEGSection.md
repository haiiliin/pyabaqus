# PEGSection object

The PEGSection object defines the properties of a solid section.

The PEGSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## PEGSection(...)



This method creates a PEGSection object.



### Path

```
mdb.models[name].PEGSection
session.odbs[name].PEGSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *material*

  A String specifying the name of the material.

### Optional arguments

- *thickness*

  A Float specifying the thickness of the section. Possible values are *thickness* >> 0.0. The default value is 1.0.

- *wedgeAngle1*

  A Float specifying the value of the x component of the angle between the bounding planes, ΔϕxΔ⁢ϕx. The default value is 0.0.

- *wedgeAngle2*

  A Float specifying the value of the y component of the angle between the bounding planes, ΔϕyΔ⁢ϕy. The default value is 0.0.

### Return value

A PEGSection object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the PEGSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PEGSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegsectionpyc.htm?ContextScope=all#simaker-pegsectionpegsectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The PEGSection object has members with the same names and descriptions as the arguments to the [PEGSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegsectionpyc.htm?ContextScope=all#simaker-pegsectionpegsectionpyc)method.



## Corresponding analysis keywords

- [SOLID SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-solidsection.htm?ContextScope=all#simakey-r-solidsection)