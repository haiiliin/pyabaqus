# InterestingPoint object

Interesting points can be located at the following:

- The middle of an edge.
- The middle of an arc.
- The center of an arc.

An InterestingPoint object is a temporary object and cannot be accessed from the [Mdb](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?ContextScope=all) object.

## Access

```
import part
import assembly
```

## InterestingPoint(...)



This method creates an interesting point along an edge. An InterestingPoint is a temporary object.



### Path

mdb.models[*name*].parts[*name*].InterestingPoint

mdb.models[*name*].rootAssembly.instances[*name*].InterestingPoint

### Required arguments

- *edge*

  An Edge object specifying the edge on which the interesting point is positioned.

- *rule*

  A SymbolicConstant specifying the position of the interesting point. Possible values are MIDDLE or CENTER.

### Optional arguments

None.

### Return value

An InterestingPoint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The InterestingPoint object has no members.