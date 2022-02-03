=====
Datum
=====

Datum commands return Feature objects and inherit the methods of Feature objects. For more details, see Feature commands. Datums can be created using methods on a Part or Assembly object.

Each command also creates a Datum object in the corresponding datum repository. The Datum object is used as an argument to other commands, such as Part and Partition commands.


Object features
---------------

Datum
~~~~~

.. autoclass:: abaqus.Datum.Datum.Datum

DatumAxis
~~~~~~~~~

.. autoclass:: abaqus.Datum.DatumAxis.DatumAxis

DatumCsys
~~~~~~~~~

.. autoclass:: abaqus.Datum.DatumCsys.DatumCsys

DatumPlane
~~~~~~~~~~

.. autoclass:: abaqus.Datum.DatumPlane.DatumPlane

DatumPoint
~~~~~~~~~~

.. autoclass:: abaqus.Datum.DatumPoint.DatumPoint