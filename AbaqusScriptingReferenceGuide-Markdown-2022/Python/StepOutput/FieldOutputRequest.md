# FieldOutputRequest object

The FieldOutputRequest object defines a field output request.

## Access

```
import step
mdb.models[name].fieldOutputRequests[name]
```

## FieldOutputRequest(...)



This method creates a FieldOutputRequest object.



### Path

```
mdb.models[name].FieldOutputRequest
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the object is created.

### Optional arguments

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region from which output is requested. The SymbolicConstant MODEL represents the whole model. The default value is MODEL.

- *variables*

  A sequence of Strings specifying output request variable or component names, or the SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for the given step. ALL represents all valid output variables. The default value is PRESELECT.

- *frequency*

  The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments. The default value is 1.

- *modes*

  The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired. The default value is ALL.

- *timeInterval*

  The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written. The default value is EVERY_TIME_INCREMENT.

- *numIntervals*

  An Int specifying the number of intervals during the step at which output database states are to be written. The default value is 20.

- *timeMarks*

  A Boolean specifying when to write results to the output database. OFF indicates that output is written immediately after the time dictated by the specified number of intervals. ON indicates that output is written at the exact times dictated by the specified number of intervals. The default value is OFF.

- *boltLoad*

  A String specifying a bolt load from which output is requested.

- *sectionPoints*

  The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for which output requested. The default is DEFAULT.

- *interactions*

  None or a sequence of Strings specifying the interaction names. The default value is None.The sequence can contain only one String.

- *rebar*

  A SymbolicConstant specifying whether output is requested for rebar. Possible values are EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.

- *filter*

  The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter object. The default value is None.

- *directions*

  A Boolean specifying whether to output directions of the local material coordinate system. The default value is ON.

- *fasteners*

  A String specifying the fastener name. The default value is an empty string.

- *assembledFastener*

  A String specifying the assembled fastener name. The default value is an empty string.

- *assembledFastenerSet*

  A String specifying the set name from the model referenced by the assembled fastener, *assembledFastener*. The default value is an empty string.

- *exteriorOnly*

  A Boolean specifying whether the output domain is restricted to the exterior of the model. This argument is only valid if *region*=MODEL. The default value is OFF.

- *layupNames*

  A List of Composite Layer Names.

- *layupLocationMethod*

  A Symbolic constant specifying the method used to indicate the output locations for composite layups. Possible values are ALL_LOCATIONS, SPECIFIED and TYPED_IN. The default value is SPECIFIED.

- *outputAtPlyTop*

  A Boolean specifying whether to output at the ply top section point. The default value is False.

- *outputAtPlyMid*

  A Boolean specifying whether to output at the ply mid section point. The default value is True.

- *outputAtPlyBottom*

  A Boolean specifying whether to output at the ply bottom section point. The default value is False.

- *position*

  A SymbolicConstant specifying the position on an element where output needs to be written. Possible values are INTEGRATION_POINTS, AVERAGED_AT_NODES, CENTROIDAL, and NODES. The default value is INTEGRATION_POINTS.

### Return value

A FieldOutputRequest object.

### Exceptions

None.



## deactivate(...)



This method deactivates the field output request in the specified step and all its subsequent steps.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the field output request is deactivated.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## move(...)



This method moves the field output request state object from one step to a different step.



### Required arguments

- *fromStepName*

  A String specifying the name of the step from which the field output request state is moved.

- *toStepName*

  A String specifying the name of the step to which the field output request state is moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## reset(...)



This method resets the field output request state of the specified step to the state of the previous step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the field output request state is reset.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## resume()



This method resumes the field output request that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

TextError.



## suppress()



This method suppresses the field output request.



### Arguments

None.

### Return value

None.

### Exceptions

TextError.



## setValues(...)



This method modifies the data for an existing FieldOutputRequest object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FieldOutputRequest](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?ContextScope=all#simaker-fieldoutputrequestfieldoutputrequestpyc) method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing FieldOutputRequest object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the field output request is modified.

### Optional arguments

- *variables*

  A sequence of Strings specifying output request variable or component names, or the SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for the given step. ALL represents all valid output variables.

- *frequency*

  The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments. The default value is 1.

- *modes*

  The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired. The default value is ALL.

- *timeInterval*

  The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written. The default value is EVERY_TIME_INCREMENT.

- *numIntervals*

  An Int equal to the number of intervals during the step at which output database states are to be written. The default value is 20.

- *timePoints*

  A String specifying the name of a time point object. The default value is equal to the number of intervals during the step at which output database states are to be written. The default value is None.

- *timeMarks*

  A Boolean specifying when to write results to the output database. The default value is OFF.

### Return value

None.

### Exceptions

None.



## Members

The FieldOutputRequest object can have the following members:

- *boltLoad*

  A String specifying a bolt load from which output is requested.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region from which output is requested. The SymbolicConstant MODEL represents the whole model. The default value is MODEL.

- *interactions*

  None or a tuple of Strings specifying the interaction names. The default value is None.The sequence can contain only one String.



## Corresponding analysis keywords

- [CONTACT OUTPUT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactoutput.htm?ContextScope=all#simakey-r-contactoutput)
- [ELEMENT OUTPUT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-elementoutput.htm?ContextScope=all#simakey-r-elementoutput)
- [ENERGY OUTPUT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-energyoutput.htm?ContextScope=all#simakey-r-energyoutput)
- [INCREMENTATION OUTPUT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-incrementationoutput.htm?ContextScope=all#simakey-r-incrementationoutput)
- [MODAL OUTPUT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-modaloutput.htm?ContextScope=all#simakey-r-modaloutput)
- [NODE OUTPUT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-nodeoutput.htm?ContextScope=all#simakey-r-nodeoutput)
- [OUTPUT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-output.htm?ContextScope=all#simakey-r-output)
- [RADIATION OUTPUT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-radiationoutput.htm?ContextScope=all#simakey-r-radiationoutput)