# HistoryOutputRequest object

The HistoryOutputRequest object defines a history output request.

## Access

```
import step
mdb.models[name].historyOutputRequests[name]
```

## HistoryOutputRequest(...)



This method creates a HistoryOutputRequest object.



### Path

```
mdb.models[name].HistoryOutputRequest
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the object is created.

### Optional arguments

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region from which output is requested. The SymbolicConstant MODEL represents the whole model. The default value is MODEL.If the region is a surface region, the surface must lie within the general contact surface domain.

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

- *boltLoad*

  A String specifying a bolt load from which output is requested. The default value is an empty string.

- *sectionPoints*

  The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for which output is requested. The default value is DEFAULT.

- *stepName*

  A String specifying the name of the step. The default value is an empty string.

- *interactions*

  None or a sequence of Strings specifying the interaction names. The default value is None.The sequence can contain only one String.

- *contourIntegral*

  A String specifying the contour integral name. The default value is None.

- *numberOfContours*

  An Int specifying the number of contour integrals to output for the contour integral object. The default value is 0.

- *stressInitializationStep*

  A String specifying the name of the stress initialization step. The default value is None.

- *contourType*

  A SymbolicConstant specifying the type of contour integral. Possible values are J_INTEGRAL, C_INTEGRAL, T_STRESS, and K_FACTORS. The default value is J_INTEGRAL.

- *kFactorDirection*

  A SymbolicConstant specifying the stress intensity factor direction. Possible values are MTS, MERR, and K110. The *kFactorDirection* argument is valid only if *contourType*=K_FACTORS. The default value is MTS.

- *rebar*

  A SymbolicConstant specifying whether output is requested for rebar. Possible values are EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.

- *integratedOutputSection*

  A String specifying the integrated output section. The default value is an empty string.

- *springs*

  A sequence of Strings specifying the springs/dashpots names. The default value is None. The sequence can contain only one String.

- *filter*

  The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter object. The default value is None.

- *fasteners*

  A String specifying the fastener name. The default value is an empty string.

- *assembledFastener*

  A String specifying the assembled fastener name. The default value is an empty string.

- *assembledFastenerSet*

  A String specifying the set name from the model referenced by the assembled fastener, *assembledFastener*. The default value is an empty string.

- *sensor*

  A Boolean specifying whether to associate the output request with a sensor definition. The default value is OFF.

- *useGlobal*

  A Boolean specifying whether to output vector-valued nodal variables in the global directions. The default value is True.

### Return value

A HistoryOutputRequest object.

### Exceptions

None.



## deactivate(...)



This method deactivates the history output request in the specified step and all subsequent steps.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the history output request is deactivated.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## move(...)



This method moves the history output request state object from one step to a different step.



### Required arguments

- *fromStepName*

  A String specifying the name of the step from which the history output request state is moved.

- *toStepName*

  A String specifying the name of the step to which the history output request state is moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## reset(...)



This method resets the history output request state of the specified step to the state of the previous step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the history output request state is reset.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## resume()



This method resumes the history output request that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

TextError.



## suppress()



This method suppresses the history output request.



### Arguments

None.

### Return value

None.

### Exceptions

TextError.



## setValues(...)



This method modifies the data for an existing HistoryOutputRequest object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [HistoryOutputRequest ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?ContextScope=all#simaker-historyoutputrequesthistoryoutputrequestpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing HistoryOutputRequest object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the history output request is modified.

### Optional arguments

- *variables*

  A sequence of Strings specifying output request variable or component names or the SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for the given step. ALL represents all valid output variables.

- *frequency*

  The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments. The default value is 1.

- *modes*

  The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired. The default value is ALL.

- *timeInterval*

  The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written. The default value is EVERY_TIME_INCREMENT.

- *numIntervals*

  An Int specifying the number of intervals during the step at which output database states are to be written. The default value is 20.

- *timePoints*

  A String specifying the name of a time point object. The default value is equal to the number of intervals during the step at which output database states are to be written. The default value is None.

### Return value

None.

### Exceptions

None.



## Members

The HistoryOutputRequest object can have the following members:

- *boltLoad*

  A String specifying a bolt load from which output is requested. The default value is an empty string.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region from which output is requested. The SymbolicConstant MODEL represents the whole model. The default value is MODEL.If the region is a surface region, the surface must lie within the general contact surface domain.

- *sectionPoints*

  The SymbolicConstant DEFAULT or a tuple of Ints specifying the section points for which output is requested. The default value is DEFAULT.

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