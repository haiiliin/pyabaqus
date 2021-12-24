# SurfaceFrictionAssignment object

The SurfaceFrictionAssignment object stores the surface friction assignment definition for surfaces in [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) objects. The SurfaceFrictionAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].surfaceFrictionAssignments
```

## changeValuesInStep(...)



This method allows modification of surface friction assignments already defined on surfaces in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the surface friction assignments are to be modified.

- *index*

  An Int specifying the position of the surface friction assignment whose value is to be modified.

- *value*

  A tuple specifying the value of the surface friction assignments for the surface whose index is referenced. Each tuple contains:

  - A Float specifying the overriding friction coefficient value to be used in the contact definition.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows addition of surface friction assignments to new surfaces in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which new surface friction assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the surface friction assignments. Each tuple contains two entries:

  - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to which the friction coefficient is assigned.
  - A Float specifying the overriding friction coefficient to be used in the contact definition.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing surface friction assignments.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each surface friction assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The SurfaceFrictionAssignment object has no members.



## Corresponding analysis keywords

- [SURFACE PROPERTY ASSIGNMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-surfacepropertyassignment.htm?ContextScope=all#simakey-r-surfacepropertyassignment), PROPERTY=FRICTION