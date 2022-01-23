===
Job
===

The Job object is the abstract base type for other Job objects. The Job object has no explicit constructor. The methods and members of the Job object are common to all objects derived from Job.

Attributes
----------

- **mdb.models[name].steps[name].name**: A String specifying the name of the new job. The name must be a valid Abaqus/CAE object name.
- **mdb.models[name].steps[name].type**: A SymbolicConstant specifying the type of job. Possible values are ANALYSIS, SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS.If the object has the type JobFromInputFile, **type=RESTART** is not available. 
- **mdb.models[name].steps[name].waitHours**: An Int specifying the number of hours to wait before submitting the job. This argument is ignored if **queue** is set. The default value is 0.This argument works in conjunction with **waitMinutes**. **waitHours** and **atTime** are mutually exclusive.
- **mdb.models[name].steps[name].waitMinutes**: An Int specifying the number of minutes to wait before submitting the job. This argument is ignored if **queue** is set. The default value is 0.This argument works in conjunction with **waitHours**. **waitMinutes** and **atTime** are mutually exclusive.
- **mdb.models[name].steps[name].numCpus**: An Int specifying the number of CPUs to use for this analysis if parallel processing is available. Possible values are **numCpus** >> 0. The default value is 1.
- **mdb.models[name].steps[name].memory**: An Int specifying the amount of memory available to Abaqus analysis. The value should be expressed in the units supplied in **memoryUnits**. The default value is 90.
- **mdb.models[name].steps[name].memoryUnits**: A SymbolicConstant specifying the units for the amount of memory used in an Abaqus analysis. Possible values are PERCENTAGE, MEGA_BYTES, and GIGA_BYTES. The default value is PERCENTAGE.
- **mdb.models[name].steps[name].getMemoryFromAnalysis**: A Boolean specifying whether to retrieve the recommended memory settings from the last datacheck or analysis run and use those values in subsequent submissions. The default value is ON.
- **mdb.models[name].steps[name].explicitPrecision**: A SymbolicConstant specifying whether to use the double precision version of Abaqus/Explicit. Possible values are SINGLE, FORCE_SINGLE, DOUBLE, DOUBLE_CONSTRAINT_ONLY, and DOUBLE_PLUS_PACK. The default value is SINGLE.
- **mdb.models[name].steps[name].nodalOutputPrecision**: A SymbolicConstant specifying the precision of the nodal output written to the output database. Possible values are SINGLE and FULL. The default value is SINGLE.
- **mdb.models[name].steps[name].parallelizationMethodExplicit**: A SymbolicConstant specifying the parallelization method for Abaqus/Explicit. This value is ignored for Abaqus/Standard. Possible values are DOMAIN and LOOP. The default value is DOMAIN.
- **mdb.models[name].steps[name].numDomains**: An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When **parallelizationMethodExplicit=DOMAIN**, **numDomains** must be a multiple of **numCpus**. The default value is 1.
- **mdb.models[name].steps[name].activateLoadBalancing**: A Boolean specifying whether to activate dyanmic load balancing for jobs running on multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.
- **mdb.models[name].steps[name].multiprocessingMode**: A SymbolicConstant specifying whether an analysis is decomposed into threads or into multiple processes that communicate through a message passing interface (MPI). Possible values are DEFAULT, THREADS,MPI, and HYBRID. The default value is DEFAULT.
- **mdb.models[name].steps[name].numThreadsPerMpiProcess**: An Int specifying the number of threads per MPI process to use for this analysis if parallel processing is available. Possible values are **numThreadsPerMpiProcess** >> 0. The default value is 1.
- **mdb.models[name].steps[name].analysis**: A SymbolicConstant specifying whether the job will be analyzed by Abaqus/Standard or Abaqus/Explicit. Possible values are STANDARD, EXPLICIT, and UNKNOWN. If the object has the type JobFromInputFile, **analysis=UNKNOWN**.
- **mdb.models[name].steps[name].status**: A SymbolicConstant specifying whether the job will be analyzed by Abaqus/Standard or Abaqus/Explicit. Possible values are STANDARD, EXPLICIT, and UNKNOWN.If the object has the type JobFromInputFile, **analysis=UNKNOWN**. 
- **mdb.models[name].steps[name].queue**: A String specifying the name of the queue to which to submit the job. The default value is an empty string.Note:You can use the **queue** argument when creating a :py:class:`abaqus.Job.Job.Job` object on a Windows workstation; however, remote queues are available only on Linux platforms.
- **mdb.models[name].steps[name].atTime**: A String specifying the time at which to submit the job. If **queue** is empty, the string syntax must be valid for the Linux `at` command. If **queue** is set, the syntax must be valid according to the system administrator. The default value is an empty string.Note:You can use the **atTime** argument when creating a :py:class:`abaqus.Job.Job.Job` object on a Windows workstation; however, the `at` command is available only on Linux platforms.
- **mdb.models[name].steps[name].scratch**: A String specifying the location of the scratch directory. The default value is an empty string.
- **mdb.models[name].steps[name].userSubroutine**: A String specifying the file containing the user's subroutine definitions. The default value is an empty string.
- **mdb.models[name].steps[name].messages**: A :py:class:`abaqus.Job.MessageArray.MessageArray` object specifying the messages received during an analysis.
- **mdb.models[name].steps[name].environment**: A tuple of Strings specifying the environment variables and their values.
- **mdb.models[name].steps[name].licenseType**: A SymbolicConstant specifying the type of license type being used in the case of the DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not available.



Create jobs
-----------

.. autoclass:: abaqus.Job.JobMdb.JobMdb
    :members:

Create queues in Session
------------------------

.. autoclass:: abaqus.Job.JobSession.JobSession
    :members:


Features of the job
-------------------

Coexecution
~~~~~~~~~~~

.. autoclass:: abaqus.Job.Coexecution.Coexecution
    :members:

Job
~~~

.. autoclass:: abaqus.Job.Job.Job
    :members:

JobFromInputFile
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Job.JobFromInputFile.JobFromInputFile
    :members:

Message
~~~~~~~

.. autoclass:: abaqus.Job.Message.Message
    :members:

MessageArray
~~~~~~~~~~~~

.. autoclass:: abaqus.Job.MessageArray.MessageArray
    :members:

ModelJob
~~~~~~~~

.. autoclass:: abaqus.Job.ModelJob.ModelJob
    :members:

OptimizationProcess
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Job.OptimizationProcess.OptimizationProcess
    :members:

Queue
~~~~~

.. autoclass:: abaqus.Job.Queue.Queue
    :members:
