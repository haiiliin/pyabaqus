# ConnectorOptions object

The ConnectorOptions object is used to define various options for connector behaviors. It can be used only in conjunction with [CDCTerm](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cdctermpyc.htm?ContextScope=all), [ConnectorDamage](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectordamagepyc.htm?ContextScope=all), [ConnectorDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectordampingpyc.htm?ContextScope=all), [ConnectorElasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorelasticitypyc.htm?ContextScope=all), [ConnectorFriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorfrictionpyc.htm?ContextScope=all), and [ConnectorPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorplasticitypyc.htm?ContextScope=all) objects. Because the [ConnectorDamage](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectordamagepyc.htm?ContextScope=all) object contains two separate ConnectorOptions repositories (one for damage initiation and one for damage evolution), there are two ConnectorOptions constructors associated with that behavior—initiationOptions and evolutionOptions. The [ConnectorPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorplasticitypyc.htm?ContextScope=all) object also contains two separate ConnectorOptions repositories (one for isotropic hardening and one for kinematic hardening), so there are two ConnectorOptions constructors associated with that behavior—isotropicOptions and kinematicOptions.

## Access

```
import section
mdb.models[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i].derivedComponent.cdcTerms[i].options
mdb.models[name].sections[name].behaviorOptions[i].derivedComponent\
.cdcTerms[i].options
mdb.models[name].sections[name].behaviorOptions[i].evolutionOptions
mdb.models[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i].derivedComponent.cdcTerms[i].options
mdb.models[name].sections[name].behaviorOptions[i].initiationOptions
mdb.models[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i].derivedComponent.cdcTerms[i].options
mdb.models[name].sections[name].behaviorOptions[i].isotropicOptions
mdb.models[name].sections[name].behaviorOptions[i].kinematicOptions
mdb.models[name].sections[name].behaviorOptions[i].options
import odbSection
session.odbs[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i].derivedComponent.cdcTerms[i].options
session.odbs[name].sections[name].behaviorOptions[i].derivedComponent\
.cdcTerms[i].options
session.odbs[name].sections[name].behaviorOptions[i].evolutionOptions
session.odbs[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i].derivedComponent.cdcTerms[i].options
session.odbs[name].sections[name].behaviorOptions[i].initiationOptions
session.odbs[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i].derivedComponent.cdcTerms[i].options
session.odbs[name].sections[name].behaviorOptions[i].isotropicOptions
session.odbs[name].sections[name].behaviorOptions[i].kinematicOptions
session.odbs[name].sections[name].behaviorOptions[i].options
```

## ConnectorOptions(...)



This method creates a connector options object to be used in conjunction with an allowable connector behavior option, derived component term, or connector section.



### Path

```
mdb.models[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i].derivedComponent.cdcTerms[i].ConnectorOptions
mdb.models[name].sections[name].behaviorOptions[i].derivedComponent\
.cdcTerms[i].ConnectorOptions
mdb.models[name].sections[name].behaviorOptions[i].ConnectorOptions
mdb.models[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i].derivedComponent.cdcTerms[i].ConnectorOptions
mdb.models[name].sections[name].behaviorOptions[i].ConnectorOptions
mdb.models[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i].derivedComponent.cdcTerms[i].ConnectorOptions
mdb.models[name].sections[name].behaviorOptions[i].ConnectorOptions
session.odbs[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i].derivedComponent.cdcTerms[i].ConnectorOptions
session.odbs[name].sections[name].behaviorOptions[i].derivedComponent\
.cdcTerms[i].ConnectorOptions
session.odbs[name].sections[name].behaviorOptions[i].ConnectorOptions
session.odbs[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i].derivedComponent.cdcTerms[i].ConnectorOptions
session.odbs[name].sections[name].behaviorOptions[i].ConnectorOptions
session.odbs[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i].derivedComponent.cdcTerms[i].ConnectorOptions
session.odbs[name].sections[name].behaviorOptions[i].ConnectorOptions
```

### Required arguments

None.

### Optional arguments

- *useBehRegSettings*

  A Boolean specifying whether or not to use the behavior-level settings for regularization options. This argument is applicable only for an Abaqus/Explicit analysis. The default value is ON.

- *regularize*

  A Boolean specifying whether or not the tabular data will be regularized. This argument is applicable only for an Abaqus/Explicit analysis and only if *useBehRegSettings*=OFF. The default value is ON.

- *defaultTolerance*

  A Boolean specifying whether or not the analysis default regularization tolerance will be used. This argument is applicable only for an Abaqus/Explicit analysis and only if *useBehRegSettings*=OFF and *regularize*=ON. The default value is ON.

- *regularization*

  A Float specifying the regularization increment to be used. This argument is applicable only for an Abaqus/Explicit analysis and only if *useBehRegSettings*=OFF, *regularize*=ON, and *defaultTolerance*=OFF. The default value is 0.03.

- *defaultRateFactor*

  A Boolean specifying whether or not the analysis default rate filter factor will be used. This argument is applicable only for an Abaqus/Explicit analysis that includes isotropic hardening with tabular definition or damage initiation with plastic motion criteria. The default value is ON.

- *rateFactor*

  A Float specifying the rate filter factor to be used. This argument is applicable only for an Abaqus/Explicit analysis that includes isotropic hardening with tabular definition or damage initiation with plastic motion criteria. This argument is also applicable only if *defaultRateFactor*=OFF. The default value is 0.9.

- *interpolation*

  A SymbolicConstant specifying the type of interpolation increment to be used on rate-dependent tabular data. This argument is applicable only for an Abaqus/Explicit analysis that includes isotropic hardening with tabular definition or damage initiation with plastic motion criteria. Possible values are LINEAR and LOGARITHMIC. The default value is LINEAR.

- *useBehExtSettings*

  A Boolean specifying whether or not to use the behavior-level settings for extrapolation options. The default value is ON.

- *extrapolation*

  A SymbolicConstant specifying the extrapolation technique to be used. This argument is applicable only if *useBehExtSettings*=OFF. Possible values are CONSTANT and LINEAR. The default value is CONSTANT.

### Return value

A ConnectorOptions object.

### Exceptions

ValueError and TextError.



## setValues(...)



This method modifies the ConnectorOptions object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorOptions ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectoroptionspyc.htm?ContextScope=all#simaker-connectoroptionsconnectoroptionspyc)method.

### Return value

None.

### Exceptions

ValueError.



## Members

The ConnectorOptions object has members with the same names and descriptions as the arguments to the [ConnectorOptions ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectoroptionspyc.htm?ContextScope=all#simaker-connectoroptionsconnectoroptionspyc)method.



## Corresponding analysis keywords

- [CONNECTOR BEHAVIOR](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorbehavior.htm?ContextScope=all#simakey-r-connectorbehavior)
- [CONNECTOR DAMAGE INITIATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectordamageinitiation.htm?ContextScope=all#simakey-r-connectordamageinitiation)
- [CONNECTOR DAMAGE EVOLUTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectordamageevolution.htm?ContextScope=all#simakey-r-connectordamageevolution)
- [CONNECTOR DAMPING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectordamping.htm?ContextScope=all#simakey-r-connectordamping)
- [CONNECTOR DERIVED COMPONENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorderivedcomponent.htm?ContextScope=all#simakey-r-connectorderivedcomponent)
- [CONNECTOR ELASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorelasticity.htm?ContextScope=all#simakey-r-connectorelasticity)
- [CONNECTOR FRICTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorfriction.htm?ContextScope=all#simakey-r-connectorfriction)
- [CONNECTOR PLASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorplasticity.htm?ContextScope=all#simakey-r-connectorplasticity)