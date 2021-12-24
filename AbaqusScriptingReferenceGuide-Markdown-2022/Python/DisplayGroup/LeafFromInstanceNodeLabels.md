# LeafFromInstanceNodeLabels object

The LeafFromInstanceNodeLabels object can be used whenever a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object is expected as an argument. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are used to specify the items in a display group. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

The LeafFromInstanceNodeLabels object is derived from the [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object.

## Access

```
import displayGroupMdbToolset
```

## LeafFromInstanceNodeLabels(...)



This method creates a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object from a sequence of Strings specifying the node labels. Leaf objects specify the items in a display group.



### Path

```
LeafFromInstanceNodeLabels
```

### Required arguments

- *nodeLabels*

  A sequence of sequences specifying node labels. Each inner sequence consists of a [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object followed by a sequence of Strings specifying node labels.

### Optional arguments

None.

### Return value

A LeafFromInstanceNodeLabels object.

### Exceptions

None.



## Members

The LeafFromInstanceNodeLabels object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.