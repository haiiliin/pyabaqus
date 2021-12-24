# SymbolOptions object

The SymbolOptions object stores values and attributes associated with a symbol plot. The SymbolOptions object has no constructor command. Abaqus creates a *defaultOdbDisplay.symbolOptions* member when you import the Visualization module. Abaqus creates a *symbolOptions* member when it creates the [OdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdisplaypyc.htm?ContextScope=all) object, using the values from *defaultOdbDisplay.symbolOptions*. Abaqus creates the *odbDisplay* member when a viewport is created, using the values from *defaultOdbDisplay*.

SymbolOptions objects are accessed in one of two ways:

- The default symbol options. These settings are used as defaults when other *symbolOptions* members are created. These settings can be set to customize user preferences.
- The symbol options associated with a particular viewport.

The SymbolOptions object is derived from the [DGSymbolOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgsymboloptionspyc.htm?ContextScope=all) object.

## Access

```
import visualization
session.defaultOdbDisplay.symbolOptions
session.viewports[name].assemblyDisplay.displayGroupInstances[name]\
.odbDisplayOptions.symbolOptions
session.viewports[name].layers[name].assemblyDisplay\
.displayGroupInstances[name].odbDisplayOptions.symbolOptions
session.viewports[name].layers[name].odbDisplay\
.displayGroupInstances[name].odbDisplayOptions.symbolOptions
session.viewports[name].layers[name].odbDisplay.symbolOptions
session.viewports[name].layers[name].partDisplay\
.displayGroupInstances[name].odbDisplayOptions.symbolOptions
session.viewports[name].odbDisplay.displayGroupInstances[name]\
.odbDisplayOptions.symbolOptions
session.viewports[name].odbDisplay.symbolOptions
session.viewports[name].partDisplay.displayGroupInstances[name]\
.odbDisplayOptions.symbolOptions
```

## setValues(...)



This method modifies the SymbolOptions object.



### Required arguments

None.

### Optional arguments

- *options*

  A SymbolOptions object from which values are to be copied. If other arguments are also supplied to setValues, they will override the values in *options*. The default value is None.

- *vectorQuantity*

  A SymbolicConstant specifying the vector quantity to display. Possible values are RESULTANT and VECTOR_COMPONENT. The default value is RESULTANT.

- *vectorLineThickness*

  A SymbolicConstant specifying the vector line thickness. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *vectorArrowheadStyle*

  A SymbolicConstant specifying the vector arrowhead style. Possible values are NONE, FILLED, and WIRE. The default value is WIRE.

- *vectorColor*

  A String specifying the vector color. The default value is "Red".

- *vectorColorMethod*

  A SymbolicConstant specifying the vector color method. Possible values are UNIFORM and SPECTRUM. The default value is SPECTRUM.

- *vectorColorSpectrum*

  A String specifying the vector color spectrum name. The default value is "Rainbow".

- *vectorIntervalNumber*

  An Int specifying the number of color intervals for vector symbols. The default value is 12.

- *symbolDensity*

  A Float specifying the factor for randomized sampling. The default value is 1.0.

- *constantLengthArrows*

  A Boolean specifying whether to use constant-length arrows for vector symbols. The default value is OFF.

- *tensorColorMethod*

  A SymbolicConstant specifying the tensor color method. Possible values are UNIFORM and SPECTRUM. The default value is SPECTRUM.

- *tensorColorSpectrum*

  A String specifying the tensor color spectrum name. The default value is "Rainbow".

- *tensorIntervalNumber*

  An Int specifying the number of color intervals for tensor symbols. The default value is 12.

- *vectorMaxValueAutoCompute*

  A Boolean specifying whether the maximum vector value is to be computed automatically. The default value is ON.

- *vectorMaxValue*

  A Float specifying the user-specified maximum vector value. The default value is *autoVectorMaxValue*.

- *vectorMinValueAutoCompute*

  A Boolean specifying whether the minimum vector value is to be computed automatically. The default value is ON.

- *vectorMinValue*

  A Float specifying the user-specified minimum vector value. The default value is *autoVectorMinValue*.

