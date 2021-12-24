# AcousticInterfaceSection object

The AcousticInterfaceSection object defines the properties of an acoustic section.

The AcousticInterfaceSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## AcousticInterfaceSection(...)



This method creates an AcousticInterfaceSection object.



### Path

```
mdb.models[name].AcousticInterfaceSection
session.odbs[name].AcousticInterfaceSection
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *thickness*

  A Float specifying the thickness of the section. Possible values are *thickness* >> 0.0. The default value is 1.0.

### Return value

An AcousticInterfaceSection object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the AcousticInterfaceSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AcousticInterfaceSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticinterfacesectionpyc.htm?ContextScope=all#simaker-acousticinterfacesectionacousticinterfacesectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The AcousticInterfaceSection object has members with the same names and descriptions as the arguments to the [AcousticInterfaceSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticinterfacesectionpyc.htm?ContextScope=all#simaker-acousticinterfacesectionacousticinterfacesectionpyc)method.



## Corresponding analysis keywords

- [INTERFACE](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-interface.htm?ContextScope=all#simakey-r-interface)