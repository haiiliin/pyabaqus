# AVIOptions object

The AVIOptions object is used to store values and attributes to be used in generating AVI animation. The AVIOptions object has no constructor. Abaqus creates the *aviOptions* member when the animation module is imported.

## Access

```
import animation
session.aviOptions
```

## setValues(...)



This method modifies the AVIOptions object.



### Required arguments

None.

### Optional arguments

- *compressionMethod*

  A SymbolicConstant specifying the compression method for the AVI format. Possible values are:

  - RAW8, specifying an uncompressed format of 8 bits per pixel.
  - RAW32, specifying an uncompressed format of 32 bits per pixel.
  - RLE8, specifying a run length encoded format of 8 bits per pixel.
  - CODEC, specifying a format defined by CODEC (encoder/decoder). The availability of the CODEC is system dependent

  The default value is RLE8.

- *compressionQuality*

  An Int specifying the quality of the compression as a percentage when the *compressionMethod* is set to CODEC.

- *codecOptions*

  A String specifying the system specific options defining the CODEC when the *compressionMethod* is set to CODEC.

- *sizeDefinition*

  A SymbolicConstant specifying how the width and height of the image are specified. Possible values are SIZE_ON_SCREEN and USER_DEFINED. The default value is SIZE_ON_SCREEN.

- *imageSize*

  A pair of Ints specifying the width and height of the image in pixels when *sizeDefinition*=USER_DEFINED. Possible values are Ints in the range (*minWidth*, *minHeight*) ≤≤ (width, height) ≤≤ (*maxWidth*, *maxHeight*). The default value is the screen size.

  Note:The values of the minimum width (*minWidth*) and height (*minHeight*) depend on the following:viewport font size,whether decorations are printed,decoration size, andscreen resolution.The minimum width and height are normally < 50 pixels. The values of the maximum width (*maxWidth*) and height (*maxHeight*) depend on the graphics capabilities of the system. The maximum width and height will be at least as large as the screen dimensions.

### Return value

None.

### Exceptions

None.



## Members

The AVIOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-avioptionspyc.htm?ContextScope=all#simaker-avioptionssetvaluespyc)method.