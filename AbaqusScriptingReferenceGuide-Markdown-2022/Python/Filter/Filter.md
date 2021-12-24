# Filter object

The Filter object is the abstract base type for other Filter objects. The Filter object has no explicit constructor. The methods and members of the Filter object are common to all objects derived from the Filter.

## Access

```
import filter
mdb.models[name].filters[name]
import odbFilter
session.odbs[name].filters[name]
```

## Members

The Filter object has the following members:

- *name*

  A String specifying the repository key. This name ANTIALIASING is reserved for filters generated internally by the program.

- *cutoffFrequency*

  A Float specifying the attenuation point of the filter. Possible values are non-negative numbers. Order is not available for OperatorFilter.

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