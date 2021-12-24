# ConnectorMomentState object

The ConnectorMomentState object stores the propagating data for a connector moment in a step. One instance of this object is created internally by the [ConnectorMoment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectormomentpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [ConnectorMoment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectormomentpyc.htm?ContextScope=all) object.

The ConnectorMomentState object has no constructor or methods.

The ConnectorMomentState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The ConnectorMomentState object has the following members:

- *m1*

  A Float or a Complex specifying the connector moment component in the connector's local 4-direction. Although *m1*, *m2*, and *m3* are optional arguments, at least one of them must be nonzero.

- *m2*

  A Float or a Complex specifying the connector moment component in the connector's local 5direction.

- *m3*

  A Float or a Complex specifying the connector moment component in the connector's local 6-direction.

- *m1State*

  A SymbolicConstant specifying the propagation state of the load component in the connector's local 4-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *m2State*

  A SymbolicConstant specifying the propagation state of the load component in the connector's local 5-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *m3State*

  A SymbolicConstant specifying the propagation state of the load component in the connector's local 6-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *status*

  A SymbolicConstant specifying the propagation state of the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - BUILT_INTO_BASE_STATE

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the load has no amplitude reference.



## Corresponding analysis keywords

- [CONNECTOR LOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorload.htm?ContextScope=all#simakey-r-connectorload) (degree of freedom: 4, 5, or 6)