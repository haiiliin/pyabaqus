# ButterworthFilter object

The ButterworthFilter object defines a Butterworth type filter.

The ButterworthFilter object is derived from the [Filter](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filterpyc.htm?ContextScope=all) object.

## Access

```
import filter
mdb.models[name].filters[name]
import odbFilter
session.odbs[name].filters[name]
```

## ButterworthFilter(...)



This method creates a ButterworthFilter object.



### Path

```
mdb.models[name].ButterworthFilter
session.odbs[name].ButterworthFilter
```

### Required arguments

- *name*

  A String specifying the repository key. This name ANTIALIASING is reserved for filters generated internally by the program.

- *cutoffFrequency*

  A Float specifying the attenuation point of the filter. Possible values are non-negative numbers. Order is not available for OperatorFilter.

### Optional arguments

- *order*

  An Int specifying the highest power of the filter transfer function. Possible values are non-negative numbers less than or equal to 20. Order is not available for OperatorFilter. The default value is 2.

- *operation*

  A SymbolicConstant specifying the filter operator. Possible values are NONE, MIN, MAX, and ABS. The default value is NONE.

- *halt*

  A Boolean specifying whether to stop the analysis if the specified limit is reached. The default value is OFF.

- *limit*

  None or a Float specifying the threshold limit, an upper or lower bound for output values depending on the operation, or a bound for stopping the analysis when Halt is used. The default value is None.

- *invariant*

  A SymbolicConstant specifying the invariant to which filtering is applied. Possible values are NONE, FIRST, and SECOND. The default value is NONE.

### Return value

A ButterworthFilter object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the ButterworthFilter object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ButterworthFilter ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-butterworthfilterpyc.htm?ContextScope=all#simaker-butterworthfilterbutterworthfilterpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The ButterworthFilter object has members with the same names and descriptions as the arguments to the [ButterworthFilter ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-butterworthfilterpyc.htm?ContextScope=all#simaker-butterworthfilterbutterworthfilterpyc)method.



## Corresponding analysis keywords

- [FILTER](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-filter.htm?ContextScope=all#simakey-r-filter)