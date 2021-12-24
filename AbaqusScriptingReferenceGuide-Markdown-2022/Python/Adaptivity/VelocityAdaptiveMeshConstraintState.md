# VelocityAdaptiveMeshConstraintState object

The VelocityAdaptiveMeshConstraintState object stores the propagating data for an Arbitrary Lagrangian Eularian (ALE) style velocity adaptive mesh constraint in a step. One instance of this object is created internally by the [VelocityAdaptiveMeshConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocityadaptivemeshconstraintpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [VelocityAdaptiveMeshConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocityadaptivemeshconstraintpyc.htm?ContextScope=all) object.

The VelocityAdaptiveMeshConstraintState object has no constructor or methods.

The VelocityAdaptiveMeshConstraintState object is derived from the [AdaptiveMeshConstraintState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshconstraintstatepyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name].adaptiveMeshConstraintStates[name]
```

## Members

The VelocityAdaptiveMeshConstraintState object has the following members:

- *v1*

  A Float specifying the velocity component in the 1-direction.

- *v2*

  A Float specifying the velocity component in the 2-direction.

- *v3*

  A Float specifying the velocity component in the 3-direction.

- *vr1*

  A Float specifying the rotational velocity component about the 1-direction.

- *vr2*

  A Float specifying the rotational velocity component about the 2-direction.

- *vr3*

  A Float specifying the rotational velocity component about the 3-direction.

- *v1State*

  A SymbolicConstant specifying the propagation state of the velocity component in the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *v2State*

  A SymbolicConstant specifying the propagation state of the velocity component in the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *v3State*

  A SymbolicConstant specifying the propagation state of the velocity component in the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *vr1State*

  A SymbolicConstant specifying the propagation state of the rotational velocity component about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *vr2State*

  A SymbolicConstant specifying the propagation state of the rotational velocity component about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *vr3State*

  A SymbolicConstant specifying the propagation state of the rotational velocity component about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [AdaptiveMeshConstraintState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshconstraintstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the adaptive mesh constraint has no amplitude reference.



## Corresponding analysis keywords

- [ADAPTIVE MESH CONSTRAINT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-adaptivemeshconstraint.htm?ContextScope=all#simakey-r-adaptivemeshconstraint), TYPE=VELOCITY (degree of freedom: 1, 2, 3, 4, 5, or 6)