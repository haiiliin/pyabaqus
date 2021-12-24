# CompositeShellSection object

The CompositeShellSection object defines the properties of a composite shell section.

The CompositeShellSection object is derived from the [GeometryShellSection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometryshellsectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].parts[name].compositeLayups[i].section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## CompositeShellSection(...)



This method creates a CompositeShellSection object.



### Path

```
mdb.models[name].parts[name].compositeLayups[i].CompositeShellSection
mdb.models[name].CompositeShellSection
session.odbs[name].CompositeShellSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *layup*

  A [SectionLayerArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionlayerpyc.htm?ContextScope=all) object specifying the shell cross-section.

### Optional arguments

- *symmetric*

  A Boolean specifying whether or not the layup should be made symmetric by the analysis. The default value is OFF.

- *thicknessType*

  A SymbolicConstant specifying the distribution used for defining the thickness of the elements. Possible values are UNIFORM, ANALYTICAL_FIELD, DISCRETE_FIELD, NODAL_ANALYTICAL_FIELD, and NODAL_DISCRETE_FIELD. The default value is UNIFORM.

- *preIntegrate*

  A Boolean specifying whether the shell section properties are specified by the user prior to the analysis (ON) or integrated during the analysis (OFF). The default value is OFF.

- *poissonDefinition*

  A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis is the value provided in *poisson*.The default value is DEFAULT.

- *poisson*

  A Float specifying the Poisson's ratio. Possible values are −1.0 ≤≤ *poisson* ≤≤ 0.5. This argument is valid only when *poissonDefinition*=VALUE. The default value is 0.5.

- *integrationRule*

  A SymbolicConstant specifying the shell section integration rule. Possible values are SIMPSON and GAUSS. The default value is SIMPSON.

- *temperature*

  A SymbolicConstant specifying the mode used for temperature and field variable input across the section thickness. Possible values are GRADIENT and POINTWISE. The default value is GRADIENT.

- *idealization*

  A SymbolicConstant specifying the mechanical idealization used for the section calculations. This member is only applicable when *preIntegrate* is set to ON. Possible values are NO_IDEALIZATION, SMEAR_ALL_LAYERS, MEMBRANE, and BENDING. The default value is NO_IDEALIZATION.

- *nTemp*

  None or an Int specifying the number of temperature points to be input. This argument is valid only when *temperature*=POINTWISE. The default value is None.

- *thicknessModulus*

  None or a Float specifying the effective thickness modulus. This argument is relevant only for continuum shells and must be used in conjunction with the argument *poisson*. The default value is None.

- *useDensity*

  A Boolean specifying whether or not to use the value of *density*. The default value is OFF.

- *density*

  A Float specifying the value of density to apply to this section. The default value is 0.0.

- *layupName*

  A String specifying the layup name for this section. The default value is an empty string.

- *thicknessField*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object used to define the thickness of the shell elements. The *thicknessField* argument applies only when *thicknessType*=ANALYTICAL_FIELD or *thicknessType*=DISCRETE_FIELD. The default value is an empty string.

- *nodalThicknessField*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object used to define the thickness of the shell elements at each node. The *nodalThicknessField* argument applies only when *thicknessType*=NODAL_ANALYTICAL_FIELD or *thicknessType*=NODAL_DISCRETE_FIELD. The default value is an empty string.

### Return value

A CompositeShellSection object.

### Exceptions

None.



## setValues(...)



This method modifies the CompositeShellSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CompositeShellSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositeshellsectionpyc.htm?ContextScope=all#simaker-compositeshellsectioncompositeshellsectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The CompositeShellSection object has members with the same names and descriptions as the arguments to the [CompositeShellSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositeshellsectionpyc.htm?ContextScope=all#simaker-compositeshellsectioncompositeshellsectionpyc)method.

In addition, the CompositeShellSection object can have the following members:

- *rebarLayers*

  A [RebarLayers](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all) object specifying reinforcement properties.

- *transverseShear*

  A [TransverseShearShell](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-transverseshearshellpyc.htm?ContextScope=all) object specifying the transverse shear stiffness properties.



## Corresponding analysis keywords

- [SHELL SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shellsection.htm?ContextScope=all#simakey-r-shellsection)
- [SHELL GENERAL SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shellgeneralsection.htm?ContextScope=all#simakey-r-shellgeneralsection)