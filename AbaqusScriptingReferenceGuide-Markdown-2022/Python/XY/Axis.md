# Axis object

The Axis object is used to store the display attributes of axes. Axes objects are automatically created when adding [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects to a [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) object.

## Access

```
import visualization
session.charts[name].axes1[i]
session.charts[name].axes2[i]
session.defaultChartOptions.defaultAxis1Options
session.defaultChartOptions.defaultAxis2Options
session.xyPlots[name].charts[name].axes1[i]
session.xyPlots[name].charts[name].axes2[i]
```

## setValues(...)



This method modifies the Axis object.



### Required arguments

None.

### Optional arguments

- *axis*

  An Axis object from which attributes are to be copied.

- *labelFrequency*

  An Int specifying the frequency of the labels with respect to the tick marks. The default value is 1.

- *labelPlacement*

  A SymbolicConstant specifying how labels are placed on the axis. Possible values are:NONE, specifying that no labels are displayed.INSIDE, specifying that the labels are placed on the inside of the axis.OUTSIDE, specifying that the labels are placed on the outside of the axis.The default value is INSIDE.

- *labelStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties to be used when displaying axis labels.

- *lineStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties used to display the axis.

- *placement*

  A SymbolicConstant specifying the placement of the axis on the grid. Possible values are:MIN_EDGE, specifying that the axis is placed at the minimum edge - for an abscissa at the bottom, for an ordinate to the left.MAX_EDGE, specifying that the axis is placed at the maximum edge - for an abscissa at the top, for an ordinate at the right.MIN_MAX_EDGE, specifying that the axis is placed at the minimum edge - for an abscissa at the bottom, for an ordinate to the left - and repeated without labels and title at the maximum edge.CENTER, specifying that the axis is placed at the center of the grid.The default value is MIN_MAX_EDGE.

- *tickLength*

  A Float specifying the length of the ticks in mm. The default value is 2.0.

- *tickPlacement*

  A SymbolicConstant specifying how tick marks are placed on the axis. Possible values are:NONE, specifying that no tick marks are displayed.INSIDE, specifying that the tick marcks are placed on the inside of the axis.OUTSIDE, specifying that the tick marcks are placed on the outside of the axis.ACROSS, specifying that the tick marcks are placed across the axis.The default value is INSIDE.

- *tickStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties to be used when displaying axis ticks.

- *titleStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties to be used when displaying the axis title.

### Return value

None.

### Exceptions

None.



## Members

The Axis object can have the following members:

- *labelFrequency*

  An Int specifying the frequency of the labels with respect to the tick marks. The default value is 1.

- *tickLength*

  A Float specifying the length of the ticks in mm. The default value is 2.0.

- *placement*

  A SymbolicConstant specifying the placement of the axis on the grid. Possible values are:MIN_EDGE, specifying that the axis is placed at the minimum edge - for an abscissa at the bottom, for an ordinate to the left.MAX_EDGE, specifying that the axis is placed at the maximum edge - for an abscissa at the top, for an ordinate at the right.MIN_MAX_EDGE, specifying that the axis is placed at the minimum edge - for an abscissa at the bottom, for an ordinate to the left - and repeated without labels and title at the maximum edge.CENTER, specifying that the axis is placed at the center of the grid.The default value is MIN_MAX_EDGE.

- *tickPlacement*

  A SymbolicConstant specifying how tick marks are placed on the axis. Possible values are:NONE, specifying that no tick marks are displayed.INSIDE, specifying that the tick marcks are placed on the inside of the axis.OUTSIDE, specifying that the tick marcks are placed on the outside of the axis.ACROSS, specifying that the tick marcks are placed across the axis.The default value is INSIDE.

- *labelPlacement*

  A SymbolicConstant specifying how labels are placed on the axis. Possible values are:NONE, specifying that no labels are displayed.INSIDE, specifying that the labels are placed on the inside of the axis.OUTSIDE, specifying that the labels are placed on the outside of the axis.The default value is INSIDE.

- *axisData*

  An [AxisData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axisdatapyc.htm?ContextScope=all) object specifying the numerical data of the axis.

- *lineStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties used to display the axis.

- *labelStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties to be used when displaying axis labels.

- *titleStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties to be used when displaying the axis title.

- *tickStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties to be used when displaying axis ticks.