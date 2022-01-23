====
Part
====

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.

Attributes
----------

- **mdb.models[name].parts[name].geometryValidity**: A Boolean specifying the validity of the geometry of the part. The value is computed, but it can be set to ON to perform feature and mesh operations on an invalid part. There is no guarantee that such operations will work if the part was originally invalid.
- **mdb.models[name].parts[name].isOutOfDate**: An Int specifying that feature parameters have been modified but that the part has not been regenerated. Possible values are 0 and 1.
- **mdb.models[name].parts[name].timeStamp**: A Float specifying when the part was last modified.
- **mdb.models[name].parts[name].vertices**: A :py:class:`abaqus.BasicGeometry.VertexArray.VertexArray` object specifying all the vertices in the part.
- **mdb.models[name].parts[name].ignoredVertices**: An :py:class:`abaqus.BasicGeometry.IgnoredVertexArray.IgnoredVertexArray` object specifying all the ignored vertices in the part.
- **mdb.models[name].parts[name].edges**: An :py:class:`abaqus.BasicGeometry.EdgeArray.EdgeArray` object specifying all the edges in the part.
- **mdb.models[name].parts[name].ignoredEdges**: An :py:class:`abaqus.BasicGeometry.IgnoredEdgeArray.IgnoredEdgeArray` object specifying all the ignored edges in the part.
- **mdb.models[name].parts[name].faces**: A :py:class:`abaqus.BasicGeometry.FaceArray.FaceArray` object specifying all the faces in the part.
- **mdb.models[name].parts[name].cells**: A :py:class:`abaqus.BasicGeometry.CellArray.CellArray` object specifying all the cells in the part.
- **mdb.models[name].parts[name].features**: A repository of :py:class:`abaqus.Assembly.Feature.Feature` objects specifying all the features in the part.
- **mdb.models[name].parts[name].featuresById**: A repository of :py:class:`abaqus.Assembly.Feature.Feature` objects specifying all :py:class:`abaqus.Assembly.Feature.Feature` objects in the part. The :py:class:`abaqus.Assembly.Feature.Feature` objects in the featuresById repository are the same as the :py:class:`abaqus.Assembly.Feature.Feature` objects in the features repository. However, the key to the objects in the featuresById repository is an integer specifying the *ID*, whereas the key to the objects in the features repository is a string specifying the *name*.
- **mdb.models[name].parts[name].datums**: A repository of :py:class:`abaqus.Datum.Datum.Datum` objects specifying all the datums in the part.
- **mdb.models[name].parts[name].elements**: A :py:class:`abaqus.Mesh.MeshElementArray.MeshElementArray` object specifying all the elements in the part.
- **mdb.models[name].parts[name].elemFaces**: A repository of :py:class:`abaqus.Mesh.MeshFace.MeshFace` objects specifying all the element faces in the part. For a given element and a given face index within that element, the corresponding :py:class:`abaqus.Mesh.MeshFace.MeshFace` object can be retrieved from the repository by using the key calculated as (i*8 + j), where i and j are zero-based element and face indices, respectively.
- **mdb.models[name].parts[name].elementFaces**: A :py:class:`abaqus.Mesh.MeshFaceArray.MeshFaceArray` object specifying all the unique element faces in the part.
- **mdb.models[name].parts[name].nodes**: A :py:class:`abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the nodes in the part.
- **mdb.models[name].parts[name].retainedNodes**: A :py:class:`abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the retained nodes in the substructure part.
- **mdb.models[name].parts[name].sets**: A repository of :py:class:`abaqus.Region.Set.Set` objects specifying for more information, see :py:class:`abaqus.Region.Set.Set`.
- **mdb.models[name].parts[name].allSets**: A repository of :py:class:`abaqus.Region.Set.Set` objects specifying the contents of the *all:py:class:`abaqus.Region.Set.Set`s* repository is the same as the contents of the *sets* repository.
- **mdb.models[name].parts[name].allInternalSets**: A repository of :py:class:`abaqus.Region.Set.Set` objects specifying picked regions.
- **mdb.models[name].parts[name].surfaces**: A repository of :py:class:`abaqus.Region.Surface.Surface` objects specifying for more information, see :py:class:`abaqus.Region.Surface.Surface`.
- **mdb.models[name].parts[name].allSurfaces**: A repository of :py:class:`abaqus.Region.Surface.Surface` objects specifying the contents of the *all:py:class:`abaqus.Region.Surface.Surface`s* repository is the same as the contents of the *surfaces* repository.
- **mdb.models[name].parts[name].allInternalSurfaces**: A repository of :py:class:`abaqus.Region.Surface.Surface` objects specifying picked regions.
- **mdb.models[name].parts[name].skins**: A repository of :py:class:`abaqus.Region.Skin.Skin` objects specifying the skins created on the part.
- **mdb.models[name].parts[name].stringers**: A repository of :py:class:`abaqus.Region.Stringer.Stringer` objects specifying the stringers created on the part.
- **mdb.models[name].parts[name].referencePoints**: A repository of :py:class:`abaqus.BasicGeometry.ReferencePoint.ReferencePoint` objects.
- **mdb.models[name].parts[name].engineeringFeatures**: An :py:class:`abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature` object.
- **mdb.models[name].parts[name].sectionAssignments**: A :py:class:`abaqus.Property.SectionAssignmentArray.SectionAssignmentArray` object.
- **mdb.models[name].parts[name].materialOrientations**: A :py:class:`abaqus.Property.MaterialOrientationArray.MaterialOrientationArray` object.
- **mdb.models[name].parts[name].compositeLayups**: A repository of :py:class:`abaqus.Property.CompositeLayup.CompositeLayup` objects.
- **mdb.models[name].parts[name].elemEdges**: A repository of :py:class:`abaqus.Mesh.MeshEdge.MeshEdge` objects specifying all the element edges in the part. For a given element and a given edge index on a given face within that element, the corresponding :py:class:`abaqus.Mesh.MeshEdge.MeshEdge` object can be retrieved from the repository by using the key calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge indices, respectively.
- **mdb.models[name].parts[name].elementEdges**: A :py:class:`abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object specifying all the unique element edges in the part.



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

.. autoclass:: abaqus.Part.Part.Part
    :members:

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