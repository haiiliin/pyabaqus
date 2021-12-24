# Path object

The Path object defines a line through your model by specifying a series of nodes or points.

## Access

```
import visualization
session.paths[name]
```

## Path(...)



This method creates a Path object.



### Path

```
session.Path
```

### Required arguments

- *name*

  A String specifying the repository key.

- *type*

  A SymbolicConstant specifying the type of path being created. Possible values are NODE_LIST, POINT_LIST, EDGE_LIST, CIRCUMFERENTIAL, and RADIAL.

- *expression*

  A sequence specifying the nodes or points that make up the path. The definition of the path expression depends on the *type* argument.

  - If *type*=NODE_LIST, *expression* must be a sequence of sequences. Each inner sequence contains two items, the first item is a String specifying the name of a part instance, and the second item can be either a sequence of Ints or a sequence of Strings, each specifying a range of Ints.
  - If *type*=POINT_LIST, *expression* must be a sequence of tuples of three Floats, specifying the coordinates of each point.
  - If *type*=EDGE_LIST, *expression* must be a sequence of sequences. Each inner sequence contains two items, the first item is a String specifying the name of the part instance, and the second item is a sequence of tuples of four Ints that uniquely identify an element edge. The four Ints are:
    1. The element label.
    2. The element face index (one-based).
    3. The face edge index (one-based).
    4. The edge direction. A positive number specifies that the edge direction runs from the edge start node to the edge end node. A negative number specifies the opposite.
  - When *type*=CIRCUMFERENTIAL or RADIAL, *expression* must be a sequence of three tuples of three Floats, specifying the coordinates of the points used to define a coordinate system.

- *circleDefinition*

  A SymbolicConstant specifying the method in which the circle is being defined. This argument is valid only when *type*=CIRCUMFERENTIAL or RADIAL. Possible values are ORIGIN_AXIS and POINT_ARC.When the value is ORIGIN_AXIS, the first two points in *expression* are points on the rotational axis and the third point lies on the x-axis. When the value is POINT_ARC, the three points in *expression* are points lying on the arc of the circle.

- *numSegments*

  An Int specifying the number of equal segments in the path. This argument is valid only when *type*=CIRCUMFERENTIAL or RADIAL.

- *startAngle*

  A Float specifying the start angle of the circumferential path. This argument is valid only when *type*=CIRCUMFERENTIAL.

- *endAngle*

  A Float specifying the end angle of the circumferential path. This argument is valid only when *type*=CIRCUMFERENTIAL.

- *radius*

  The SymbolicConstant CIRCLE_RADIUS or a Float specifying the radius of the circumferential path. This argument is valid only when *type*=CIRCUMFERENTIAL.

- *radialAngle*

  A Float specifying the angle between the radial path and the *X*-axis of the specified coordinate system. This argument is valid only when *type*=RADIAL.

- *startRadius*

  The SymbolicConstant CIRCLE_RADIUS or a Float specifying the start radius of the radial path. This argument is valid only when *type*=RADIAL.

- *endRadius*

  The SymbolicConstant CIRCLE_RADIUS or a Float specifying the end radius of the radial path. This argument is valid only when *type*=RADIAL.

### Optional arguments

None.

### Return value

A Path object.

### Exceptions

ModelError, ErrorUnsupportedNodeData, ErrorUnsupportedPointData, ErrorIncorrectPathData, KeyError, ErrorEmptyPathName, ErrorPathNotFound, and ErrorNoOdbPathDisplay.

ValueError: When *type*=CIRCUMFERENTIAL or RADIAL, the three points specified in *expression* are collinear.



## Members

The Path object has members with the same names and descriptions as the arguments to the [Path ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pathpyc.htm?ContextScope=all#simaker-pathpathpyc)method.

In addition, the Path object can have the following member:

- *coordinates*

  If *type*=NODE_LIST, *coordinates* is a sequence of tuples of three Floats. This can be used as the value for the *expression* argument when creating a Path object of *type* = POINT_LIST.