# GeometricProperties object

The GeometricProperties object specifies surface interaction properties.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].geometricProperties
```

## GeometricProperties(...)



This method creates a GeometricProperties object.



### Path

```
mdb.models[name].interactionProperties[name].GeometricProperties
```

### Required arguments

None.

### Optional arguments

- *contactArea*

  A Float specifying the out-of-plane thickness of the surface for a two-dimensional model or cross-sectional area for every node in the node-based surface. The default value is 1.0.

- *padThickness*

  None or a Float specifying the thickness of an interfacial layer between the contacting surfaces. If *padThickness*=None, there is no interfacial layer. The default value is None.

- *trackingThickness*

  None or a Float specifying the thickness that determines the contacting surfaces to be tracked. The input value for this parameter cannot be negative. An internal default value is used if a zero value is input or if the parameter is omitted.

- *dependentVariables*

  An Int specifying the number of state-dependent variables. The default value is 0. This argument is applicable only if *modelType*=MODELTYPE_USER or *modelType*=MODELTYPE_USER_INTERACTION.

- *numProperties*

  An Int specifying the number of property values required. The default value is 0. This argument is applicable only if *modelType*=MODELTYPE_USER or *modelType*=MODELTYPE_USER_INTERACTION.

- *useUnsymmetricEqunProcedure*

  A Boolean specifying whether to use unsymmetric equation solution procedures. This argument is applicable only if *modelType*=MODELTYPE_USER or *modelType*=MODELTYPE_USER_INTERACTION.

- *modelType*

  A SymbolicConstant specifying the surface interaction model type.

### Return value

A GeometricProperties object.

### Exceptions

None.



## setValues(...)



This method modifies the GeometricProperties object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GeometricProperties](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricpropertiespyc.htm?ContextScope=all#simaker-geometricpropertiesgeometricpropertiespyc) method.

### Return value

None.

### Exceptions

None.



## Members

The GeometricProperties object has members with the same names and descriptions as the arguments to the [GeometricProperties](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricpropertiespyc.htm?ContextScope=all#simaker-geometricpropertiesgeometricpropertiespyc) method.



## Corresponding analysis keywords

- [SURFACE INTERACTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-surfaceinteraction.htm?ContextScope=all#simakey-r-surfaceinteraction)