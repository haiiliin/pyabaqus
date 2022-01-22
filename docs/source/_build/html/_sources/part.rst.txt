====
Part
====

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.


Create parts
------------

.. autoclass:: abaqus.Part.PartModel.PartModel
    :members:

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

Object features
---------------

Basic features of Part
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Part.PartBase.PartBase
    
    .. automethod:: setValues
    .. automethod:: addGeomToSketch
    .. automethod:: assignThickness
    .. automethod:: backup
    .. automethod:: checkGeometry
    .. automethod:: clearGeometryCache
    .. automethod:: deleteAllFeatures
    .. automethod:: deleteFeatures
    .. automethod:: getAngle
    .. automethod:: getAssociatedCADPaths
    .. automethod:: getCADParameters
    .. automethod:: getCentroid
    .. automethod:: getCoordinates
    .. automethod:: getCurvature
    .. automethod:: getDistance
    .. automethod:: getLength
    .. automethod:: getPerimeter
    .. automethod:: getVolume
    .. automethod:: getMassProperties
    .. automethod:: getFeatureFaces
    .. automethod:: getFeatureEdges
    .. automethod:: getFeatureCells
    .. automethod:: getFeatureVertices
    .. automethod:: isAlignedWithSketch
    .. automethod:: printAssignedSections
    .. automethod:: projectEdgesOntoSketch
    .. automethod:: projectReferencesOntoSketch
    .. automethod:: queryAttributes
    .. automethod:: queryCachedStates
    .. automethod:: queryGeometry
    .. automethod:: queryRegionsMissingSections
    .. automethod:: queryDisjointPlyRegions
    .. automethod:: regenerate
    .. automethod:: regenerationWarnings
    .. automethod:: removeInvalidGeometry
    .. automethod:: restore
    .. automethod:: resumeAllFeatures
    .. automethod:: resumeFeatures
    .. automethod:: resumeLastSetFeatures
    .. automethod:: saveGeometryCache
    .. automethod:: setAssociatedCADPaths
    .. automethod:: suppressFeatures
    .. automethod:: writeAcisFile
    .. automethod:: writeCADParameters
    .. automethod:: writeIgesFile
    .. automethod:: writeStepFile
    .. automethod:: writeVdaFile
    .. automethod:: copyMeshPattern
    .. automethod:: smoothNodes
    .. automethod:: Lock
    .. automethod:: Unlock
    .. automethod:: LockForUpgrade


Edit Mesh features of Part
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.EditMesh.MeshEditPart.MeshEditPart
    :members:


Mesh features of Part
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Mesh.MeshPart.MeshPart
    :members:


Property features of Part
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Property.PropertyPart.PropertyPart
    :members:


Region features of Part
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Region.RegionPart.RegionPart
    :members:

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