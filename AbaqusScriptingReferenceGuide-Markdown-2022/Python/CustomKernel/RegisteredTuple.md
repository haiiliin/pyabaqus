# RegisteredTuple object

This class allows you to create a tuple that can be queried from the GUI and is capable of notifying the GUI when the contents of any of the tuple's members change.

The RegisteredTuple object is derived from the [CommandRegister](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-commandregisterpyc.htm?ContextScope=all) object.

## Access

```
import customKernel
```

## RegisteredTuple(...)



This method creates a RegisteredTuple object.



### Path

customKernel.RegisteredTuple

### Required arguments

- *tuple*

  A tuple of objects. These objects must be derived from the CommandRegister class.

### Optional arguments

None.

### Return value

A RegisteredTuple object.

### Exceptions

None.



## Methods()



The RegisteredTuple object supports the same methods as a standard Python list object.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The RegisteredTuple object has no members.