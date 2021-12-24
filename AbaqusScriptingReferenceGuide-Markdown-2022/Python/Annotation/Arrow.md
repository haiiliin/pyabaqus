# Arrow object

The Arrow object stores the visual settings and location of an arrow annotation.

The Arrow object is derived from the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object.

## Access

```
import annotationToolset
mdb.annotations[name]
session.odbs[name].userData.annotations[name]
session.viewports[name].annotationsToPlot[i]
```

## Arrow(...)



This method creates an Arrow object.



### Path

mdb.Arrow

session.odbs[*name*].userData.Arrow

### Required arguments

- *name*

  A String specifying the annotation repository key.

### Optional arguments

- *startPoint*

  A pair of Floats specifying the start point *X*- and *Y*-offsets in millimeters from *startAnchor*. The default value is (0, 0).

- *endPoint*

  A pair of Floats specifying the end point *X*- and *Y*-offsets in millimeters from *endAnchor*. The default value is (0, 0).

- *startAnchor*

  A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats specifies the *X*- and *Y*-coordinates as percentages of the viewport width and height. A sequence of three Floats specifies the *X*-, *Y*-, and *Z*-coordinates of a point in the model coordinate system. A SymbolicConstant indicates a relative position. Possible values are:BOTTOM_LEFTBOTTOM_CENTERBOTTOM_RIGHTCENTER_LEFTCENTERCENTER_RIGHTTOP_LEFTTOP_CENTERTOP_RIGHTThe default value is BOTTOM_LEFT.

- *endAnchor*

  A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats specifies the *X*- and *Y*-coordinates as percentages of the viewport width and height. A Sequence of three Floats specifies the *X*-, *Y*-, and *Z*-coordinates of a point in the model coordinate system. A SymbolicConstant indicates a relative position. Possible values are:BOTTOM_LEFTBOTTOM_CENTERBOTTOM_RIGHTCENTER_LEFTCENTERCENTER_RIGHTTOP_LEFTTOP_CENTERTOP_RIGHTThe default value is BOTTOM_LEFT.

- *startHeadStyle*

  A SymbolicConstant specifying the style of the start head. Possible values are:ARROWFILLED_ARROWHOLLOW_CIRCLEFILLED_CIRCLEHOLLOW_DIAMONDFILLED_DIAMONDHOLLOW_SQUAREFILLED_SQUARENONEThe default value is NONE.

- *endHeadStyle*

  A SymbolicConstant specifying the style of the end head. Possible values are:ARROWFILLED_ARROWHOLLOW_ CIRCLEFILLED_CIRCLEHOLLOW_DIAMONDFILLED_DIAMONDHOLLOW_SQUAREFILLED_SQUARENONEThe default value is FILLED_ARROW.

- *startGap*

  A Float specifying the distance in millimeters between the arrow start point and the arrow start head. The default value is 0.0.

- *endGap*

  A Float specifying the distance in millimeters between the arrow end point and the arrow end head. The default value is 0.0.

- *color*

  A String specifying the color of the arrow. Possible string values are any valid color. The default value is "White".

- *lineStyle*

  A SymbolicConstant specifying the line style of the arrow. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.

- *lineThickness*

  A SymbolicConstant specifying the line thickness of the arrow. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

### Return value

An Arrow object.

### Exceptions

InvalidNameError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## translateStartPoint(...)



This method translates the start point of the Arrow object on the viewport plane.



### Required arguments

None.

### Optional arguments

- *x*

  A Float specifying the *X* translation amount in millimeters.

- *y*

  A Float specifying the*Y* translation amount in millimeters.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## translateEndPoint(...)



This method translates the end point of the Arrow object on the viewport plane.



### Required arguments

None.

### Optional arguments

- *x*

  A Float specifying the *X* translation amount in millimeters.

- *y*

  A Float specifying the*Y* translation amount in millimeters.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## setValues(...)



This method modifies the Arrow object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Arrow ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-arrowpyc.htm?ContextScope=all#simaker-arrowarrowpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The Arrow object has members with the same names and descriptions as the arguments to the [Arrow ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-arrowpyc.htm?ContextScope=all#simaker-arrowarrowpyc)method.