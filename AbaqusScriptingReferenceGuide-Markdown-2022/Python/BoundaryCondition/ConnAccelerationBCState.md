# ConnAccelerationBCState object

The ConnAccelerationBCState object stores the propagating data of a connector acceleration boundary condition in a step. One instance of this object is created internally by the [ConnAccelerationBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connaccelerationbcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [ConnAccelerationBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connaccelerationbcpyc.htm?ContextScope=all) object.

The ConnAccelerationBCState object has no constructor or methods.

The ConnAccelerationBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The ConnAccelerationBCState object has the following members:

- *a1*

  A Float specifying the connector acceleration component in the connector's local 1-direction.

- *a2*

  A Float specifying the connector acceleration component in the connector's local 2-direction.

- *a3*

  A Float specifying the connector acceleration component in the connector's local 3-direction.

- *ar1*

  A Float specifying the connector acceleration component in the connector's local 4-direction.

- *ar2*

  A Float specifying the connector acceleration component in the connector's local 5-direction.

- *ar3*

  A Float specifying the connector acceleration component in the connector's local 6-direction.

- *a1State*

  A SymbolicConstant specifying the propagation state of the connector acceleration component in the connector's local 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *a2State*

  A SymbolicConstant specifying the propagation state of the connector acceleration component in the connector's local 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *a3State*

  A SymbolicConstant specifying the propagation state of the connector acceleration component in the connector's local 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ar1State*

  A SymbolicConstant specifying the propagation state of the connector acceleration component in the connector's local 4-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ar2State*

  A SymbolicConstant specifying the propagation state of the connector acceleration component in the connector's local 5-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ar3State*

  A SymbolicConstant specifying the propagation state of the connector acceleration component in the connector's local 6-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [CONNECTOR MOTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectormotion.htm?ContextScope=all#simakey-r-connectormotion), TYPE=ACCELERATION (degree of freedom: 1, 2, 3, 4, 5, or 6)