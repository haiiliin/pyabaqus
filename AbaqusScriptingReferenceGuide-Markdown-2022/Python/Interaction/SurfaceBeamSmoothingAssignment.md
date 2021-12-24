# SurfaceBeamSmoothingAssignment object

The SurfaceBeamSmoothingAssignment object stores the surface beam smoothing assignment definition for surfaces in [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects. The SurfaceBeamSmoothingAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].surfaceBeamSmoothingAssignments
```

## changeValuesInStep(...)



This method allows modification of surface beam smoothing assignments already defined on surfaces in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the surface beam smoothing assignments are to be modified.

- *index*

  An Int specifying the position of the surface beam smoothing assignment whose value is to be modified.

- *value*

  A tuple specifying the value of the surface beam smoothing assignments for the surface whose index is referenced. Each tuple contains one entry:A Float specifying the surface beam smoothing value to be used for the surface.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows addition of surface beam smoothing assignments to new surfaces in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which new surface beam smoothing assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the surface beam smoothing assignments. Each tuple contains two entries:A region object specifying the surface to which the smoothing is assigned.A Float specifying the surface smoothing value to be used for the surface.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing surface beam smoothing assignments from [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each surface beam smoothing assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The SurfaceBeamSmoothingAssignment object has no members.



## Corresponding analysis keywords

- [SURFACE PROPERTY ASSIGNMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-surfacepropertyassignment.htm?ContextScope=all#simakey-r-surfacepropertyassignment), PROPERTY=BEAM SMOOTHING