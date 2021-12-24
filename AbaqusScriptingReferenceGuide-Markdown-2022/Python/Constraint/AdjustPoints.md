# AdjustPoints object

The AdjustPoints constraint object is used to adjust points (nodes) to a surface.

The AdjustPoints object is derived from the [Constraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].constraints[name]
```

## AdjustPoints(...)



This method creates an AdjustPoints object.



### Path

```
mdb.models[name].AdjustPoints
```

### Required arguments

- *name*

  A String specifying the constraint repository key.

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surface to which the *controlPoints* are adjusted.

- *controlPoints*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the constraint control points.

### Optional arguments

None.

### Return value

An AdjustPoints object.

### Exceptions

None.



## setValues(...)



This method modifies the AdjustPoints object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AdjustPoints ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adjustpointspyc.htm?ContextScope=all#simaker-adjustpointsadjustpointspyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The AdjustPoints object has members with the same names and descriptions as the arguments to the [AdjustPoints ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adjustpointspyc.htm?ContextScope=all#simaker-adjustpointsadjustpointspyc)method.

In addition, the AdjustPoints object has the following member:

- *suppressed*

  A Boolean specifying whether the constraint is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [ADJUST](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-adjust.htm?ContextScope=all#simakey-r-adjust)