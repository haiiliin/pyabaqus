# OptionArg object

The OptionArg object is used to store values and attributes as a temporary object to be associated with a viewCutOptions object. The OptionArg object has only a constructor command.

## Access

```
import visualization
session.defaultOdbDisplay.viewCutOptions.aboveOptions
session.defaultOdbDisplay.viewCutOptions.belowOptions
session.defaultOdbDisplay.viewCutOptions.onOptions
session.viewports[name].layers[name].odbDisplay.viewCutOptions\
.aboveOptions
session.viewports[name].layers[name].odbDisplay.viewCutOptions\
.belowOptions
session.viewports[name].layers[name].odbDisplay.viewCutOptions\
.onOptions
session.viewports[name].odbDisplay.viewCutOptions.aboveOptions
session.viewports[name].odbDisplay.viewCutOptions.belowOptions
session.viewports[name].odbDisplay.viewCutOptions.onOptions
```

## OptionArg(...)



This method creates an OptionArg object.



### Path

visualization.OptionArg

### Required arguments

None.

### Optional arguments

- *renderStyle*

  A SymbolicConstant specifying the render style of the plot. Possible values are WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is WIREFRAME.

- *visibleEdges*

  A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR, FEATURE, FREE, and NONE. The default value is FEATURE.NONE can be used only when *renderStyle*=SHADED.

- *edgeColorWireHide*

  A String specifying the color to be used to plot the edges of the undeformed plot when *renderStyle*=WIREFRAME or HIDDEN. The default value is "Green".

- *edgeColorFillShade*

  A String specifying the color to be used to plot the edges of the undeformed plot when *renderStyle*=FILLED or SHADED. The default value is "Black".

- *edgeLineStyle*

  A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.

- *edgeLineThickness*

  A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *colorCodeOverride*

  A Boolean specifying whether to allow color coded items in the output database to override the edge and fill color settings. The default value is ON.

- *fillColor*

  A String specifying the color to be used to fill elements when *renderStyle*=FILLED or SHADED. The default value is "Green".

- *translucency*

  A Boolean specifying whether to set translucency. The default value is OFF.

- *translucencyFactor*

  A Float specifying the translucency factor when *translucency* = ON. Possible values are 0.0 ≤≤ *translucencyFactor* ≤≤ 1.0. The default value is 0.3.

### Return value

An OptionArg object.

### Exceptions

RangeError.



## Members

The OptionArg object has members with the same names and descriptions as the arguments to the [OptionArg ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optionargpyc.htm?ContextScope=all#simaker-optionargoptionargpyc)method.