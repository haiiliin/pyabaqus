===========================
Header of the Python script
===========================

Before you can access the Abaqus model and output database, you need to import some modules. In most cases, `abaqus`, `abaqusConstants`, and `driverUtils` is required:

.. code-block:: python

    from abaqus import *
    from abaqusConstants import *
    from driverUtils import *

In the module `abaqus`, two import objects are provided, `mdb` and `session`, which represent the Abaqus model database and a object controls the Abaqus options. 

The `mdb` object is the high-level Abaqus model database. A model database stores models and analysis controls.

.. autoclass:: abaqus.Mdb.Mdb.Mdb
    :members:
    :inherited-members:
