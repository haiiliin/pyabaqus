# CompositeSolidSection object

The CompositeSolidSection object defines the properties of a composite solid section.

The CompositeSolidSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## CompositeSolidSection(...)



This method creates a CompositeSolidSection object.



### Path

```
mdb.models[name].CompositeSolidSection
session.odbs[name].CompositeSolidSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *layup*

  A [SectionLayerArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionlayerpyc.htm?ContextScope=all) object specifying the solid cross-section.

### Optional arguments

- *symmetric*

  A Boolean specifying whether or not the layup should be made symmetric by the analysis. The default value is OFF.

- *layupName*

  A String specifying the layup name for this section. The default value is an empty string.

### Return value

A CompositeSolidSection object.

### Exceptions

None.



## setValues(...)



This method modifies the CompositeSolidSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CompositeSolidSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositesolidsectionpyc.htm?ContextScope=all#simaker-compositesolidsectioncompositesolidsectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The CompositeSolidSection object has members with the same names and descriptions as the arguments to the [CompositeSolidSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositesolidsectionpyc.htm?ContextScope=all#simaker-compositesolidsectioncompositesolidsectionpyc)method.



## Corresponding analysis keywords

- [SOLID SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-solidsection.htm?ContextScope=all#simakey-r-solidsection)