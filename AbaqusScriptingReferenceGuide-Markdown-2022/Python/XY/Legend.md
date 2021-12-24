# Legend object

The Legend object is used to store the display attributes of the chart legend. A legend object is automatically created when creating a [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) object.

## Access

```
import visualization
session.charts[name].legend
session.defaultChartOptions.legend
session.xyPlots[name].charts[name].legend
```

## setValues(...)



This method modifies the Legend object.



### Required arguments

None.

### Optional arguments

- *legend*

  A Legend object from which attributes are to be copied.

- *show*

  A Boolean specifying whether to show the legend. The default value is ON.

- *showMinMax*

  A Boolean specifying whether to display the minimum and maximum values. The default value is OFF.

- *title*

  A String specifying the title to appear on the legend. The default value is an empty string.

- *numberFormat*

  A SymbolicConstant specifying how the minimum and maximum values are formatted. Possible values are AUTOMATIC, DECIMAL, SCIENTIFIC, and ENGINEERING. The default value is AUTOMATIC.

- *numDigits*

  An Int specifying the number of significant digits displayed for the minimum and maximum values. Possible values are 1 to 7. The default value is 2.

- *textStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties used to display the legend text.

- *titleStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties used to display the legend title.

### Return value

None.

### Exceptions

None.



## Members

The Legend object can have the following members:

- *numberFormat*

  A SymbolicConstant specifying how the minimum and maximum values are formatted. Possible values are AUTOMATIC, DECIMAL, SCIENTIFIC, and ENGINEERING. The default value is AUTOMATIC.

- *numDigits*

  An Int specifying the number of significant digits displayed for the minimum and maximum values. Possible values are 1 to 7. The default value is 2.

- *show*

  A Boolean specifying whether to show the legend. The default value is ON.

- *showMinMax*

  A Boolean specifying whether to display the minimum and maximum values. The default value is OFF.

- *area*

  An [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object specifying the area of the legend.

- *textStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties used to display the legend text.

- *title*

  A String specifying the title to appear on the legend. The default value is an empty string.

- *titleStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties used to display the legend title.