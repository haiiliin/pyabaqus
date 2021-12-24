# SmoothingAssignment object

The SmoothingAssignment object stores the surface smoothing assignment definition for surfaces in [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) and [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects. The SmoothingAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].smoothingAssignments
```

## changeValuesInStep(...)



This method allows modification of surface smoothing assignments already defined on surfaces in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the surface smoothing assignments are to be modified.

- *index*

  An Int specifying the position of the surface smoothing assignment whose value is to be modified.

- *value*

  A tuple specifying the value of the surface smoothing assignments for the surface whose index is referenced. Each tuple contains one entry:A SymbolicConstant specifying the surface smoothing value to be used for the surface. Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, and TOROIDAL.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows addition of surface smoothing assignments to new surfaces in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which new surface smoothing assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the surface smoothing assignments. Each tuple contains two entries:

  - A region object specifying the surface to which the smoothing is assigned.
  - A SymbolicConstant specifying the surface smoothing value to be used for the surface. Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, and TOROIDAL.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing surface smoothing assignments from [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) and [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each surface smoothing assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The SmoothingAssignment object has no members.



## Corresponding analysis keywords

- [SURFACE PROPERTY ASSIGNMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-surfacepropertyassignment.htm?ContextScope=all#simakey-r-surfacepropertyassignment), PROPERTY=GEOMETRIC CORRECTION