========
Material
========

A Material object is the object used to specify a material. The Material object stores the various settings that determine how a material behaves. 
A material is created by combining one or more individual material options and sub  options. 
A particular material option is associated with the Material object through a member. For example: the *acousticMedium* member may contain an AcousticMedium object. 
The alternative of having a MaterialOption abstract base class and a container of MaterialOptions was rejected because it would make it more difficult to enforce the fact that one Material object cannot contain two AcousticMedium objects, for example. 


Access
------

- `mdb.models[name].materials[name]`
- `session.odbs[name].materials[name]`


Create a material
-----------------

.. autoclass:: abaqus.Material.MaterialModel.MaterialModel
    :members:

.. autoclass:: abaqus.Material.MaterialOdb.MaterialOdb
    :members:


Assign properties of the material
---------------------------------

.. autoclass:: abaqus.Material.Material.Material
    :members:
