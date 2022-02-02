========
Assembly
========

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Assembly commands create Feature objects on only the rootAssembly object. The commands that create Feature objects on only the Part object are described in Part commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.

Assembly Attributes
-------------------

- **mdb.models[name].rootAssembly.isOutOfDate**: An Int specifying that feature parameters have been modified but that the assembly has not been regenerated. Possible values are 0 and 1.
- **mdb.models[name].rootAssembly.timeStamp**: A Float specifying which gives an indication when the assembly was last modified.
- **mdb.models[name].rootAssembly.isLocked**: An Int specifying whether the assembly is locked or not. Possible values are 0 and 1.
- **mdb.models[name].rootAssembly.regenerateConstraintsTogether**: A Boolean specifying whether the positioning constraints in the assembly should be regenerated together before regenerating other assembly features. The default value is ON.If the assembly has position constraint features and you modify the value of **regenerateConstraintsTogether**, Abaqus/CAE will regenerate the assembly features.
- **mdb.models[name].rootAssembly.vertices**: A :py:class:`abaqus.BasicGeometry.VertexArray.VertexArray` object specifying all the vertices existing at the assembly level. This member does not provide access to the vertices at the instance level.
- **mdb.models[name].rootAssembly.edges**: An :py:class:`abaqus.BasicGeometry.EdgeArray.EdgeArray` object specifying all the edges existing at the assembly level. This member does not provide access to the edges at the instance level.
- **mdb.models[name].rootAssembly.elements**: A :py:class:`abaqus.Mesh.MeshElementArray.MeshElementArray` object specifying all the elements existing at the assembly level. This member does not provide access to the elements at the instance level.
- **mdb.models[name].rootAssembly.nodes**: A :py:class:`abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the nodes existing at the assembly level. This member does not provide access to the nodes at the instance level.
- **mdb.models[name].rootAssembly.instances**: A repository of :py:class:`abaqus.Assembly.PartInstance.PartInstance` objects.
- **mdb.models[name].rootAssembly.datums**: A repository of :py:class:`abaqus.Datum.Datum.Datum` objects specifying all :py:class:`abaqus.Datum.Datum.Datum` objects in the assembly.
- **mdb.models[name].rootAssembly.features**: A repository of :py:class:`abaqus.Assembly.Feature.Feature` objects specifying all :py:class:`abaqus.Assembly.Feature.Feature` objects in the assembly.
- **mdb.models[name].rootAssembly.featuresById**: A repository of :py:class:`abaqus.Assembly.Feature.Feature` objects specifying all :py:class:`abaqus.Assembly.Feature.Feature` objects in the assembly.The :py:class:`abaqus.Assembly.Feature.Feature` objects in the featuresById repository are the same as the :py:class:`abaqus.Assembly.Feature.Feature` objects in the features repository. However, the key to the objects in the featuresById repository is an integer specifying the **ID**, whereas the key to the objects in the features repository is a string specifying the **name**.
- **mdb.models[name].rootAssembly.surfaces**: A repository of :py:class:`abaqus.Region.Surface.Surface` objects specifying for more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.allSurfaces**: A repository of :py:class:`abaqus.Region.Surface.Surface` objects specifying for more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.allInternalSurfaces**: A repository of :py:class:`abaqus.Region.Surface.Surface` objects specifying picked regions.
- **mdb.models[name].rootAssembly.sets**: A repository of :py:class:`abaqus.Region.Set.Set` objects.
- **mdb.models[name].rootAssembly.allSets**: A repository of :py:class:`abaqus.Region.Set.Set` objects specifying for more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.allInternalSets**: A repository of :py:class:`abaqus.Region.Set.Set` objects specifying picked regions.
- **mdb.models[name].rootAssembly.skins**: A repository of :py:class:`abaqus.Region.Skin.Skin` objects specifying the skins created on the assembly.
- **mdb.models[name].rootAssembly.stringers**: A repository of :py:class:`abaqus.Region.Stringer.Stringer` objects specifying the stringers created on the assembly.
- **mdb.models[name].rootAssembly.referencePoints**: A repository of :py:class:`abaqus.BasicGeometry.ReferencePoint.ReferencePoint` objects.
- **mdb.models[name].rootAssembly.modelInstances**: A repository of :py:class:`abaqus.Assembly.ModelInstance.ModelInstance` objects.
- **mdb.models[name].rootAssembly.allInstances**: A :py:class:`abaqus.Assembly.PartInstance.PartInstance` object specifying the PartInstances and A :py:class:`abaqus.Assembly.ModelInstance.ModelInstance` object specifying the ModelInstances.
- **mdb.models[name].rootAssembly.engineeringFeatures**: An :py:class:`abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature` object.
- **mdb.models[name].rootAssembly.modelName**: A String specifying the name of the model to which the assembly belongs.
- **mdb.models[name].rootAssembly.connectorOrientations**: A :py:class:`abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientationArray` object.
- **mdb.models[name].rootAssembly.sectionAssignments**: A :py:class:`abaqus.Property.SectionAssignmentArray.SectionAssignmentArray` object.


PartInstance Attributes
-----------------------

- **mdb.models[name].rootAssembly.instances[name].name**: A String specifying the repository key. The name must be a valid Abaqus object name.
- **mdb.models[name].rootAssembly.instances[name].dependent**: A Boolean specifying whether the part instance is dependent or independent. If **dependent**=OFF, the part instance is independent. The default value is OFF.
- **mdb.models[name].rootAssembly.instances[name].excludedFromSimulation**: A Boolean specifying whether the part instance is excluded from the simulation. If **excludedFromSimulation**=ON, the part instance is excluded from the simulation. The default value is OFF.
- **mdb.models[name].rootAssembly.instances[name].geometryValidity**: A Boolean specifying the validity of the geometry of the instance. The value is computed, but it can be set to ON to perform feature and mesh operations on an invalid instance. There is no guarantee that such operations will work if the instance was originally invalid.
- **mdb.models[name].rootAssembly.instances[name].analysisType**: A SymbolicConstant specifying the part type. Possible values are DEFORMABLE_BODY, EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE.
- **mdb.models[name].rootAssembly.instances[name].referenceNode**: An Int specifying the reference node number. This member is valid only if **analysisType**=DISCRETE_RIGID_SURFACE or ANALYTIC_RIGID_SURFACE.
- **mdb.models[name].rootAssembly.instances[name].part**: A :py:class:`abaqus.Part.Part.Part` object specifying the instanced part.
- **mdb.models[name].rootAssembly.instances[name].sets**: A repository of :py:class:`abaqus.Region.Set.Set` objects specifying the sets created on the part. For more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.instances[name].surfaces**: A repository of :py:class:`abaqus.Region.Surface.Surface` objects specifying the surfaces created on the part. For more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.instances[name].skins**: A repository of :py:class:`abaqus.Region.Skin.Skin` objects specifying the skins created on the part. For more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.instances[name].stringers**: A repository of :py:class:`abaqus.Region.Stringer.Stringer` objects specifying the stringers created on the part. For more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.instances[name].vertices**: A :py:class:`abaqus.BasicGeometry.VertexArray.VertexArray` object.
- **mdb.models[name].rootAssembly.instances[name].ignoredVertices**: An :py:class:`abaqus.BasicGeometry.IgnoredVertexArray.IgnoredVertexArray` object.
- **mdb.models[name].rootAssembly.instances[name].edges**: An :py:class:`abaqus.BasicGeometry.EdgeArray.EdgeArray` object.
- **mdb.models[name].rootAssembly.instances[name].ignoredEdges**: An :py:class:`abaqus.BasicGeometry.IgnoredEdgeArray.IgnoredEdgeArray` object.
- **mdb.models[name].rootAssembly.instances[name].faces**: A :py:class:`abaqus.BasicGeometry.FaceArray.FaceArray` object.
- **mdb.models[name].rootAssembly.instances[name].cells**: A :py:class:`abaqus.BasicGeometry.CellArray.CellArray` object.
- **mdb.models[name].rootAssembly.instances[name].datums**: A repository of :py:class:`abaqus.Datum.Datum.Datum` objects.
- **mdb.models[name].rootAssembly.instances[name].elements**: A :py:class:`abaqus.Mesh.MeshElementArray.MeshElementArray` object.
- **mdb.models[name].rootAssembly.instances[name].nodes**: A :py:class:`abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.
- **mdb.models[name].rootAssembly.instances[name].elemFaces**: A repository of :py:class:`abaqus.Mesh.MeshFace.MeshFace` objects specifying all the element faces in the part instance. For a given element and a given face index within that element, the corresponding :py:class:`abaqus.Mesh.MeshFace.MeshFace` object can be retrieved from the repository by using the key calculated as (i*8 + j), where i and j are zero-based element and face indices, respectively.
- **mdb.models[name].rootAssembly.instances[name].elementFaces**: A :py:class:`abaqus.Mesh.MeshFaceArray.MeshFaceArray` object.
- **mdb.models[name].rootAssembly.instances[name].elemEdges**: A repository of :py:class:`abaqus.Mesh.MeshEdge.MeshEdge` objects specifying all the element edges in the part instance. For a given element and a given edge index on a given face within that element, the corresponding :py:class:`abaqus.Mesh.MeshEdge.MeshEdge` object can be retrieved from the repository by using the key calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge indices, respectively.
- **mdb.models[name].rootAssembly.instances[name].elementEdges**: A :py:class:`abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object.
- **mdb.models[name].rootAssembly.instances[name].referencePoints**: A repository of :py:class:`abaqus.BasicGeometry.ReferencePoint.ReferencePoint` objects.
- **mdb.models[name].rootAssembly.instances[name].partName**: A String specifying the name of the part from which the instance was created.


ModelInstance Attributes
------------------------

- **mdb.models[name].rootAssembly.instances[name].sets**: A repository of :py:class:`abaqus.Region.Set.Set` objects specifying the sets created on the assembly. For more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.instances[name].surfaces**: A repository of :py:class:`abaqus.Region.Surface.Surface` objects specifying the surfaces created on the assembly. For more information, see :doc:`/reference/mdb/model/part_assembly/region`.
- **mdb.models[name].rootAssembly.instances[name].vertices**: A :py:class:`abaqus.BasicGeometry.VertexArray.VertexArray` object.
- **mdb.models[name].rootAssembly.instances[name].edges**: An :py:class:`abaqus.BasicGeometry.EdgeArray.EdgeArray` object.
- **mdb.models[name].rootAssembly.instances[name].elements**: A :py:class:`abaqus.Mesh.MeshElementArray.MeshElementArray` object.
- **mdb.models[name].rootAssembly.instances[name].nodes**: A :py:class:`abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.
- **mdb.models[name].rootAssembly.instances[name].datums**: A repository of :py:class:`abaqus.Datum.Datum.Datum` objects.
- **mdb.models[name].rootAssembly.instances[name].referencePoints**: A repository of :py:class:`abaqus.BasicGeometry.ReferencePoint.ReferencePoint` objects.



