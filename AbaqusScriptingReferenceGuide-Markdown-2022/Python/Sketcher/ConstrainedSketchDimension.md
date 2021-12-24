# ConstrainedSketchDimension object

The ConstrainedSketchDimension object stores the dimensions associated with a sketch.

## Access

```
import sketch
mdb.models[name].sketches[name].dimensions[i]
```

## AngularDimension(...)



This method constructs a ConstrainedSketchDimension object between two [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects, with the given angle between them.



### Path

```
mdb.models[name].sketches[name].AngularDimension
```

### Required arguments

- *line1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the first line.

- *line2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the second line.

- *textPoint*

  A pair of Floats specifying the location of the dimension text.

### Optional arguments

- *value*

  A Float specifying the angle between the two lines.

- *reference*

  A Boolean specifying whether the created dimension enforces the above value or if it simply measures the angle between two lines.

### Return value

A ConstrainedSketchDimension object (None if the dimension cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## HorizontalDimension(...)



This method constructs a ConstrainedSketchDimension object between two vertices. A horizontal dimension indicates the horizontal distance along the *X*-axis between two vertices.



### Path

```
mdb.models[name].sketches[name].HorizontalDimension
```

### Required arguments

- *vertex1*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object specifying the first endpoint.

- *vertex2*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object specifying the second endpoint.

- *textPoint*

  A pair of Floats specifying the location of the dimension text.

### Optional arguments

- *value*

  A Float distance between the two vertices.

- *reference*

  A Boolean specifying whether the created dimension enforces the above value or if it simply measures the distance between the two vertices.

### Return value

A ConstrainedSketchDimension object (None if the dimension cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## ObliqueDimension(...)



This method constructs a ConstrainedSketchDimension object between two vertices. An oblique dimension indicates the distance between two vertices.



### Path

```
mdb.models[name].sketches[name].ObliqueDimension
```

### Required arguments

- *vertex1*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object specifying the first endpoint.

- *vertex2*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object specifying the second endpoint.

- *textPoint*

  A pair of Floats specifying the location of the dimension text.

### Optional arguments

- *value*

  A Float specifying the distance between the two [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects.

- *reference*

  A Boolean specifying whether the created dimension enforces the above value or if it simply measures the distance between the two vertices.

### Return value

A ConstrainedSketchDimension object (None if the dimension cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## RadialDimension(...)



This method constructs a ConstrainedSketchDimension object on a circular or elliptical arc. A radial dimension indicates the radius of an arc or circle or the major or minor radius of an ellipse.



### Path

```
mdb.models[name].sketches[name].RadialDimension
```

### Required arguments

- *curve*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the circular or elliptical arc.

- *textPoint*

  A pair of Floats specifying the location of the dimension text.

### Optional arguments

- *value*

  A Float specifying the radius of the arc, circle or ellipse.

- *reference*

  A Boolean specifying whether the created dimension enforces the above value or if it simply measures the angle between two lines.

- *majorRadius*

  A Float specifying the major Radius if *curve* is an ellipse. This is mutually exclusive with *value* and *minorRadius*.

- *minorRadius*

  A Float specifying the minor Radius if *curve* is an ellipse. This is mutually exclusive with *value* and *majorRadius*.

### Return value

A ConstrainedSketchDimension object (None if the dimension cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## VerticalDimension(...)



This method constructs a ConstrainedSketchDimension between two vertices. A vertical dimension controls the vertical distance along the *Y*-axis between two vertices.



### Path

```
mdb.models[name].sketches[name].VerticalDimension
```

### Required arguments

- *vertex1*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object specifying the first endpoint.

- *vertex2*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object specifying the second endpoint.

- *textPoint*

  A pair of Floats specifying the location of the dimension text.

### Optional arguments

- *value*

  A Float specifying the angle between the two lines.

- *reference*

  A Boolean specifying whether the created dimension enforces the above value or if it simply measures the angle between two lines.

### Return value

A ConstrainedSketchDimension object (None if the dimension cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## DistanceDimension(...)



This method constructs a ConstrainedSketchDimension object between two [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all), or a[ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) and [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object. A distance dimension specifies the shortest distance between two entities.



### Path

```
mdb.models[name].sketches[name].DistanceDimension
```

### Required arguments

- *entity1*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object or [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object.

- *entity2*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object or [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object.

- *textPoint*

  A pair of Floats specifying the location of the dimension text.

### Optional arguments

- *value*

  A Float specifying the angle between the two lines.

- *reference*

  A Boolean specifying whether the created dimension enforces the above value or if it simply measures the angle between two lines.

### Return value

A ConstrainedSketchDimension object (None if the dimension cannot be created).

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The ConstrainedSketchDimension object has no members.