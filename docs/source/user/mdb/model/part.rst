====
Part
====

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.

Create parts
------------

.. autoclass:: abaqus.Part.PartModel.PartModel

.. autoclass:: abaqus.Part.PartBase.PartBase
    
    .. automethod:: PartFromBooleanCut
    .. automethod:: PartFromBooleanMerge
    .. automethod:: PartFromExtrude2DMesh
    .. automethod:: PartFromGeometryFile
    .. automethod:: PartFromInstanceMesh
    .. automethod:: PartFromGeometryFile
    .. automethod:: PartFromMesh
    .. automethod:: PartFromMeshMirror
    .. automethod:: PartFromNodesAndElements
    .. automethod:: PartFromOdb
    .. automethod:: PartFromSection3DMeshByPlane
    .. automethod:: PartFromSubstructure
    .. automethod:: Part2DGeomFrom2DMesh
    .. automethod:: PartFromSubstructure
    .. automethod:: PartFromSubstructure
