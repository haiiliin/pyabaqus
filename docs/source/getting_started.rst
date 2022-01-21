Getting Started
===============


Introduction
------------

`pyabaqus` is a Python package to run Abaqus fluently, it is a package to make Abaqus 
modeling, calculation, visualization easily. Using `pyabaqus`, you can simply build the Abaqus 
model, submit and monitor the job, and visualize the results in just one Python script, you 
don't even need to open Abaqus the whole time. 


Two Python interpreters
~~~~~~~~~~~~~~~~~~~~~~~

Before we go any further, it is necessary for us to understand two Python interpreters.

When we use the Abaqus/CAE graphical user interface (GUI) to create a model and to visualize 
the results, commands are issued internally by Abaqus/CAE after every operation. These 
commands reflect the geometry you created along with the options and settings you selected 
from each dialog box. The GUI generates commands in an object-oriented programming language 
called Python. The commands issued by the GUI are sent to the Abaqus/CAE kernel. The kernel 
interprets the commands and uses the options and settings to create an internal representation 
of our model. The kernel is the brains behind Abaqus/CAE. The GUI is the interface between the 
user and the kernel. 

In a word, Abaqus use Python language to interact with the Abaqus kernel, everything that can 
be done in Abaqus/CAE, can also be done using Python script. Abaqus has already installed a 
Python interpreter so that Abaqus/CAE can use it to interact with the Abaqus kernel. 

For some reasons, we cannot directly use the Python interpreter inside Abaqus to build an 
Abaqus model. But fortunately, we can use the commands provided by Abaqus to access it. i.e.

.. code-block:: sh
    
    abaqus cae
        [database=database-file]
        [replay=replay-file]
        [recover=journal-file]
        [startup=startup-file]
        [script=script-file]
        [noGUI=noGUI-file]
        [noenvstartup]
        [noSavedOptions]
        [noSavedGuiPrefs]
        [noStartupDialog]
        [custom=script-file]
        [guiTester=GUI-script]
        [guiRecord]
        [guiNoRecord]


Usually, we can use the noGUI-file or script-file to execute our Python script in Abaqus.

Another Python interpreter, is the Python interpreter installed by ourselves, where `pyabaqus` 
is installed. `pyabaqus` provides a bridge to connect our Python script to Abaqus Python 
interpreter, it provides type hints for Python scripting for Abaqus, enabling us to write a 
Abaqus Python script quickly.


Installation
------------

`pyabaqus` is uploaded to `PyPI <https://pypi.org/project/pyabaqus>`_, you can simply install 
it using pip:

.. code-block:: sh

   pip install pyabaqus


You may install the latest development version by cloning the 
`GitHub repository <https://github.com/Haiiliin/pyabaqus>`_ and using `python` to install from 
the local directory:

.. code-block:: sh

    git clone https://github.com/Haiiliin/pyabaqus.git
    python setup.py install



Dependencies
------------

Required dependencies:
    * PyQt5, used for GUI window of Job monitor

Once you have installed `pyabaqus` and `PyQt5`, you can start to build your Abaqus model right 
now.


Abaqus command
--------------

In order to use Abaqus command to execute the Python script and submit the job, you need to tell 
Abaqus where the Abaqus command located. Usually, Abaqus command locates in a directory like this: 

.. code-block:: sh

    C:/SIMULIA/Commands/abaqus.bat

You can add the directory `C:/SIMULIA/Commands` to the system environment variable `path`, or you can create a new system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e., `C:/SIMULIA/Commands/abaqus.bat`
