.. pyabaqus documentation master file, created by
   sphinx-quickstart on Thu Jan 20 15:04:03 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyabaqus documentation
======================

Type hints for Python scripting of Abaqus.

`pyabaqus` is a Python package providing type hints for Python scripting of Abaqus, you can 
use it to write you Python script of Abaqus fluently, even without doing anything in Abaqus. 
It also provides some simple APIs to execute the Abaqus commands so that you can run your 
Python script to build the model, submit the job and extract the output data in just one 
Python script, even without opening the Abaqus/CAE.

.. you can use it to run Abaqus fluently, it is a package to make Abaqus 
.. modeling, calculation, visualization easily. Using `pyabaqus`, you can simply build the Abaqus 
.. model, submit and monitor the job, and visualize the results in just one python script, you 
.. don't even need to open Abaqus the whole time.

Other links for this project
----------------------------

* GitHub repository: `Haiiliin/pyabaqus: Type hints for Python scripting of Abaqus <https://github.com/Haiiliin/pyabaqus>`_
* PyPI: `pyabaqus · PyPI <https://pypi.org/project/pyabaqus/>`_
* PDF version of this documentation: `pyabaqus.pdf <https://github.com/Haiiliin/pyabaqus/releases/latest/download/pyabaqus.pdf>`_
* Abaqus Executor: `executor_setup.exe <https://github.com/Haiiliin/pyabaqus-executor/releases/latest/download/executor_setup.exe>`_

Related project
---------------

Abaqus Executor is an application to run your Abaqus model more fluently,
check it in `github.com/Haiiliin/pyabaqus-executor <https://github.com/Haiiliin/pyabaqus-executor>`_ or check 
the `documentation <https://executor.haiiliin.com/>`_.

Quick Start
-----------

Installation
~~~~~~~~~~~~

`pyabaqus` is uploaded to `PyPI <https://pypi.org/project/pyabaqus>`_, you can simply install
it using pip:

.. code-block:: sh

   pip install pyabaqus

`pyabaqus` is also uploaded to `anaconda <https://anaconda.org/haiiliin/pyabaqus>`_, you can use 
`conda` to install it:
```shell
conda install -c haiiliin pyabaqus
```

You may install the latest development version by cloning the
`GitHub repository <https://github.com/Haiiliin/pyabaqus>`_ and use `python` to install from
the local directory:

.. code-block:: sh

   git clone https://github.com/Haiiliin/pyabaqus.git
   python setup.py install

Write your Abaqus/Python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After installing the `pyabaqus` package, you can start writing your own Abaqus/Python script
to build your model. You can refer
`pyabaqus/tests at main · Haiiliin/pyabaqus <https://github.com/Haiiliin/pyabaqus/tree/main/tests>`_
for some tests of the script, for more detailed documentation, please check
`pyabaqus documentation <https://haiiliin.com/pyabaqus/>`_.

Setup your Abaqus Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use Abaqus command to execute the Python script and submit the job, you need to tell
`pyabaqus` where the Abaqus command is located. Usually, Abaqus command locates in a directory like this:

.. code-block:: sh

   C:/SIMULIA/Commands/abaqus.bat

You can add the directory `C:/SIMULIA/Commands` to the system environment variable `Path`, or you can create a new
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e.,
`C:/SIMULIA/Commands/abaqus.bat`

Run your Abaqus/Python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can just run your Abaqus/Python script using your own Python interpreter that `pyabaqus` is installed.

- Create an Abaqus Model

.. image:: images/Model.gif
    :width: 100%
    :align: center
    :alt: Create an Abaqus Model

- Extract Output Data

.. image:: images/Output.gif
    :width: 100%
    :align: center
    :alt: Extract Output Data

What next?
----------

You may wonder how does this package work, 
you can go :doc:`getting_started` for more detailed introduction and go
:doc:`tutorials` for a simple tutorial. For more documentation about 
Abaqus/Python scripting, please check :doc:`user` for a list of 
descriptions of objects and methods of Abaqus models, check :doc:`references` 
for more detailed API references.

Documentation
-------------

.. toctree::
   :maxdepth: 1
   :caption: Contents

   getting_started
   tutorials
   user
   references

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
