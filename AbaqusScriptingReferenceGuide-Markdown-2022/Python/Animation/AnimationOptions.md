# AnimationOptions object

The AnimationOptions object is used to store values and attributes associated with an [AnimationController](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-animationcontrollerpyc.htm?ContextScope=all) object.

The AnimationOptions object has no constructor command. Abaqus creates the *animationOptions* member when it creates the [AnimationController](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-animationcontrollerpyc.htm?ContextScope=all) object.

## Access

```
import animation
session.animationOptions
```

## setValues(...)



This method modifies the AnimationOptions object.



### Required arguments

None.

### Optional arguments

- *mode*

  A SymbolicConstant specifying the animation mode. Possible values are PLAY_ONCE, LOOP, LOOP_BACKWARD, and SWING. The default value is LOOP.

- *frameRate*

  An Int specifying the animation rate in frames/second. Possible values are 1 ≤≤ *frameRate* ≤≤ 100. The default value is 50.

- *frameCounter*

  A Boolean specifying whether to show the frame counter. The default value is ON.

- *relativeScaling*

  A SymbolicConstant specifying the relative scaling when the [AnimationController](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-animationcontrollerpyc.htm?ContextScope=all) object's *animationType*=SCALE_FACTOR or HARMONIC. Possible values are FULL_CYCLE and HALF_CYCLE. The default value is HALF_CYCLE.

- *numScaleFactorFrames*

  An Int specifying the number of frames to be used when the [AnimationController](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-animationcontrollerpyc.htm?ContextScope=all) object's *animationType*=SCALE_FACTOR or HARMONIC. The default value is 7.

- *timeHistoryMode*

  A SymbolicConstant specifying whether the time history animation is time based or frame based. Possible values are FRAME_BASED and TIME_BASED. The default value is FRAME_BASED.

- *maxTime*

  A Float specifying the maximum time for time based time history animation when *maxTimeAutoCompute* = False.

- *maxTimeAutoCompute*

  A Boolean specifying whether the animation maximum time value should be computed from the active frames when *timeHistoryMode* is set to TIME_BASED. The default value is ON.

- *minTime*

  A Float specifying the minimum time for time based time history animation when *minTimeAutoCompute* = False.

- *minTimeAutoCompute*

  A Boolean specifying whether the animation minimum time value should be computed from the active frames when *timeHistoryMode* is set to TIME_BASED. The default value is ON.

- *timeIncrement*

  A Float specifying the time increment for frame selection when *timeHistoryMode* is set to TIME_BASED.

- *xyUseHighlightMethod*

  A Boolean specifying whether to use the highlight method to draw the time tracker line and symbols. The default value is ON.

- *xyShowLine*

  A Boolean specifying whether to show the time tracker line. The default value is ON.

- *xyLineStyle*

  A SymbolicConstant specifying the *X–Y* time tracker line style. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.

- *xyLineThickness*

  A SymbolicConstant specifying the *X–Y* time tracker line thickness. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is MEDIUM.

- *xyLineColor*

  A String specifying the color used to plot the *X–Y* time tracker line when *xyUseHighlightMethod* = False. The default value is "Yellow".

- *xyShowSymbol*

  A Boolean specifying whether to show the time tracker symbols. The default value is ON.

- *xySymbolMarker*

  A SymbolicConstant specifying the marker type to be used for all animation capable *X–Y* curve or the SymbolicConstant DEFAULT specifying that the system will take the marker associated to each curve Possible values are:

  - FILLED_CIRCLE
  - FILLED_SQUARE
  - FILLED_DIAMOND
  - FILLED_TRI
  - HOLLOW_CIRCLE
  - HOLLOW_SQUARE
  - HOLLOW_DIAMOND
  - HOLLOW_TRI
  - CROSS
  - XMARKER
  - DEFAULT

  The default value is DEFAULT.

- *xySymbolSize*

  A SymbolicConstant specifying the size of the markers. Possible values are SMALL, MEDIUM, and LARGE. The default value is MEDIUM.

- *xySymbolColor*

  A String specifying the color used to plot *X–Y* time tracker symbols when *xyUseHighlightMethod* = False. When setting the color to 'Default' the system will take the color associated to each curve. The default value is "Default".

### Return value

None.

### Exceptions

None.



## Members

The AnimationOptions object can have the following members:

- *mode*

  A SymbolicConstant specifying the animation mode. Possible values are PLAY_ONCE, LOOP, LOOP_BACKWARD, and SWING. The default value is LOOP.

- *frameRate*

  An Int specifying the animation rate in frames/second. Possible values are 1 ≤≤ *frameRate* ≤≤ 100. The default value is 50.

- *frameCounter*

  A Boolean specifying whether to show the frame counter. The default value is ON.

- *relativeScaling*

  A SymbolicConstant specifying the relative scaling when the [AnimationController](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-animationcontrollerpyc.htm?ContextScope=all) object's *animationType*=SCALE_FACTOR or HARMONIC. Possible values are FULL_CYCLE and HALF_CYCLE. The default value is HALF_CYCLE.

- *numScaleFactorFrames*

  An Int specifying the number of frames to be used when the [AnimationController](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-animationcontrollerpyc.htm?ContextScope=all) object's *animationType*=SCALE_FACTOR or HARMONIC. The default value is 7.

- *timeHistoryMode*

  A SymbolicConstant specifying whether the time history animation is time based or frame based. Possible values are FRAME_BASED and TIME_BASED. The default value is FRAME_BASED.

- *maxTime*

  A Float specifying the maximum time for time based time history animation when *maxTimeAutoCompute* = False.

- *maxTimeAutoCompute*

  A Boolean specifying whether the animation maximum time value should be computed from the active frames when *timeHistoryMode* is set to TIME_BASED. The default value is ON.

- *maxTimeAutoValue*

  A Float specifying the maximum time when *timeHistoryMode* is set to TIME_BASED and the *maxTimeAutoCompute* value is True. This value is computed as the maximum time of all active frames displayed in viewports where the animation is active.

- *minTime*

  A Float specifying the minimum time for time based time history animation when *minTimeAutoCompute* = False.

- *minTimeAutoCompute*

  A Boolean specifying whether the animation minimum time value should be computed from the active frames when *timeHistoryMode* is set to TIME_BASED. The default value is ON.

- *minTimeAutoValue*

  A Float specifying the minimum time when *timeHistoryMode* is set to TIME_BASED and the *minTimeAutoCompute* value is True. This value is computed as the minimum time of all active frames displayed in viewports where the animation is active.

- *timeIncrement*

  A Float specifying the time increment for frame selection when *timeHistoryMode* is set to TIME_BASED.

- *xyUseHighlightMethod*

  A Boolean specifying whether to use the highlight method to draw the time tracker line and symbols. The default value is ON.

- *xyShowLine*

  A Boolean specifying whether to show the time tracker line. The default value is ON.

- *xyLineStyle*

  A SymbolicConstant specifying the *X–Y* time tracker line style. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.

- *xyLineThickness*

  A SymbolicConstant specifying the *X–Y* time tracker line thickness. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is MEDIUM.

- *xyShowSymbol*

  A Boolean specifying whether to show the time tracker symbols. The default value is ON.

- *xySymbolMarker*

  A SymbolicConstant specifying the marker type to be used for all animation capable *X–Y* curve or the SymbolicConstant DEFAULT specifying that the system will take the marker associated to each curve Possible values are:

  - FILLED_CIRCLE
  - FILLED_SQUARE
  - FILLED_DIAMOND
  - FILLED_TRI
  - HOLLOW_CIRCLE
  - HOLLOW_SQUARE
  - HOLLOW_DIAMOND
  - HOLLOW_TRI
  - CROSS
  - XMARKER
  - DEFAULT

  The default value is DEFAULT.

- *xySymbolSize*

  A SymbolicConstant specifying the size of the markers. Possible values are SMALL, MEDIUM, and LARGE. The default value is MEDIUM.

- *xyLineColor*

  A String specifying the color used to plot the *X–Y* time tracker line when *xyUseHighlightMethod* = False. The default value is "Yellow".

- *xySymbolColor*

  A String specifying the color used to plot *X–Y* time tracker symbols when *xyUseHighlightMethod* = False. When setting the color to 'Default' the system will take the color associated to each curve. The default value is "Default".