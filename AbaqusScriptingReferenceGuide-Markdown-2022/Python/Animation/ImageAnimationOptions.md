# ImageAnimationOptions object

The ImageAnimationOptions object is used to store values and attributes associated with saving viewport animations. The ImageAnimationOptions object has no constructor. Abaqus creates the *imageAnimationOptions* member when the animation module is imported.

## Access

```
import animation
session.imageAnimationOptions
```

## setValues(...)



This method modifies the ImageAnimationOptions object.



### Required arguments

None.

### Optional arguments

- *frameRate*

  An Int specifying the frame rate to record on the saved animation file. The effective frame rate in frames per second will be obtained by dividing the given frame rate by the time scale.

- *timeScale*

  An Int specifying the time scale to apply to the frame rate.

- *vpDecorations*

  A Boolean specifying whether to capture the viewport border and title. The default value is ON.

- *vpBackground*

  A Boolean specifying whether to capture viewport backgrounds. The default value is OFF.

- *compass*

  A Boolean specifying whether to capture the view compass. The default value is OFF.

### Return value

None.

### Exceptions

None.



## Members

The ImageAnimationOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-imageanimationoptionspyc.htm?ContextScope=all#simaker-imageanimationoptionssetvaluespyc)method.