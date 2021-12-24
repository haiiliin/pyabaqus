# DGOrientationOptions object

The DGOrientationOptions object stores values and attributes associated with a material orientation plot. The DGOrientationOptions object has no constructor command. Abaqus creates an *odbDisplayOptions.materialOrientationOptions* member when a display group instance is created, using values from *odbDisplay.materialOrientationOptions*.

## Access

```
session.viewports[name].assemblyDisplay.displayGroupInstances[name]\
.odbDisplayOptions.materialOrientationOptions
session.viewports[name].layers[name].assemblyDisplay\
.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
session.viewports[name].layers[name].odbDisplay\
.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
session.viewports[name].layers[name].partDisplay\
.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
session.viewports[name].odbDisplay.displayGroupInstances[name]\
.odbDisplayOptions.materialOrientationOptions
session.viewports[name].partDisplay.displayGroupInstances[name]\
.odbDisplayOptions.materialOrientationOptions
```

## Members

The DGOrientationOptions object can have the following members:

- *showAxis1*

  A Boolean specifying whether axis 1 of the material orientation triad should be displayed. The default value is ON.

- *showAxis2*

  A Boolean specifying whether axis 2 of the material orientation triad should be displayed. The default value is ON.

- *showAxis3*

  A Boolean specifying whether axis 3 of the material orientation triad should be displayed. The default value is ON.

- *symbolSize*

  A Float specifying the size of the material orientation triad. The default value is 6.0.

- *lineThickness*

  A SymbolicConstant specifying the thickness of the material orientation triad. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *orientation*

  A SymbolicConstant specifying the orientation used for composites. Possible values are PLY and LAYUP. The default value is PLY.

- *arrowheadStyle*

  A SymbolicConstant specifying the arrowhead style for the material orientation triad. Possible values are NONE, FILLED, and WIRE. The default value is NONE.

- *scaleMode*

  A SymbolicConstant specifying the scaling basis for the material orientation triad. Possible values are MODEL_SIZE and SCREEN_SIZE. The default value is MODEL_SIZE.

- *axis1Color*

  A String specifying the color of axis 1 of the material orientation triad. The default value is "Cyan".

- *axis2Color*

  A String specifying the color of axis 2 of the material orientation triad. The default value is "Yellow".

- *axis3Color*

  A String specifying the color of axis 3 of the material orientation triad. The default value is "Red".