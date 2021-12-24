# writeFreeBodyReport

This command writes a free body output report to a file.

## writeFreeBodyReport



This method writes a FreeBody object to a user-defined ASCII file.



### Path

session.writeFreeBodyReport

### Required arguments

- *fileName*

  A String specifying the name of the file to which the free body output will be written.

- *append*

  A Boolean specifying whether to append the free body output to an existing file. The default value is ON.

### Optional arguments

- *step*

  An Int identifying the step from which to obtain values. The default value is the current step.

- *frame*

  An Int identifying the frame from which to obtain values. The default value is the current frame.

- *stepFrame*

  A SymbolicConstant indicating whether to obtain the values from the specified frame or from all active frames. Possible values are SPECIFY and ALL. The default value is SPECIFY.

- *odb*

  An Odb object specifying the output database from which data will be read.