# MonitorMgr object

An instance of the MonitorMgr object is created when you import the abaqus module. No other instance of the MonitorMgr object is required. (This MonitorMgr object is not to be confused with the degree of freedom (DOF) monitor that is constructed from the [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) object.)

## Access

```
monitorManager
```

## addMessageCallback(...)



This method specifies a callback function that will be called when the specified message is received from the analysis product.

For more information, see [An example of a callback function](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAECMDRefMap/simacmd-c-intaclcallback.htm?ContextScope=all).



### Required arguments

- *jobName*

  A String specifying the name of the job to be monitored or the SymbolicConstant ANY_JOB.

- *messageType*

  A SymbolicConstant specifying which message type will call this callback. Possible values are:ABORTEDANY_JOBANY_MESSAGE_TYPECOMPLETEDEND_STEPERRORHEADINGHEALER_JOBHEALER_TYPEINTERRUPTEDITERATIONJOB_ABORTEDJOB_COMPLETEDJOB_INTERRUPTEDJOB_SUBMITTEDMONITOR_DATAODB_FILEODB_FRAMESIMULATION_ABORTEDSIMULATION_COMPLETEDSIMULATION_INTERRUPTEDSIMULATION_SUBMITTEDSTARTEDSTATUSSTEPWARNING

- *callback*

  A Python function to be called. The interface definition of the callback function is :`def onMessage(jobName, messageType, data, userData)`*jobName* is a String.*messageType* is a SymbolicConstant with possible values as listed previously for the addMessageCallback method.*data* is a [DataObject](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dataobjectpyc.htm?ContextScope=all) object.*userData* is the object passed as the *userData* argument to the addMessageCallback method.

### Optional arguments

- *userData*

  Any Python object or None. This object is passed to the callback function.

### Return value

None.

### Exceptions

None.



## removeMessageCallback(...)



This method removes a callback function. You specify the callback function to remove using the same arguments you used to add the callback.



### Required arguments

- *jobName*

  A String specifying the name of the job to be monitored or the SymbolicConstant ANY_JOB.

- *messageType*

  A SymbolicConstant specifying which message type will call this callback. Possible values are:

  - ABORTED
  - ANY_JOB
  - ANY_MESSAGE_TYPE
  - COMPLETED
  - END_STEP
  - ERROR
  - HEADING
  - HEALER_JOB
  - HEALER_TYPE
  - INTERRUPTED
  - ITERATION
  - JOB_ABORTED
  - JOB_COMPLETED
  - JOB_INTERRUPTED
  - JOB_SUBMITTED
  - MONITOR_DATA
  - ODB_FILE
  - ODB_FRAME
  - SIMULATION_ABORTED
  - SIMULATION_COMPLETED
  - SIMULATION_INTERRUPTED
  - SIMULATION_SUBMITTED
  - STARTED
  - STATUS
  - STEP
  - WARNING

- *callback*

  A Python function to be called; it must be the same as the *callback* argument specified in the original call to addMessageCallback.

- *userData*

  Any Python object or None; it must be the same as the *userData* argument specified in the original call to addMessageCallback.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## checkMonitorStatus()



This method raises a MonitorError exception if the monitoring status is not ENABLED.



### Arguments

None.

### Return value

None.

### Exceptions

- MonitorError:

  Status is not ENABLED



## Members

The MonitorMgr object has no members.