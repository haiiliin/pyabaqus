# Load object

The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.

## Access

```
import load
mdb.models[name].loads[name]
```

## deactivate(...)



This method deactivates the load in the specified step and all its subsequent steps.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is deactivated.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## move(...)



This method moves the load state object from one step to a different step.



### Required arguments

- *fromStepName*

  A String specifying the name of the step from which the load state is moved.

- *toStepName*

  A String specifying the name of the step to which the load state is moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## reset(...)



This method resets the load state of the specified step to the state of the previous general analysis step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load state is reset.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## resume()



This method resumes the load that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the load.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



This method allows you to delete existing loads.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each load to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Load object can have the following members:

- *name*

  A String specifying the load repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.