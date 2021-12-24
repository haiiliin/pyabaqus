# XYCurve object

The XYCurve object is used to plot *X–Y* data and to store its display attributes.

## Access

```
import visualization
session.charts[name].axes1[i].axisData.curves[i]
session.charts[name].axes2[i].axisData.curves[i]
session.charts[name].curves[name]
session.curves[name]
session.defaultChartOptions.defaultAxis1Options.axisData.curves[i]
session.defaultChartOptions.defaultAxis2Options.axisData.curves[i]
session.xyPlots[name].charts[name].axes1[i].axisData.curves[i]
session.xyPlots[name].charts[name].axes2[i].axisData.curves[i]
session.xyPlots[name].charts[name].curves[name]
session.xyPlots[name].curves[name]
```

## Curve(...)



This method creates an XYCurve object from an [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) object.



### Path

session.Curve

### Required arguments

- *name*

  A String specifying the repository key.

- *data*

  An [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) object specifying the data for the curve.

### Optional arguments

None.

### Return value

An XYCurve object.

### Exceptions

InvalidNameError.



## setValues(...)



This method modifies the XYCurve object.



### Required arguments

None.

### Optional arguments

- *displayTypes*

  A sequence of SymbolicConstants specifying that describe how curves are to be displayed. Possible values are LINE and SYMBOL. The default value is (LINE).

- *legendLabel*

  A String specifying the label to be displayed in the legend. By default, the label is system defined.

- *symbolFrequency*

  An Int specifying the frequency of plotting the markers. Possible values are *symbolFrequency* >> 0. If *symbolFrequency*=1, then markers are plotted at every point. The default value is 1.

- *useDefault*

  A Boolean specifying whether to use the system supplied legend label. The default value is ON.

### Return value

None.

### Exceptions

None.



## Members

The XYCurve object can have the following members:

- *name*

  A String specifying the repository key.

- *symbolFrequency*

  An Int specifying the frequency of plotting the markers. Possible values are *symbolFrequency* >> 0. If *symbolFrequency*=1, then markers are plotted at every point. The default value is 1.

- *useDefault*

  A Boolean specifying whether to use the system supplied legend label. The default value is ON.

- *legendSource*

  A SymbolicConstant specifying how the system supplied, default legend label is to be generated. Possible values are CURVE_LEGEND, CURVE_NAME, and CURVE_NAME_LEGEND. The default value is CURVE_LEGEND.

- *data*

  An [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) object specifying the data for the curve.

- *lineStyle*

  A [LineStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linestylepyc.htm?ContextScope=all) object specifying the line properties used to display the curve.

- *symbolStyle*

  A [SymbolStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-symbolstylepyc.htm?ContextScope=all) object specifying the symbol properties used to display the curve.

- *legendLabel*

  A String specifying the label to be displayed in the legend. By default, the label is system defined.

- *displayTypes*

  A tuple of SymbolicConstants specifying that describe how curves are to be displayed. Possible values are LINE and SYMBOL. The default value is (LINE).