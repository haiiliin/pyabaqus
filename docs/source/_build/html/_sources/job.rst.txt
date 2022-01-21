===
Job
===

The Job object is the abstract base type for other Job objects. The Job object has no explicit constructor. The methods and members of the Job object are common to all objects derived from Job.


Access
------

- `mdb.coexecutions[name].jobs[name]`
- `mdb.adaptivityProcesses[name].job`
- `mdb.jobs[name]`


Create a job
------------

.. autoclass:: abaqus.Job.JobMdb.JobMdb
    :members:


Features of the job
-------------------

.. autoclass:: abaqus.Job.ModelJob.ModelJob
    :members:
    :inherited-members:
