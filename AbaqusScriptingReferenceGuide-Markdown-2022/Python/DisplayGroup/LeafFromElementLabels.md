# LeafFromElementLabels object

The LeafFromElementLabels object can be used whenever a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object is expected as an argument. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are used to specify the items in a display group. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

The LeafFromElementLabels object is derived from the [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object.

This page discusses:

## Access

```
import displayGroupOdbToolset
```

## LeafFromElementLabels(...)



This method creates a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object from a sequence of element labels that belong to a single part instance.



### Path

```
LeafFromElementLabels
```

### Required arguments

- *partInstanceName*

  A String specifying the name of the part instance to which *elementLabels* refers.

- *elementLabels*

  A sequence of Strings specifying expressions that denote element labels. The expression can be any of the following:An Int specifying a single element label; for example, `1`.A String specifying a single element label; for example, `'7'`.A String specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`.

### Optional arguments

None.

### Return value

A LeafFromElementLabels object.

### Exceptions

None.



## Members

The LeafFromElementLabels object has members with the same names and descriptions as the arguments to the [LeafFromElementLabels ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leaffromelementlabelspyc.htm?ContextScope=all#simaker-leaffromelementlabelsleaffromelementlabelspyc)method.

In addition, the LeafFromElementLabels object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.