- *tensorQuantity*

  A SymbolicConstant specifying the tensor quantity to display. Possible values are ALL_PRINCIPAL_COMPONENTS, PRINCIPAL_COMPONENT, ALL_DIRECT_COMPONENTS, and DIRECT_COMPONENT. The default value is ALL_PRINCIPAL_COMPONENTS.

- *arrowSymbolSize*

  An Int specifying the length of vector and tensor symbols. The default value is 6.

- *tensorMaxPrinColor*

  A String specifying the color of the maximum principal tensor symbols. The default value is "Red".

- *tensorMinPrinColor*

  A String specifying the color of the minimum principal tensor symbols. The default value is "Cyan".

- *tensorMidPrinColor*

  A String specifying the color of the intermediate principal tensor symbols. The default value is "Yellow".

- *tensorSelectedPrinColor*

  A String specifying the color of the selected principal tensor symbols. The default value is "Red".

- *tensorLineThickness*

  A SymbolicConstant specifying the line thickness of the tensor symbols. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *tensorArrowheadStyle*

  A SymbolicConstant specifying the arrowhead style of the tensor symbols. Possible values are NONE, FILLED, and WIRE. The default value is WIRE.

- *tensorMaxValueAutoCompute*

  A Boolean specifying whether the maximum tensor value is to be computed automatically. The default value is ON.

- *tensorMaxValue*

  A Float specifying the user-specified maximum tensor value. The default value is *autoTensorMaxValue*.

- *tensorMinValueAutoCompute*

  A Boolean specifying whether the minimum tensor value is to be computed automatically. The default value is ON.

- *tensorMinValue*

  A Float specifying the user-specified minimum tensor value. The default value is *autoTensorMinValue*.

### Return value

None.

### Exceptions

RangeError.



## Members

The SymbolOptions object can have the following members:

- *vectorQuantity*

  A SymbolicConstant specifying the vector quantity to display. Possible values are RESULTANT and VECTOR_COMPONENT. The default value is RESULTANT.

- *vectorMaxValueAutoCompute*

  A Boolean specifying whether the maximum vector value is to be computed automatically. The default value is ON.

- *vectorMaxValue*

  A Float specifying the user-specified maximum vector value. The default value is *autoVectorMaxValue*.

- *vectorMinValueAutoCompute*

  A Boolean specifying whether the minimum vector value is to be computed automatically. The default value is ON.

- *vectorMinValue*

  A Float specifying the user-specified minimum vector value. The default value is *autoVectorMinValue*.

- *tensorQuantity*

  A SymbolicConstant specifying the tensor quantity to display. Possible values are ALL_PRINCIPAL_COMPONENTS, PRINCIPAL_COMPONENT, ALL_DIRECT_COMPONENTS, and DIRECT_COMPONENT. The default value is ALL_PRINCIPAL_COMPONENTS.

- *tensorMaxValueAutoCompute*

  A Boolean specifying whether the maximum tensor value is to be computed automatically. The default value is ON.

- *tensorMaxValue*

  A Float specifying the user-specified maximum tensor value. The default value is *autoTensorMaxValue*.

- *tensorMinValueAutoCompute*

  A Boolean specifying whether the minimum tensor value is to be computed automatically. The default value is ON.

- *tensorMinValue*

  A Float specifying the user-specified minimum tensor value. The default value is *autoTensorMinValue*.

- *autoVectorMaxValue*

  The SymbolicConstant NOT_SET or a Float specifying the vector maximum value when *vectorMaxValueAutoCompute*=ON. This value is read-only. The default value is NOT_SET.

- *autoVectorMinValue*

  The SymbolicConstant NOT_SET or a Float specifying the vector minimum value when *vectorMinValueAutoCompute*=ON. This value is read-only. The default value is NOT_SET.

- *autoTensorMaxValue*

  The SymbolicConstant NOT_SET or a Float specifying the tensor maximum value when *tensorMaxValueAutoCompute*=ON. This value is read-only. The default value is NOT_SET.

- *autoTensorMinValue*

  The SymbolicConstant NOT_SET or a Float specifying the tensor minimum value when *tensorMinValueAutoCompute*=ON. This value is read-only. The default value is NOT_SET.

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