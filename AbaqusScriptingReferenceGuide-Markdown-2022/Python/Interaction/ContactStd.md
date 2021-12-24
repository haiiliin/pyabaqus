# ContactStd object

The ContactStd object defines the contact domain and associated properties during contact in an Abaqus/Standard analysis.

The ContactStd object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## ContactStd(...)



This method creates a ContactStd object.



### Path

```
mdb.models[name].ContactStd
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which this contact interaction is created.

### Optional arguments

- *useAllstar*

  A Boolean specifying whether the contacting surface pairs consist of all exterior faces in the model.

- *globalSmoothing*

  A Boolean specifying whether surface smoothing (geometric correction) is automatically applied to all eligible surfaces. The default value is ON.

- *includedPairs*

  A [RegionPairs](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpairspyc.htm?ContextScope=all) object specifying the domain pairs included in contact.

- *excludedPairs*

  A [RegionPairs](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpairspyc.htm?ContextScope=all) object specifying the domain pairs excluded from contact.

- *contactPropertyAssignments*

  A [ContactPropertyAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertyassignmentpyc.htm?ContextScope=all) object specifying the contact property assignments in the contact domain.

- *surfaceThicknessAssignments*

  A [SurfaceThicknessAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacethicknessassignmentpyc.htm?ContextScope=all) object specifying the surface thickness assignments in the contact domain.

- *surfaceOffsetAssignments*

  A [SurfaceOffsetAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceoffsetassignmentpyc.htm?ContextScope=all) object specifying the surface offset fraction assignments in the contact domain.

- *surfaceFeatureAssignments*

  A [SurfaceFeatureAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacefeatureassignmentpyc.htm?ContextScope=all) object specifying the surface feature angle assignments in the contact domain.

- *surfaceBeamSmoothingAssignments*

  A [SurfaceBeamSmoothingAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacebeamsmoothingassignmentpyc.htm?ContextScope=all) object specifying the surface beam smoothing assignments in the contact domain.

- *surfaceVertexCriteriaAssignments*

  A [SurfaceVertexCriteriaAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacevertexcriteriaassignmentpyc.htm?ContextScope=all) object specifying the surface vertex criteria assignments in the contact domain.

- *mainSecondaryAssignments*

  A [MainSecondaryAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-masterslaveassignmentpyc.htm?ContextScope=all) object specifying the main-secondary assignments in the contact domain.

- *initializationAssignments*

  An [InitializationAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-initializationassignmentpyc.htm?ContextScope=all) object specifying the contact initialization assignments in the contact domain.

- *stabilizationAssignments*

  A [StabilizationAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stabilizationassignmentpyc.htm?ContextScope=all) object specifying the contact stabilization assignments in the contact domain.

- *smoothingAssignments*

  A [SmoothingAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothingassignmentpyc.htm?ContextScope=all) object specifying the surface smoothing assignments in the contact domain.

- *slidingTransitionAssignments*

  A [SlidingTransitionAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-slidingtransitionassignmentpyc.htm?ContextScope=all) object specifying the sliding transition assignments in the contact domain.

- *slidingFormulationAssignments*

  A [SlidingFormulationAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-slidingformulationassignmentpyc.htm?ContextScope=all) object specifying the sliding formulation assignments in the contact domain.

### Return value

A ContactStd object.

### Exceptions

None.

## ContactStd(...)



This method creates a ContactStd object.



### Path

```
mdb.models[name].ContactStd
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which this contact interaction is created.

### Optional arguments

- *globalSmoothing*

  A Boolean specifying whether surface smoothing (geometric correction) is automatically applied to all eligible surfaces. The default value is ON.

- *surfaceBeamSmoothingAssignments*

  A sequence of tuples specifying the surface beam smoothing assignments. Each tuple contains two entries:

  - A region object specifying the surface to which the smoothing is assigned.
  - A Float specifying the surface smoothing value to be used for the surface.

- *surfaceVertexCriteriaAssignments*

  A sequence of tuples specifying the surface vertex criteria assignments. Each tuple contains two entries:

  - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to which the vertex criteria is assigned.
  - A Float or a SymbolicConstant specifying the vertex criteria value to be used for the surface. Possible values of the SymbolicConstant are ALL_VERTICES or NO_VERTICES.

- *slidingFormulationAssignments*

  A sequence of tuples specifying the sliding formulation assignments. Each tuple contains two entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the sliding formulation attribute is assigned.
  - A SymbolicConstant specifying the overriding the smoothness value to be used for the first surface. Possible values of the SymbolicConstant are NONE and SMALL_SLIDING.

- *useAllstar*

  A Boolean specifying whether the contacting surface pairs consist of all exterior faces in the model.

