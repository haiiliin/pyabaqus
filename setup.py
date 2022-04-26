import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyabaqus",
    version="1.0.14",
    author="WANG Hailin",
    author_email="hailin.wang@connect.polyu.hk",
    description="Type hints for Abaqus/Python scripting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haiiliin/.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    py_modules=['abaqusConstants', 'animation', 'annotationToolset', 'assembly', 'caeModules', 'caePrefsAccess',
                'calibration', 'connectorBehavior', 'customKernel', 'deleteObjectCallback', 'displayGroupMdbToolset',
                'displayGroupOdbToolset', 'driverUtils', 'field', 'fields', 'inpParser', 'interaction', 'material',
                'mesh', 'meshEdit', 'methodCallback', 'monitorManager', 'odbAccess', 'odbConnectorBehavior',
                'odbMaterial', 'odbSection', 'part', 'redentABQ', 'section', 'symbolicConstants', 'textRepr',
                'upgradeScript', 'visualization'],
)
