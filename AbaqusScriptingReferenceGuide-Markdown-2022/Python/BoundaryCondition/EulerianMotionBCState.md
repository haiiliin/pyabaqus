# EulerianMotionBCState object

The EulerianMotionBCState object stores the propagating data for an Eulerian mesh motion boundary condition in a step. One instance of this object is created internally by the [EulerianMotionBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianmotionbcpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [EulerianMotionBC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianmotionbcpyc.htm?ContextScope=all) object.

The EulerianMotionBCState object has no constructor or methods.

The EulerianMotionBCState object is derived from the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].boundaryConditionStates[name]
```

## Members

The EulerianMotionBCState object has the following members:

- *ctrPosition1*

  A SymbolicConstant specifying the 1-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *ctrPosition2*

  A SymbolicConstant specifying the 2-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *ctrPosition3*

  A SymbolicConstant specifying the 3-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition1*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition2*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition3*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition1*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition2*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition3*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio1*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 1 direction. If *expansionRatio1*=None, then there is no upper limit. The default value is None.

- *expansionRatio2*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 2 direction. If *expansionRatio2*=None, then there is no upper limit. The default value is None.

- *expansionRatio3*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 3 direction. If *expansionRatio3*=None, then there is no upper limit. The default value is None.

- *contractRatio1*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 1 direction. The default value is 0.0.

- *contractRatio2*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 2 direction. The default value is 0.0.

- *contractRatio3*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 3 direction. The default value is 0.0.

- *allowContraction*

  A Boolean specifying whether the mesh is allowed to contract . The default value is ON.

- *aspectLimit*

  A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh aspects, 1-2, 2-3, 3-1). The default value is 10.0.

- *vmaxFactor*

  A Float specifying the multiplier for the mesh nodal velocity limit. The default value is 1.01.

- *volThreshold*

  A Float specifying the lower bounds on the volume fraction when determining which nodes to include in the surface bounding box calculation for an Eulerian material surface. This argument applies only when *followRegion*=False. The default value is 0.5.

- *bufferSize*

  None or a Float specifying the buffer between the surface box and the Eulerian section mesh bounding box. The default value is 2.0.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

- *status*

  A SymbolicConstant specifying the propagation state of the [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) object. Possible values are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the boundary condition has no amplitude reference.



## Corresponding analysis keywords

- [EULERIAN MESH MOTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-eulerianmeshmotion.htm?ContextScope=all#simakey-r-eulerianmeshmotion)