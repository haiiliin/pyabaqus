# AnimationController object

The AnimationController object controls all object-based animation to be displayed in the viewports. The AnimationController object has no constructor. Abaqus creates the *animationController* member when it creates the [Session](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sessionpyc.htm?ContextScope=all) object.

## Access

```
import animation
session.viewports[name].animationController
```

## play(...)



This method begins the animation.



### Required arguments

None.

### Optional arguments

- *duration*

  The SymbolicConstant UNLIMITED or an Int specifying how many seconds to play the animation. The default value is UNLIMITED.

### Return value

None.

### Exceptions

- If *animationType*=NONE:

  AnimationError: animationType not set



## stop()



This method stops the animation.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## incrementFrame()



This method increments the animation frame.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## decrementFrame()



This method decrements the animation frame.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## showFrame(...)



This method renders the specified frame of the animation.



### Required arguments

None.

### Optional arguments

- *frame*

  An Int specifying the frame number.

- *value*

  A Float specifying the frame: for *animationType*=TIME_HISTORY the frame with the time nearest to this value, for *animationType*=HARMONIC the frame with the angle nearest to this value, for *animationType*=SCALE_FACTOR the frame with the scale value nearest to this value.

### Return value

None.

### Exceptions

None.



## showFirstFrame()



This method renders the first frame of the animation.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## showLastFrame()



This method renders the last frame of the animation.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the AnimationController object.



### Required arguments

None.

### Optional arguments

- *animationType*

  A SymbolicConstant specifying the type of movie to play. Possible values are SCALE_FACTOR, HARMONIC, TIME_HISTORY, and NONE. The default value is NONE.

### Return value

None.

### Exceptions

RangeError.



## Members

The AnimationController object can have the following members:

- *animationType*

  A SymbolicConstant specifying the type of movie to play. Possible values are SCALE_FACTOR, HARMONIC, TIME_HISTORY, and NONE. The default value is NONE.

- *state*

  A SymbolicConstant specifying the state of the animation controller. Possible values are STOP and PLAY. The default value is STOP.