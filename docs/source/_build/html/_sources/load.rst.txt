==================
Load and Load Case
==================


Load
----

The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.


Access
~~~~~~

- `mdb.models[name].loads[name]`


Create a load
~~~~~~~~~~~~~

.. autoclass:: abaqus.LoadAndLoadCase.LoadModel.LoadModel
    :members:


Features of load
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.LoadAndLoadCase.Load.Load
    :members:


Load case
---------

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.

Access
~~~~~~

- `mdb.models[name].steps[name].loadCases[name]`



Create a load case
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.LoadAndLoadCase.LoadStep.LoadStep
    :members:


Features of load case
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.LoadAndLoadCase.LoadCase.LoadCase
    :members: