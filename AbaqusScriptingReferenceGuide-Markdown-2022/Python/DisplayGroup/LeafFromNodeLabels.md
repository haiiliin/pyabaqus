# LeafFromNodeLabels object

The LeafFromNodeLabels object can be used whenever a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object is expected as an argument. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are used to specify the items in a display group. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

The LeafFromNodeLabels object is derived from the [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object.

## Access

```
import displayGroupOdbToolset
```

## LeafFromNodeLabels(...)



This method creates a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object from a sequence of node labels that belong to a single part instance.



### Path

```
LeafFromNodeLabels
```

### Required arguments

- *partInstanceName*

  A String specifying the name of the part instance to which *nodeLabels* refers.

- *nodeLabels*

  A sequence of Strings specifying expressions that denote node labels. The expression can be any of the following:An Int specifying a single node label; for example, `1`.A String specifying a single node label; for example, `'7'`.A String specifying a sequence of node labels; for example, `'3:5'` and `'3:15:3'`.

### Optional arguments

None.

### Return value

A LeafFromNodeLabels object.

### Exceptions

None.



## Members

The LeafFromNodeLabels object has members with the same names and descriptions as the arguments to the [LeafFromNodeLabels ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leaffromnodelabelspyc.htm?ContextScope=all#simaker-leaffromnodelabelsleaffromnodelabelspyc)method.

In addition, the LeafFromNodeLabels object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.