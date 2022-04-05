# pyabaqus
 Type hints for Abaqus/Python scripting

`pyabaqus` is a Python package providing type hints for Python scripting of Abaqus, you can 
use it to write you Python script of Abaqus fluently, even without doing anything in Abaqus. 
It also provides some simple APIs to execute the Abaqus commands so that you can run your 
Python script to build the model, submit the job and extract the output data in just one 
Python script, even without opening the Abaqus/CAE. 

## Quick start

### Installation

`pyabaqus` is uploaded to [PyPI](https://pypi.org/project/pyabaqus), you can simply install 
it using pip:
```shell
pip install pyabaqus
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
Abaqus where the Abaqus command located. Usually, Abaqus command locates in a directory like this: 
```shell
C:/SIMULIA/Commands/abaqus.bat
```
You can add the directory `C:/SIMULIA/Commands` to the system environment variable `path`, or you can create a new 
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e., 
`C:/SIMULIA/Commands/abaqus.bat`

### Run your Abaqus/Python script

Now you can just run your Abaqus/Python script using your own Python interpreter that `pyabaqus` is installed.

- Create an Abaqus Model

  ![Model](https://github.com/Haiiliin/pyabaqus/blob/main/screenshots/Model.gif "Create an Abaqus Model")

- Extract Output Data

  ![Output](https://github.com/Haiiliin/pyabaqus/blob/main/screenshots/Output.gif "Extract Output Data")

## Other links for this project

- GitHub repository: [github.com/Haiiliin/pyabaqus](https://github.com/Haiiliin/pyabaqus)
- PyPI: [pyabaqus · PyPI](https://pypi.org/project/pyabaqus/)
- Documentation: [pyabaqus documentation](https://haiiliin.com/pyabaqus/)

## Related project

Abaqus Executor is an application to run your Abaqus model more fluently,
check it in [github.com/Haiiliin/pyabaqus-executor](https://github.com/Haiiliin/pyabaqus-executor).

