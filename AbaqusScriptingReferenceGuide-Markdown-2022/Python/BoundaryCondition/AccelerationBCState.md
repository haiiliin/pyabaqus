# AccelerationBCState object

The AccelerationBCState object stores the propagating data of an acceleration boundary condition in a step. One instance of this object is created internally by the [AccelerationBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [AccelerationBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbcpyc.htm?ContextScope=all) object.

The AccelerationBCState object has no constructor or methods.

The AccelerationBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The AccelerationBCState object has the following members:

- *a1*

  A Float specifying the acceleration component in the 1-direction.

- *a2*

  A Float specifying the acceleration component in the 2-direction.

- *a3*

  A Float specifying the acceleration component in the 3-direction.

- *ar1*

  A Float specifying the rotational acceleration component about the 1-direction.

- *ar2*

  A Float specifying the rotational acceleration component about the 2-direction.

- *ar3*

  A Float specifying the rotational acceleration component about the 3-direction.

- *a1State*

  A SymbolicConstant specifying the propagation state of the acceleration component in the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *a2State*

  A SymbolicConstant specifying the propagation state of the acceleration component in the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *a3State*

  A SymbolicConstant specifying the propagation state of the acceleration component in the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ar1State*

  A SymbolicConstant specifying the propagation state of the rotational acceleration component about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ar2State*

  A SymbolicConstant specifying the propagation state of the rotational acceleration component about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ar3State*

  A SymbolicConstant specifying the propagation state of the rotational acceleration component about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [BOUNDARY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-boundary.htm?ContextScope=all#simakey-r-boundary), TYPE=ACCELERATION (degree of freedom: 1, 2, 3, 4, 5, or 6)