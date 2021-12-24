# TrussSection object

The TrussSection object defines the properties of a truss section.

The TrussSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## TrussSection(...)



This method creates a TrussSection object.



### Path

```
mdb.models[name].TrussSection
session.odbs[name].TrussSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *material*

  A String specifying the name of the material.

### Optional arguments

- *area*

  A Float specifying the cross-sectional area for the section. Possible values are *area* >> 0. The default value is 1.0.

### Return value

A TrussSection object.

### Exceptions

RangeError and InvalidNameError.



## setValues(...)



This method modifies the TrussSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TrussSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-trusssectionpyc.htm?ContextScope=all#simaker-trusssectiontrusssectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The TrussSection object has members with the same names and descriptions as the arguments to the [TrussSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-trusssectionpyc.htm?ContextScope=all#simaker-trusssectiontrusssectionpyc)method.



## Corresponding analysis keywords

- [SOLID SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-solidsection.htm?ContextScope=all#simakey-r-solidsection)