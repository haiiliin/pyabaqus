# JobFromInputFile object

The JobFromInputFile object defines a [Job](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobpyc.htm?ContextScope=all) object which analyzes a model contained in an input file.

The JobFromInputFile object is derived from the [Job](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobpyc.htm?ContextScope=all) object.

## Access

```
import job
mdb.jobs[name]
```

## JobFromInputFile(...)



This method creates an analysis job using an input file for the model definition.



### Path

```
mdb.JobFromInputFile
```

### Required arguments

- *name*

  A String specifying the name of the new job. The name must be a valid Abaqus/CAE object name.

- *inputFileName*

  A String specifying the input file to read. Possible values are any valid file name. If the .inp extension is not included in the value of the argument, the system will append it for the user.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of job. Possible values are ANALYSIS, SYNTAXCHECK, and RECOVER. The default value is ANALYSIS.For theJobFromInputFile object, *type*=RESTART is not currently supported.

- *queue*

  A String specifying the name of the queue to which to submit the job. The default value is an empty string.Note: You can use the *queue* argument when creating a Job object on a Windows workstation; however, remote queues are available only on Linux platforms.

- *waitHours*

  An Int specifying the number of hours to wait before submitting the job. This argument is ignored if *queue* is set. The default value is 0.This argument works in conjunction with *waitMinutes*. *waitHours* and *atTime* are mutually exclusive.

- *waitMinutes*

  An Int specifying the number of minutes to wait before submitting the job. This argument is ignored if *queue* is set. The default value is 0.This argument works in conjunction with *waitHours*. *waitMinutes* and *atTime* are mutually exclusive.

- *atTime*

  A String specifying the time at which to submit the job. If *queue* is empty, the string syntax must be valid for the Linux `at` command. If *queue* is set, the syntax must be valid according to the system administrator. The default value is an empty string.Note: You can use the *atTime* argument when creating a Job object on a Windows workstation; however, the `at` command is available only on Linux platforms.

- *scratch*

  A String specifying the location of the scratch directory. The default value is an empty string.

- *userSubroutine*

  A String specifying the file containing the user's subroutine definitions. The default value is an empty string.

- *numCpus*

  An Int specifying the number of CPUs to use for this analysis if parallel processing is available. Possible values are *numCpus* >> 0. The default value is 1.

- *memory*

  An Int specifying the amount of memory available to Abaqus analysis. The value should be expressed in the units supplied in *memoryUnits*. The default value is 90.

- *memoryUnits*

  A SymbolicConstant specifying the units for the amount of memory used in an Abaqus analysis. Possible values are PERCENTAGE, MEGA_BYTES, and GIGA_BYTES. The default value is PERCENTAGE.

- *explicitPrecision*

  A SymbolicConstant specifying whether to use the double precision version of Abaqus/Explicit. Possible values are SINGLE, FORCE_SINGLE, DOUBLE, DOUBLE_CONSTRAINT_ONLY, and DOUBLE_PLUS_PACK. The default value is SINGLE.

- *nodalOutputPrecision*

  A SymbolicConstant specifying the precision of the nodal output written to the output database. Possible values are SINGLE and FULL. The default value is SINGLE.

- *parallelizationMethodExplicit*

  A SymbolicConstant specifying the parallelization method for Abaqus/Explicit. This value is ignored for Abaqus/Standard. Possible values are DOMAIN and LOOP. The default value is DOMAIN.

- *numDomains*

  An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When *parallelizationMethodExplicit*=DOMAIN, *numDomains* must be a multiple of *numCpus*. The default value is 1.

- *activateLoadBalancing*

  A Boolean specifying whether to activate dyanmic load balancing for jobs running on multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.

- *multiprocessingMode*

  A SymbolicConstant specifying whether an analysis is decomposed into threads or into multiple processes that communicate through a message passing interface (MPI). Possible values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.

- *licenseType*

  A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not available.

### Return value

A JobFromInputFile object.

### Exceptions

AbaqusException

ValueError

- If the user attempts to provide RESTART as a value to argument type:

  ValueError: RESTART of input file job is not currently supported



## setValues(...)



This method modifies the JobFromInputFile object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [JobFromInputFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobfrominputfilepyc.htm?ContextScope=all#simaker-jobfrominputfilejobfrominputfilepyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The JobFromInputFile object has members with the same names and descriptions as the arguments to the [JobFromInputFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobfrominputfilepyc.htm?ContextScope=all#simaker-jobfrominputfilejobfrominputfilepyc) method.

In addition, the JobFromInputFile object can have the following members:

- *getMemoryFromAnalysis*

  A Boolean specifying whether to retrieve the recommended memory settings from the last datacheck or analysis run and use those values in subsequent submissions. The default value is ON.

- *analysis*

  A SymbolicConstant specifying whether the job will be analyzed by Abaqus/Standard or Abaqus/Explicit. Possible values are STANDARD, EXPLICIT, and UNKNOWN.If the object has the type JobFromInputFile, *analysis*=UNKNOWN.

- *status*

  A SymbolicConstant specifying the status of the analysis. Possible values are SUBMITTED, RUNNING, ABORTED, TERMINATED, COMPLETED, CHECK_RUNNING, and CHECK_COMPLETED.If the *message* member is empty, *status* is set to NONE.

- *messages*

  A [MessageArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-messagepyc.htm?ContextScope=all) object specifying the messages received during an analysis.

- *environment*

  A tuple of Strings specifying the environment variables and their values.