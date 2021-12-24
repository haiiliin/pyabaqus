# Message object

The Message object contains information about a given phase of the simulation. Job messages are not returned if a script is run without the Abaqus/CAE GUI (using the noGUI option).

## Access

```
import job
mdb.coexecutions[name].jobs[name].messages[i]
mdb.jobs[name].messages[i]
```

## Members

The Message object has the following members:

- *type*

  A SymbolicConstant specifying the type of message. Possible values are:

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
  - STARTED
  - STATE_FRAME
  - STATUS
  - STEP
  - WARNING

- *data*

  A Dictionary object specifying the data returned by the analysis product. The value depends on the message returned. For a list of the possible entries, see the members of [DataObject](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dataobjectpyc.htm?ContextScope=all).