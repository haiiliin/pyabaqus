# ConstrainedSketch object

A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include [ConstrainedSketchGeometry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects contained in the Geometry Repository, such as Line, Arc, and Spline. Vertex, Dimension, Constraint, and Parameter objects are contained in their respective repositories.

## Access

```
import sketch
mdb.models[name].sketches[name]
```

## ConstrainedSketch(...)



This method creates a ConstrainedSketch object. If the sketch cannot be created, the method returns None.



### Path

```
mdb.models[name].ConstrainedSketch
```

### Required arguments

- *name*

  A String specifying the repository key.

- *sheetSize*

  A Float specifying the sheet size.

### Optional arguments

- *gridSpacing*

  A Float specifying the spacing between gridlines. Possible values are Floats >> 0. The default value is approximately 2 percent of *sheetSize*.

- *transform*

  A sequence of sequences of Floats specifying the three-dimensional orientation of the sketch. The sequence is a 3 × 4 transformation matrix specifying the axis of rotation and the translation vector. Possible values are any Floats.The default value for the axis of rotation is the identity matrix`(1.0, 0.0, 0.0),  (0.0, 1.0, 0.0),  (0.0, 0.0, 1.0)`The default value for the translation vector is`(0.0, 0.0, 0.0)`The default values position the sketch on the *X–Y* plane centered at the origin.

### Return value

A ConstrainedSketch object.

### Exceptions

None.

## ConstrainedSketch(...)



This method copies one ConstrainedSketch object to a new ConstrainedSketch object. Note: If the name of the sketch to be copied to is __edit__, Abaqus creates an exact copy that contains both reference geometry and a non-identity transform matrix. Otherwise, the Sketch copy constructor strips the reference geometry from the copied sketch and sets the transform matrix to identity, creating a standalone copy.







### Path

```
mdb.models[name].ConstrainedSketch
```

### Required arguments

- *name*

  A String specifying the repository key.

- *objectToCopy*

  A ConstrainedSketch object to be copied.

### Optional arguments

None.

### Return value

A ConstrainedSketch object.

### Exceptions

InvalidNameError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## ConstrainedSketchFromGeometryFile(...)



This method creates a ConstrainedSketch object and places it in the sketches repository.



### Path

```
mdb.models[name].ConstrainedSketchFromGeometryFile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *geometryFile*

  An [AcisFile](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object specifying a file containing geometry. The geometry in the file is converted to two-dimensional sketch geometry in the *X–Y* plane.

### Optional arguments

None.

### Return value

A ConstrainedSketch object.

### Exceptions

InvalidNameError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## print()



This method prints the following statistics about a sketch:

- The sketch Id (a positive integer).
- The number of geometry curves (the number of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects).
- The number of dimensions (the number of [ConstrainedSketchDimension](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchdimensionpyc.htm?ContextScope=all) objects).
- The number of vertices (the number of [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects).



### Arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## assignCenterline(...)



This method indicates the construction line that will be used as a centerline for revolved features.



### Required arguments

- *line*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying a construction line that indicates the centerline of revolved features.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## assignCenterOfTwist(...)



This method indicates the isolated point that will be used as the center of twist when an extruded feature is created with twist.



### Required arguments

- *point*

  A [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object specifying an isolated point that indicates the center of twist for extruded features that use a twist angle.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## autoDimension(...)



This method applies dimensions to the selected [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects in an effort to make the ConstrainedSketch well defined.



### Required arguments

- *objectList*

  A sequence specifying the [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects to dimension.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## autoTrimCurve(...)



This method automatically trims a selected [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object at the specified location. If the object does not intersect other [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects, the entire selected object will be deleted.



### Required arguments

- *curve1*

  The [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object to be trimmed.

- *point1*

  A pair of Floats specifying the location on [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) where the trimming should be applied. *point1* and *parameter1* are mutually exclusive.

- *parameter1*

  A Float specifying the parameter location on the [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) where the trimming should be applied. *point1* and *parameter1* are mutually exclusive.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## breakCurve(...)



This method breaks a specified [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object (*curve1*) using another specified [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object (*curve2*). If the selected [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects intersect, then only *curve1* will be broken; *curve2* is not affected by the operation. The location for the break is determined by the specified point values.



### Required arguments

- *curve1*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the object to be broken.

- *point1*

  A pair of Floats specifying the location on *curve1* near where the break should be applied.

- *curve2*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying where *curve1* should be broken.

- *point2*

  A pair of Floats specifying the location on *curve2* near where *curve1* should be broken.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## copyMirror(...)



This method creates copies of the given [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects, mirrors them about a selected line, and inserts them into the appropriate repositories of the ConstrainedSketch object.



### Required arguments

- *mirrorLine*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the line about which Abaqus will mirror the sketch.

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects specifying the sketch to be copied and mirrored.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## copyMove(...)



This method creates copies of the given [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects, moves them from their original position, and inserts them into the appropriate repositories of the ConstrainedSketch object.



### Required arguments

- *vector*

  A sequence of two Floats specifying the translation vector.

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects to be copied and moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## copyRotate(...)



This method creates copies of the given [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects, rotates them, and inserts them into the appropriate repositories of the ConstrainedSketch object.



### Required arguments

- *centerPoint*

  A pair of Floats specifying the center of rotation.

- *angle*

  A Float specifying the angle of rotation in degrees.

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects to be copied and moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## copyScale(...)



This method creates copies of the given [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects, scales them by the specified value about a selected point, and inserts them into the appropriate repositories of the ConstrainedSketch object.



### Required arguments

- *scaleValue*

  A Float specifying the value for scaling.

- *scaleCenter*

  A pair of Floats specifying the center of scaling.

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects to be copied and scaled.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## delete(...)



This method deletes the given [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all), [ConstrainedSketchDimension](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchdimensionpyc.htm?ContextScope=all), or [ConstrainedSketchConstraint](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchconstraintpyc.htm?ContextScope=all) objects.



### Required arguments

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all), [ConstrainedSketchDimension](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchdimensionpyc.htm?ContextScope=all), or [ConstrainedSketchConstraint](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchconstraintpyc.htm?ContextScope=all) objects to be deleted.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## deleteParameter(...)



The command deletes a specified parameter.



### Required arguments

- *name*

  A String specifying the name of the parameter to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## dragEntity(...)



This method drags a specified [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) or [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object to a specific location.



### Required arguments

- *entity*

  A [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) or [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object specifying the object to drag.

- *points*

  A sequence of sequences of three Floats specifying a sequence of points along which to drag the entity. The order of points in the sequence defines a path that determines the solution.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## linearPattern(...)



This method copies [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects in a linear pattern along one or two directions. This method also copies any associated dimension or constraint objects that exist between the given objects.



### Required arguments

- *number1*

  An Integer specifying the total number of copies, including the original objects, that appear along the first direction in the pattern. Possible values are 1 ≤≤ *number1* ≤≤ 1000.

- *spacing1*

  A Float specifying the spacing between copies along the first direction in the pattern. Possible values are 0.0 ≤≤ *spacing1* .

- *angle1*

  A Float specifying the angle in degrees of the first direction in the pattern. Possible values are –360.0 ≤≤ *angle1* ≤≤ 360.0.

### Optional arguments

- *vertexList*

  A sequence of [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects to copy.

- *geomList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects to copy.

- *number2*

  An integer specifying the total number of copies, including the original objects, that appear along the second direction in the pattern. Possible values are 1 ≤≤ *number2* ≤≤ 1000. The default value is 1. The value of either *number1* or *number2* must be greater than one.

- *spacing2*

  A Float specifying the spacing between copies along the first direction in the pattern. Possible values are 0.0 ≤≤ *spacing2*. The default value is *spacing1*.

- *angle2*

  A Float specifying the angle in degrees of the first direction in the pattern. Possible values are –360.0 ≤≤ *angle2* ≤≤ 360.0. The default value is 90° beyond the value of *angle1*.

### Return value

None.

### Exceptions

- AbaqusException

  Number must be greater than 1 for at least one direction

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## mergeVertices(...)



This method merges the [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects that lie within the specified distance of each other. If only one [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object is selected, it will merge all [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects that lie within the specified distance of that vertex. If more than one vertex is selected, the search will be restricted to only the selected [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects.



### Required arguments

- *value*

  A Float specifying the search radius.

- *vertexList*

  A sequence of [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects to be merged.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## move(...)



This method translates the given [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects by the given vector.



### Required arguments

- *vector*

  A sequence of two Floats specifying the translation vector.

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects specifying the objects to be translated.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## offset(...)



This method creates copies of the selected [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects, offsets them by the specified distance in the specified direction, and inserts them into the ConstrainedSketch object's appropriate repositories. If connected objects are selected, trim or extend is carried out to complete the offset.



### Required arguments

- *distance*

  A Float specifying the distance to be offset.

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects to be copied and offset.

- *side*

  A SymbolicConstant specifying which side the offset should occur. Possible values are LEFT and RIGHT.

### Optional arguments

- *filletCorners*

  A Boolean specifying whether the corners need to be rounded instead of being extended.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## radialPattern(...)



This method copies [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects in a radial pattern about a specified center point.



### Required arguments

- *number*

  An Int specifying the total number of copies, including the original objects, that appear in the radial pattern. Possible values are 2 ≤≤ *number2* ≤≤ 1000.

- *totalAngle*

  A Float specifying the total angle in degrees between the first and last instance in the pattern. A positive angle corresponds to a counter-clockwise direction. The values 360° and -360° represent a special case where the pattern makes a full circle. In this case, because the copy would overlay the original, the copy is not placed at the last position. Possible values are –360.0 ≤≤ *totalAngle* ≤≤ 360.0.

- *centerPoint*

  A pair of Floats specifying the center of the radial pattern.

### Optional arguments

- *vertexList*

  A sequence of [ConstrainedSketchVertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects to copy.

- *geomList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects to copy.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## resetView()



This method resets the view to be perpendicular to the sketching plane.



### Arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## rectangle(...)



This method creates four lines that form a rectangle with diagonal corners defined by the given points and inserts them into the geometry repository of the ConstrainedSketch object.



### Required arguments

- *point1*

  A pair of Floats specifying the first corner of the rectangle.

- *point2*

  A pair of Floats specifying the second corner of the rectangle.

### Optional arguments

None.

### Return value

An Int specifying the success or failure of the method. A value of 0 indicates failure.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## removeGapsAndOverlaps(...)



This method removes gaps and overlaps between sketch geometries specified by the user. This method is particularly useful when cleaning up imported sketches



### Required arguments

- *tolerance*

  A float value which specifies the largest size of the gap or overlap between entities that is to be removed. Typically this value is small and is used to close gaps and overlaps which may not exist in the originating program but exist in the sketch because of mismatched tolerances between the two programs.

- *geomList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects where the gaps and overlaps are to be removed.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## repairShortEdges(...)



This method deletes the short edges specified, optionally selecting only those short edges whose lengths are smaller than the specified tolerance and healing the resultant gap in the sketch. This method is particularly useful in conjunction with removeGapsAndOverlap when cleaning up imported sketches.



### Required arguments

- *geomList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects where the short edges are to be removed.

### Optional arguments

- *tolerance*

  A float value that is used to select and delete only those edges specified in *geomList* whose lengths are smaller than the given value. The default value is –1.0. This value implies that all edges specified in *geomList* will be removed and the sketch healed to remove gaps left by their removal.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## retrieveSketch(...)



This method copies all [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all), [ConstrainedSketchDimension](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchdimensionpyc.htm?ContextScope=all), [ConstrainedSketchConstraint](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchconstraintpyc.htm?ContextScope=all), and [ConstrainedSketchParameter](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchparameterpyc.htm?ContextScope=all) objects from the specified ConstrainedSketch object. The new objects are added to the existing objects (if any). The objects in the specified ConstrainedSketch object are not modified by the retrieve operation.



### Required arguments

- *sketch*

  A ConstrainedSketch object specifying the object from which to copy.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## rotate(...)



This method rotates the given [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects by the given angle and about the given point.



### Required arguments

- *centerPoint*

  A pair of Floats specifying the center of rotation.

- *angle*

  A Float specifying the angle of rotation in degrees.

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) specifying the objects to be rotated.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## scale(...)



This method scales the given [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects by the given scale factor and about the given point.



### Required arguments

- *scaleValue*

  A Float specifying the value of scale.

- *scaleCenter*

  A pair of Floats specifying the center of scale.

- *objectList*

  A sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects specifying the objects to be scaled.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setPrimaryObject(...)



This method makes the ConstrainedSketch object the primary object in the current viewport. The sketch remains the primary object in the current viewport until an unsetPrimaryobject command is issued.



### Required arguments

- *option*

  A SymbolicConstant specifying how the sketch is displayed. Possible values are:STANDALONE: Indicates a new stand-alone sketch. The current viewport is cleared and is replaced by the stand-alone sketch. The view direction is set to −ZZ.SUPERIMPOSE: Indicates that the sketch is superimposed on the current viewport. The view direction is changed to be perpendicular to the sketch plane. The change is effected smoothly as an animated sequence of many small viewing steps.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## trimExtendCurve(...)



This method trims or extends a specified [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object (*curve1*) using another specified [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object (*curve2*). *curve2* is not affected by the operation. The location for the trim or extend is determined by the specified point values.



### Required arguments

- *curve1*

  The [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the object to be trimmed or extended.

- *point1*

  A pair of Floats specifying the location on *curve1* where trim or extend should be applied.

- *curve2*

  The [ConstrainedSketchGeometry](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the object to which *curve1* is trimmed or extended. *curve2* is not trimmed or extended.

- *point2*

  A pair of Floats specifying the location on *curve2* near where *curve1* should be trimmed or extended.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## undo()



This method undoes the effects of the last ConstrainedSketch object method.



### Arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## unsetPrimaryObject()



This method removes the ConstrainedSketch object from the current viewport, reversing the effects of the setPrimaryobject command. If the *option* argument was set to SUPERIMPOSE, the viewport will be returned to the view orientation that was in place when the setPrimaryobject command was issued. If the *option* argument was set to STANDALONE, the viewport will be left empty.



### Arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## writeAcisFile(...)



This method exports the geometry of the sketch to a named file in ACIS format.



### Required arguments

- *fileName*

  A String specifying the file name.

### Optional arguments

- *version*

  A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS Version 12.0. The default value is the current version of ACIS.

### Return value

None.

### Exceptions

InvalidNameError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## writeIgesFile(...)



This method exports the geometry of the sketch to a named file in IGES format.



### Required arguments

- *filename*

  A String specifying the file name.

### Optional arguments

- *flavor*

  A SymbolicConstant specifying a particular flavor of IGES to export. Possible values areSTANDARD, AUTOCAD, SOLIDWORKS, JAMA, and MSBO.

### Return value

None.

### Exceptions

InvalidNameError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The ConstrainedSketch object can have the following members:

- *constraints*

  A repository of [ConstrainedSketchConstraint](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchconstraintpyc.htm?ContextScope=all) objects.

- *dimensions*

  A repository of [ConstrainedSketchDimension](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchdimensionpyc.htm?ContextScope=all) objects.

- *geometry*

  A [ConstrainedSketchGeometryArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object specifying the sketch geometry, such as lines, arcs, circles, and splines.

- *parameters*

  A repository of [ConstrainedSketchParameter](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchparameterpyc.htm?ContextScope=all) objects specifying sketch parameters, which may be associated with dimensions.

- *sketchOptions*

  A [ConstrainedSketchOptions](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchoptionspyc.htm?ContextScope=all) object specifying the sketch option settings.

- *vertices*

  A [ConstrainedSketchVertexArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object.

- *imageOptions*

  A [ConstrainedSketchImageOptions](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchimageoptionspyc.htm?ContextScope=all) object.