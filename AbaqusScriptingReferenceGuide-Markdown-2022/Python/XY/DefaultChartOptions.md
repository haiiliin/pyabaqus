# DefaultChartOptions object

The DefaultChartOptions object is used to hold on default chart and axis attributes. The DefaultChartOptions object attributes are used whenever Chart or Axis are created. A DefaultChartOptions object is automatically created when opening a session.

## Access

```
import visualization
session.defaultChartOptions
```

## setValues(...)



This method modifies the DefaultChartOptions object.



### Required arguments

None.

### Optional arguments

- *areaStyle*

  An [AreaStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areastylepyc.htm?ContextScope=all) object specifying an [AreaStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areastylepyc.htm?ContextScope=all) used to hold on to the default display properties for the chart area.

- *aspectRatio*

  A Float specifying the default aspect ratio of the grid area. A value of -1 specifies that the gridArea will take up all available space. The default value is −1.

- *defaultAxis1Options*

  An [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object specifying an [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object used to hold on to the default properties for direction 1 axes—the abscissa for a Cartesian chart.

- *defaultAxis2Options*

  An [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object specifying an [Axis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axispyc.htm?ContextScope=all) object used to hold on to the default properties for direction 2 axes—the ordinate for a Cartesian chart.

- *gridArea*

  An [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object specifying how to display the grid area by default.

- *legend*

  A [Legend](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-legendpyc.htm?ContextScope=all) object specifying the default attributes for the legend of the chart.

- *majorAxis1GridStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the default line properties to be used when drawing major gridlines along axis 1.

- *majorAxis2GridStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the default line properties to be used when drawing major gridlines along axis 2.

- *minorAxis1GridStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the default line properties to be used when drawing minor gridlines along axis 1.

- *minorAxis2GridStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the default line properties to be used when drawing minor gridlines along axis 2.

- *tagAreaStyle*

  An [AreaStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areastylepyc.htm?ContextScope=all) object specifying the default area properties to be used when creating tags.

- *tagBorder*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the default tag area border properties to be used when creating tags.

- *tagTextStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the default text properties to be used when creating tags.

- *useQuantityType*

  A Boolean specifying whether to use the [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) to associate curves with axes. The default value is ON.

### Return value

None.

### Exceptions

None.



## Members

The DefaultChartOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-defaultchartoptionspyc.htm?ContextScope=all#simaker-defaultchartoptionssetvaluespyc)method.