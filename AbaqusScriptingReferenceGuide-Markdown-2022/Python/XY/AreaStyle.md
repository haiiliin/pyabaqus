# AreaStyle object

The AreaStyle object is used to define how areas are to be filled when drawing XY-plot objects.

AreaStyle objects are automatically created whenever an [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object is created. AreaStyle objects can be created using the methods described below.

## Access

```
import visualization
session.charts[name].area.style
session.charts[name].gridArea.style
session.charts[name].legend.area.style
session.charts[name].tagAreaStyle
session.defaultChartOptions.areaStyle
session.defaultChartOptions.gridArea.style
session.defaultChartOptions.legend.area.style
session.defaultChartOptions.tagAreaStyle
session.defaultPlot.area.style
session.defaultPlot.title.area.style
session.xyPlots[name].area.style
session.xyPlots[name].charts[name].area.style
session.xyPlots[name].charts[name].gridArea.style
session.xyPlots[name].charts[name].legend.area.style
session.xyPlots[name].charts[name].tagAreaStyle
session.xyPlots[name].title.area.style
```

## AreaStyle(...)



This method creates an AreaStyle.



### Path

session.AreaStyle

xyPlot.AreaStyle

### Required arguments

None.

### Optional arguments

- *color*

  A String specifying the color to be used when filling an area with this AreaStyle object. The default value is "White".

- *fill*

  A Boolean specifying whether to fill the area when using this AreaStyle. The default value is ON.

- *style*

  A SymbolicConstant specifying the area pattern style to be used when filling an area using this AreaStyle. The default value is SOLID.

### Return value

An AreaStyle object.

### Exceptions

ColorError



## setValues(...)



This method modifies the AreaStyle object.



### Required arguments

None.

### Optional arguments

- *color*

  A String specifying the color to be used when filling an area with this AreaStyle object. The default value is "White".

- *fill*

  A Boolean specifying whether to fill the area when using this AreaStyle. The default value is ON.

- *style*

  A SymbolicConstant specifying the area pattern style to be used when filling an area using this AreaStyle. The default value is SOLID.

### Return value

None.

### Exceptions

None.



## Members

The AreaStyle object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areastylepyc.htm?ContextScope=all#simaker-areastylesetvaluespyc)method.