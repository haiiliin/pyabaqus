# Callback commands

These functions execute Python commands or functions.

## addImportCallback



This function defines a function to be called when a specified Abaqus/CAE module is imported. You cannot specify a custom module.

For more information, see [An example of a callback function](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAECMDRefMap/simacmd-c-intaclcallback.htm?ContextScope=all).



### Path

addImportCallback

### Required arguments

- *moduleName*

  A String specifying the name of a specified Abaqus/CAE module.

- *callback*

  A Python function to be called. The interface definition of the callback function is :`def functionName(moduleName, userData)`*moduleName* is a String.*userData* is the object passed as the *userData* argument to the addImportCallback method.

### Optional arguments

- *userData*

  Any Python object or None. This object is passed to the callback function.

### Return value

None.

### Exceptions

None.



## removeImportCallback



This function removes a callback added in addImportCallback.



### Path

removeImportCallback

### Required arguments

- *callback*

  A Python function to be called; it must be the same as the *callback* argument specified in the original call to addImportCallback.

- *userData*

  Any Python object or None; it must be the same as the *userData* argument specified in the original call to addImportCallback.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.