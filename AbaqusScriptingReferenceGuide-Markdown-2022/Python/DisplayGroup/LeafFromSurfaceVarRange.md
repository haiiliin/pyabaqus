# LeafFromSurfaceVarRange object

The LeafFromSurfaceVarRange object can be used whenever a Leaf object is expected as an argument. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are used to specify the items in a display group. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

The LeafFromSurfaceVarRange object is derived from the [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object.

## Access

```
import displayGroupOdbToolset
```

## LeafFromSurfaceVarRange(...)



This method creates a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object from surfaces with values lying in a variable range.



### Path

```
LeafFromSurfaceVarRange
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

A LeafFromSurfaceVarRange object.

### Exceptions

None.



## Members

The LeafFromSurfaceVarRange object has members with the same names and descriptions as the arguments to the [LeafFromSurfaceVarRange ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leaffromsurfacevarrangepyc.htm?ContextScope=all#simaker-leaffromsurfacevarrangeleaffromsurfacevarrangepyc)method.

In addition, the LeafFromSurfaceVarRange object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.