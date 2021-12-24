# ConnVelocityBCState object

The ConnVelocityBCState object stores the propagating data for a velocity boundary condition in a step. One instance of this object is created internally by the [ConnVelocityBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connvelocitybcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [ConnVelocityBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connvelocitybcpyc.htm?ContextScope=all) object.

The ConnVelocityBCState object has no constructor or methods.

The ConnVelocityBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The ConnVelocityBCState object has the following members:

- *v1*

  A Float specifying the velocity component in the connector's local 1-direction.

- *v2*

  A Float specifying the velocity component in the connector's local 2-direction.

- *v3*

  A Float specifying the velocity component in the connector's local 3-direction.

- *vr1*

  A Float specifying the rotational velocity component in the connector's local 4-direction.

- *vr2*

  A Float specifying the rotational velocity component in the connector's local 5-direction.

- *vr3*

  A Float specifying the rotational velocity component in the connector's local 6-direction.

- *v1State*

  A SymbolicConstant specifying the propagation state of the velocity component in the connector's local 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *v2State*

  A SymbolicConstant specifying the propagation state of the velocity component in the connector's local 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *v3State*

  A SymbolicConstant specifying the propagation state of the velocity component in the connector's local 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *vr1State*

  A SymbolicConstant specifying the propagation state of the rotational velocity component in the connector's local 4–direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *vr2State*

  A SymbolicConstant specifying the propagation state of the rotational velocity component in the connector's local 5–direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *vr3State*

  A SymbolicConstant specifying the propagation state of the rotational velocity component in the connector's local 6–direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [CONNECTOR MOTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectormotion.htm?ContextScope=all#simakey-r-connectormotion), TYPE=VELOCITY (degree of freedom: 1, 2, 3, 4, 5, or 6)