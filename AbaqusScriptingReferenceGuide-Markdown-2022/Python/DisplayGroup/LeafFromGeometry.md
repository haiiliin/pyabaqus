# LeafFromGeometry object

The LeafFromGeometry object can be used whenever a [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object is expected as an argument. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are used to specify the items in a display group. [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

The LeafFromGeometry object is derived from the [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object.

## Access

```
import displayGroupMdbToolset
```

## LeafFromGeometry(...)



This method creates a Leaf object from a sequence of edge, face and cell geometry objects. Any combination of edge, face or cell arguments is allowed however the arguments must specify at least one object--it is not permissible to create an empty leaf.



### Path

```
LeafFromGeometry
```

### Required arguments

None.

### Optional arguments

- *edgeSeq*

  A sequence of geometry edges.

- *faceSeq*

  A sequence of geometry faces.

- *cellSeq*

  A sequence of geometry cells.

### Return value

A LeafFromGeometry object.

### Exceptions

- If at least one of the sequences is not passed to this method:

  Cannot define empty leaf.



## Members

The LeafFromGeometry object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.