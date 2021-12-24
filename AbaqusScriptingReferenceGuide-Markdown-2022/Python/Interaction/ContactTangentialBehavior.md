# ContactTangentialBehavior object

The ContactTangentialBehavior object specifies tangential behavior for a contact interaction property.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].tangentialBehavior
```

## TangentialBehavior(...)



This method creates a ContactTangentialBehavior object.



### Path

```
mdb.models[name].interactionProperties[name].TangentialBehavior
```

### Required arguments

None.

### Optional arguments

- *formulation*

  A SymbolicConstant specifying the friction formulation. Possible values are FRICTIONLESS, PENALTY, EXPONENTIAL_DECAY, ROUGH, LAGRANGE, and USER_DEFINED. The default value is FRICTIONLESS.

- *directionality*

  A SymbolicConstant specifying the directionality of the friction. Possible values are ISOTROPIC and ANISOTROPIC. The default value is ISOTROPIC.

- *slipRateDependency*

  A Boolean specifying whether the data depend on slip rate. The default value is OFF.

- *pressureDependency*

  A Boolean specifying whether the data depend on contact pressure. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variables. The default value is 0.

- *exponentialDecayDefinition*

  A SymbolicConstant specifying the exponential decay definition. Possible values are COEFFICIENTS and TEST_DATA. The default value is COEFFICIENTS.

- *table*

  A sequence of sequences of Floats specifying tangential behavior. The items in the table data are described below.

- *shearStressLimit*

  None or a Float specifying the shear stress limit. If *shearStressLimit*=None, there is no upper limit. The default value is None.

- *maximumElasticSlip*

  A SymbolicConstant specifying what the maximum elastic slip will be. Possible values are FRACTION and ABSOLUTE_DISTANCE. The default value is FRACTION.

- *fraction*

  A Float specifying the fraction of a characteristic surface dimension. The default value is 0.0.

- *absoluteDistance*

  A Float specifying the absolute distance. The default value is 0.0.

- *elasticSlipStiffness*

  None or a Float specifying the elastic slip stiffness. If *elasticSlipStiffness*=None, there is no upper limit. The default value is None.

- *nStateDependentVars*

  An Int specifying the number of state-dependent variables. The default value is 0.

- *useProperties*

  A Boolean specifying whether property values will be used. The default value is OFF.

### Table data

If *formulation*=PENALTY or LAGRANGE, the table data specify the following:

- Friction coefficient in the first slip direction, μ1μ1.
- Friction coefficient in the second slip direction, μ2μ2 (if *directionality*=ANISOTROPIC).
- Slip rate, if the data depend on slip rate.
- Contact pressure, if the data depend on contact pressure.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *formulation*=EXPONENTIAL_DECAY and *exponentialDecayDefinition*=COEFFICIENTS, the table data specify the following:

- Static friction coefficient.
- Kinetic friction coefficient.
- Decay coefficient.

If *formulation*=EXPONENTIAL_DECAY and *exponentialDecayDefinition*=TEST_DATA, the table data specify the following:

- Friction coefficient.
- Slip rate.

If *formulation*=USER_DEFINED, the table data specify the following:

- Friction property.

### Return value

A ContactTangentialBehavior object.

### Exceptions

None.



## setValues(...)



This method modifies the ContactTangentialBehavior object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ContactTangentialBehavior ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contacttangentialbehaviorpyc.htm?ContextScope=all#simaker-contacttangentialbehaviortangentialbehaviorpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The ContactTangentialBehavior object has the following members:

- *formulation*

  A SymbolicConstant specifying the friction formulation. Possible values are FRICTIONLESS, PENALTY, EXPONENTIAL_DECAY, ROUGH, LAGRANGE, and USER_DEFINED. The default value is FRICTIONLESS.

- *directionality*

  A SymbolicConstant specifying the directionality of the friction. Possible values are ISOTROPIC and ANISOTROPIC. The default value is ISOTROPIC.

- *slipRateDependency*

  A Boolean specifying whether the data depend on slip rate. The default value is OFF.

- *pressureDependency*

  A Boolean specifying whether the data depend on contact pressure. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variables. The default value is 0.

- *exponentialDecayDefinition*

  A SymbolicConstant specifying the exponential decay definition. Possible values are COEFFICIENTS and TEST_DATA. The default value is COEFFICIENTS.

- *shearStressLimit*

  None or a Float specifying the shear stress limit. If *shearStressLimit*=None, there is no upper limit. The default value is None.

- *maximumElasticSlip*

  A SymbolicConstant specifying what the maximum elastic slip will be. Possible values are FRACTION and ABSOLUTE_DISTANCE. The default value is FRACTION.

- *fraction*

  A Float specifying the fraction of a characteristic surface dimension. The default value is 0.0.

- *absoluteDistance*

  A Float specifying the absolute distance. The default value is 0.0.

- *elasticSlipStiffness*

  None or a Float specifying the elastic slip stiffness. If *elasticSlipStiffness*=None, there is no upper limit. The default value is None.

- *nStateDependentVars*

  An Int specifying the number of state-dependent variables. The default value is 0.

- *useProperties*

  A Boolean specifying whether property values will be used. The default value is OFF.

- *table*

  A tuple of tuples of Floats specifying tangential behavior. The items in the table data are described below.



## Corresponding analysis keywords

- [FRICTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-friction.htm?ContextScope=all#simakey-r-friction)
- [CHANGE FRICTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-changefriction.htm?ContextScope=all#simakey-r-changefriction)