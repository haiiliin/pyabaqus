# ConstrainedSketchGeometry object

The ConstrainedSketchGeometry object stores the geometry of a sketch, such as lines, circles, arcs, and construction lines.

## Access

```
import sketch
mdb.models[name].sketches[name].geometry[i]
mdb.models[name].sketches[name].geometry[i][i]
```

## Arc3Points(...)



This method constructs an arc using a two endpoints and an intermediate third point on the arc.



### Path

```
mdb.models[name].sketches[name].Arc3Points
```

### Required arguments

- *point1*

  A pair of Floats specifying the first endpoint of the arc.

- *point2*

  A pair of Floats specifying the second endpoint of the arc.

- *point3*

  A pair of Floats specifying the third point on the arc.

### Optional arguments

None.

### Return value

A ConstrainedSketchGeometry object (None if the arc cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## ArcByCenterEnds(...)



This method constructs an arc using a center point and two vertices. The Arc object is added to the geometry repository of the [ConstrainedSketch](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object. The arc is created in a clockwise fashion from *point1* to *point2*.



### Path

```
mdb.models[name].sketches[name].ArcByCenterEnds
```

### Required arguments

- *center*

  A pair of Floats specifying the center point of the arc.

- *point1*

  A pair of Floats specifying the first endpoint of the arc.

- *point2*

  A pair of Floats specifying the second endpoint of the arc.

- *direction*

  A SymbolicConstant specifying the direction of the arc. Possible values are CLOCKWISE and COUNTERCLOCKWISE.

### Optional arguments

None.

### Return value

A ConstrainedSketchGeometry object (None if the arc cannot be created).

### Exceptions

If incompatible data are given, the second endpoint is ignored.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## ArcByStartEndTangent(...)



This method constructs an arc using two vertices. The Arc object is added to the geometry repository of the [ConstrainedSketch](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

```
mdb.models[name].sketches[name].ArcByStartEndTangent
```

### Required arguments

- *point1*

  A pair of Floats specifying the first endpoint of the arc.

- *point2*

  A pair of Floats specifying the second endpoint of the arc.

- *vector*

  A sequence of two Floats specifying the start direction for constructing the arc.

### Optional arguments

None.

### Return value

A ConstrainedSketchGeometry object (None if the arc cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## CircleByCenterPerimeter(...)



This method constructs a circle using a center point and a point on the perimeter. The circle is added to the geometry repository of the [ConstrainedSketch](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

```
mdb.models[name].sketches[name].CircleByCenterPerimeter
```

### Required arguments

- *center*

  A pair of Floats specifying the center point of the circle.

- *point1*

  A pair of Floats specifying a point on the perimeter of the circle.

### Return value

A ConstrainedSketchGeometry object (None if the circle cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## ConstructionCircleByCenterPerimeter(...)



This method constructs a construction circle using a center point and a point on the perimeter. The circle is added to the geometry repository of the [ConstrainedSketch](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

```
mdb.models[name].sketches[name].ConstructionCircleByCenterPerimeter
```

### Required arguments

- *center*

  A pair of Floats specifying the center point of the construction circle.

- *point1*

  A pair of Floats specifying a point on the perimeter of the construction circle.

### Return value

A ConstrainedSketchGeometry object (None if the circle cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## EllipseByCenterPerimeter(...)



This method constructs an ellipse using a center point, a major axis point, and a minor axis point. The ellipse is added to the geometry repository of the [ConstrainedSketch](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

```
mdb.models[name].sketches[name].EllipseByCenterPerimeter
```

### Required arguments

- *center*

  A pair of Floats specifying the center point of the ellipse.

- *axisPoint1*

  A pair of Floats specifying the major or minor axis point of the ellipse.

- *axisPoint2*

  A pair of Floats specifying the minor or major axis point of the ellipse.

### Optional arguments

None.

### Return value

A ConstrainedSketchGeometry object (None if the ellipse cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## FilletByRadius(...)



This method constructs a fillet arc of a given radius between two curves. The fillet is added to the geometry repository of the [ConstrainedSketch](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

```
mdb.models[name].sketches[name].FilletByRadius
```

### Required arguments

- *radius*

  A Float specifying the radius of the fillet arc. Possible values are Floats > 0.

- *curve1*

  A ConstrainedSketchGeometry object specifying the first curve.

- *nearPoint1*

  A pair of Floats specifying a point on the sketch near where the user wishes the fillet to intersect with *curve1*. This point does not need to be on*curve1*; it is used as a hint to draw the fillet.

- *curve2*

  A ConstrainedSketchGeometry object specifying the second curve.

- *nearPoint2*

  A pair of Floats specifying a point on the sketch near where the user wishes the fillet to intersect with *curve2*. This point does not need to be on *curve2*; it is used as a hint to draw the fillet.

### Optional arguments

None.

### Return value

A ConstrainedSketchGeometry object (None if the fillet cannot be created).

### Exceptions

- If the radius given cannot be used to create a fillet between the two curves given:

  Range Error: cannot construct the Fillet specified

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Line(...)



This method creates a line between two given points.



### Path

```
mdb.models[name].sketches[name].Line
```

### Required arguments

- *point1*

  A pair of Floats specifying the first endpoint.

- *point2*

  A pair of Floats specifying the second endpoint.

### Optional arguments

None.

### Return value

A ConstrainedSketchGeometry object (None if the line cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## ConstructionLine(...)



This method creates an oblique construction line that runs between two given points.



### Path

```
mdb.models[name].sketches[name].ConstructionLine
```

### Required arguments

- *point1*

  A pair of Floats specifying the first endpoint.

- *point2*

  A pair of Floats specifying the second endpoint.

### Optional arguments

None.

### Return value

A ConstrainedSketchGeometry object (None if the line cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Spline(...)



This method creates a spline curve running through a sequence of points.



### Path

```
mdb.models[name].sketches[name].Spline
```

### Required arguments

- *points*

  A sequence of pairs of Floats specifying the points through which the spline passes.

### Optional arguments

- *constrainPoints*

  A Boolean that determines whether the points given are to constrained to always remain on the Spline. The default is True. For a large sequence of *points*, significant performance gains may be achieved by setting the value to False.

### Return value

A ConstrainedSketchGeometry object (None if the spline cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Spot(...)



This method creates a spot construction point located at the specified coordinates. The spot is added to the vertex repository of the [ConstrainedSketch](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

```
mdb.models[name].sketches[name].Spot
```

### Required arguments

- *point*

  A pair of Floats specifying the coordinates of the spot construction point.

### Optional arguments

None.

### Return value

A ConstrainedSketchGeometry object (None if the spot cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getVertices()



This method returns an list of [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects which are a part of the given ConstrainedSketchGeometry object.



### Arguments

None.

### Return value

A list of [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getSize()



This method returns the length of the given ConstrainedSketchGeometry object.



### Arguments

None.

### Return value

The length of the given ConstrainedSketchGeometry.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getPointAtDistance(...)



This method returns a point offset along the given ConstrainedSketchGeometry from the given end by a specified arc length distance or a percentage of the total length of the ConstrainedSketchGeometry object.



### Required arguments

- *point*

  A pair of Floats specifying the point from which the distance is to be measured.

- *distance*

  A float specifying the arc length distance along the ConstrainedSketchGeometry from the *point* at which the required point is situated.

### Optional arguments

- *percentage*

  A Boolean that specifies if the *distance* is an absolute distance or is a fraction relative to the length of the ConstrainedSketchGeometry object.

### Return value

A pair of floats representing the point along the edge.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The ConstrainedSketchGeometry object has the following members:

- *id*

  An Int specifying the index of the sketch entity in the ConstrainedSketchGeometryArray.

- *curveType*

  A SymbolicConstant specifying the geometry of the sketch entity. Possible values are ARC, CIRCLE, ELLIPSE, LINE, and SPLINE.

- *type*

  A SymbolicConstant specifying the type of sketch entity. Possible values are REGULAR, REFERENCE, and CONSTRUCTION.

- *pointOn*

  A tuple of Floats specifying the *X*- and*Y*-coordinates of a point located on the geometry.