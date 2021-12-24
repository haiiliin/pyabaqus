# LoadCase object

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.

## Access

```
import step
mdb.models[name].steps[name].loadCases[name]
```

## LoadCase(...)



This method creates a load case in a step.



### Path

```
mdb.models[name].steps[name].LoadCase
```

### Required arguments

- *name*

  A String specifying the name of the object.

### Optional arguments

- *boundaryConditions*

  A sequence of (String, Float) sequences specifying the name of a BoundaryCondition followed by a nonzero Float scaling factor. The default value is an empty sequence.

- *loads*

  A sequence of (String, Float) sequences specifying the name of a Load followed by a nonzero Float specifying a scale factor. The default value is an empty sequence.

- *includeActiveBaseStateBC*

  A Boolean specifying whether to include all active boundary conditions propagated or modified from the base state. The default value is ON.

### Return value

A LoadCase object.

### Exceptions

RangeError.



## resume()



This method resumes the load case that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the load case.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the LoadCase object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [LoadCase ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadcasepyc.htm?ContextScope=all#simaker-loadcaseloadcasepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The LoadCase object has members with the same names and descriptions as the arguments to the [LoadCase ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadcasepyc.htm?ContextScope=all#simaker-loadcaseloadcasepyc)method.

In addition, the LoadCase object has the following member:

- *suppressed*

  A Boolean specifying whether the load case is suppressed or not. The default value is OFF.