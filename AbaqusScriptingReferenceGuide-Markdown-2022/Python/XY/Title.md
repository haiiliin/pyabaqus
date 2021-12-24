# Title object

The Title object is used to store the display attributes of the XYPlot title. An Title object is automatically created when creating a [XYPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all) object.

## Access

```
import visualization
session.defaultPlot.title
session.xyPlots[name].title
```

## setValues(...)



This method modifies the Title object.



### Required arguments

None.

### Optional arguments

- *title*

  A Title object from which attributes are to be copied.

- *text*

  A String specifying the text to appear as a title. By default the title is set to the [XYPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all) object name. The default value is an empty string.

- *area*

  An [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object specifying the area of the title.

- *useDefault*

  A Boolean specifying whether to show the default title. The default value is OFF.

- *titleStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties used to display the legend title.

### Return value

None.

### Exceptions

None.



## Members

The Title object can have the following members:

- *useDefault*

  A Boolean specifying whether to show the default title. The default value is OFF.

- *area*

  An [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object specifying the area of the title.

- *text*

  A String specifying the text to appear as a title. By default the title is set to the [XYPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all) object name. The default value is an empty string.

- *titleStyle*

  A [TextStyle](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-textstylepyc.htm?ContextScope=all) object specifying the text properties used to display the legend title.