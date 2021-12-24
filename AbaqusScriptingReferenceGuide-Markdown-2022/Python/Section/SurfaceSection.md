# SurfaceSection object

The SurfaceSection object defines the properties of a surface section.

The SurfaceSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## SurfaceSection(...)



This method creates a SurfaceSection object.



### Path

```
mdb.models[name].SurfaceSection
session.odbs[name].SurfaceSection
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *useDensity*

  A Boolean specifying whether or not to use the value of *density*. The default value is OFF.

- *density*

  A Float specifying the value of density to apply to this section. The default value is 0.0.

### Return value

A SurfaceSection object.

### Exceptions

RangeError and InvalidNameError.



## Members

The SurfaceSection object has members with the same names and descriptions as the arguments to the [SurfaceSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacesectionpyc.htm?ContextScope=all#simaker-surfacesectionsurfacesectionpyc)method.

In addition, the SurfaceSection object can have the following member:

- *rebarLayers*

  A [RebarLayers](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all) object specifying reinforcement properties.



## Corresponding analysis keywords

- [SURFACE SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-surfacesection.htm?ContextScope=all#simakey-r-surfacesection)