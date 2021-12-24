# ContourOptions object

The ContourOptions object stores values and attributes associated with a contour plot. The ContourOptions object has no constructor command. Abaqus creates a *defaultOdbDisplay.contourOptions* member when you import the Visualization module. Abaqus creates a *contourOptions* member when it creates the [OdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdisplaypyc.htm?ContextScope=all) object, using the values from *defaultOdbDisplay.contourOptions*. Abaqus creates the *odbDisplay* member when a viewport is created, using the values from *defaultOdbDisplay*.

ContourOptions objects are accessed in one of two ways:

- The default contour options. These settings are used as defaults when other *contourOptions* members are created. These settings can be set to customize user preferences.
- The contour options associated with a particular viewport.

The ContourOptions object is derived from the [DGContourOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgcontouroptionspyc.htm?ContextScope=all) object.

## Access

```
import visualization
session.defaultOdbDisplay.contourOptions
session.viewports[name].assemblyDisplay.displayGroupInstances[name]\
.odbDisplayOptions.contourOptions
session.viewports[name].layers[name].assemblyDisplay\
.displayGroupInstances[name].odbDisplayOptions.contourOptions
session.viewports[name].layers[name].odbDisplay.contourOptions
session.viewports[name].layers[name].odbDisplay\
.displayGroupInstances[name].odbDisplayOptions.contourOptions
session.viewports[name].layers[name].partDisplay\
.displayGroupInstances[name].odbDisplayOptions.contourOptions
session.viewports[name].odbDisplay.contourOptions
session.viewports[name].odbDisplay.displayGroupInstances[name]\
.odbDisplayOptions.contourOptions
session.viewports[name].partDisplay.displayGroupInstances[name]\
.odbDisplayOptions.contourOptions
```

## setValues(...)



This method modifies the ContourOptions object.



### Required arguments

None.

### Optional arguments

- *options*

  A ContourOptions object from which values are to be copied. If other arguments are also supplied to setValues, they will override the values in *options*. The default value is None.

- *contourType*

  A SymbolicConstant specifying the contour type. Possible values are LINE, BANDED, QUILT, and ISOSURFACE. The default value is BANDED.

- *contourMethod*

  A SymbolicConstant specifying the contour rendering method. Possible values are TEXTURE_MAPPED and TESSELLATED. The default value is TEXTURE_MAPPED.

- *tickmarkPlots*

  A Boolean specifying whether tick mark plots should be displayed on line-type elements. If *tickmarkPlots*=ON, Abaqus displays a tick mark plot. If *tickmarkPlots*=OFF, Abaqus displays contours on the element faces. The default value is OFF.

- *contourStyle*

  A SymbolicConstant specifying the interval style of the contour plot. Possible values are CONTINUOUS and UNIFORM. The default value is UNIFORM.

- *numIntervals*

  An Int specifying the number of intervals when *contourStyle*=UNIFORM. Possible values are 2 ≤≤ *numIntervals* ≤≤ 24. The default value is 12.

- *intervalType*

  A SymbolicConstant specifying the interval type of the contour plot. Possible values are UNIFORM, LOG, and USER_DEFINED. The default value is UNIFORM.

- *intervalValues*

  A sequence of Floats specifying the interval values when *intervalType*=USER_DEFINED.

- *maxAutoCompute*

  A Boolean specifying whether the contour range maximum value should be computed from the output data to be contoured. The default value is ON.

- *maxValue*

  A Float specifying the contour range maximum value to be used in the plot when *maxAutoCompute*=ON. The default value is *autoMaxValue*.

- *minAutoCompute*

  A Boolean specifying whether the contour range minimum value should be computed from the output data to be contoured. The default value is ON.

- *minValue*

  A Float specifying the contour range minimum value to be used in the plot when *minAutoCompute*=ON. The default value is *autoMinValue*.

- *animationAutoLimits*

  A SymbolicConstant specifying the method to be used when contour limits are automatically computed for animation. *animationAutoLimits* will only effect the minimum limit and/or maximum limit when *minAutoCompute* and/or *maxAutoCompute*=True. Possible values are FIRST_AND_LAST, CURRENT_FRAME, RECOMPUTE_EACH_FRAME, and ALL_FRAMES. The default value is ALL_FRAMES.

- *edgeColorLine*

  A String specifying the edge color to be used when *contourType*=LINE. The default value is "White".

- *edgeColorBandedQuilt*

  A String specifying the edge color to be used when *contourType*=BANDED or QUILT. The default value is "Black".

- *spectrum*

  A String specifying the name of the color spectrum to be used in the contour plot. The default value is "Rainbow".

- *reversedContourLegendRange*

  A Boolean specifying whether the contour legend should show the lowest value at the top and the highest value at the bottom (*reversedContourLegendRange*=ON) or vice versa. The default value is OFF.

- *outsideLimitsMode*

  A SymbolicConstant specifying the color of contour values that exceed the limits of the plot. Possible values are SPECTRUM and SPECIFY.When *outsideLimitsMode*=SPECTRUM, the maximum and minimum contour spectrum colors are used for values that exceed the limits of the plot. When *outsideLimitsMode*=SPECIFY, the values of *outsideLimitsAboveColor* and *outsideLimitsBelowColor* are used for values that exceed the limits of the plot.

