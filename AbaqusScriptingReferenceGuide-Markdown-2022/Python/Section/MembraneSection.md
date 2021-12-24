# MembraneSection object

The MembraneSection object defines the properties of a membrane section.

The MembraneSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## MembraneSection(...)



This method creates a MembraneSection object.



### Path

```
mdb.models[name].MembraneSection
session.odbs[name].MembraneSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *material*

  A String specifying the name of the material.

### Optional arguments

- *thickness*

  A Float specifying the thickness for the section. Possible values are *thickness* >> 0.0. The default value is 1.0.

- *thicknessType*

  A SymbolicConstant specifying the distribution used for defining the thickness of the elements. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM.

- *poissonDefinition*

  A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis is the value provided in *poisson*.The default value is DEFAULT.

- *poisson*

  A Float specifying the section Poisson's ratio. Possible values are −1.0 ≤≤ *poisson* ≤≤ 0.5. This argument is valid only when *poissonDefinition*=VALUE. The default value is 0.5.

- *thicknessField*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object used to define the thickness of the shell elements. The *thicknessField* argument applies only when *thicknessType*=ANALYTICAL_FIELD or *thicknessType*=DISCRETE_FIELD. The default value is an empty string.

### Return value

A MembraneSection object.

### Exceptions

RangeError and InvalidNameError.



## setValues(...)



This method modifies the MembraneSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MembraneSection](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-membranesectionpyc.htm?ContextScope=all#simaker-membranesectionmembranesectionpyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The MembraneSection object has members with the same names and descriptions as the arguments to the [MembraneSection](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-membranesectionpyc.htm?ContextScope=all#simaker-membranesectionmembranesectionpyc) method, except for the *thicknessType* and *thicknessField* arguments.

In addition, the MembraneSection object can have the following member:

- *rebarLayers*

  A [RebarLayers](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all) object specifying reinforcement properties.



## Corresponding analysis keywords

- [MEMBRANE SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-membranesection.htm?ContextScope=all#simakey-r-membranesection)