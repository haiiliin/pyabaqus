# pyabaqus
 Type hints for Abaqus/Python scripting

`pyabaqus` is a Python package providing type hints for Python scripting of Abaqus, you can 
use it to write your Python script of Abaqus fluently, even without doing anything in Abaqus. 
It also provides some simple APIs to execute the Abaqus commands so that you can run your 
Python script to build the model, submit the job and extract the output data in just one 
Python script, even without opening the Abaqus/CAE. 

## Other links for this project

- GitHub repository: [github.com/haiiliin/pyabaqus](https://github.com/haiiliin/pyabaqus)
- PyPI: [pypi.org/project/pyabaqus](https://pypi.org/project/pyabaqus/)
- Anaconda: [anaconda.org/haiiliin/pyabaqus](https://anaconda.org/haiiliin/pyabaqus)
- Documentation: [haiiliin.com/pyabaqus](https://haiiliin.com/pyabaqus/)

## New Features

- **Jupyter Notebook support (Since V1.0.15)**
  
  You can put your Abaqus/Python script into a Jupyter Notebook.
  When you run the notebook, the package will convert the notebook into a plain Python file 
  with the same name but with `.py` suffix instead of `.ipynb`, and then it will be submitted 
  to Abaqus kernel. 

  Go [github.com/haiiliin/pyabaqus/tree/main/tests](https://github.com/haiiliin/pyabaqus/tree/main/tests/compression)
  for tests using Jupyter Notebooks to build the Abaqus model.

## Installation
 
In order to use the **Jupyter Notebook** feature, you have to install the following packages:
```shell
pip install ipyparams  # to read the file name of the notebook
pip install notebook
pip install jupyterlab
```
Or use `conda` to install (the `ipyparams` package is only distributed in `PyPI`, 
so you have to install it using `pip`):
```shell
conda install jupyterlab
conda install jupyter notebook
```

Try the following command to make sure the `jupyter` command is available. 
```shell
jupyter --version
```

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
cd pyabaqus
python setup.py install
```

# Explore more

For detailed usage of this package, please refer the [documentation](https://haiiliin.com/pyabaqus/).
