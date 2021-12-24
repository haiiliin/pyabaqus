# ViewCutOptions object

The ViewCutOptions object stores values and attributes associated with a view cut plot. The ViewCutOptions object has no constructor command. Abaqus creates a *defaultOdbDisplay.viewCutOptions* member when you import the Visualization module. Abaqus creates an *viewCutOptions* member when it creates the [OdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdisplaypyc.htm?ContextScope=all) object, using the values from *defaultOdbDisplay.viewCutOptions*. Abaqus creates the *odbDisplay* member when a viewport is created, using the values from *defaultOdbDisplay*.

ViewCutOptions objects are accessed in one of two ways:

- The default view cut options. These settings are used as defaults when other *viewCutOptions* members are created. These settings can be set to customize user preferences.
- The view cut options associated with a particular viewport.

## Access

```
import visualization
session.defaultOdbDisplay.viewCutOptions
session.viewports[name].layers[name].odbDisplay.viewCutOptions
session.viewports[name].odbDisplay.viewCutOptions
```

## setValues(...)



This method modifies the ViewCutOptions object.



### Required arguments

None.

### Optional arguments

- *options*

  A ViewCutOptions object from which values are to be copied. If other arguments are also supplied to setValues, they will override the values in *options*. The default value is None.

- *belowOptions*

  None or an [OptionArg](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optionargpyc.htm?ContextScope=all) object specifying values to be used for defining the options applicable on the model below the cut. The default value is None.

- *useBelowOptions*

  A Boolean specifying whether to use the options defined for displaying the model below the cut. The default value is OFF.

- *onOptions*

  None or an [OptionArg](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optionargpyc.htm?ContextScope=all) object specifying values to be used for defining the options applicable on the model on the cut. The default value is None.

- *useOnOptions*

  A Boolean specifying whether to use the options defined for displaying the model on the cut. The default value is OFF.

- *aboveOptions*

  None or an [OptionArg](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optionargpyc.htm?ContextScope=all) object specifying values to be used for defining the options applicable on the model above the cut. The default value is None.

- *useAboveOptions*

  A Boolean specifying whether to use the options defined for displaying the model above the cut. The default value is OFF.

- *freeBodyCutThru*

  A SymbolicConstant specifying the domain through which the free body cuts. Possible values are CURRENT_DISPLAY_GROUP and WHOLE_MODEL. The default value is CURRENT_DISPLAY_GROUP.

- *freeBodyStepThru*

  A SymbolicConstant specifying the domain through which the free body steps. Possible values are ACTIVE_CUT_RANGE and PREDEFINED_PATH. The default value is ACTIVE_CUT_RANGE.

- *numCutFreeBody*

  An Int specifying number of free bodies per view cut. The default value is 1.

- *displaySlicing*

  A Boolean specifying whether to display slicing. The default value is OFF.

- *slicingAtPathNodes*

  A Boolean specifying whether to slice at path nodes. The default value is OFF.

- *freeBodySumOnPath*

  A Boolean specifying whether to put the summation point at the path. The default value is ON.

- *cutFreeBodyMin*

  A Float specifying free body minimum value. The default value is 0.0.

- *cutFreeBodyMax*

  A Float specifying free body maximum value. The default value is 0.0.

- *showHeatFlowRate*

  A SymbolicConstant specifying whether to show the heat flow rate when available. Possible values are ON and OFF. The default value is ON.

- *summationLoc*

  A SymbolicConstant specifying the summation location for the free body cut. Possible values are CENTROID and SPECIFY. The default value is CENTROID.

- *componentResolution*

  A SymbolicConstant specifying the component resolution choice for the free body cut. Possible values are NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.

- *csysName*

  The SymbolicConstant GLOBAL or a String specifying the coordinate system name for the free body cut's component resolution. The default value is GLOBAL.

- *pathName*

  A String specifying the name of the path along which slicing occurs. The default value is an empty string.

- *summationPoint*

  A sequence of three Floats specifying the summation point for the free body cut. The default value is (0, 0, 0).

- *yAxis*

  A sequence of three Floats specifying the Y axis for free body component resolution. The default value is (0, 1, 0).

### Return value

None.

### Exceptions

RangeError.



## Members

The ViewCutOptions object can have the following members:

- *useBelowOptions*

  A Boolean specifying whether to use the options defined for displaying the model below the cut. The default value is OFF.

- *useOnOptions*

  A Boolean specifying whether to use the options defined for displaying the model on the cut. The default value is OFF.

- *useAboveOptions*

  A Boolean specifying whether to use the options defined for displaying the model above the cut. The default value is OFF.

- *numCutFreeBody*

  An Int specifying number of free bodies per view cut. The default value is 1.

- *displaySlicing*

  A Boolean specifying whether to display slicing. The default value is OFF.

- *slicingAtPathNodes*

  A Boolean specifying whether to slice at path nodes. The default value is OFF.

- *freeBodySumOnPath*

  A Boolean specifying whether to put the summation point at the path. The default value is ON.

- *cutFreeBodyMin*

  A Float specifying free body minimum value. The default value is 0.0.

- *cutFreeBodyMax*

  A Float specifying free body maximum value. The default value is 0.0.

- *freeBodyCutThru*

  A SymbolicConstant specifying the domain through which the free body cuts. Possible values are CURRENT_DISPLAY_GROUP and WHOLE_MODEL. The default value is CURRENT_DISPLAY_GROUP.

- *freeBodyStepThru*

  A SymbolicConstant specifying the domain through which the free body steps. Possible values are ACTIVE_CUT_RANGE and PREDEFINED_PATH. The default value is ACTIVE_CUT_RANGE.

- *showHeatFlowRate*

  A SymbolicConstant specifying whether to show the heat flow rate when available. Possible values are ON and OFF. The default value is ON.

- *summationLoc*

  A SymbolicConstant specifying the summation location for the free body cut. Possible values are CENTROID and SPECIFY. The default value is CENTROID.

- *componentResolution*

  A SymbolicConstant specifying the component resolution choice for the free body cut. Possible values are NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.

- *belowOptions*

  None or an [OptionArg](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optionargpyc.htm?ContextScope=all) object specifying values to be used for defining the options applicable on the model below the cut. The default value is None.

- *onOptions*

  None or an [OptionArg](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optionargpyc.htm?ContextScope=all) object specifying values to be used for defining the options applicable on the model on the cut. The default value is None.

- *aboveOptions*

  None or an [OptionArg](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optionargpyc.htm?ContextScope=all) object specifying values to be used for defining the options applicable on the model above the cut. The default value is None.

- *csysName*

  The SymbolicConstant GLOBAL or a String specifying the coordinate system name for the free body cut's component resolution. The default value is GLOBAL.

- *pathName*

  A String specifying the name of the path along which slicing occurs. The default value is an empty string.

- *summationPoint*

  A tuple of three Floats specifying the summation point for the free body cut. The default value is (0, 0, 0).

- *yAxis*

  A tuple of three Floats specifying the Y axis for free body component resolution. The default value is (0, 1, 0).