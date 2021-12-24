# DisplacementBCState object

The DisplacementBCState object stores the propagating data for a displacement/rotation boundary condition in a step. One instance of this object is created internally by the [DisplacementBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [DisplacementBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbcpyc.htm?ContextScope=all) object.

The DisplacementBCState object has no constructor or methods.

The DisplacementBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The DisplacementBCState object has the following members:

- *u1*

  A Float or a Complex specifying the displacement component in the 1-direction.

- *u2*

  A Float or a Complex specifying the displacement component in the 2-direction.

- *u3*

  A Float or a Complex specifying the displacement component in the 3-direction.

- *ur1*

  A Float or a Complex specifying the rotational displacement component about the 1-direction.

- *ur2*

  A Float or a Complex specifying the rotational displacement component about the 2-direction.

- *ur3*

  A Float or a Complex specifying the rotational displacement component about the 3-direction.

- *u1State*

  A SymbolicConstant specifying the propagation state of the displacement component in the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *u2State*

  A SymbolicConstant specifying the propagation state of the displacement component in the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *u3State*

  A SymbolicConstant specifying the propagation state of the displacement component in the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ur1State*

  A SymbolicConstant specifying the propagation state of the rotational displacement component about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ur2State*

  A SymbolicConstant specifying the propagation state of the rotational displacement component about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *ur3State*

  A SymbolicConstant specifying the propagation state of the rotational displacement component about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [BOUNDARY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-boundary.htm?ContextScope=all#simakey-r-boundary), TYPE=DISPLACEMENT (degree of freedom: 1, 2, 3, 4, 5, or 6)