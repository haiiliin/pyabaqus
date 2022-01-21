=======
Section
=======

The Section object defines the properties of a section. The Section object is the abstract base type for other Section objects. The Section object has no explicit  constructor. The methods and members of the Section object are common to all objects derived from the Section. 


Access
------

- `mdb.models[name].sections[name]`
- `session.odbs[name].sections[name]`


Create a section
----------------

In Mdb
~~~~~~

.. autoclass:: abaqus.Section.SectionModel.SectionModel
    :members:


In Odb
~~~~~~

.. autoclass:: abaqus.Section.SectionOdb.SectionOdb
    :members:


Basic features of Section
-------------------------

.. autoclass:: abaqus.Section.SectionBase.SectionBase
    :members:


Features of the Beam Section
----------------------------

.. autoclass:: abaqus.Section.Section.Section
    :members:

