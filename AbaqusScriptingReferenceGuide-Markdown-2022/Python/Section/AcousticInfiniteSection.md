# AcousticInfiniteSection object

The AcousticInfiniteSection object defines the properties of an acoustic section.

The AcousticInfiniteSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## AcousticInfiniteSection(...)



This method creates an AcousticInfiniteSection object.



### Path

```
mdb.models[name].AcousticInfiniteSection
session.odbs[name].AcousticInfiniteSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *material*

  A String specifying the name of the material.

### Optional arguments

- *thickness*

  A Float specifying the thickness of the section. Possible values are *thickness* >> 0.0. The default value is 1.0.

- *order*

  An Int specifying the number of ninth-order polynomials that will be used to resolve the variation of the acoustic field in the infinite direction. Possible values are 0 << *order* ≤≤ 10. The default value is 10.

### Return value

An AcousticInfiniteSection object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the AcousticInfiniteSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AcousticInfiniteSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticinfinitesectionpyc.htm?ContextScope=all#simaker-acousticinfinitesectionacousticinfinitesectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The AcousticInfiniteSection object has members with the same names and descriptions as the arguments to the [AcousticInfiniteSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticinfinitesectionpyc.htm?ContextScope=all#simaker-acousticinfinitesectionacousticinfinitesectionpyc)method.



## Corresponding analysis keywords

- [SOLID SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-solidsection.htm?ContextScope=all#simakey-r-solidsection)