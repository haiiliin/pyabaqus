# EulerianSection object

The EulerianSection object defines the properties of a Eulerian section.

The EulerianSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## EulerianSection(...)



This method creates a EulerianSection object.



### Path

```
mdb.models[name].EulerianSection
session.odbs[name].EulerianSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *data*

  A String-to-String Dictionary specifying a dictionary mapping Material instance names to Material names. Internally the specified mapping gets sorted on Material instance name.

### Optional arguments

None.

### Return value

An EulerianSection object.

### Exceptions

None.



## setValues(...)



This method modifies the EulerianSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [EulerianSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-euleriansectionpyc.htm?ContextScope=all#simaker-euleriansectioneuleriansectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The EulerianSection object has members with the same names and descriptions as the arguments to the [EulerianSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-euleriansectionpyc.htm?ContextScope=all#simaker-euleriansectioneuleriansectionpyc)method.



## Corresponding analysis keywords

- [EULERIAN SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-euleriansection.htm?ContextScope=all#simakey-r-euleriansection)