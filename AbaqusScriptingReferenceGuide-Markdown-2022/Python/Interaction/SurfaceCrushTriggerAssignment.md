# SurfaceCrushTriggerAssignment object

The SurfaceCrushTriggerAssignment object stores the surface crush trigger assignment definition for surfaces in [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) objects. The SurfaceCrushTriggerAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].surfaceCrushTriggerAssignments
```

## changeValuesInStep(...)



This method allows modification of surface crush trigger assignments already defined on surfaces in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the surface crush trigger assignments are to be modified.

- *index*

  An Int specifying the position of the surface crush trigger assignment whose value is to be modified.

- *value*

  A tuple specifying the value of the surface crush trigger assignments for the surface whose index is referenced. Each tuple contains three entries:

  - A SymbolicConstant specifying the trigger option to be used for the surface. Possible values of the SymbolicConstant are TRIGGER, NO_TRIGGER, or NO_CRUSH.
  - A Float specifying the crush stress value to be used for the surface.
  - A Float specifying the crush initiation angle value to be used for the surface.
  - A Float specifying the crush continuation angle value to be used for the surface.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows addition of surface crush trigger assignments to new surfaces in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which new surface crush trigger assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the surface crush trigger assignments. Each tuple contains four entries:

  - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to which the feature angle is assigned.
  - A SymbolicConstant specifying the trigger option to be used for the surface. Possible values of the SymbolicConstant are TRIGGER, NO_TRIGGER, or NO_CRUSH.
  - A Float specifying the crush stress value to be used for the surface.
  - A Float specifying the crush initiation angle value to be used for the surface.
  - A Float specifying the crush continuation angle value to be used for the surface.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing surface crush trigger assignments from a [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) object.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each surface crush trigger assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The SurfaceCrushTriggerAssignment object has no members.



## Corresponding analysis keywords

- [SURFACE PROPERTY ASSIGNMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-surfacepropertyassignment.htm?ContextScope=all#simakey-r-surfacepropertyassignment), PROPERTY=CRUSH TRIGGER