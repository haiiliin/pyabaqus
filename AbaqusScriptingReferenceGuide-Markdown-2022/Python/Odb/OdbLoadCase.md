# OdbLoadCase object

The OdbLoadCase object describes a load case.

## Access

```
import odbAccess
session.odbs[name].steps[name].frames[i].loadCase
session.odbs[name].steps[name].historyRegions[name].loadCase
session.odbs[name].steps[name].loadCases[name]
```

## LoadCase(...)



This method creates an OdbLoadCase object.



### Path

session.odbs[*name*].steps[*name*].LoadCase

### Required arguments

- *name*

  A String specifying the name of the OdbLoadCase object.

### Optional arguments

None.

### Return value

An OdbLoadCase object.

### Exceptions

None.



## Members

The OdbLoadCase object has members with the same names and descriptions as the arguments to the [LoadCase ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?ContextScope=all#simaker-odbloadcaseloadcasepyc)method.