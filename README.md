# pyabaqus 2022

[![Maintainer](https://img.shields.io/badge/maintainer-haiiliin-blue)](https://github.com/haiiliin)
[![Documentation Status](https://readthedocs.org/projects/pyabaqus/badge/?version=latest)](https://pyabaqus.haiiliin.com/en/latest/?badge=latest)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/haiiliin/pyabaqus/blob/main/LICENSE)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyabaqus.svg)](https://www.python.org/)
[![made-with-sphinx-doc](https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/)
[![Anaconda platforms](https://anaconda.org/haiiliin/pyabaqus/badges/platforms.svg)](https://anaconda.org/haiiliin/pyabaqus)
[![GitHub release](https://img.shields.io/github/release/haiiliin/pyabaqus.svg)](https://GitHub.com/haiiliin/pyabaqus/releases/)
[![PyPI download month](https://img.shields.io/pypi/dm/ansicolortags.svg)](https://pypi.python.org/pypi/pyabaqus/)

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
- Read the Docs: [readthedocs.org/projects/pyabaqus](https://readthedocs.org/projects/pyabaqus/)
- Documentation: [pyabaqus.haiiliin.com](https://pyabaqus.haiiliin.com/en/latest/)

## Pull Requests are Welcome

Since `pyabaqus` is reconstructed from the official Abaqus documentation,
many of the docstrings are not well formatted, for example, the Raises section, 
the math equations, the attributes of the objects, due to the limitation of 
my time, those things are left behind, if anyone is willing to make any 
contributions, please feel free to create your pull requests.

## New Features

- **Jupyter Notebook support (Since V1.0.15)**
  
  You can put your Abaqus/Python script into a Jupyter Notebook.
  When you run the notebook, the package will convert the notebook into a plain Python file 
  with the same name but with `.py` suffix instead of `.ipynb`, and then it will be submitted 
  to Abaqus kernel. 

  Go [github.com/haiiliin/pyabaqus/tree/main/tests](https://github.com/haiiliin/pyabaqus/tree/main/tests/compression)
  for tests using Jupyter Notebooks to build the Abaqus model.

## Installation

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

## Bindings to Abaqus Version

The main version of pyabaqus, is consistent with the Abaqus version. For example, pyabaqus 2021 and 2021.1 are both 
corresponding to Abaqus 2021, the later version fixes some wrong docstrings (especially the format). 
The latest sub-versions of pyabaqus corresponding to Abaqus are:

- [pyabaqus 2022](https://github.com/haiiliin/pyabaqus/releases/tag/2022) (Corresponding to Abaqus 2022)
- [pyabaqus 2021.1](https://github.com/haiiliin/pyabaqus/releases/tag/2021.1) (Corresponding to Abaqus 2021)
- [pyabaqus 2020](https://github.com/haiiliin/pyabaqus/releases/tag/2020) (Corresponding to Abaqus 2020)
- [pyabaqus 2019.1](https://github.com/haiiliin/pyabaqus/releases/tag/2019.1) (Corresponding to Abaqus 2019)
- [pyabaqus 2018](https://github.com/haiiliin/pyabaqus/releases/tag/2018) (Corresponding to Abaqus 2018)
- [pyabaqus 2017](https://github.com/haiiliin/pyabaqus/releases/tag/2017) (Corresponding to Abaqus 2017)
- [pyabaqus 2016](https://github.com/haiiliin/pyabaqus/releases/tag/2016) (Corresponding to Abaqus 2016)

## Optional Installations
 
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

You may install the latest development version by cloning the 
[GitHub repository](https://github.com/Haiiliin/pyabaqus) and use `python` to install from 
the local directory:

```shell
git clone https://github.com/Haiiliin/pyabaqus.git
cd pyabaqus
python setup.py install
```

## Setup Abaqus Environment

In order to use Abaqus command to execute the Python script and submit the job, you need to tell
`pyabaqus` where the Abaqus command is located. Usually, Abaqus command locates in a directory like this:

```
C:/SIMULIA/Commands/abaqus.bat
```

You can add the directory `C:/SIMULIA/Commands` to the system environment variable `Path`, or you can create a new
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e.,
`C:/SIMULIA/Commands/abaqus.bat`.

## Screenshots

- Create an Abaqus Model

  ![Model](https://github.com/Haiiliin/pyabaqus/blob/main/docs/source/images/model-code.gif "Create an Abaqus Model")

- Extract Output Data

  ![Output](https://github.com/Haiiliin/pyabaqus/blob/main/docs/source/images/output-code.gif "Extract Output Data")

## Explore more

For detailed usage of this package, please refer to the [documentation](https://haiiliin.com/pyabaqus/).
