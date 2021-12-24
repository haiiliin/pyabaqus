# DefaultPlot object

The DefaultPlot object is used to hold on default plot attributes. The DefaultPlot object attributes are used whenever an [XYPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all) object is created. A DefaultPlot object is automatically created when opening a session.

## Access

```
import visualization
session.defaultPlot
```

## Members

The DefaultPlot object can have the following members:

- *area*

  An [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object specifying an [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) used to hold on to the default display properties for the plot area.

- *title*

  A [Title](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-titlepyc.htm?ContextScope=all) object specifying a [Title](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-titlepyc.htm?ContextScope=all) object used to hold on to the default properties of the XY-Plot title.