- *outsideLimitsAboveColor*

  A String specifying the color to be used for values that exceed the limits of the plot when *outsideLimitsMode*=SPECIFY. The default value is "Grey80".

- *outsideLimitsBelowColor*

  A String specifying the color to be used for values that exceed the limits of the plot when *outsideLimitsMode*=SPECIFY. The default value is "Grey20".

- *intervalLineAttributes*

  A sequence of sequences of SymbolicConstants specifying the line style and line thickness for each interval in the plot when *contourType*=LINE. The size of the outer sequence must be equal to *numIntervals*-1. The inner sequence consists of two SymbolicConstants specifying the line style and line thickness. For possible values, refer to the *edgeLineStyle* and *edgeLineThickness* members of the [DGCommonOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgcommonoptionspyc.htm?ContextScope=all) object. The default is ((SOLID, VERY_THIN), ).

- *contourEdges*

  A Boolean specifying whether to plot the edges of each contour interval when *contourType*=BANDED or ISOSURFACE. The default value is OFF.

- *contourEdgeColor*

  A String specifying the color to be used to plot the contour edges when *contourType*=BANDED or ISOSURFACE. The default value is "Grey60".

- *contourEdgeStyle*

  A SymbolicConstant specifying the edge line style to be used to plot the contour edges when *contourType*=BANDED or ISOSURFACE. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.

- *contourEdgeThickness*

  A SymbolicConstant specifying the edge line thickness to be used to plot the edge of the contour intervals when *contourType*=BANDED or ISOSURFACE. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *tickmarkAxisLength*

  A SymbolicConstant specifying the length of the tick mark plot axes. Possible values are SHORT, MEDIUM, and LONG. The default value is MEDIUM.

- *tickmarkBaseValue*

  A Float specifying the base contour value defining the tick mark axis contour value that intersects the elements. Possible values are *autoMinValue* ≤≤ *tickmarkBaseValue* ≤≤ *autoMaxValue*. The default value is 0.0.

- *tickmarkOrientation*

  A SymbolicConstant specifying the orientation of the tick mark plots. Possible values are N1 and N2. The default value is N2.

- *tickmarkCurveColor*

  A String specifying the color to be used to plot the tick mark curve. The default value is "Cyan".

- *averagedOrientationDisplay*

  A Boolean specifying the display of the nodal averaged coordinate systems used when averaging element vector or tensor data. The default value is OFF.

- *extrapolatedAveraging*

  A Boolean specifying whether to auto-compute contour limits using extrapolated values alone or extrapolated values that are averaged. The default value is OFF.

- *showMaxLocation*

  A Boolean specifying whether to display location of maximum value. The default value is OFF.

- *showMinLocation*

  A Boolean specifying whether to display location of minimum value. The default value is OFF.

- *legendHideOutsideLimits*

  A Boolean specifying whether to hide the values outside the specified minimum/maximum for the contour interval when *legendHideOutsideLimits*=ON. The default value is OFF.

### Return value

None.

### Exceptions

RangeError.



## Members

The ContourOptions object can have the following members:

- *contourType*

  A SymbolicConstant specifying the contour type. Possible values are LINE, BANDED, QUILT, and ISOSURFACE. The default value is BANDED.

- *numIntervals*

  An Int specifying the number of intervals when *contourStyle*=UNIFORM. Possible values are 2 ≤≤ *numIntervals* ≤≤ 24. The default value is 12.

- *intervalType*

  A SymbolicConstant specifying the interval type of the contour plot. Possible values are UNIFORM, LOG, and USER_DEFINED. The default value is UNIFORM.

- *maxAutoCompute*

  A Boolean specifying whether the contour range maximum value should be computed from the output data to be contoured. The default value is ON.

- *maxValue*

  A Float specifying the contour range maximum value to be used in the plot when *maxAutoCompute*=ON. The default value is *autoMaxValue*.

- *minAutoCompute*

  A Boolean specifying whether the contour range minimum value should be computed from the output data to be contoured. The default value is ON.

- *minValue*

  A Float specifying the contour range minimum value to be used in the plot when *minAutoCompute*=ON. The default value is *autoMinValue*.

- *animationAutoLimits*

  A SymbolicConstant specifying the method to be used when contour limits are automatically computed for animation. *animationAutoLimits* will only effect the minimum limit and/or maximum limit when *minAutoCompute* and/or *maxAutoCompute*=True. Possible values are FIRST_AND_LAST, CURRENT_FRAME, RECOMPUTE_EACH_FRAME, and ALL_FRAMES. The default value is ALL_FRAMES.

- *outsideLimitsMode*

  A SymbolicConstant specifying the color of contour values that exceed the limits of the plot. Possible values are SPECTRUM and SPECIFY.When *outsideLimitsMode*=SPECTRUM, the maximum and minimum contour spectrum colors are used for values that exceed the limits of the plot. When *outsideLimitsMode*=SPECIFY, the values of *outsideLimitsAboveColor* and *outsideLimitsBelowColor* are used for values that exceed the limits of the plot.

