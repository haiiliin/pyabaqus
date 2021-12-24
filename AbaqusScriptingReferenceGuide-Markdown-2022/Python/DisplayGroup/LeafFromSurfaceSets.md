# LeafFromSurfaceSets object

The LeafFromSurfaceSets object can be used whenever a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object is expected as an argument. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are used to specify the items in a display group. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

The LeafFromSurfaceSets object is derived from the [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object.

## Access

```
import displayGroupOdbToolset
```

## LeafFromSurfaceSets(...)



This method creates a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object from a sequence of surface sets.



### Path

```
LeafFromSurfaceSets
```

### Required arguments

- *surfaceSets*

  A sequence of Strings specifying surface sets, or a String specifying a single surface set.

### Optional arguments

None.

### Return value

A LeafFromSurfaceSets object.

### Exceptions

None.



## Members

The LeafFromSurfaceSets object has members with the same names and descriptions as the arguments to the [LeafFromSurfaceSets ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leaffromsurfacesetspyc.htm?ContextScope=all#simaker-leaffromsurfacesetsleaffromsurfacesetspyc)method.

In addition, the LeafFromSurfaceSets object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.