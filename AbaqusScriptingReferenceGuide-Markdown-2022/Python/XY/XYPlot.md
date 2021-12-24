# XYPlot object

The XYPlot object is used to display [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) objects.

## Access

```
import visualization
session.xyPlots[name]
```

## XYPlot(...)



This method creates an empty XYPlot object.



### Path

```
session.XYPlot
```

### Required arguments

- *name*

  A String specifying the name of the XYPlot object.

### Optional arguments

None.

### Return value

An XYPlot object.

### Exceptions

InvalidNameError.



## autoColor(...)



This method distributes the colors on all curves displayed in the XYPlot using the color palette defined by the xyColors [AutoColors](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-autocolorspyc.htm?ContextScope=all) object.



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



This method distributes the symbols on all curves displayed in the XYPlot.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## fitCurves()



This method resets the transform of all the charts of the XYPlot object. It cancels any zoom or pan action.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## next(...)



This method restores the *transform* member of the active [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) object to the next setting in the transform list. (There is a list of eight transforms stored for each chart.) If there is no next transform, no action is taken.



### Required arguments

None.

### Optional arguments

- *drawImmediately*

  A Boolean specifying the viewport should refresh immediately after the command is processed. This is typically only used when writing a script and it is desirable to show intermediate results before the script completes. The default value is False.

### Return value

None.

### Exceptions

None.



## previous(...)



This method restores the *transform* member of the active [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) object to the previous setting in the transform list. (There is a list of eight transforms stored for each chart.) If there is no next transform, no action is taken.



### Required arguments

None.

### Optional arguments

- *drawImmediately*

  A Boolean specifying the viewport should refresh immediately after the command is processed. This is typically only used when writing a script and it is desirable to show intermediate results before the script completes. The default value is False.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the XYPlot object.



### Required arguments

None.

### Optional arguments

- *title*

  A [Title](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-titlepyc.htm?ContextScope=all) object specifying the title of the XYPlot object.

- *transform*

  A sequence of Floats specifying a transformation matrix used to scale or pan along the axes of the active [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) object of this XYPlot.

### Return value

None.

### Exceptions

None.



## Members

The XYPlot object has members with the same names and descriptions as the arguments to the [XYPlot ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all#simaker-xyplotxyplotpyc)method.

In addition, the XYPlot object can have the following members:

- *area*

  An [Area](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-areapyc.htm?ContextScope=all) object specifying position, padding, background and borders of the XYPlot object.

- *title*

  A [Title](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-titlepyc.htm?ContextScope=all) object specifying the title of the XYPlot object.

- *charts*

  A repository of [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) objects.

- *curves*

  A repository of [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects.

- *transform*

  A tuple of Floats specifying a transformation matrix used to scale or pan along the axes of the active [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) object of this XYPlot.