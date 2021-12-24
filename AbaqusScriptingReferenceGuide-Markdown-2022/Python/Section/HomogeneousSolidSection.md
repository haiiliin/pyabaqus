# HomogeneousSolidSection object

The HomogeneousSolidSection object defines the properties of a solid section.

The HomogeneousSolidSection object is derived from the [SolidSection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solidsectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## HomogeneousSolidSection(...)



This method creates a HomogeneousSolidSection object.



### Path

```
mdb.models[name].HomogeneousSolidSection
session.odbs[name].HomogeneousSolidSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *material*

  A String specifying the name of the material.

### Optional arguments

- *thickness*

  A Float specifying the thickness of the section. Possible values are None or greater than zero. The default value is 1.0.

### Return value

A HomogeneousSolidSection object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the HomogeneousSolidSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [HomogeneousSolidSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-homogeneoussolidsectionpyc.htm?ContextScope=all#simaker-homogeneoussolidsectionhomogeneoussolidsectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The HomogeneousSolidSection object has members with the same names and descriptions as the arguments to the [HomogeneousSolidSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-homogeneoussolidsectionpyc.htm?ContextScope=all#simaker-homogeneoussolidsectionhomogeneoussolidsectionpyc)method.



## Corresponding analysis keywords

- [SOLID SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-solidsection.htm?ContextScope=all#simakey-r-solidsection)