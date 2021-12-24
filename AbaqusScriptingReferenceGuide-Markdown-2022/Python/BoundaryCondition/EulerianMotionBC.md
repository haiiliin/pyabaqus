# EulerianMotionBC object

The EulerianMotionBC object stores the data for an Eulerian mesh motion boundary condition.

The EulerianMotionBC object is derived from the [BoundaryCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].boundaryConditions[name]
```

## EulerianMotionBC(...)



This method creates an EulerianMotionBC object.



### Path

```
mdb.models[name].EulerianMotionBC
```

### Required arguments

- *name*

  A String specifying the boundary condition repository key.

- *createStepName*

  A String specifying the name of the step in which the boundary condition is created.

- *instanceName*

  A String specifying the name of the Eulerian part instance.

### Optional arguments

- *followRegion*

  A Boolean specifying whether the mesh will follow a regular surface region or an Eulerian surface. The default value is ON.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

- *materialName*

  A String specifying the name of the Eulerian surface to follow. This argument applies only when *followRegion*=False.

- *ctrPosition1*

  A SymbolicConstant specifying the 1-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition1*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition1*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio1*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 1 direction. If *expansionRatio1*=None, then there is no upper limit. The default value is None.

- *contractRatio1*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 1 direction. The default value is 0.0.

- *ctrPosition2*

  A SymbolicConstant specifying the 2-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition2*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition2*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio2*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 2 direction. If *expansionRatio2*=None, then there is no upper limit. The default value is None.

- *contractRatio2*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 2 direction. The default value is 0.0.

- *ctrPosition3*

  A SymbolicConstant specifying the 3-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition3*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition3*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio3*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 3 direction. If *expansionRatio3*=None, then there is no upper limit. The default value is None.

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

### Return value

An EulerianMotionBC object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing EulerianMotionBC object in the step where it is created.



### Required arguments

None.

### Optional arguments

- *instanceName*

  A String specifying the name of the Eulerian part instance.

- *followRegion*

  A Boolean specifying whether the mesh will follow a regular surface region or an Eulerian surface. The default value is ON.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

- *materialName*

  A String specifying the name of the Eulerian surface to follow. This argument applies only when *followRegion*=False.

- *ctrPosition1*

  A SymbolicConstant specifying the 1-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition1*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition1*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio1*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 1 direction. If *expansionRatio1*=None, then there is no upper limit. The default value is None.

- *contractRatio1*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 1 direction. The default value is 0.0.

- *ctrPosition2*

  A SymbolicConstant specifying the 2-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition2*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition2*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio2*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 2 direction. If *expansionRatio2*=None, then there is no upper limit. The default value is None.

- *contractRatio2*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 2 direction. The default value is 0.0.

- *ctrPosition3*

  A SymbolicConstant specifying the 3-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition3*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition3*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio3*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 3 direction. If *expansionRatio3*=None, then there is no upper limit. The default value is None.

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

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing EulerianMotionBC object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the boundary condition is modified.

### Optional arguments

- *ctrPosition1*

  A SymbolicConstant specifying the 1-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition1*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition1*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio1*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 1 direction. If *expansionRatio1*=None, then there is no upper limit. The default value is None.

- *contractRatio1*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 1 direction. The default value is 0.0.

- *ctrPosition2*

  A SymbolicConstant specifying the 2-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition2*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition2*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio2*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 2 direction. If *expansionRatio2*=None, then there is no upper limit. The default value is None.

- *contractRatio2*

  A Float specifying the lower bounds on the allowable scaling of the mesh in the 2 direction. The default value is 0.0.

- *ctrPosition3*

  A SymbolicConstant specifying the 3-direction translational constraint on the center of the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

- *posPosition3*

  A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default value is FREE.

- *negPosition3*

  A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default value is FREE.

- *expansionRatio3*

  None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 3 direction. If *expansionRatio3*=None, then there is no upper limit. The default value is None.

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

### Return value

None.

### Exceptions

None.



## Members

The EulerianMotionBC object can have the following members:

- *name*

  A String specifying the boundary condition repository key.

- *followRegion*

  A Boolean specifying whether the mesh will follow a regular surface region or an Eulerian surface. The default value is ON.

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

- *instanceName*

  A String specifying the name of the Eulerian part instance.

- *materialName*

  A String specifying the name of the Eulerian surface to follow. This argument applies only when *followRegion*=False.

- *category*

  A SymbolicConstant specifying the category of the boundary condition. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the boundary condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.