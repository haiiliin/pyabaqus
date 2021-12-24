# EmbeddedRegion object

The EmbeddedRegion object allows you to embed a region of the model within a “host” region of the model or within the whole model.

The EmbeddedRegion object is derived from the [Constraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].constraints[name]
```

## EmbeddedRegion(...)



This method creates a EmbeddedRegion object.



### Path

```
mdb.models[name].EmbeddedRegion
```

### Required arguments

- *name*

  A String specifying the constraint repository key.

- *embeddedRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the body region to be embedded.

- *hostRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the host region. A value of None indicates that the host region is the whole model.

### Optional arguments

- *weightFactorTolerance*

  A Float specifying a small value below which the weighting factors will be zeroed out. The default value is 10–6.

- *toleranceMethod*

  A SymbolicConstant specifying the method used to determine the embedded element tolerance. Possible values are ABSOLUTE, FRACTIONAL, and BOTH. The default value is BOTH.

- *absoluteTolerance*

  A Float specifying the absolute value by which a node on the embedded region may lie outside the host region. If *absoluteTolerance*=0.0, the *fractionalTolerance* value will be used. The default value is 0.0.This argument applies only when *toleranceMethod*=ABSOLUTE or BOTH.

- *fractionalTolerance*

  A Float specifying the fractional value by which a node on the embedded region may lie outside the host region. The fractional value is based on the average element size within the host region. The default value is 0.05.If both tolerance arguments are specified, the smaller value will be used.This argument applies only when *toleranceMethod*=FRACTIONAL or BOTH.

### Return value

An EmbeddedRegion object.

### Exceptions

None.



## setValues(...)



This method modifies the EmbeddedRegion object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [EmbeddedRegion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-embeddedregionpyc.htm?ContextScope=all#simaker-embeddedregionembeddedregionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The EmbeddedRegion object has members with the same names and descriptions as the arguments to the [EmbeddedRegion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-embeddedregionpyc.htm?ContextScope=all#simaker-embeddedregionembeddedregionpyc)method.

In addition, the EmbeddedRegion object has the following member:

- *suppressed*

  A Boolean specifying whether the constraint is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [EMBEDDED ELEMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-embeddedelement.htm?ContextScope=all#simakey-r-embeddedelement)