import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyabaqus",
    version="0.0.5",
    author="WANG Hailin",
    author_email="hailin.wang@connect.polyu.hk",
    description="Convert Abaqus Scripting Reference into Python objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hailin-Wang/pyabaqus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['abaqusConstants', 'animation', 'annotationToolset', 'assembly', 'caeModules', 'caePrefsAccess',
                'calibration', 'connectorBehavior', 'customKernel', 'deleteObjectCallback', 'displayGroupMdbToolset',
                'displayGroupOdbToolset', 'driverUtils', 'field','fields','inpParser', 'interaction', 'material',
                'mesh', 'meshEdit', 'methodCallback', 'monitorManager', 'odbAccess', 'odbConnectorBehavior',
                'odbMaterial', 'odbSection', 'part', 'redentABQ', 'section', 'symbolicConstants', 'testRepr',
                'upgradeScript', 'visualization'],
    python_requires='>=3.6',
)