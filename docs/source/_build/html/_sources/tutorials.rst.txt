Tutorials
=========


Usually in Abaqus, we have several things to do:
    * Build the model
    * Submit the monitor the job
    * Get the output data and visualize it

Build an Abaqus model
---------------------

The most convenient way to build an Abaqus model is to do it in Abaqus CAE. When we use the 
Abaqus/CAE graphical user interface (GUI) to create a model and to visualize the results, 
commands are issued internally by Abaqus/CAE after every operation. These commands reflect the 
geometry you created along with the options and settings you selected from each dialog box.

Therefore, we can build our Abaqus model using Python script. We can totally use the Python 
script to build our Abaqus model, although it is not an efficient way. Usually, we do 
something in Abaqus/CAE, and check the Python script in the reply `.rpy` file. And then copy 
it to our script file, this works, but not nicely.

However, if type hints are provided in Python scripting of Abaqus, things will getting much 
easier, and that is what `pyabaqus` does.

