# CavityRadiation object

The CavityRadiation object defines cavities for thermal radiation heat transfer and controls the calculation of viewfactors.

The CavityRadiation object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## CavityRadiation(...)



This method creates a CavityRadiation object.



### Path

```
mdb.models[name].CavityRadiation
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the cavity radiation interaction should be created.

- *surfaces*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surfaces for which radiation viewfactor control is being specified.

### Optional arguments

- *surfaceEmissivities*

  A sequence of Strings specifying the names of the Cavity Radiation properties containing the surface emissivity data. One name per specified surface. The emissivity data is ignored when *surfaceReflection*=OFF.

- *ambientTemp*

  None or a Float specifying the reference ambient temperature value, θ0θ0. Specifying a value indicates an open cavity. The default value is None.

- *blocking*

  A SymbolicConstant specifying the blocking checks to be performed in the viewfactor calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING. The default value is BLOCKING_ALL.

- *blockingSurfaces*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surfaces that provide blocking inside the cavity. This argument applies only when *blocking*=PARTIAL_BLOCKING.

- *rangeOfView*

  None or a Float specifying the maximum distance between surface facets at which viewfactors are calculated. More distant facets are deemed too far apart to exchange significant amounts of heat through radiation effects, and the viewfactors between these facets are assumed to be zero. If *rangeOfView*=None, there is no upper limit. The default value is None.

- *surfaceReflection*

  A Boolean specifying whether heat reflections are to be included in the cavity radiation calculations. The default value is ON.

- *viewfactorAccurTol*

  A Float specifying the acceptable tolerance for the viewfactor calculations. The default value is 0.05.

- *minInfinitesimalRatio*

  A Float specifying the facet area ratio above which the infinitesimal-to-finite area approximation is used for viewfactor calculations. The default value is 64.0.

- *numPointsPerEdge*

  An Int specifying the number of Gauss integration points to be used along each edge when the numerical integration of contour integrals is used for viewfactor calculations. One to five integration points are allowed. The default value is 3.

- *minLumpedAreaDS*

  A Float specifying the nondimensional distance-square value above which the lumped area approximation is used for viewfactor calculations. The default value is 5.0.

- *cyclicSymmetry*

  A Boolean specifying whether cyclic symmetry will be applied. This argument cannot be specified for axisymmetric models. The default value is OFF.

- *cyclicImages*

  An Int specifying the number of cyclically similar images that compose the cavity formed as a result of this symmetry. This argument applies only when *cyclicSymmetry*=ON. The default value is 2.

- *cyclicRotPt*

  A [ModelDot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying the rotation axis point. This argument applies only when *cyclicSymmetry*=ON.

- *cyclicRotEndPt*

  A [ModelDot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying the rotation axis end point. This argument applies only for three-dimensional models, and only when *cyclicSymmetry*=ON.

- *cyclicSymPt*

  A [ModelDot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying the symmetry axis end point. This argument applies only when *cyclicSymmetry*=ON.

- *periodicSymmetries*

  An Int specifying the number of periodic symmetries that will be applied. The default value is 0.

- *periodicImages_1*

  An Int specifying the number of repetitions used in the numerical calculation of the cavity viewfactors resulting from the first periodic symmetry. The result of this symmetry is a cavity composed of the cavity surface defined in the model plus twice the value of *periodicImages_1*. This argument applies only when *periodicSymmetries* is greater than zero. The default value is 2.

- *periodicImages_2*

  An Int specifying the number of repetitions used in the numerical calculation of the cavity viewfactors resulting from the second periodic symmetry. The result of this symmetry is a cavity composed of the cavity surface defined in the model plus twice the value of *periodicImages_2*. This argument applies only when *periodicSymmetries* is greater than one. The default value is 2.

- *periodicImages_3*

  An Int specifying the number of repetitions used in the numerical calculation of the cavity viewfactors resulting from the third periodic symmetry. The result of this symmetry is a cavity composed of the cavity surface defined in the model plus twice the value of *periodicImages_3*. This argument applies only when *periodicSymmetries* = 3. The default value is 2.

- *periodicSymAxis_1*

  A straight Edge, a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum axis, or an ElementEdge object indicating the first line of symmetry in two-dimensional models. This argument applies only for 2D models, and when *periodicSymmetries* is greater than zero.

- *periodicSymAxis_2*

  A straight Edge, a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum axis, or an ElementEdge object indicating the second line of symmetry in two-dimensional models. This argument applies only for two-dimensional models, and when *periodicSymmetries* = 2.

- *periodicSymPlane_1*

  A planar Face, an ElementFace, or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum plane; indicating the first plane of symmetry in three-dimensional models. This argument applies only for three-dimensional models, and when *periodicSymmetries* is greater than zero.

- *periodicSymPlane_2*

  A planar Face, an ElementFace, or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum plane; indicating the second plane of symmetry in three-dimensional models. This argument applies only for three-dimensional models, and when *periodicSymmetries* is greater than one.

- *periodicSymPlane_3*

  A planar Face, an ElementFace, or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum plane; indicating the third plane of symmetry in three-dimensional models. This argument applies only for three-dimensional models, and when *periodicSymmetries* = 3.

- *periodicDistance_1*

  A sequence of sequences of Floats specifying the two points of the vector that describes the periodic distance for the first periodic symmetry. Each point is defined by a tuple of three coordinates indicating its position. This argument applies only when *periodicSymmetries* is greater than zero. The default value is an empty sequence.

- *periodicDistance_2*

  A sequence of sequences of Floats specifying the two points of the vector that describes the periodic distance for the second periodic symmetry. Each point is defined by a tuple of three coordinates indicating its position. This argument applies only when *periodicSymmetries* is greater than one. The default value is an empty sequence.

- *periodicDistance_3*

  A sequence of sequences of Floats specifying the two points of the vector that describes the periodic distance for the third periodic symmetry. Each point is defined by a tuple of three coordinates indicating its position. This argument applies only when *periodicSymmetries* = 3. The default value is an empty sequence.

- *periodicSymZ*

  None or a Float specifying the Z value indicating the symmetry reference line in axisymmetric models. This argument applies only for axisymmetric models, and when *periodicSymmetries* = 1. The default value is None.

- *periodicDistZ*

  None or a Float specifying the Z value indicating the periodic distance in axisymmetric models. This argument applies only for axisymmetric models, and when *periodicSymmetries* = 1. The default value is None.

- *reflectionSymmetries*

  An Int specifying the number of reflection symmetries will be applied. The default value is 0.

- *reflectionSymAxis_1*

  A straight Edge, a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum axis, or an ElementEdge object indicating the first line of symmetry in two-dimensional models. This argument applies only for two-dimensional models, and when *reflectionSymmetries* is greater than zero.

- *reflectionSymAxis_2*

  A straight Edge, a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum axis, or an ElementEdge object indicating the second line of symmetry in two-dimensional models. This argument applies only for two-dimensional models, and when *reflectionSymmetries* = 2.

- *reflectionSymPlane_1*

  A planar Face, an ElementFace, or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum plane; indicating the first plane of symmetry in three-dimensional models. This argument applies only for three-dimensional models, and when *reflectionSymmetries* is greater than zero.

- *reflectionSymPlane_2*

  A planar Face, an ElementFace, or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum plane; indicating the second plane of symmetry in three-dimensional models. This argument applies only for three-dimensional models, and when *reflectionSymmetries* is greater than one.

- *reflectionSymPlane_3*

  A planar Face, an ElementFace, or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object representing a datum plane; indicating the third plane of symmetry in three-dimensional models. This argument applies only for three-dimensional models, and when *reflectionSymmetries* = 3.

- *reflectionSymZ*

  None or a Float specifying the Z value indicating the symmetry reference line in axisymmetric models. This argument applies only for axisymmetric models, and when *reflectionSymmetries* = 1. The default value is None.

### Return value

A CavityRadiation object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing CavityRadiation object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CavityRadiation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cavityradiationpyc.htm?ContextScope=all#simaker-cavityradiationcavityradiationpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data of an existing CavityRadiation object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *blocking*

  A SymbolicConstant specifying the blocking checks to be performed in the viewfactor calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING. The default value is BLOCKING_ALL.

- *blockingSurfaces*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surfaces that provide blocking inside the cavity. This argument applies only when *blocking*=PARTIAL_BLOCKING.

- *rangeOfView*

  None or a Float specifying the maximum distance between surface facets at which viewfactors are calculated. More distant facets are deemed too far apart to exchange significant amounts of heat through radiation effects, and the viewfactors between these facets are assumed to be zero. If *rangeOfView*=None, there is no upper limit. The default value is None.

- *surfaceReflection*

  A Boolean specifying whether heat reflections are to be included in the cavity radiation calculations. The default value is ON.

- *viewfactorAccurTol*

  A Float specifying the acceptable tolerance for the viewfactor calculations. The default value is 0.05.

### Return value

None.

### Exceptions

None.



## Members

The CavityRadiation object can have the following members:

- *name*

  A String specifying the repository key.

- *ambientTemp*

  None or a Float specifying the reference ambient temperature value, θ0θ0. Specifying a value indicates an open cavity. The default value is None.

- *minInfinitesimalRatio*

  A Float specifying the facet area ratio above which the infinitesimal-to-finite area approximation is used for viewfactor calculations. The default value is 64.0.

- *numPointsPerEdge*

  An Int specifying the number of Gauss integration points to be used along each edge when the numerical integration of contour integrals is used for viewfactor calculations. One to five integration points are allowed. The default value is 3.

- *minLumpedAreaDS*

  A Float specifying the nondimensional distance-square value above which the lumped area approximation is used for viewfactor calculations. The default value is 5.0.

- *cyclicSymmetry*

  A Boolean specifying whether cyclic symmetry will be applied. This argument cannot be specified for axisymmetric models. The default value is OFF.

- *cyclicImages*

  An Int specifying the number of cyclically similar images that compose the cavity formed as a result of this symmetry. This argument applies only when *cyclicSymmetry*=ON. The default value is 2.

- *periodicSymmetries*

  An Int specifying the number of periodic symmetries that will be applied. The default value is 0.

- *periodicImages_1*

  An Int specifying the number of repetitions used in the numerical calculation of the cavity viewfactors resulting from the first periodic symmetry. The result of this symmetry is a cavity composed of the cavity surface defined in the model plus twice the value of *periodicImages_1*. This argument applies only when *periodicSymmetries* is greater than zero. The default value is 2.

- *periodicImages_2*

  An Int specifying the number of repetitions used in the numerical calculation of the cavity viewfactors resulting from the second periodic symmetry. The result of this symmetry is a cavity composed of the cavity surface defined in the model plus twice the value of *periodicImages_2*. This argument applies only when *periodicSymmetries* is greater than one. The default value is 2.

- *periodicImages_3*

  An Int specifying the number of repetitions used in the numerical calculation of the cavity viewfactors resulting from the third periodic symmetry. The result of this symmetry is a cavity composed of the cavity surface defined in the model plus twice the value of *periodicImages_3*. This argument applies only when *periodicSymmetries* = 3. The default value is 2.

- *periodicSymZ*

  None or a Float specifying the Z value indicating the symmetry reference line in axisymmetric models. This argument applies only for axisymmetric models, and when *periodicSymmetries* = 1. The default value is None.

- *periodicDistZ*

  None or a Float specifying the Z value indicating the periodic distance in axisymmetric models. This argument applies only for axisymmetric models, and when *periodicSymmetries* = 1. The default value is None.

- *reflectionSymmetries*

  An Int specifying the number of reflection symmetries will be applied. The default value is 0.

- *reflectionSymZ*

  None or a Float specifying the Z value indicating the symmetry reference line in axisymmetric models. This argument applies only for axisymmetric models, and when *reflectionSymmetries* = 1. The default value is None.

- *createStepName*

  A String specifying the name of the step in which the cavity radiation interaction should be created.

- *surfaces*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surfaces for which radiation viewfactor control is being specified.

- *surfaceEmissivities*

  A tuple of Strings specifying the names of the Cavity Radiation properties containing the surface emissivity data. One name per specified surface. The emissivity data is ignored when *surfaceReflection*=OFF.

- *cyclicRotPt*

  A [ModelDot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying the rotation axis point. This argument applies only when *cyclicSymmetry*=ON.

- *cyclicRotEndPt*

  A [ModelDot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying the rotation axis end point. This argument applies only for three-dimensional models, and only when *cyclicSymmetry*=ON.

- *cyclicSymPt*

  A [ModelDot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying the symmetry axis end point. This argument applies only when *cyclicSymmetry*=ON.

- *periodicDistance_1*

  A tuple of tuples of Floats specifying the two points of the vector that describes the periodic distance for the first periodic symmetry. Each point is defined by a tuple of three coordinates indicating its position. This argument applies only when *periodicSymmetries* is greater than zero. The default value is an empty sequence.

- *periodicDistance_2*

  A tuple of tuples of Floats specifying the two points of the vector that describes the periodic distance for the second periodic symmetry. Each point is defined by a tuple of three coordinates indicating its position. This argument applies only when *periodicSymmetries* is greater than one. The default value is an empty sequence.

- *periodicDistance_3*

  A tuple of tuples of Floats specifying the two points of the vector that describes the periodic distance for the third periodic symmetry. Each point is defined by a tuple of three coordinates indicating its position. This argument applies only when *periodicSymmetries* = 3. The default value is an empty sequence.



## Corresponding analysis keywords

- [CAVITY DEFINITION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cavitydefinition.htm?ContextScope=all#simakey-r-cavitydefinition), SET PROPERTY
- [CYCLIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cyclic.htm?ContextScope=all#simakey-r-cyclic)
- [EMISSIVITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-emissivity.htm?ContextScope=all#simakey-r-emissivity)
- [PERIODIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-periodic.htm?ContextScope=all#simakey-r-periodic)
- [RADIATION SYMMETRY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-radiationsymmetry.htm?ContextScope=all#simakey-r-radiationsymmetry)
- [RADIATION VIEWFACTOR](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-radiationviewfactor.htm?ContextScope=all#simakey-r-radiationviewfactor)
- [REFLECTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-reflection.htm?ContextScope=all#simakey-r-reflection)