# TemperatureBCState object

The TemperatureBCState object stores the propagating data for a temperature boundary condition in a step. One instance of this object is created internally by the [TemperatureBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturebcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [TemperatureBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturebcpyc.htm?ContextScope=all) object.

The TemperatureBCState object has no constructor or methods.

The TemperatureBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The TemperatureBCState object has the following members:

- *magnitude*

  A Float specifying the temperature magnitude.

- *magnitudeState*

  A SymbolicConstant specifying the propagation state of the temperature magnitude. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *dofState*

  A SymbolicConstant specifying the propagation state of the *dof* member. Possible values are SET and UNCHANGED.

- *dof*

  A tuple of Ints specifying the degrees of freedom to which the boundary condition is applied.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [BOUNDARY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-boundary.htm?ContextScope=all#simakey-r-boundary) (degree of freedom: 11 for solids; 11, 12, etc. for shells)