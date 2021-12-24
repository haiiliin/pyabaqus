# DataObject object

An instance of the DataObject object is passed to each callback. The DataObject object has no methods. The members of a DataObject object depend on the type of the object. All DataObject instances have the following members, regardless of type:

- *clientHost*
- *clientName*
- *phase*
- *processId*
- *threadId*
- *timeStamp*

The possible DataObject types and the additional members for each type are as follows:

- ABORTED

  *message*

- COMPLETED

  *message*

- END_STEP

  *stepId*

- ERROR

  *message*

- HEADING

  *heading*

- MONITOR_DATA

  *dof**node**nset**procedure**time**value*

- ODB_FILE

  *file*

- STARTED

  No additional members.

- STATUS

  *attempts**equilibrium**increment**iterations**severe**step**stepTime**timeIncrement**totalTime*

- STEP

  *stepId**stepName*

- WARNING

  *message*

## Members

The DataObject object has the following members:

- *phase*

  A SymbolicConstant specifying the phase of the analysis. Possible values are BATCHPRE_PHASE, PACKAGER_PHASE, STANDARD_PHASE, EXPLICIT_PHASE, CALCULATOR_PHASE, and UNKNOWN_PHASE.

- *processId*

  An Int specifying the process ID of the analysis product.

- *threadId*

  An Int specifying the thread ID of the analysis product. Threads are used for parallel or multiprocessing; in most cases *threadId* is set to zero.

- *timeStamp*

  An Int specifying the time the message was sent in seconds since 00:00:00 UTC, January 1, 1970.

- *attempts*

  An Int specifying the number of attempts made to reach equilibrium during this step.

- *dof*

  An Int specifying the degree of freedom requested for monitoring the output.

- *equilibrium*

  An Int specifying the number of equilibrium iterations made during this increment.

- *increment*

  An Int specifying the increment of the analysis.

- *iterations*

  An Int specifying the number of iterations in the step.

- *node*

  An Int specifying the node number requested for monitoring output.

- *severe*

  An Int specifying the number of severe discontinuity iterations completed during this increment.

- *step*

  An Int specifying the current step number. Step number 1 corresponds to the first step.

- *stepId*

  An Int specifying the ID of the step.

- *stepTime*

  A Float specifying the step time corresponding to the current increment.

- *time*

  A Float specifying the total time corresponding to the monitor data.

- *timeIncrement*

  A Float specifying the time increment used in the current step.

- *totalTime*

  A Float specifying the total time completed in the analysis.

- *value*

  A Float specifying the current value of the degree of freedom requested for monitoring.

- *clientHost*

  A String specifying the host name of the machine that is running the analysis.

- *clientName*

  A String specifying the name of the client that responded to the callback function. Possible values are BatchPre, Packager, Standard, Explicit, and Calculator.

- *file*

  A String specifying the full path of the output database.

- *heading*

  A String specifying the job heading.

- *message*

  A String specifying the job heading.

- *nset*

  A String specifying the node set specified for monitoring output.

- *stepName*

  A String specifying the name of the step.