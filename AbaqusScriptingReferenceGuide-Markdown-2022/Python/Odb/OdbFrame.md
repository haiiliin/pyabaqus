# OdbFrame object

The domain of the OdbFrame object is taken from the parent step.

## Access

```
import odbAccess
session.odbs[name].steps[name].frames[i]
```

## Frame(...)



This method creates an OdbFrame object and appends it to the frame sequence.



### Path

```
session.odbs[name].steps[name].Frame
```

### Required arguments

- *incrementNumber*

  An Int specifying the frame increment number within the step. The base frame has normally increment number 0, and the results run from 1. In case of multiple load cases, the same increment number is duplicated for each loadcase.

- *frameValue*

  A Float specifying the value in units determined by the *domain* member of the [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) object. The equivalent in the time domain is *stepTime*; in the frequency domain the equivalent is *frequency*; and in the modal domain the equivalent is *mode*.

### Optional arguments

- *description*

  A String specifying the contents of the frame. The default value is an empty string.

### Return value

An OdbFrame object.

### Exceptions

None.

## Frame(...)



This constructor creates an OdbFrame object in the frequency domain and appends it to the frame sequence. The arguments to the constructor are valid only when *domain*=FREQUENCY or *domain*=MODAL.



### Path

```
session.odbs[name].steps[name].Frame
```

### Required arguments

- *mode*

  An Int specifying the eigenmode. This member is valid only if *domain*=MODAL.

- *frequency*

  A Float specifying the frequency. This member is valid only if *domain*=FREQUENCY or if the *procedureType* member of the [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) object=FREQUENCY. The default value is 0.0.

### Optional arguments

- *description*

  A String specifying the contents of the frame. The default value is an empty string.

### Return value

An OdbFrame object.

### Exceptions

None.

## Frame(...)



This constructor creates an OdbFrame object for a specific load case and appends it to the frame sequence.



### Path

```
session.odbs[name].steps[name].Frame
```

### Required arguments

- *loadCase*

  An [OdbLoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?ContextScope=all) object specifying the load case for the frame.

### Optional arguments

- *description*

  A String specifying the contents of the frame. The default value is an empty string.

- *frequency*

  A Float specifying the frequency. This member is valid only if *domain*=FREQUENCY or if the *procedureType* member of the [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) object=FREQUENCY. The default value is 0.0.

### Return value

An OdbFrame object.

### Exceptions

None.



## Members

The OdbFrame object has members with the same names and descriptions as the arguments to the [Frame ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all#simaker-odbframeframepyc)method.

In addition, the OdbFrame object can have the following members:

- *cyclicModeNumber*

  An Int specifying the cyclic mode number associated with the data stored on this frame. Only frequency analyses of cyclic symmetry models possess cyclic mode numbers.

- *domain*

  A SymbolicConstant specifying the domain of the step of which the frame is a member. Possible values are TIME, FREQUENCY, and MODAL.

- *frequency*

  A Float specifying the frequency. This member is valid only if *domain*=FREQUENCY or if the *procedureType* member of the [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) object=FREQUENCY. The default value is 0.0.

- *mode*

  An Int specifying the eigenmode. This member is valid only if *domain*=MODAL.

- *associatedFrame*

  An OdbFrame object specifying the real or imaginary portion of the data corresponding to this cyclic symmetry mode.

- *fieldOutputs*

  A repository of [FieldOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?ContextScope=all) objects specifying the key to the *fieldOutputs*repository is a String representing an output variable.

- *loadCase*

  An [OdbLoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?ContextScope=all) object specifying the load case for the frame.