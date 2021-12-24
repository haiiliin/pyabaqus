# AbaqusBoolean object

The AbaqusBoolean object is used in a similar way to the SymbolicConstant object. If you pass an AbaqusBoolean object to the Python repr() function, the function returns the text without quotes. In effect, the text is the variable that, by convention, refers to the AbaqusBoolean object.

An AbaqusBoolean object has a value of 0 or 1, and an AbaqusBoolean object can be tested in an if statement. You can use an AbaqusBoolean object as an argument to a method in place of 1 or 0. Conversely, you can pass a 0 or a 1 to an Abaqus Scripting Interface method that expects a Boolean argument, and the 0 or 1 will be coerced to the appropriate AbaqusBoolean value.

There are only two possible values for an AbaqusBoolean object: 1 and 0. You can import both values from the symbolicConstants module or from the abaqus module. Abaqus Scripting Interface commands that expect an AbaqusBoolean object will also accept a Python bool (True, False), or a Python int (1, 0).

## Access

```
from symbolicConstants import *
from abaqusConstants import *
```

## AbaqusBoolean(...)



The AbaqusBoolean method creates an AbaqusBoolean object.



### Path

AbaqusBoolean

### Required arguments

- *value*

  An Int specifying whether the AbaqusBoolean object will test true or false. Possible values are 0 and 1, which will create the AbaqusBoolean method OFF and ON, respectively.

### Optional arguments

None.

### Return value

An AbaqusBoolean object.

### Exceptions

None.