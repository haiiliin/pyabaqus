========
Assembly
========

An Assembly object is a container for instances of parts. The Assembly object has no constructor command. Abaqus creates the rootAssembly member when a Model object is created.


Access

- `mdb.models[name].rootAssembly`


Features of Assembly
--------------------


Basic features of the Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.AssemblyBase.AssemblyBase
    :members:


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

