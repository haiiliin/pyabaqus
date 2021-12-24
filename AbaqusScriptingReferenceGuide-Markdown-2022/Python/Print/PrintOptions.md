# PrintOptions object

The PrintOptions object stores the common settings that Abaqus uses for all print methods. The PrintOptions object has no constructor. Abaqus creates the *printOptions* member when a session is started.

## Access

```
session.printOptions
```

## setValues(...)



This method modifies the PrintOptions object.



### Required arguments

None.

### Optional arguments

- *rendition*

  A SymbolicConstant specifying how the image is rendered. Possible values are BLACK_AND_WHITE, GREYSCALE, and COLOR. The default value is COLOR.

- *vpDecorations*

  A Boolean specifying whether the output includes the viewport border and title. The default value is ON.

- *vpBackground*

  A Boolean specifying whether the output includes viewport backgrounds. The default value is OFF.

- *compass*

  A Boolean specifying whether the output includes the view compass The default value is OFF.

- *printCommand*

  A String specifying the default print command that will be used by the printToPrinter method if no *printCommand* argument is provided. The default value is "lpr".

- *deleteTemporaryFiles*

  A Boolean specifying whether to delete the temporary files created when an image is printed. The default value is ON.You should set the *deleteTemporaryFiles* argument to False if your printer does not support print spooling.

- *reduceColors*

  A Boolean specifying whether the raster image printed is reduced from true color to 256 colors to reduce file size. The quality of the image will be compromised. The default value is OFF.

### Return value

None.

### Exceptions

None.



## Members

The PrintOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-printoptionspyc.htm?ContextScope=all#simaker-printoptionssetvaluespyc)method.