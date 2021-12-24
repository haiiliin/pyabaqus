# Stream object

TheStream object defines a set of streamlines in fluid mechanics.

## Access

```
import visualization
session.streams[name]
```

## Stream(...)



This method creates aStream object and places it in the streams repository.



### Path

```
session.Stream
```

### Required arguments

- *name*

  A string name for the stream.

- *numPointsOnRake*

  An integer specifying the number of points along the rake.

### Optional arguments

- *pointA*

  A tuple of 3 floats specifying the starting point of the rake. Alternatively, a string representation of the node selected in the viewport.

- *pointB*

  A tuple of 3 floats specifying the end point of the rake. Alternatively, a string representation of the node selected in the viewport.

- *path*

  A[Path](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pathpyc.htm?ContextScope=all) object that specifies the rake.

### Return value

A Stream object.

### Exceptions

None.



## Members

The Stream object has no members.