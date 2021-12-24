# Coexecution object

The Coexecution object contains a set of jobs as associated parameters to define a co-simulation analysis.

## Access

```
import job
mdb.coexecutions[name]
```

## kill()



This method kills the analysis of a co-execution.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## submit(...)



This method submits a co-execution for analysis.



### Required arguments

None.

### Optional arguments

- *consistencyChecking*

  A Boolean specifying whether to perform consistency checking for the individual jobs. The default value is ON. It is not recommended to turn the consistency checking off unless you are absolutely sure the models are all consistent.

- *datacheckJob*

  A Boolean specifying whether to run the co-execution as a datacheck analysis. The default value is False. The *datacheckJob* and *continueJob* arguments cannot both be True.

- *continueJob*

  A Boolean specifying whether to run the co-execution as a continuation analysis. The default value is False. The *datacheckJob* and *continueJob* arguments cannot both be True.

### Return value

None.

### Exceptions

None.



## writeInput(...)



This method writes an input file for each analysis in the co-execution.



### Required arguments

None.

### Optional arguments

- *consistencyChecking*

  A Boolean specifying whether to perform consistency checking for the individual jobs. The default value is ON. It is not recommended to turn the consistency checking off unless you are absolutely sure the models are all consistent.

### Return value

None.

### Exceptions

None.



## waitForCompletion()



This method interrupts the execution of the script until the end of all the analyses. If you call the waitForCompletion method and the *status* member is neither SUBMITTED nor RUNNING, Abaqus assumes the analysis has either completed or aborted and returns immediately.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Coexecution object can have the following members:

- *name*

  A String specifying the name of the new job. The name must be a valid Abaqus/CAE object name.

- *type*

  A SymbolicConstant specifying the type of analysis to execute for the co-execution. Possible values are ANALYSIS, SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS.

- *mainAnalysisProduct*

  A SymbolicConstant specifying the analysis product type of the main model for the co-execution. The default value is ABAQUS.

- *waitHours*

  An Int specifying the number of hours to wait before submitting the co-execution. This argument is ignored if *queue* is set. The default value is 0.This argument works in conjunction with *waitMinutes*. *waitHours* and *atTime* are mutually exclusive.

- *waitMinutes*

  An Int specifying the number of minutes to wait before submitting the job. This argument is ignored if *queue* is set. The default value is 0.This argument works in conjunction with *waitHours*. *waitMinutes* and *atTime* are mutually exclusive.

- *status*

  A SymbolicConstant specifying the status of the co-execution. Possible values are SUBMITTED, RUNNING, ABORTED, TERMINATED, COMPLETED, CHECK_SUBMITTED, CHECK_RUNNING, and CHECK_COMPLETED.If the *message* member of all the jobs are empty, *status* is set to NONE.

- *queue*

  A String specifying the name of the queue to which to submit the co-execution. The default value is an empty string.Note:You can use the *queue* argument when creating a Coexecution object on a Windows workstation; however, remote queues are available only on Linux platforms.

- *atTime*

  A String specifying the time at which to submit the co-execution. If *queue* is empty, the string syntax must be valid for the Linux `at` command. If *queue* is set, the syntax must be valid according to the system administrator. The default value is an empty string.Note:You can use the *atTime* argument when creating a Coexecution object on a Windows workstation; however, the `at` command is available only on Linux platforms.

- *jobs*

  A repository of [Job](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobpyc.htm?ContextScope=all) objects specifying the jobs that comprise this co-execution.

- *secondaryModels*

  A tuple of Strings specifying the names of the secondary models for the co-execution.

- *secondaryAnalysisProducts*

  A tuple of SymbolicConstants specifying the analysis product types of the secondary models for the co-execution. The default value is an empty sequence.

- *mainModel*

  A String specifying the name of the main model for the co-execution.

- *licenseType*

  A SymbolicConstant specifying the type of license type being used in case of DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default value is DEFAULT.If the license model is not DSLS SimUnit then the licenseType is not available.



## Corresponding analysis keywords

- [HEADING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-heading.htm?ContextScope=all#simakey-r-heading)
- [PREPRINT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-preprint.htm?ContextScope=all#simakey-r-preprint)