- *includedPairs*

  A sequence of pairs of [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects or SymbolicConstants that specifies the surface pairs in contact. Possible values of the SymbolicConstants are ALLSTAR and SELF. This argument is valid only when *useAllstar*=OFF.

- *excludedPairs*

  A sequence of pairs of [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects or SymbolicConstants that specifies the surface pairs excluded from contact. Possible values of the SymbolicConstants are ALLSTAR and SELF.

- *contactPropertyAssignments*

  A sequence of tuples specifying the properties assigned to each surface pair. Each tuple contains three entries:

  - A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object or the SymbolicConstant GLOBAL.
  - A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object or the SymbolicConstant SELF.
  - A String specifying an [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object associated with this pair of regions.

- *surfaceFeatureAssignments*

  A sequence of tuples specifying the surface feature angle assignments in the contact domain. Each tuple contains two entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the surface feature angle is assigned.
  - A Float or a SymbolicConstant specifying the overriding feature angle value to be used in the contact definition. Possible values of the SymbolicConstant are PERIMETER or NONE.

- *surfaceThicknessAssignments*

  A sequence of tuples specifying the surface thickness assignments in the contact domain. Each tuple contains three entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the surface thickness is assigned.
  - A Float or a SymbolicConstant specifying the overriding thickness value to be used in the contact definition. The SymbolicConstant ORIGINAL may be specified instead of a floating point value.
  - A Float specifying a scale factor that multiplies the thickness value specified in the second entry.

- *surfaceOffsetAssignments*

  A sequence of tuples specifying the surface offset fraction assignments in the contact domain. Each tuple contains two entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the surface offset fraction is assigned.
  - A Float or a SymbolicConstant specifying the offset fraction value to be used in the contact definition. Possible values of the SymbolicConstant are ORIGINAL, SPOS, or SNEG.

- *mainSecondaryAssignments*

  A sequence of tuples specifying main-secondary assignments in the contact domain. Each tuple contains three entries:

  - A region object or the SymbolicConstant GLOBAL specifying the first surface that defines the main-secondary assignment.
  - A region object specifying the second surface in the main-secondary assignment definition.
  - A SymbolicConstant specifying the status of the first surface. Possible values are MAIN, SECONDARY, and BALANCED.

- *initializationAssignments*

  A sequence of tuples specifying the contact initialization data assigned to each surface pair. Each tuple contains three entries:

  - A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object or the SymbolicConstant GLOBAL.
  - A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object or the SymbolicConstant SELF.
  - A String specifying a [StdStabilization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdstabilizationpyc.htm?ContextScope=all) object associated with this pair of regions.

- *stabilizationAssignments*

  A sequence of tuples specifying the contact stabilization assigned to each surface pair. Each tuple contains three entries:

  - A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object or the SymbolicConstant GLOBAL.
  - A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object or the SymbolicConstant SELF.
  - A String specifying a [StdStabilization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdstabilizationpyc.htm?ContextScope=all) object associated with this pair of regions.

- *smoothingAssignments*

  A sequence of tuples specifying the surface smoothing assignments in the contact domain. Each tuple contains two entries:

  - A region object specifying the surface to which the smoothing option is assigned.
  - A SymbolicConstant specifying the smoothing option to be used in the contact definition. Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, or TOROIDAL.

- *slidingTransitionAssignments*

  A sequence of tuples specifying sliding transition assignments in the contact domain. Each tuple contains three entries:

  - A region object or the SymbolicConstant GLOBAL specifying the first surface that defines the sliding transition assignment.
  - A region object specifying the second surface in the sliding transition assignment definition.
  - A SymbolicConstant specifying the smoothness value. Possible values are ELEMENT_ORDER_SMOOTHING, LINEAR_SMOOTHING, and QUADRATIC_SMOOTHING.

### Return value

A ContactStd object.

### Exceptions

None.



## Members

The ContactStd object can have the following members:

- *name*

  A String specifying the repository key.

- *globalSmoothing*

  A Boolean specifying whether surface smoothing (geometric correction) is automatically applied to all eligible surfaces. The default value is ON.

- *includedPairs*

  A [RegionPairs](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpairspyc.htm?ContextScope=all) object specifying the domain pairs included in contact.

- *excludedPairs*

  A [RegionPairs](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpairspyc.htm?ContextScope=all) object specifying the domain pairs excluded from contact.

- *contactPropertyAssignments*

  A [ContactPropertyAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertyassignmentpyc.htm?ContextScope=all) object specifying the contact property assignments in the contact domain.

- *surfaceThicknessAssignments*

  A [SurfaceThicknessAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacethicknessassignmentpyc.htm?ContextScope=all) object specifying the surface thickness assignments in the contact domain.

- *surfaceOffsetAssignments*

  A [SurfaceOffsetAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceoffsetassignmentpyc.htm?ContextScope=all) object specifying the surface offset fraction assignments in the contact domain.

- *mainSecondaryAssignments*

  A [MainSecondaryAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-masterslaveassignmentpyc.htm?ContextScope=all) object specifying the main-secondary assignments in the contact domain.

- *initializationAssignments*

  An [InitializationAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-initializationassignmentpyc.htm?ContextScope=all) object specifying the contact initialization assignments in the contact domain.

- *stabilizationAssignments*

  A [StabilizationAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stabilizationassignmentpyc.htm?ContextScope=all) object specifying the contact stabilization assignments in the contact domain.

- *smoothingAssignments*

  A [SmoothingAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothingassignmentpyc.htm?ContextScope=all) object specifying the surface smoothing assignments in the contact domain.

- *surfaceFeatureAssignments*

  A [SurfaceFeatureAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacefeatureassignmentpyc.htm?ContextScope=all) object specifying the surface feature angle assignments in the contact domain.

- *slidingTransitionAssignments*

  A [SlidingTransitionAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-slidingtransitionassignmentpyc.htm?ContextScope=all) object specifying the sliding transition assignments in the contact domain.

- *assignEdgeToEdgeformulation*

  A Boolean specifying whether to assign the edge-to-edge formulation. The default value is False.

- *edgeToEdgeFormulation*

  A symbolic constant specifying edge-to-edge formulation. The default value is NO.



## Corresponding analysis keywords

- [CONTACT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contact.htm?ContextScope=all#simakey-r-contact)