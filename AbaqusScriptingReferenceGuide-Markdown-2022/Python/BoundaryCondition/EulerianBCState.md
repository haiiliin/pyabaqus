# EulerianBCState object

The EulerianBCState object stores the propagating data for an Eulerian boundary condition in a step. One instance of this object is created internally by the [EulerianBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianbcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [EulerianBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianbcpyc.htm?ContextScope=all) object.

The EulerianBCState object has no constructor or methods.

The EulerianBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The EulerianBCState object has the following members:

- *definition*

  A SymbolicConstant specifying the material flow conditions to be defined. Possible values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.

- *definitionState*

  A SymbolicConstant specifying the propagation state of the definition member. Possible values are UNSET, SET, and UNCHANGED.

- *inflowType*

  A SymbolicConstant specifying the material flow conditions to be defined. Possible values are FREE, NONE, and VOID. The default value is FREE.

- *inflowTypeState*

  A SymbolicConstant specifying the propagation state of the definition member. Possible values are UNSET, SET, and UNCHANGED.

- *outflowType*

  A SymbolicConstant specifying the material flow conditions to be defined. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The default value is ZERO_PRESSURE.

- *outflowTypeState*

  A SymbolicConstant specifying the propagation state of the definition member. Possible values are UNSET, SET, and UNCHANGED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [EULERIAN BOUNDARY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-eulerianboundary.htm?ContextScope=all#simakey-r-eulerianboundary)