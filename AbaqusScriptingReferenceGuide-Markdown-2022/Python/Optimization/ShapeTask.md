# ShapeTask object

The ShapeTask object defines a shape task.

The ShapeTask object is derived from the [OptimizationTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationtaskpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name]
      
```

## ShapeTask(...)



This method creates a ShapeTask object.



### Path

```
          mdb.models[name].ShapeTask
        
```

### Required arguments

- *name*

  A String specifying the optimization task repository key.

### Optional arguments

- *abaqusSensitivities*

  A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities. The default value is True.

- *absoluteStepSizeControl*

  A SymbolicConstant specifying whether to control the permitted absolute step size by the average optimization displacement or minimum optimization displacement. Possible values are MINIMUM and AVERAGE. The default value is MINIMUM.

- *activateDurability*

  A boolean specifying whether or not the durability approach of optimization is turned on. The default value is ON.

- *additionalDurabilityFiles*

  A String specifying the path of additional files pertaining to durability optimization. Only valid if the *activateDurability* argument is ON.

- *algorithm*

  A SymbolicConstant specifying the optimization task algorithm. Possible values are GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is CONDITION_BASED_OPTIMIZATION.

- *constrainedLaplacianConvergenceLevel*

  A SymbolicConstant specifying the constrained Laplacian convergence level. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.

- *curvatureSmoothingEdgeLength*

  A Float specifying the edge length for the movement vector. The default value is 5.0.

- *durabilityInputfile*

  A string specifying the path of the input file. Only valid if the *activateDurability* argument is ON and is a required argument in that case.

- *durabilitySolver*

  A String specifying the type of solver for durability optimization. Possible values are: FE_SAFE, FEMFAT, FALANCS, MSC_FATIGUE, FE_FATIGUE, DESIGN_LIFE, CUSTOM, FEMSITE. The default value is FE_SAFE. Only valid if the *activateDurability* argument is ON.

- *equalityConstraintTolerance*

  A Float specifying the equality constraint tolerance. The default value is 10–3.

- *featureRecognitionAngle*

  A Float specifying the mesh smoothing feature recognition angle for edges and corners. The default value is 30.0.

- *filterExponent*

  A Float specifying the weight depending on the radius, used when *filterMaxRadius* is specified. The default value is 1.0.

- *filterMaxRadius*

  None or a Float specifying the maximum influence radius for equivalent stress. The default value is None.

- *filterRadiusReduction*

  None or a Float specifying the reduction of the radius depending on surface bending, used when *filterMaxRadius* is specified. The default value is None.

- *firstCycleDeletedVolumeTechnique*

  A SymbolicConstant specifying the method of specifying volume that can be removed immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and ABSOLUTE. The default value is OFF.

- *freezeBoundaryConditionRegions*

  A Boolean specifying whether to exclude nodes with boundary conditions from the optimization. The default value is OFF.

- *frozenBoundaryConditionRegion*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region in which to freeze boundary condition regions, or the SymbolicConstant MODEL, used with *freezeBoundaryConditionRegions*. The default value is MODEL.

- *geometricRestrictionEvaluationFrequency*

  A SymbolicConstant specifying the frequency of evaluating geometric restrictions during mesh smoothing. Possible values are LOW, MEDIUM, and HIGH. The default value is LOW.

- *growthScaleFactor*

  A Float specifying the scale factor to apply to optimization displacements for nodes with growth. The default value is 1.0.

- *haltUponViolation*

  A Boolean specifying whether to halt the optimization if quality criteria are not satisified. The default value is OFF.

- *layerReferenceRegion*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region specifying the first node layer for mesh smoothing, used when *meshSmoothingRegionMethod* is TASK_REGION_LAYERS. The default value is None.

- *meshSmoothingRegionMethod*

  A SymbolicConstant specifying the method used to determine the mesh smoothing region. The REGION value uses the *smoothingRegion*. The NUMBER_OF_LAYERS value uses the *layerReferenceRegion*. The TASK_REGION_LAYERS value will smooth six layers using the task region. Possible values are TASK_REGION_LAYERS, REGION, and NUMBER_OF_LAYERS. The default value is TASK_REGION_LAYERS.

- *meshSmoothingStrategy*

  A SymbolicConstant specifying the method smoothing strategy. Possible values are CONSTRAINED_LAPLACIAN and LOCAL_GRADIENT. The default value is CONSTRAINED_LAPLACIAN.

- *midsideInterpolation*

  A SymbolicConstant specifying the approach used when treating midside node positions during optimization. POSITIONS indicates midside node positions are interpolated linearly by position. OPTIMIZATION_DISPLACEMENT indicates they are interpolated by optimization displacement of corner nodes. Possible values are POSITIONS and OPTIMIZATION_DISPLACEMENT. The default value is POSITIONS.

- *numFreeNodeLayers*

  The SymbolicConstant FIX_NONE or an Int specifying the number of node layers adjoining the task region to remain free during mesh smoothing. A value of 0 indicates that no layers are free and all layers are fixed. The default value is 0.

- *numSmoothedElementLayers*

  None or an Int specifying the number of layers for mesh smoothing when *meshSmoothingRegionMethod* is NUMBER_OF_LAYERS. The default value is None.

- *presumeFeasibleBCRegionAtStart*

  A Boolean specifying whether to ignore automatically frozen boundary condition regions in the first design cycle. This is used with *freezeBoundaryConditionRegions*. The default value is ON.

- *quadMaxAngle*

  A Float specifying the maximum angle for quad elements during mesh smoothing. The default value is 160.0.

- *quadMinAngle*

  A Float specifying the minimum angle for quad elements during mesh smoothing. The default value is 20.0.

- *quadSkew*

  A Float specifying the skew angle for quad elements during mesh smoothing, used with *reportQualityViolation*. The default value is 30.0.

- *quadTaper*

  A Float specifying the taper for quad elements during mesh smoothing, used with *reportQualityViolation*. The default value is 0.5.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the optimization task is applied. The default value is MODEL.

- *reportPoorQualityElements*

  A Boolean specifying whether to report poor quality elements during mesh smoothing. The default value is OFF.

- *reportQualityViolation*

  A Boolean specifying whether to report a quality criteria violation during mesh smoothing. The default value is OFF.

- *shrinkScaleFactor*

  A Float specifying the scale factor to apply to optimization displacements for nodes with shrinkage. The default value is 1.0.

- *smoothingRegion*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the mesh smoothing region, used when *meshSmoothingRegionMethod* is REGION. The default value is None.

- *targetMeshQuality*

  A SymbolicConstant specifying the target mesh quality for mesh smoothing. Possible values are NONE, LOW, MEDIUM, and HIGH. The default value is LOW.

- *tetAspectRatio*

  A Float specifying the tet element aspect ratio during mesh smoothing. The default value is 100.0.

- *tetMaxAspect*

  A Float specifying the maximum tet element aspect ratio during mesh smoothing. The default value is 8.0.

- *tetMinAspect*

  A Float specifying the minimum tet element aspect ratio during mesh smoothing. The default value is 0.222.

- *tetSkew*

  A Float specifying the tet element skew value during mesh smoothing. The default value is 100.0.

- *triMaxAngle*

  A Float specifying the tri element maximum angle during mesh smoothing. The default value is 140.0.

- *triMinAngle*

  A Float specifying the tri element maximum angle during mesh smoothing. The default value is 20.0.

- *updateShapeBasisVectors*

  A SymbolicConstant specifying whether to update shape basis vectors in the first design cycle or every design cycle. Possible values are EVERY_CYCLE and FIRST_CYCLE. The default value is EVERY_CYCLE.

- *groupOperator*

  A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities. The default value of False means that the existing algorithm will be used.

### Return value

A ShapeTask object.

### Exceptions

None.



## setValues(...)



This method modifies the ShapeTask object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all#simaker-shapetaskshapetaskpyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The ShapeTask object has members with the same names and descriptions as the arguments to the [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all#simaker-shapetaskshapetaskpyc) method.

In addition, the ShapeTask object can have the following members:

- *designResponses*

  A repository of [DesignResponse](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designresponsepyc.htm?ContextScope=all) objects.

- *objectiveFunctions*

  A repository of [ObjectiveFunction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-objectivefunctionpyc.htm?ContextScope=all) objects.

- *optimizationConstraints*

  A repository of [OptimizationConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationconstraintpyc.htm?ContextScope=all) objects.

- *geometricRestrictions*

  A repository of [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) objects.

- *stopConditions*

  A repository of [StopCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stopconditionpyc.htm?ContextScope=all) objects.