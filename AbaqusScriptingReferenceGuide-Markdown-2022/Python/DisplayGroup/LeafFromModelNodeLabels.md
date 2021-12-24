# LeafFromModelNodeLabels object

The LeafFromModelNodeLabels object can be used whenever a Leaf object is expected as an argument. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are used to specify the items in a display group. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

The LeafFromModelNodeLabels object is derived from the [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object.

## Access

```
import displayGroupOdbToolset
```

## LeafFromModelNodeLabels(...)



This method creates a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object from a sequence of node labels spanning several part instances.



### Path

```
LeafFromModelNodeLabels
```

### Required arguments

- *nodeLabels*

  A sequence of Strings specifying expressions that denote node labels per part instance in the model. Each part instance node expression is a sequence of a String specifying the part instance name and a sequence of node expressions; for example, `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions can be any of the following:An Int specifying a single node label; for example, `1`.A String specifying a single node label; for example, `'7'`.A String specifying a sequence of node labels; for example, `'3:5'` and `'3:15:3'`.

### Optional arguments

None.

### Return value

A LeafFromModelNodeLabels object.

### Exceptions

None.



## Members

The LeafFromModelNodeLabels object has members with the same names and descriptions as the arguments to the [LeafFromModelNodeLabels ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leaffrommodelnodelabelspyc.htm?ContextScope=all#simaker-leaffrommodelnodelabelsleaffrommodelnodelabelspyc)method.

In addition, the LeafFromModelNodeLabels object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.