# DGSymbolOptions object

The DGSymbolOptions object stores values and attributes associated with a symbol plot. The DGSymbolOptions object has no constructor command. Abaqus creates an *odbDisplayOptions.symbolOptions* member when a display group instance is created, using values from *odbDisplay.symbolOptions*.

## Access

```
session.viewports[name].assemblyDisplay.displayGroupInstances[name]\
.odbDisplayOptions.symbolOptions
session.viewports[name].layers[name].assemblyDisplay\
.displayGroupInstances[name].odbDisplayOptions.symbolOptions
session.viewports[name].layers[name].odbDisplay\
.displayGroupInstances[name].odbDisplayOptions.symbolOptions
session.viewports[name].layers[name].partDisplay\
.displayGroupInstances[name].odbDisplayOptions.symbolOptions
session.viewports[name].odbDisplay.displayGroupInstances[name]\
.odbDisplayOptions.symbolOptions
session.viewports[name].partDisplay.displayGroupInstances[name]\
.odbDisplayOptions.symbolOptions
```

## Members

The DGSymbolOptions object can have the following members:

- *vectorLineThickness*

  A SymbolicConstant specifying the vector line thickness. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *vectorColorMethod*

  A SymbolicConstant specifying the vector color method. Possible values are UNIFORM and SPECTRUM. The default value is SPECTRUM.

- *tensorColorMethod*

  A SymbolicConstant specifying the tensor color method. Possible values are UNIFORM and SPECTRUM. The default value is SPECTRUM.

- *vectorArrowheadStyle*

  A SymbolicConstant specifying the vector arrowhead style. Possible values are NONE, FILLED, and WIRE. The default value is WIRE.

- *arrowSymbolSize*

  An Int specifying the length of vector and tensor symbols. The default value is 6.

- *vectorIntervalNumber*

  An Int specifying the number of color intervals for vector symbols. The default value is 12.

- *symbolDensity*

  A Float specifying the factor for randomized sampling. The default value is 1.0.

- *constantLengthArrows*

  A Boolean specifying whether to use constant-length arrows for vector symbols. The default value is OFF.

- *tensorIntervalNumber*

  An Int specifying the number of color intervals for tensor symbols. The default value is 12.

- *tensorLineThickness*

  A SymbolicConstant specifying the line thickness of the tensor symbols. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *tensorArrowheadStyle*

  A SymbolicConstant specifying the arrowhead style of the tensor symbols. Possible values are NONE, FILLED, and WIRE. The default value is WIRE.

- *numberFormatT*

  A SymbolicConstant specifying the number format for tensor. Possible values are SCIENTIFIC, FIXED, and ENGINEERING. The default value is SCIENTIFIC.

- *numberFormatV*

  A SymbolicConstant specifying the number format for vector. Possible values are SCIENTIFIC, FIXED, and ENGINEERING. The default value is SCIENTIFIC.

- *arrowScaleMode*

  A SymbolicConstant specifying the arrow scaling mode. Possible values are MODEL_SIZE and SCREEN_SIZE. The default value is MODEL_SIZE.

- *drawLabelT*

  A Boolean specifying whether to draw tensor labels. The default value is OFF.

- *drawLabelV*

  A Boolean specifying whether to draw vector labels. The default value is OFF.

- *numDigitsT*

  An Int specifying the number of digits in the tensor label. The default value is 2.

- *numDigitsV*

  An Int specifying the number of digits in the vector label. The default value is 2.

- *vectorColor*

  A String specifying the vector color. The default value is "Red".

- *vectorColorSpectrum*

  A String specifying the vector color spectrum name. The default value is "Rainbow".

- *tensorColorSpectrum*

  A String specifying the tensor color spectrum name. The default value is "Rainbow".

- *textColorT*

  A String specifying the text color for tensor. The default value is "Yellow".

- *textColorV*

  A String specifying the text color for vector. The default value is "Yellow".

- *textFontT*

  A String specifying the text font for tensor. The default value is "verdana".

- *textFontV*

  A String specifying the text font for vector. The default value is "verdana".

- *tensorMaxPrinColor*

  A String specifying the color of the maximum principal tensor symbols. The default value is "Red".

- *tensorMinPrinColor*

  A String specifying the color of the minimum principal tensor symbols. The default value is "Cyan".

- *tensorMidPrinColor*

  A String specifying the color of the intermediate principal tensor symbols. The default value is "Yellow".

- *tensorSelectedPrinColor*

  A String specifying the color of the selected principal tensor symbols. The default value is "Red".