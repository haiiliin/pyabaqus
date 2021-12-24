# Session object

The following commands operate on Session objects. For more information about the Session object, see [Session object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sessionpyc.htm?ContextScope=all).

## Access

```
import animation
```

## writeImageAnimation(...)



This method writes the animations present in the list of canvas objects to a file. It generates an animation file using the given file name and file format and uses the values in the appropriate options object.



### Required arguments

- *fileName*

  A String specifying the name of the animation file to generate.

- *format*

  A SymbolicConstant specifying the format of the generated file. Possible values are AVI, QUICKTIME, VRML, and COMPRESSED_VRML.

### Optional arguments

- *canvasObjects*

  A sequence specifying the canvas objects to capture. The default behavior is to capture all canvas objects.

### Return value

None.

### Exceptions

None.