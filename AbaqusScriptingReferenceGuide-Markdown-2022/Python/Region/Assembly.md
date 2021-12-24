# Assembly object

The following commands operate on Assembly objects. For more information about the Assembly object, see [Assembly object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?ContextScope=all).

## Access

```
import regionToolset
```

## clashSets(...)



This command prints a message describing the relationship between the contents of two sets. Possible outcomes are:

- Both sets are the same.
- Set 2 is a subset of set 1.
- Set 2 is a superset of set 1.
- Set 2 intersects set 1.
- Set 2 touches set 1 (their boundaries intersect).
- Set 2 and set 1 are disjoint.

This command accepts only positional arguments and has no keywords.



### Required arguments

- *arg1*

  A Set or Surface object specifying set 1.

- *arg2*

  A Set or Surface object specifying set 2.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## deleteSets(...)



This command deletes the given sets from the assembly.



### Required arguments

- *setNames*

  A sequence of Strings specifying the set names that will be deleted from the assembly.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## markSetInternal(...)



This command marks the given Set as internal or external.



### Required arguments

- *setName*

  A string specifying the Set name.

- *internalSet*

  A Boolean specifying whether the Set should be marked as internal.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## markSurfaceInternal(...)



This command marks the given Surface as internal or external.



### Required arguments

- *setName*

  A string specifying the Surface name.

- *internalSurface*

  A Boolean specifying whether the Surface should be marked as internal.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## isSetInternal(...)



This command returns a flag indicating whether the Set is Internal.



### Required arguments

- *setName*

  A string specifying the Set name.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## isSurfaceInternal(...)



This command returns a flag indicating whether the Surface is Internal.



### Required arguments

- *surfaceName*

  A string specifying the Surface name.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## deleteSurfaces(...)



This command deletes the given surfaces from the assembly.



### Required arguments

- *surfaceNames*

  A sequence of Strings specifying the surface names that will be deleted from the assembly.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.