- *extrapolatedAveraging*

  A Boolean specifying whether to auto-compute contour limits using extrapolated values alone or extrapolated values that are averaged. The default value is OFF.

- *showMaxLocation*

  A Boolean specifying whether to display location of maximum value. The default value is OFF.

- *showMinLocation*

  A Boolean specifying whether to display location of minimum value. The default value is OFF.

- *autoMaxValue*

  A Float specifying the maximum value to be used in the plot. The value is computed from the output data to be contoured. This value is read-only.

- *autoMinValue*

  A Float specifying the minimum value to be used in the plot. The value is computed from the output data to be contoured. This value is read-only.

- *outsideLimitsAboveColor*

  A String specifying the color to be used for values that exceed the limits of the plot when *outsideLimitsMode*=SPECIFY. The default value is "Grey80".

- *outsideLimitsBelowColor*

  A String specifying the color to be used for values that exceed the limits of the plot when *outsideLimitsMode*=SPECIFY. The default value is "Grey20".

- *spectrum*

  A String specifying the name of the color spectrum to be used in the contour plot. The default value is "Rainbow".

- *reversedContourLegendRange*

  A Boolean specifying whether the contour legend should show the lowest value at the top and the highest value at the bottom (*reversedContourLegendRange*=ON) or vice versa. The default value is OFF.

- *intervalValues*

  A tuple of Floats specifying the interval values when *intervalType*=USER_DEFINED.

- *contourMethod*

  A SymbolicConstant specifying the contour rendering method. Possible values are TEXTURE_MAPPED and TESSELLATED. The default value is TEXTURE_MAPPED.

- *tickmarkPlots*

  A Boolean specifying whether tick mark plots should be displayed on line-type elements. If *tickmarkPlots*=ON, Abaqus displays a tick mark plot. If *tickmarkPlots*=OFF, Abaqus displays contours on the element faces. The default value is OFF.

- *contourStyle*

  A SymbolicConstant specifying the interval style of the contour plot. Possible values are CONTINUOUS and UNIFORM. The default value is UNIFORM.

- *contourEdges*

  A Boolean specifying whether to plot the edges of each contour interval when *contourType*=BANDED or ISOSURFACE. The default value is OFF.

- *contourEdgeStyle*

  A SymbolicConstant specifying the edge line style to be used to plot the contour edges when *contourType*=BANDED or ISOSURFACE. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.

- *contourEdgeThickness*

  A SymbolicConstant specifying the edge line thickness to be used to plot the edge of the contour intervals when *contourType*=BANDED or ISOSURFACE. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *averagedOrientationDisplay*

  A Boolean specifying the display of the nodal averaged coordinate systems used when averaging element vector or tensor data. The default value is OFF.

- *matchingPlyLabels*

  A Boolean specifying whether the label for the matching ply shows up in the viewport. The default value is OFF.

- *colorByMatchingPlies*

  A Boolean specifying whether the contour color is driven by the matching ply. The default value is OFF.

- *tickmarkAxisLength*

  A SymbolicConstant specifying the length of the tick mark plot axes. Possible values are SHORT, MEDIUM, and LONG. The default value is MEDIUM.

- *tickmarkBaseValue*

  A Float specifying the base contour value defining the tick mark axis contour value that intersects the elements. Possible values are *autoMinValue* ≤≤ *tickmarkBaseValue* ≤≤ *autoMaxValue*. The default value is 0.0.

- *tickmarkOrientation*

  A SymbolicConstant specifying the orientation of the tick mark plots. Possible values are N1 and N2. The default value is N2.

- *edgeColorLine*

  A String specifying the edge color to be used when *contourType*=LINE. The default value is "White".

- *edgeColorBandedQuilt*

  A String specifying the edge color to be used when *contourType*=BANDED or QUILT. The default value is "Black".

- *contourEdgeColor*

  A String specifying the color to be used to plot the contour edges when *contourType*=BANDED or ISOSURFACE. The default value is "Grey60".

- *tickmarkCurveColor*

  A String specifying the color to be used to plot the tick mark curve. The default value is "Cyan".

- *intervalLineAttributes*

  A tuple of tuples of SymbolicConstants specifying the line style and line thickness for each interval in the plot when *contourType*=LINE. The size of the outer sequence must be equal to *numIntervals*-1. The inner sequence consists of two SymbolicConstants specifying the line style and line thickness. For possible values, refer to the *edgeLineStyle* and *edgeLineThickness* members of the [DGCommonOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgcommonoptionspyc.htm?ContextScope=all) object. The default is ((SOLID, VERY_THIN), ).

- *legendHideOutsideLimits*

  A Boolean specifying whether to hide the values outside the specified min/max in the contour legend. This setting hides the *autoMinValue* and *autoMaxValue* from the spectrum when *legendHideOutsideLimits*=ON.The default value is OFF.