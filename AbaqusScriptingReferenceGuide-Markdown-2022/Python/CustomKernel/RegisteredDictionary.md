# RegisteredDictionary object

This class allows you to create a dictionary that can be queried from the GUI and is capable of notifying the GUI when the contents of the dictionary change. The keys to a RegisteredDictionary must be either strings or integers.

The RegisteredDictionary object is derived from the [CommandRegister](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-commandregisterpyc.htm?ContextScope=all) object.

## Access

```
import customKernel
```

## RegisteredDictionary()



This method creates a RegisteredDictionary object.



### Path

customKernel.RegisteredDictionary

### Arguments

None.

### Return value

A RegisteredDictionary object.

### Exceptions

None.



## Methods()



The RegisteredDictionary object supports the same methods as a Python dictionary. In addition, the RegisteredDictionary object supports the changeKey method.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## changeKey(...)



This method changes the name of a key in the dictionary.



### Required arguments

- *fromName*

  A String or an integer specifying the name of the key to be changed.

- *toName*

  A String or an integer specifying the new name for the key.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The RegisteredDictionary object has no members.