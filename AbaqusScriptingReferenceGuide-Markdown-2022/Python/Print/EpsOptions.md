# EpsOptions object

The EpsOptions object stores the settings that Abaqus uses when printing using Encapsulated PostScript format. The EpsOptions object has no constructor. Abaqus creates the *epsOptions* member when a session is started.

## Access

```
session.epsOptions
```

## setValues(...)



This method modifies the EpsOptions object.



### Required arguments

None.

### Optional arguments

- *imageSize*

  The SymbolicConstant SIZE_ON_SCREEN or a pair of Floats specifying the width and height of the image in the units specified by *units*. Possible numeric values are *imageSize* ≥≥ (*minWidth*, *minHeight*). The default value is SIZE_ON_SCREEN.Note:The minimum value of width and height (*minWidth* and *minHeight*) is 10 mm (approximately 0.4 inches).

- *units*

  A SymbolicConstant specifying the units of the *imageSize* argument. This argument is ignored if *imageSize* is SIZE_ON_SCREEN. Possible values are INCHES and MM. The default value is INCHES.

- *resolution*

  A SymbolicConstant specifying the resolution of the image in dots per inch (dpi). The *resolution* can be DPI_1200 only if *imageFormat*=VECTOR. Possible values are DPI_75, DPI_150, DPI_300, DPI_450, DPI_600, and DPI_1200. The default value is DPI_150.

- *fontType*

  A SymbolicConstant specifying the PostScript font substitution rules to be applied. Possible values are PS_ALWAYS, PS_IF_AVAILABLE, and AS_DISPLAYED. The default value is PS_IF_AVAILABLE.

- *imageFormat*

  A SymbolicConstant specifying how the viewport display will be represented. Possible values are VECTOR and RASTER. The default value is VECTOR.

- *shadingQuality*

  A SymbolicConstant specifying how fine the shading of curved surfaces will be for vector images. Possible values are EXTRA COARSE, COARSE, MEDIUM, FINE, and EXTRA FINE. The default value is MEDIUM.

### Return value

None.

### Exceptions

RangeError.

- If either element of *imageSize* is out of range:

  RangeError: imageSize must be SIZE_ON_SCREEN or a sequence of 2 Floats >= (*minWidth*, *minHeight*)



## Members

The EpsOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-epsoptionspyc.htm?ContextScope=all#simaker-epsoptionssetvaluespyc)method.