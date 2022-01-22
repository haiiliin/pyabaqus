========
Assembly
========

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Assembly commands create Feature objects on only the rootAssembly object. The commands that create Feature objects on only the Part object are described in Part commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.


Create instances
----------------

.. autoclass:: abaqus.Assembly.AssemblyModel.AssemblyModel

    .. automethod:: Instance


Object features
---------------


Basic features of the Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

