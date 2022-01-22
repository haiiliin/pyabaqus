==========
Mdb object
==========

Mdb commands are used to create and upgrade an Abaqus model database that stores models and analysis controls.


Attributes
----------

- **mdb.version**: An Int specifying the release number of the Mdb object in memory
- **mdb.lastChangedCount**: A Float specifying the value of a counter associated with the Mdb object. The counter indicates when the Mdb object was last changed
- **mdb.jobs[name]**: A repository of :py:class:`abaqus.Job.Job.Job` objects
- **mdb.adaptivityProcesses[name]**: A repository of :py:class:`abaqus.Adaptivity.AdaptivityProcess.AdaptivityProcess` objects
- **mdb.coexecutions[name]**: A repository of :py:class:`abaqus.Job.Coexecution.Coexecution` objects
- **mdb.optimizationProcesses[name]**: A repository of :py:class:`abaqus.Job.OptimizationProcess.OptimizationProcess` objects
- **mdb.meshEditOptions[name]**: A :py:class:`abaqus.EditMesh.MeshEditOptions.MeshEditOptions` object specifying the undo/redo behavior when editing meshes on parts or part instances
- **mdb.models[name]**: A repository of :py:class:`abaqus.Model.Model.Model` objects
- **mdb.customData**: A :py:class:`abaqus.CustomKernel.RepositorySupport.RepositorySupport` object
- **mdb.annotations**: A repository of :py:class:`abaqus.Annotation.Annotation.Annotation` objects


Create models
-------------

.. autoclass:: abaqus.Mdb.Mdb.Mdb
    :members:


Open third-party files
----------------------

.. autoclass:: abaqus.Part.AcisMdb.AcisMdb
    :members:


Create jobs
-----------

.. autoclass:: abaqus.Job.JobMdb.JobMdb
    :members:


Object features
---------------

.. autoclass:: abaqus.Mdb.MdbBase.MdbBase
    :members:
