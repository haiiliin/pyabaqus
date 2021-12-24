# ConstrainedSketchConstraint object

The ConstrainedSketchConstraint object stores the constraints associated with a sketch.

## Access

```
import sketch
mdb.models[name].sketches[name].constraints[i]
```

## CoincidentConstraint(...)



This method creates a coincident constraint. This constraint applies to two vertices, to a vertex and a [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object, or to two [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects of the same type and constrains them to be coincident.



### Path

```
mdb.models[name].sketches[name].CoincidentConstraint
```

### Required arguments

- *entity1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object or a [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifying the first object.

- *entity2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object or a [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifying the second object.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## ConcentricConstraint(...)



This method creates a concentric constraint. This constraint applies to any combination of circles, arcs, ellipses, and points and constrains them to be concentric. A concentric constraint implies that the center of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects coincide.



### Path

```
mdb.models[name].sketches[name].ConcentricConstraint
```

### Required arguments

- *entity1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the first arc, circle, ellipse, or sketch vertex.

- *entity2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the second arc, circle, ellipse, or sketch vertex.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## EqualLengthConstraint(...)



This method creates an equal length constraint. This constraint applies to lines and constrains them such that their lengths are equal.



### Path

```
mdb.models[name].sketches[name].EqualLengthConstraint
```

### Required arguments

- *entity1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the first line.

- *entity2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the second line.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## EqualRadiusConstraint(...)



This method creates an equal radius constraint. This constraint applies to circles and arcs and constrains them such that their radii are equal.



### Path

```
mdb.models[name].sketches[name].EqualRadiusConstraint
```

### Required arguments

- *entity1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the first arc or circle.

- *entity2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) specifying the second arc or circle.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## FixedConstraint(...)



This method creates a fixed constraint. This constraint applies to a [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object or a [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object and constrains them to be fixed in space. Both the location and the shape of the sketch geometry is fixed.



### Path

```
mdb.models[name].sketches[name].FixedConstraint
```

### Required arguments

- *entity*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object or a [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifying the item to fix in space.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## HorizontalConstraint(...)



This method creates a horizontal constraint. This constraint applies to a line and constrains it to be horizontal.



### Path

```
mdb.models[name].sketches[name].HorizontalConstraint
```

### Required arguments

- *entity*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the line to constrain.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## VerticalConstraint(...)



This method creates a vertical constraint. This constraint applies to a line and constrains it to be vertical.



### Path

```
mdb.models[name].sketches[name].VerticalConstraint
```

### Required arguments

- *entity*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the line to constrain.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## ParallelConstraint(...)



This method creates a parallel constraint. This constraint applies to lines and constrains them to be parallel.



### Path

```
mdb.models[name].sketches[name].ParallelConstraint
```

### Required arguments

- *entity1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the first line.

- *entity2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the second line.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## PerpendicularConstraint(...)



This method creates a perpendicular constraint. This constraint applies to different types of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects and constrains them to be perpendicular to each other.



### Path

```
mdb.models[name].sketches[name].PerpendicularConstraint
```

### Required arguments

- *entity1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the first object.

- *entity2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the second object.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## EqualDistanceConstraint(...)



This method creates an equal distance constraint. This constraint can be applied between a midpoint [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object and any other two [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects or between a midpoint [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object and two [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects that are lines. The equal distance constraint forces the midpoint vertex to remain at an equal distance from the two other vertices or lines.



### Path

```
mdb.models[name].sketches[name].EqualDistanceConstraint
```

### Required arguments

- *entity1*

  A[ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the first line or [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object.

- *entity2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the second line or [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object.

- *midpoint*

  A [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifying the vertex that will be positioned an equal distance from *entity1* and *entity2*.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## TangentConstraint(...)



This method creates a tangent constraint. This constraint applies to different types of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects and constrains them to remain tangential.



### Path

```
mdb.models[name].sketches[name].TangentConstraint
```

### Required arguments

- *entity1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the first object.

- *entity2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the second object.

### Optional arguments

None.

### Return value

A ConstrainedSketchConstraint object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The ConstrainedSketchConstraint object has no members.