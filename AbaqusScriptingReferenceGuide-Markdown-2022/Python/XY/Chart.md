# Chart object

The Chart object is used to display [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects. A Chart object is automatically created when creating an [XYPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all) object

## Access

```
import visualization
session.charts[name]
session.xyPlots[name].charts[name]
```

## autoColor(...)



This method distributes the colors on all curves displayed in the chart using the color palette defined by the xyColors object.



### Required arguments

None.

### Optional arguments

- *lines*

  A Boolean defining whether color distribution affects curve lines.

- *symbols*

  A Boolean defining whether color distribution affects curve symbols.

### Return value

None.

### Exceptions

None.



## autoSymbol()



This method distributes the symbols on all curves displayed in the chart.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## fitCurves()



This method resets the transform of the chart. It cancels any zoom or pan action.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## getAxis1(...)



This method returns the [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object used for displaying the Axis1 of the [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) specified by name or object or used for the given [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object.



### Required arguments

- *curve*

  The name or the [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) object associated to the [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object.

- *quantityType*

  The [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object associated to the [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object.

### Optional arguments

None.

### Return value

An [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object.

### Exceptions

If the given [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) is not used in the Chart.

XypError: Curve not found:

- If both arguments are specified.

  TypeError: Specify curve or quantityType; too many arguments; expected 1, got 2.

- If the given [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) is not used in the Chart.

  ValueError: QuantityType not found



## getAxis2(...)



This method returns the [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object used for displaying the Axis2 of the [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) specified by name or object or used for the given [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object.



### Required arguments

- *curve*

  The name or the [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) object associated to the [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object.

- *quantityType*

  The [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object associated to the [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object.

### Optional arguments

None.

### Return value

An [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object.

### Exceptions

If the given [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) is not used in the Chart.

XypError: Curve not found:

- If both arguments are specified.

  TypeError: Specify curve or quantityType; too many arguments; expected 1, got 2.

- If the given [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) is not used in the Chart.

  ValueError: QuantityType not found



## moveAxisUp(...)



This method moves the relative position of the given [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object up in the axis sequence of the Chart.



### Required arguments

- *axis*

  The [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object to be moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## moveAxisDown(...)



This method moves the relative position of the given [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object down in the axis sequence of the Chart.



### Required arguments

- *axis*

  The [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object to be moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## removeCurve(...)



This method removes the given [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) from the Chart.



### Required arguments

- *curve*

  The XYCurve name or the [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) object or a sequence of XYCurve names or [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects to be removed from the Chart.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the Chart object.



### Required arguments

None.

### Optional arguments

- *chart*

  A Chart object from which attributes are to be copied.

- *curvesToPlot*

  A sequence of Strings specifying the names of the curves to plot. In addition to this type, the argument can also be one of the following:A String specifying the name of the curve to plot.An [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) object specifying the curve to plot.A sequence of [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects specifying the curves to plot (as returned by the curveSet method).

- *aspectRatio*

  A Float specifying the aspect ratio of the grid area. A value of -1 specifies that the gridArea will take up all available space. The default value is −1.

- *transform*

  A sequence of Floats specifying a transformation matrix used to scale or pan along the axes of the Chart.

- *view*

  A [View](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewpyc.htm?ContextScope=all) object.

- *useQuantityType*

  A Boolean specifying whether to use the [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) to associate curves with axes. The default value is ON.

### Return value

None.

### Exceptions

RangeError.



## Members

The Chart object can have the following members:

- *name*

  A String specifying the name of the Chart object.

- *useQuantityType*

  A Boolean specifying whether to use the [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) to associate curves with axes. The default value is ON.

- *aspectRatio*

  A Float specifying the aspect ratio of the grid area. A value of -1 specifies that the gridArea will take up all available space. The default value is −1.

- *curves*

  A repository of [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects specifying a repository of [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects to display in the Chart.

- *axes1*

  An [AxisArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object specifying a read-only sequence of axis objects displayed as axes1 - the abscissa for a Cartesian chart.

- *axes2*

  An [AxisArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object specifying a read-only sequence of axis objects displayed as axes2 - the ordinate for a Cartesian chart.

- *area*

  An [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object specifying position, padding, background and borders of the chart.

- *gridArea*

  An [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object specifying how to display the grid area.

- *legend*

  A [Legend](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-legendpyc.htm?ContextScope=all) object specifying the attributes for the legend of the chart.

- *majorAxis1GridStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties to be used when drawing major gridlines along axis 1.

- *majorAxis2GridStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties to be used when drawing major gridlines along axis 2.

- *minorAxis1GridStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties to be used when drawing minor gridlines along axis 1.

- *minorAxis2GridStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties to be used when drawing minor gridlines along axis 2.

- *tagTextStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties to be used when creating tags.

- *tagAreaStyle*

  An [AreaStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areastylepyc.htm?ContextScope=all) object specifying the area properties to be used when creating tags.

- *tagBorder*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the tag area border properties to be used when creating tags.

- *transform*

  A tuple of Floats specifying a transformation matrix used to scale or pan along the axes of the Chart.