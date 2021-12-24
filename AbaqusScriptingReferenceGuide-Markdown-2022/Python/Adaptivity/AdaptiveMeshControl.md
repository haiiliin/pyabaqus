# AdaptiveMeshControl object

The AdaptiveMeshControl object is used to control various aspects of Arbitrary Lagrangian Eularian (ALE) style adaptive smoothing and advection algorithms applied to an ALE adaptive mesh domain.

## Access

```
import step
mdb.models[name].adaptiveMeshControls[name]
```

## AdaptiveMeshControl(...)



This method creates an AdaptiveMeshControl object.



### Path

```
mdb.models[name].AdaptiveMeshControl
```

### Required arguments

- *name*

  A String specifying the name of the object.

### Optional arguments

- *remapping*

  A SymbolicConstant specifying the remapping algorithm. Possible values are FIRST_ORDER_ADVECTION and SECOND_ORDER_ADVECTION. The default value is SECOND_ORDER_ADVECTION.

- *smoothingAlgorithm*

  A SymbolicConstant specifying the type of smoothing algorithm to use. Possible values are STANDARD and GEOMETRY_ENHANCED. The default value is GEOMETRY_ENHANCED.

- *smoothingPriority*

  A SymbolicConstant specifying the type of smoothing to perform. Possible values are UNIFORM and GRADED. The default value is UNIFORM.

- *initialFeatureAngle*

  A Float specifying the initial geometric feature angle, θI, in degrees. Possible values are 0° ≤θI≤ 180°. The default value is 30.0.

- *transitionFeatureAngle*

  A Float specifying the transitional feature angle, θT, in degrees. Possible values are 0° ≤θT≤ 180°. The default value is 30.0.

- *momentumAdvection*

  A SymbolicConstant specifying the type of momentum advection algorithm. Possible values are ELEMENT_CENTER_PROJECTION and HALF_INDEX_SHIFT. The default value is ELEMENT_CENTER_PROJECTION.

- *meshingPredictor*

  A SymbolicConstant specifying the nodal starting location to use for remeshing. Possible values are CURRENT and PREVIOUS. The default value is CURRENT.

- *curvatureRefinement*

  A Float specifying the solution dependence weight, αC. Possible values are 0.0 ≤αC≤ 1.0. The default value is 1.0.

- *volumetricSmoothingWeight*

  A Float specifying the weight used by Abaqus/Explicit for the volumetric smoothing method. The default value is 1.0.

- *laplacianSmoothingWeight*

  A Float specifying the weight for the Laplacian smoothing method. The default value is 0.0.

- *equipotentialSmoothingWeight*

  A Float specifying the weight for the equipotential smoothing method. The default value is 0.0.

- *meshConstraintAngle*

  A Float specifying the initial geometric feature angle, θC. Possible values are 0° ≤θC≤ 180°. The default value is 60.0.

- *originalConfigurationProjectionWeight*

  A Float specifying the weight for the original configuration projection method. The default value is 1.0.

- *standardVolumetricSmoothingWeight*

  A Float specifying the weight used by Abaqus/Standard for the volumetric smoothing method. The default value is 0.0.

### Return value

An AdaptiveMeshControl object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the AdaptiveMeshControl object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AdaptiveMeshControl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshcontrolpyc.htm?ContextScope=all#simaker-adaptivemeshcontroladaptivemeshcontrolpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The AdaptiveMeshControl object has members with the same names and descriptions as the arguments to the [AdaptiveMeshControl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshcontrolpyc.htm?ContextScope=all#simaker-adaptivemeshcontroladaptivemeshcontrolpyc)method.