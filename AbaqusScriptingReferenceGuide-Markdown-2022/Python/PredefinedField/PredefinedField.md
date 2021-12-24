# PredefinedField object

The PredefinedField object is the base object for the objects in the predefined field repository. The methods and members of the PredefinedField object are common to all objects derived from PredefinedField.

An instance of any PredefinedField object can be obtained through the predefined field repository of the [Model](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?ContextScope=all) object. An instance of any PredefinedFieldState object can be obtained through the predefined field repository of the [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].predefinedFields[name]
```

## move(...)



This method moves a specific [PredefinedFieldState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldstatepyc.htm?ContextScope=all) object from one step to a different step.



### Required arguments

- *fromStepName*

  A String specifying the name of the step from which the [PredefinedFieldState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldstatepyc.htm?ContextScope=all) object is moved.

- *toStepName*

  A String specifying the name of the step to which the [PredefinedFieldState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldstatepyc.htm?ContextScope=all) object is moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## resume()



This method resumes the predefined field that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the predefined field.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



This method allows you to delete existing fields.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each field to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The PredefinedField object can have the following members:

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the predefined field is applied. *Region* is ignored if the predefined field has an *instances* member available. *Region* is also ignored if the predefined field has a *distributionType* member available, and *distributionType*=FROM_FILE or FROM_FILE_AND_USER_DEFINED.