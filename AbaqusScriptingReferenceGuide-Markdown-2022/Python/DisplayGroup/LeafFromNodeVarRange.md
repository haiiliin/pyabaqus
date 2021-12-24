# LeafFromNodeVarRange object

The LeafFromNodeVarRange object can be used whenever a Leaf object is expected as an argument. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are used to specify the items in a display group. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

The LeafFromNodeVarRange object is derived from the [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object.

## Access

```
import displayGroupOdbToolset
```

## LeafFromNodeVarRange(...)



This method creates a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object from nodes with values lying in a variable range.



### Path

```
LeafFromNodeVarRange
```

### Required arguments

None.

### Optional arguments

- *minimumRange*

  A Float specifying the minimum value for the variable range. The default value is −3.40282346639E38.

- *maximumRange*

  A Float specifying the maximum value for the variable range. The default value is 3.40282346639e+038.

- *insideRange*

  A Boolean specifying the method used to evaluate the range. If *insideRange*=ON, the range falls inside the specified minimum and maximum values. The default value is ON.

### Return value

A LeafFromNodeVarRange object.

### Exceptions

None.



## Members

The LeafFromNodeVarRange object has members with the same names and descriptions as the arguments to the [LeafFromNodeVarRange ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leaffromnodevarrangepyc.htm?ContextScope=all#simaker-leaffromnodevarrangeleaffromnodevarrangepyc)method.

In addition, the LeafFromNodeVarRange object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.