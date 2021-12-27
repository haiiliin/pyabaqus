# ContactExp object

The ContactExp object defines the contact domain and associated properties during contact in an Abaqus/Explicit analysis.

The ContactExp object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## ContactExp(...)



This method creates a ContactExp object.



### Path

```
mdb.models[name].ContactExp
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which this contact interaction is created.

### Optional arguments

- *useAllstar*

  A Boolean specifying whether the contacting surface pair consists of all exterior faces, shell edges, beam segments, analytical rigid surfaces, and, when applicable, Eulerian material surfaces.

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

- *smoothingAssignments*

  A [SmoothingAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothingassignmentpyc.htm?ContextScope=all) object specifying the surface smoothing assignments in the contact domain.

- *surfaceCrushTriggerAssignments*

  A [SurfaceCrushTriggerAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecrushtriggerassignmentpyc.htm?ContextScope=all) object specifying the surface crush trigger assignments in the contact domain.

- *surfaceFrictionAssignments*

  A [SurfaceFrictionAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacefrictionassignmentpyc.htm?ContextScope=all) object specifying the surface friction assignments in the contact domain.

- *mainSecondaryAssignments*

  A [MainSecondaryAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-masterslaveassignmentpyc.htm?ContextScope=all) object specifying the main-secondary assignments in the contact domain.

- *polarityAssignments*

  A [PolarityAssignments](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-polarityassignmentpyc.htm?ContextScope=all) object specifying the polarity assignments in the contact domain.

### Return value

A ContactExp object.

### Exceptions

None.

## ContactExp(...)



This method creates a ContactExp object.



### Path

```
mdb.models[name].ContactExp
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which this contact interaction is created.

### Optional arguments

- *globalSmoothing*

  A Boolean specifying whether surface smoothing (geometric correction) is automatically applied to all eligible surfaces. The default value is ON.

- *surfaceCrushTriggerAssignments*

  A sequence of tuples specifying the surface crush trigger assignments. Each tuple contains four entries:

  - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to which the feature angle is assigned.
  - A SymbolicConstant specifying the trigger option to be used for the surface. Possible values of the SymbolicConstant are TRIGGER, NO_TRIGGER, or NO_CRUSH.
  - A Float specifying the crush stress value to be used for the surface.
  - A Float specifying the crush initiation angle value to be used for the surface.
  - A Float specifying the crush continuation angle value to be used for the surface.

- *surfaceFrictionAssignments*

  A sequence of tuples specifying the surface friction assignments. Each tuple contains two entries:

  - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to which the friction coefficient is assigned.
  - A Float specifying the overriding friction coefficient to be used in the contact definition.

- *useAllstar*

  A Boolean specifying whether the contacting surface pair consists of all exterior faces, shell edges, beam segments, analytical rigid surfaces, and, when applicable, Eulerian material surfaces.

- *includedPairs*

  A sequence of pairs of [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects or SymbolicConstants that specifies the surface pairs in contact. Possible values of the SymbolicConstants are ALLSTAR and SELF. This argument is valid only when *useAllstar*=OFF.

- *excludedPairs*

  A sequence of pairs of [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects or SymbolicConstants that specify the surface pairs excluded from contact. Possible values of the SymbolicConstants are ALLSTAR and SELF.

- *contactPropertyAssignments*

  A sequence of tuples specifying the properties assigned to each surface pair. Each tuple contains three entries:

  - A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object or the SymbolicConstant GLOBAL.
  - A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object or the SymbolicConstant SELF.
  - A String specifying an [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object associated with this pair of regions.

- *surfaceThicknessAssignments*

  A sequence of tuples specifying the surface thickness assignments in the contact domain. Each tuple contains three entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the surface thickness is assigned.
  - A Float or a SymbolicConstant specifying the overriding thickness value to be used in the contact definition. Possible values of the SymbolicConstant are ORIGINAL or THINNING.
  - A Float specifying a scale factor that multiplies the thickness value specified in the second entry.

- *surfaceOffsetAssignments*

  A sequence of tuples specifying the surface offset fraction assignments in the contact domain. Each tuple contains two entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the surface offset fraction is assigned.
  - A Float or a SymbolicConstant specifying the offset fraction value to be used in the contact definition. Possible values of the SymbolicConstant are ORIGINAL, SPOS, or SNEG.

- *surfaceFeatureAssignments*

  A sequence of tuples specifying the surface feature angle assignments in the contact domain. Each tuple contains two entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the surface feature angle is assigned.
  - A Float or a SymbolicConstant specifying the overriding feature angle value to be used in the contact definition. Possible values of the SymbolicConstant are PERIMETER, ALL, PICKED, or NONE.

- *smoothingAssignments*

  A sequence of tuples specifying the surface smoothing assignments in the contact domain. Each tuple contains two entries:

  - A region object specifying the surface to which the smoothing option is assigned.
  - A SymbolicConstant specifying the smoothing option to be used in the contact definition. Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, or TOROIDAL.

- *mainSecondaryAssignments*

  A sequence of tuples specifying pure main-secondary assignments in the contact domain. Each tuple contains three entries:

  - A region object or the SymbolicConstant GLOBAL specifying the first surface that defines the main-secondary assignment.
  - A region object specifying the second surface in the main-secondary assignment definition.
  - A SymbolicConstant specifying the status of the first surface. Possible values are MAIN and SECONDARY.

- *polarityAssignments*

  A sequence of tuples specifying polarity assignments in the contact domain. Each tuple contains three entries:

  - A region object or the SymbolicConstant GLOBAL specifying the first surface that defines the polarity assignment.
  - A region object specifying the second surface in the polarity assignment definition.
  - A SymbolicConstant specifying the polarity of the second surface. Possible values are SPOS, SNEG, and TWO_SIDED.

### Return value

A ContactExp object.

### Exceptions

None.



## Members

The ContactExp object can have the following members:

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

- *surfaceFeatureAssignments*

  A [SurfaceFeatureAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacefeatureassignmentpyc.htm?ContextScope=all) object specifying the surface feature angle assignments in the contact domain.

- *smoothingAssignments*

  A [SmoothingAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothingassignmentpyc.htm?ContextScope=all) object specifying the surface smoothing assignments in the contact domain.

- *mainSecondaryAssignments*

  A [MainSecondaryAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-masterslaveassignmentpyc.htm?ContextScope=all) object specifying the main-secondary assignments in the contact domain.

- *polarityAssignments*

  A [PolarityAssignments](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-polarityassignmentpyc.htm?ContextScope=all) object specifying the polarity assignments in the contact domain.



## Corresponding analysis keywords

- [CONTACT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contact.htm?ContextScope=all#simakey-r-contact)