Create instances
----------------

.. autoclass:: abaqus.Assembly.AssemblyModel.AssemblyModel

    .. automethod:: Instance


Object features
---------------


Basic features of the Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.Assembly.Assembly
    :members:

.. autoclass:: abaqus.Assembly.AssemblyBase.AssemblyBase
    :members:

.. autoclass:: abaqus.Assembly.AssemblyModel.AssemblyModel

    .. automethod:: convertAllSketches
    .. automethod:: linkInstances


Edit Mesh features of the Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.EditMesh.MeshEditAssembly.MeshEditAssembly
    :members:


Mesh features of the Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Mesh.MeshAssembly.MeshAssembly
    :members:


Property features of the Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Property.PropertyAssembly.PropertyAssembly
    :members:


Table Collection features of the Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.TableCollection.TableCollectionAssembly.TableCollectionAssembly
    :members:

ConnectorOrientation
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.ConnectorOrientation.ConnectorOrientation
    :members:

ConnectorOrientationArray
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientationArray
    :members:

Feature
~~~~~~~

.. autoclass:: abaqus.Assembly.Feature.Feature
    :members:

ModelInstance
~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.ModelInstance.ModelInstance
    :members:

PartInstance
~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.PartInstance.PartInstance
    :members:

PartInstanceArray
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.PartInstanceArray.PartInstanceArray
    :members:

