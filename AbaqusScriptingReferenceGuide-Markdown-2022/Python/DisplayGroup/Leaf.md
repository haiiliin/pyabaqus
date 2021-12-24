# Leaf object

Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which are then used as arguments to [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) commands.

Leaf objects have similarities to Set objects; however, Leaf objects are evaluated when the DisplayGroup expression is evaluated, and they can have SymbolicConstant values (which are also evaluated when the DisplayGroup expression is evaluated).

## Access

```
        import displayGroupMdbToolset
        import displayGroupOdbToolset
      
```

## Leaf(...)



This method creates a Leaf object.



### Path

```
Leaf
```

### Required arguments

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.

### Optional arguments

None.

### Return value

A Leaf object.

### Exceptions

None.



## Members

The Leaf object has members with the same names and descriptions as the arguments to the [Leaf ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all#simaker-leafleafpyc)method.