# ConnectorFriction object

The ConnectorFriction object defines Coulomb-like or hysteretic friction behavior for one or more components of a connector's relative motion.

The ConnectorFriction object is derived from the [ConnectorBehaviorOption](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorbehavioroptionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name].behaviorOptions[i]
import odbSection
session.odbs[name].sections[name].behaviorOptions[i]
```

## ConnectorFriction(...)



This method creates a connector friction behavior option for a [ConnectorSection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorsectionpyc.htm?ContextScope=all) object. Depending upon the arguments provided, the friction behavior can be Coulomb-like or hysteretic in nature.



### Path

```
          import connectorBehavior
          connectorBehavior.ConnectorFriction
          import odbConnectorBehavior
          odbConnectorBehavior.ConnectorFriction
        
```

### Required arguments

None.

### Optional arguments

- *frictionModel*

  A SymbolicConstant specifying the desired frictional response model. Possible values are PREDEFINED and USER_CUSTOMIZED. The default value is PREDEFINED.

- *slipStyle*

  A SymbolicConstant specifying the method of indicating the slip direction: either specified or computed based upon the force potential data. Possible values are SPECIFY and COMPUTE. The default value is SPECIFY.This argument is applicable only if *frictionModel*=USER_CUSTOMIZED.

- *tangentDirection*

  None or an Int specifying the direction for which the frictional behavior is specified. Possible values are 1 ≤≤ *tangentDirection* ≤≤ 6, indicating an available component of relative motion. This argument applies only if *frictionModel*=USER_CUSTOMIZED and if *slipStyle*=SPECIFY. The default value is None.

- *stickStiffness*

  None or a Float specifying the stick stiffness associated with the frictional behavior in the direction specified by *tangentDirection*. If this argument is omitted, Abaqus computes an appropriate number for the stick stiffness. The default value is None.

- *componentType*

  A SymbolicConstant specifying the type of the *independentComponents*. Possible values are POSITION, MOTION, and NO_INDEPENDENT_COMPONENTS. The default value is NO_INDEPENDENT_COMPONENTS.

- *slipDependency*

  A Boolean specifying whether the table data depend on accumulated slip. The default value is OFF.This argument applies only if *frictionModel*=USER_CUSTOMIZED.

- *temperatureDependency*

  A Boolean specifying whether the table data depend on temperature. The default value is OFF.This argument applies only if *frictionModel*=USER_CUSTOMIZED.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.This argument applies only if *frictionModel*=USER_CUSTOMIZED.

- *useContactForceComponent*

  A Boolean specifying whether the contact force component will be defined. The default value is OFF.This argument applies only if *frictionModel*=USER_CUSTOMIZED.

- *contactForceStyle*

  A SymbolicConstant specifying the method of indicating the contact force component direction: either specified or computed based on upon a DerivedComponent. Possible values are COMPONENT_NUMBER and DERIVED_COMPONENT. The default value is COMPONENT_NUMBER.This argument is applicable only if *frictionModel*=USER_CUSTOMIZED and if *useContactForceComponent*=ON.

- *contactForceComponent*

  An Int specifying the contact force component direction. This argument applies only if *frictionModel*=USER_CUSTOMIZED, if *useContactForceComponent*=ON, and if *contactForceStyle*=COMPONENT_NUMBER. The default value is 0.

- *forcePotentialOperator*

  A SymbolicConstant specifying the contribution operator for the force potential contributions. Possible values are SUM and MAXIMUM. The default value is SUM.This argument is applicable only if *frictionModel*=USER_CUSTOMIZED and if *slipStyle*=COMPUTE.

- *forcePotentialExponent*

  A Float specifying the number equal to the inverse of the overall exponent in the force potential definition. The default value is 2.0.This argument is applicable only if *frictionModel*=USER_CUSTOMIZED, if *slipStyle*=COMPUTE, and if *forcePotentialOperator*=SUM.

- *connectorPotentials*

  A [ConnectorPotentialArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorpotentialpyc.htm?ContextScope=all) object specifying one [ConnectorPotential](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorpotentialpyc.htm?ContextScope=all) object for each force potential contribution. This member can be specified only if *frictionModel*=USER_CUSTOMIZED, and if *slipStyle*=COMPUTE.

- *table*

  A sequence of sequences of Floats specifying friction properties. The default value is an empty sequence.If *frictionModel*=PREDEFINED, each sequence of the table data specifies:If applicable, the first geometric scaling constant relevant to frictional interactions.Etc., up to as many geometric scaling constants as are associated with this connection type.Internal contact force/moment generating friction in the first predefined slip direction.If applicable, internal contact force/moment generating friction in the second predefined slip direction.Connector constitutive relative motion in the direction specified by *independentComponent*.Accumulated slip in the first predefined slip direction, if the data depend on accumulated slip.Temperature, if the data depend on temperature.Value of the first field variable, if the data depend on field variables.Value of the second field variable.Etc.If *frictionModel*=USER_CUSTOMIZED, each sequence of the table data specifies:Effective radius of the cylindrical or spherical surface over which frictional slip occurs in the connector associated with frictional effects in the direction specified by *tangentDirection*. This radius is relevant only if the connection type includes an available rotational component of relative motion and *tangentDirection*=SLIP_DIRECTION.Internal contact force/moment generating friction in the direction specified by *tangentDirection*.Connector constitutive relative motion in the direction specified by *independentComponent*.Accumulated slip in the direction specified by *tangentDirection*, if the data depend on accumulated slip.Temperature, if the data depend on temperature.Value of the first field variable, if the data depend on field variables.Value of the second field variable.Etc.

- *independentComponents*

  A sequence of Ints specifying the independent components. Possible values are 1 ≤≤ *independentComponents* ≤≤ 6. In addition, each independent component value must be unique. The *independentComponents* argument applies only if *frictionModel*=USER_CUSTOMIZED. Only available components can be specified. The default value is an empty sequence.

### Return value

A ConnectorFriction object.

### Exceptions

ValueError and TextError.



## setValues(...)



This method modifies the ConnectorFriction object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorFriction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorfrictionpyc.htm?ContextScope=all#simaker-connectorfrictionconnectorfrictionpyc)method.

### Return value

None.

### Exceptions

ValueError.



## Members

The ConnectorFriction object has members with the same names and descriptions as the arguments to the [ConnectorFriction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorfrictionpyc.htm?ContextScope=all#simaker-connectorfrictionconnectorfrictionpyc)method.

In addition, the ConnectorFriction object can have the following members:

- *tangentialBehavior*

  A [TangentialBehavior](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tangentialbehaviorpyc.htm?ContextScope=all) object.

- *derivedComponent*

  A [DerivedComponent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-derivedcomponentpyc.htm?ContextScope=all) object specifying the [DerivedComponent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-derivedcomponentpyc.htm?ContextScope=all) used to compute the contact force component direction. This argument applies only if *frictionModel*=USER_CUSTOMIZED, if *useContactForceComponent*=ON, and if *contactForceStyle*=DERIVED_COMPONENT.

- *options*

  A [ConnectorOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectoroptionspyc.htm?ContextScope=all) object specifying the [ConnectorOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectoroptionspyc.htm?ContextScope=all) used to define tabular options for this [ConnectorBehaviorOption](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorbehavioroptionpyc.htm?ContextScope=all).



## Corresponding analysis keywords

- [CONNECTOR FRICTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorfriction.htm?ContextScope=all#simakey-r-connectorfriction), [FRICTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-friction.htm?ContextScope=all#simakey-r-friction), [CONNECTOR POTENTIAL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorpotential.htm?ContextScope=all#simakey-r-connectorpotential), [CONNECTOR DERIVED COMPONENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorderivedcomponent.htm?ContextScope=all#simakey-r-connectorderivedcomponent)