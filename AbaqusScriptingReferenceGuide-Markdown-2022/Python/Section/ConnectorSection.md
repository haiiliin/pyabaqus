# ConnectorSection object

A ConnectorSection object describes the connection type and the behavior of a connector.

The ConnectorSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## ConnectorSection(...)



This method creates a ConnectorSection object.



### Path

```
mdb.models[name].ConnectorSection
session.odbs[name].ConnectorSection
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *assembledType*

  A SymbolicConstant specifying the assembled connection type. Possible values are:NONEBEAMBUSHINGCVJOINTCYLINDRICALHINGEPLANARRETRACTORSLIPRINGTRANSLATORUJOINTWELDThe default value is NONE.You cannot include the *assembledType* argument if *translationalType* or *rotationalType* are given a value other than NONE. At least one of the arguments *assembledType*, *translationalType*, or *rotationalType* must be given a value other than NONE.

- *rotationalType*

  A SymbolicConstant specifying the basic rotational connection type. Possible values are:NONEALIGNCARDANCONSTANT_VELOCITYEULERFLEXION_TORSIONFLOW_CONVERTERPROJECTION_FLEXION_TORSIONREVOLUTEROTATIONROTATION_ACCELEROMETERUNIVERSALThe default value is NONE.You cannot include the *rotationalType* argument if *assembledType* is given a value other than NONE. At least one of the arguments *assembledType*, *translationalType*, or *rotationalType* must be given an value other than NONE.

- *translationalType*

  A SymbolicConstant specifying the basic translational connection type. Possible values are:NONEACCELEROMETERAXIALCARTESIANJOINLINKPROJECTION_CARTESIANRADIAL_THRUSTSLIDE_PLANESLOTThe default value is NONE.You cannot include the *translationalType* argument if *assembledType* is given a value other than NONE. At least one of the arguments *assembledType*, *translationalType*, or *rotationalType* must be given an value other than NONE.

- *integration*

  A SymbolicConstant specifying the time integration scheme to use for analysis. This argument is applicable only to an Abaqus/Explicit analysis. Possible values are UNSPECIFIED, IMPLICIT, and EXPLICIT. The default value is UNSPECIFIED.

- *u1ReferenceLength*

  None or a Float specifying the reference length associated with constitutive response for the first component of relative motion. The default value is None.

- *u2ReferenceLength*

  None or a Float specifying the reference length associated with constitutive response for the second component of relative motion. The default value is None.

- *u3ReferenceLength*

  None or a Float specifying the reference length associated with constitutive response for the third component of relative motion. The default value is None.

- *ur1ReferenceAngle*

  None or a Float specifying the reference angle in degrees associated with constitutive response for the fourth component of relative motion. The default value is None.

- *ur2ReferenceAngle*

  None or a Float specifying the reference angle in degrees associated with constitutive response for the fifth component of relative motion. The default value is None.

- *ur3ReferenceAngle*

  None or a Float specifying the reference angle in degrees associated with constitutive response for the sixth component of relative motion. The default value is None.

- *massPerLength*

  None or a Float specifying the mass per unit reference length of belt material. This argument is applicable only when *assembledType*=SLIPRING, and must be specified in that case. The default value is None.

- *contactAngle*

  None or a Float specifying the contact angle made by the belt wrapping around node b. This argument is applicable only to an Abaqus/Explicit analysis, and only when *assembledType*=SLIPRING. The default value is None.

- *materialFlowFactor*

  A Float specifying the scaling factor for material flow at node b. This argument is applicable only when *assembledType*=RETRACTOR or *rotationalType*=FLOW_CONVERTER. The default value is 1.0.

- *regularize*

  A Boolean specifying whether or not all tabular data associated with the *behaviorOptions* will be regularized. This argument is applicable only for an Abaqus/Explicit analysis. The default value is ON.

- *defaultTolerance*

  A Boolean specifying whether or not the default regularization tolerance will be used for all tabular data associated with the *behaviorOptions*. This argument is applicable only for an Abaqus/Explicit analysis and only if *regularize*=ON. The default value is ON.

- *regularization*

  A Float specifying the regularization increment to be used for all tabular data associated with the *behaviorOptions*. This argument is applicable only for an Abaqus/Explicit analysis and only if *regularize*=ON and *defaultTolerance*=OFF. The default value is 0.03.

- *extrapolation*

  A SymbolicConstant specifying the extrapolation technique to be used for all tabular data associated with the *behaviorOptions*. Possible values are CONSTANT and LINEAR. The default value is CONSTANT.

- *behaviorOptions*

  A [ConnectorBehaviorOptionArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorbehavioroptionpyc.htm?ContextScope=all) object.

### Return value

A ConnectorSection object.

### Exceptions

InvalidNameError and RangeError.



## setValues(...)



This method modifies the ConnectorSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorsectionpyc.htm?ContextScope=all#simaker-connectorsectionconnectorsectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The ConnectorSection object has members with the same names and descriptions as the arguments to the [ConnectorSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorsectionpyc.htm?ContextScope=all#simaker-connectorsectionconnectorsectionpyc)method.



## Corresponding analysis keywords

- [CONNECTOR SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorsection.htm?ContextScope=all#simakey-r-connectorsection)
- [CONNECTOR BEHAVIOR](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorbehavior.htm?ContextScope=all#simakey-r-connectorbehavior)
- [CONNECTOR CONSTITUTIVE REFERENCE](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorconstitutivereference.htm?ContextScope=all#simakey-r-connectorconstitutivereference)