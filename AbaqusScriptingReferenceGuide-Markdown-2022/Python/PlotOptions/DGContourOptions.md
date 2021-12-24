# DGContourOptions object

The DGContourOptions object stores values and attributes associated with a contour plot. The DGContourOptions object has no constructor command. Abaqus creates an *odbDisplayOptions.contourOptions* member when a display group instance is created, using values from *odbDisplay.contourOptions*.

## Access

```
session.viewports[name].assemblyDisplay.displayGroupInstances[name]\
.odbDisplayOptions.contourOptions
session.viewports[name].layers[name].assemblyDisplay\
.displayGroupInstances[name].odbDisplayOptions.contourOptions
session.viewports[name].layers[name].odbDisplay\
.displayGroupInstances[name].odbDisplayOptions.contourOptions
session.viewports[name].layers[name].partDisplay\
.displayGroupInstances[name].odbDisplayOptions.contourOptions
session.viewports[name].odbDisplay.displayGroupInstances[name]\
.odbDisplayOptions.contourOptions
session.viewports[name].partDisplay.displayGroupInstances[name]\
.odbDisplayOptions.contourOptions
```

## Members

The DGContourOptions object can have the following members:

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