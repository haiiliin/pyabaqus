# ConnectorPotential object

The ConnectorPotential object is used to define a restricted set of mathematical functions to represent yield or limiting surfaces in the space spanned by connector available components. It can be used only in conjunction with [ConnectorDamage](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectordamagepyc.htm?ContextScope=all), [ConnectorFriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorfrictionpyc.htm?ContextScope=all), and [ConnectorPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorplasticitypyc.htm?ContextScope=all) objects. Because the [ConnectorDamage](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectordamagepyc.htm?ContextScope=all) object contains two separate ConnectorPotential repositories (one for damage initiation and one for damage evolution), there are two ConnectorPotential constructors associated with that behavior—IniPotential and EvoPotential.

## Access

```
import section
mdb.models[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i]
mdb.models[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i]
mdb.models[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i]
import odbSection
session.odbs[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i]
session.odbs[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i]
session.odbs[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i]
```

## ConnectorPotential(...)



This method creates a connector potential object to be used in conjunction with an allowable connector behavior option.



### Path

```
mdb.models[name].sections[name].behaviorOptions[i].ConnectorPotential
session.odbs[name].sections[name].behaviorOptions[i]\
.ConnectorPotential
```

### Required arguments

None.

### Optional arguments

- *componentStyle*

  A SymbolicConstant specifying whether a component number or the name of the [DerivedComponent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-derivedcomponentpyc.htm?ContextScope=all) object will be used in the contribution. Possible values are COMPONENT_NUMBER and DERIVED_COMPONENT. The default value is COMPONENT_NUMBER.

- *componentNumber*

  An Int specifying the component number used in the contribution. This argument is applicable only if *componentStyle*=COMPONENT_NUMBER. Possible values are 1 ≤≤ *componentNumber* ≤≤ 6. Only available components can be specified. The default value is 0.

- *sign*

  A SymbolicConstant specifying the sign of the contribution. Possible values are POSITIVE and NEGATIVE. The default value is POSITIVE.

- *scaleFactor*

  A Float specifying the scaling factor for the contribution. The default value is 1.0.

- *positiveExponent*

  A Float specifying the positive exponent for the contribution. The default value is 2.0.This argument is ignored if the potential operator of the invoking behavior option is set to MAXIMUM.

- *shiftFactor*

  A Float specifying the shift factor for the contribution. The default value is 0.0.

- *hFunction*

  A SymbolicConstant specifying the H function of the contribution: either absolute value, Macauley bracket, or the identity function. Possible values are ABS, MACAULEY, and IDENTITY. The default value is ABS.The value of IDENTITY can be used only if *positiveExponent*=1.0 and the potential exponent of the invoking behavior option is also 1.0 (i.e., the potential operator of the invoking behavior option must be SUM).

### Return value

A ConnectorPotential object.

### Exceptions

ValueError and TextError.



## setValues(...)



This method modifies the ConnectorPotential object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorPotential ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorpotentialpyc.htm?ContextScope=all#simaker-connectorpotentialconnectorpotentialpyc)method.

### Return value

None.

### Exceptions

ValueError.



## Members

The ConnectorPotential object has members with the same names and descriptions as the arguments to the [ConnectorPotential ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorpotentialpyc.htm?ContextScope=all#simaker-connectorpotentialconnectorpotentialpyc)method.

In addition, the ConnectorPotential object can have the following member:

- *derivedComponent*

  A [DerivedComponent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-derivedcomponentpyc.htm?ContextScope=all) object specifying the [DerivedComponent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-derivedcomponentpyc.htm?ContextScope=all) used in the contribution. This argument is applicable only if *componentStyle*=DERIVED_COMPONENT.



## Corresponding analysis keywords

- [CONNECTOR POTENTIAL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorpotential.htm?ContextScope=all#simakey-r-connectorpotential)