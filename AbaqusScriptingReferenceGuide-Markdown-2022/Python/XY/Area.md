# Area object

The Area object is used to display a rectangular area in an XYPlot. The Area object has no constructor. Area objects are automatically created whenever a [XYPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all), [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all), PlotTitle, or Legend objects are created.

## Access

```
import visualization
session.charts[name].area
session.charts[name].gridArea
session.charts[name].legend.area
session.defaultChartOptions.gridArea
session.defaultChartOptions.legend.area
session.defaultPlot.area
session.defaultPlot.title.area
session.xyPlots[name].area
session.xyPlots[name].charts[name].area
session.xyPlots[name].charts[name].gridArea
session.xyPlots[name].charts[name].legend.area
session.xyPlots[name].title.area
```

## setValues(...)



This method modifies the Area object.



### Required arguments

None.

### Optional arguments

- *area*

  An Area object from which attributes are to be copied.

- *style*

  An [AreaStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areastylepyc.htm?ContextScope=all) object.

- *border*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object.

- *positionMethod*

  A SymbolicConstant specifying how the area is positioned. Possible values are AUTO_ALIGN and MANUAL. The default value is AUTO_ALIGN.

- *alignment*

  A SymbolicConstant specifying the relative position of the area in its parent when *positionMethod*=AUTO_ALIGN. Possible values are:

  - BOTTOM_LEFT
  - BOTTOM_CENTER
  - BOTTOM_RIGHT
  - CENTER_LEFT
  - CENTER
  - CENTER_RIGHT
  - TOP_LEFT
  - TOP_CENTER
  - TOP_RIGHT

  The default value is BOTTOM_LEFT.

- *sizeMethod*

  A SymbolicConstant specifying how the area size is defined. Possible values are AUTOMATIC and MANUAL. The default value is AUTOMATIC.

- *originOffset*

  A pair of Floats specifying the X- and Y-offsets of the origin as a fraction of the available area. The *originOffset* argument is ignored unless *positionMethod*=MANUAL. The default value is (-1, 0). The valid range for each float is (0, 1).

- *widthScale*

  A Float specifying the scale as a fraction of the width of the available area when the sizeMethod=MANUAL. The valid range is (0, 1). The default value is 1.0.

- *heightScale*

  A Float specifying the scale as a fraction of the height of the available area when the *sizeMethod*=MANUAL. The valid range is (0, 1). The default value is 1.0.

- *inset*

  A Boolean specifying whether the area is inset or occupies a reserved area. The default value is OFF.

- *pl*

  A Float specifying the left padding of the area in mm. The default value is 1.0.

- *pr*

  A Float specifying the right padding of the area in mm. The default value is 1.0.

- *pt*

  A Float specifying the top padding of the area in mm. The default value is 1.0.

- *pb*

  A Float specifying the bottom padding of the area in mm. The default value is 1.0.

### Return value

None.

### Exceptions

RangeError.



## Members

The Area object can have the following members:

- *inset*

  A Boolean specifying whether the area is inset or occupies a reserved area. The default value is OFF.

- *positionMethod*

  A SymbolicConstant specifying how the area is positioned. Possible values are AUTO_ALIGN and MANUAL. The default value is AUTO_ALIGN.

- *alignment*

  A SymbolicConstant specifying the relative position of the area in its parent when *positionMethod*=AUTO_ALIGN. Possible values are:

  - BOTTOM_LEFT
  - BOTTOM_CENTER
  - BOTTOM_RIGHT
  - CENTER_LEFT
  - CENTER
  - CENTER_RIGHT
  - TOP_LEFT
  - TOP_CENTER
  - TOP_RIGHT

  The default value is BOTTOM_LEFT.

- *sizeMethod*

  A SymbolicConstant specifying how the area size is defined. Possible values are AUTOMATIC and MANUAL. The default value is AUTOMATIC.

- *width*

  A Float specifying the width of the area in mm. The default value is 1.0.

- *height*

  A Float specifying the height of the area in mm. The default value is 1.0.

- *widthScale*

  A Float specifying the scale as a fraction of the width of the available area when the sizeMethod=MANUAL. The valid range is (0, 1). The default value is 1.0.

- *heightScale*

  A Float specifying the scale as a fraction of the height of the available area when the *sizeMethod*=MANUAL. The valid range is (0, 1). The default value is 1.0.

- *pl*

  A Float specifying the left padding of the area in mm. The default value is 1.0.

- *pr*

  A Float specifying the right padding of the area in mm. The default value is 1.0.

- *pt*

  A Float specifying the top padding of the area in mm. The default value is 1.0.

- *pb*

  A Float specifying the bottom padding of the area in mm. The default value is 1.0.

- *style*

  An [AreaStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areastylepyc.htm?ContextScope=all) object specifying whether and how to fill the area.

- *border*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying whether and how to draw the border of the area.

- *origin*

  A pair of Floats specifying the X- and Y-offsets in millimeters from the lower-left corner of the XYPlot.

- *originOffset*

  A pair of Floats specifying the X- and Y-offsets of the origin as a fraction of the available area. The *originOffset* argument is ignored unless *positionMethod*=MANUAL. The default value is (-1, 0). The valid range for each float is (0, 1).