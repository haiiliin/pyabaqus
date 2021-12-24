# DerivedComponent object

A DerivedComponent object describes user-customized components for use in defining [ConnectorFriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorfrictionpyc.htm?ContextScope=all) and [Potential](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-potentialpyc.htm?ContextScope=all) objects.

## Access

```
import section
mdb.models[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i].derivedComponent
mdb.models[name].sections[name].behaviorOptions[i].derivedComponent
mdb.models[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i].derivedComponent
mdb.models[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i].derivedComponent
import odbSection
session.odbs[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i].derivedComponent
session.odbs[name].sections[name].behaviorOptions[i].derivedComponent
session.odbs[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i].derivedComponent
session.odbs[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i].derivedComponent
```

## DerivedComponent()



This method creates a DerivedComponent object.



### Path

```
mdb.models[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i].DerivedComponent
mdb.models[name].sections[name].behaviorOptions[i].DerivedComponent
mdb.models[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i].DerivedComponent
mdb.models[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i].DerivedComponent
session.odbs[name].sections[name].behaviorOptions[i]\
.connectorPotentials[i].DerivedComponent
session.odbs[name].sections[name].behaviorOptions[i].DerivedComponent
session.odbs[name].sections[name].behaviorOptions[i]\
.evolutionPotentials[i].DerivedComponent
session.odbs[name].sections[name].behaviorOptions[i]\
.initiationPotentials[i].DerivedComponent
```

### Arguments

None.

### Return value

A DerivedComponent object.

### Exceptions

ValueError and TextError.



## setValues(...)



This method modifies the DerivedComponent object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DerivedComponent ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-derivedcomponentpyc.htm?ContextScope=all#simaker-derivedcomponentderivedcomponentpyc)method.

### Return value

None.

### Exceptions

ValueError.



## Members

The DerivedComponent object can have the following member:

- *cdcTerms*

  A [CDCTermArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cdctermpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [CONNECTOR DERIVED COMPONENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorderivedcomponent.htm?ContextScope=all#simakey-r-connectorderivedcomponent)