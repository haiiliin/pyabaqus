# pyabaqus
 Type hints for Abaqus/Python scripting

`pyabaqus` is a Python package providing type hints for Python scripting of Abaqus, you can 
use it to write your Python script of Abaqus fluently, even without doing anything in Abaqus. 
It also provides some simple APIs to execute the Abaqus commands so that you can run your 
Python script to build the model, submit the job and extract the output data in just one 
Python script, even without opening the Abaqus/CAE. 

## Other links for this project

- GitHub repository: [github.com/Haiiliin/pyabaqus](https://github.com/Haiiliin/pyabaqus)
- PyPI: [pyabaqus · PyPI](https://pypi.org/project/pyabaqus/)
- Documentation: [pyabaqus documentation](https://haiiliin.com/pyabaqus/)


## Related project

Abaqus Executor is an application to run your Abaqus model more fluently,
check it in [github.com/Haiiliin/pyabaqus-executor](https://github.com/Haiiliin/pyabaqus-executor)
or check the [documentation](https://executor.haiiliin.com/).

## Quick start

### Installation

`pyabaqus` is using type hints features that require Python 3.9 or a later version, 
please upgrade it to Python 3.9 or a later version if you are using an earlier version.

`pyabaqus` is uploaded to [PyPI](https://pypi.org/project/pyabaqus), you can simply install 
it using pip:
```shell
pip install pyabaqus
```

`pyabaqus` is also uploaded to [anaconda](https://anaconda.org/haiiliin/pyabaqus), you can use 
`conda` to install it:
```shell
conda install -c haiiliin pyabaqus
```

You may install the latest development version by cloning the 
[GitHub repository](https://github.com/Haiiliin/pyabaqus) and use `python` to install from 
the local directory:

```shell
git clone https://github.com/Haiiliin/pyabaqus.git
python setup.py install
```

### Write your Abaqus/Python script

After installing the `pyabaqus` package, you can start writing your own Abaqus/Python script 
to build your model. You can refer 
[pyabaqus/tests at main · Haiiliin/pyabaqus](https://github.com/Haiiliin/pyabaqus/tree/main/tests)
for some tests of the script, for more detailed documentation, please check 
[pyabaqus documentation](https://haiiliin.com/pyabaqus/).

### Setup your Abaqus Environment

In order to use Abaqus command to execute the Python script and submit the job, you need to tell 
`pyabaqus` where the Abaqus command located. Usually, Abaqus command locates in a directory like this: 
```shell
C:/SIMULIA/Commands/abaqus.bat
```
You can add the directory `C:/SIMULIA/Commands` to the system environment variable `Path`, or you can create a new 
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e., 
`C:/SIMULIA/Commands/abaqus.bat`.

### Run your Abaqus/Python script

Now you can just run your Abaqus/Python script using your own Python interpreter that `pyabaqus` is installed.

- Create an Abaqus Model

  ![Model](https://github.com/Haiiliin/pyabaqus/blob/main/screenshots/Model.gif "Create an Abaqus Model")

- Extract Output Data

  ![Output](https://github.com/Haiiliin/pyabaqus/blob/main/screenshots/Output.gif "Extract Output Data")

## What next?

You may wonder how does this package work, 
you can go [pyabaqus documentation: Getting Started](https://pyabaqus.haiiliin.com/getting_started.html) for more detailed introduction and go
[pyabaqus documentation: Tutorials](https://pyabaqus.haiiliin.com/tutorials.html) for a simple tutorial. For more documentation about 
Abaqus/Python scripting, please check [pyabaqus documentation: User Manual](https://pyabaqus.haiiliin.com/user.html) for a list of 
descriptions of objects and methods of Abaqus models, check [pyabaqus documentation: API References](https://pyabaqus.haiiliin.com/references.html) 
for more detailed API references.
