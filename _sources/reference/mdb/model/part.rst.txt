====
Part
====

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.


Create parts
------------

.. automethod:: abaqus.Part.PartModel.PartModel.Part
    
.. automethod:: abaqus.Part.PartBase.PartBase.PartFromBooleanCut

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromBooleanMerge

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromGeometryFile

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromInstanceMesh

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromGeometryFile

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromMesh

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromMeshMirror

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromNodesAndElements

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromOdb

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromSubstructure

.. automethod:: abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromSubstructure

.. automethod:: abaqus.Part.PartBase.PartBase.PartFromSubstructure

Object features
---------------

Part
~~~~

.. autoclass:: abaqus.Part.Part.Part
    :members:
    :inherited-members:

AcisFile
~~~~~~~~

.. autoclass:: abaqus.Part.AcisFile.AcisFile
    :members:

AcisMdb
~~~~~~~

.. autoclass:: abaqus.Part.AcisMdb.AcisMdb
    :members:

Feature
~~~~~~~

.. autoclass:: abaqus.Part.Feature.Feature
    :members: