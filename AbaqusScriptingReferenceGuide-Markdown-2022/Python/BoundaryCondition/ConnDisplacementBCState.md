# ConnDisplacementBCState object

The ConnDisplacementBCState object stores the propagating data for a connector displacement/rotation boundary condition in a step. One instance of this object is created internally by the [ConnDisplacementBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conndisplacementbcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [ConnDisplacementBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conndisplacementbcpyc.htm?ContextScope=all) object.

The ConnDisplacementBCState object has no constructor or methods.

The ConnDisplacementBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The ConnDisplacementBCState object has the following members:

- *u1*

  A Float or a Complex specifying the displacement component in the connector's local 1-direction.

- *u2*

  A Float or a Complex specifying the displacement component in the connector's local 2-direction.

- *u3*

  A Float or a Complex specifying the displacement component in the connector's local 3-direction.

- *ur1*

  A Float or a Complex specifying the rotational component in the connector's local 4-direction.

- *ur2*

  A Float or a Complex specifying the rotational component in the connector's local 5-direction.

- *ur3*

  A Float or a Complex specifying the rotational component in the connector's local 6-direction.

- *u1State*

  A SymbolicConstant specifying the propagation state of the displacement component in the connector's local 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *u2State*

  A SymbolicConstant specifying the propagation state of the displacement component in the connector's local 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *u3State*

  A SymbolicConstant specifying the propagation state of the displacement component in the connector's local 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ur1State*

  A SymbolicConstant specifying the propagation state of the rotational component in the connector's local 4-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ur2State*

  A SymbolicConstant specifying the propagation state of the rotational component in the connector's local 5-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ur3State*

  A SymbolicConstant specifying the propagation state of the rotational component in the connector's local 6-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [CONNECTOR MOTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectormotion.htm?ContextScope=all#simakey-r-connectormotion), TYPE=DISPLACEMENT (degree of freedom: 1, 2, 3, 4, 5, or 6)