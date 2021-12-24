# SlidingFormulationAssignment object

The SlidingFormulationAssignment object stores the sliding formulation assignment definition for surfaces in [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects. The SlidingFormulationAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].slidingFormulationAssignments
```

## changeValuesInStep(...)



This method allows you to modify sliding formulation assignments already defined on surface pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the sliding formulation assignments are to be modified.

- *index*

  An Int specifying the position of the sliding formulation assignment whose value is to be modified.

- *value*

  A SymbolicConstant specifying the value of the smoothness of the surface-to-surface formulation on sliding to be assigned to the surface whose index is referenced. Possible values are NONE and SMALL_SLIDING.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows you to add sliding formulation assignments to new surface pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the sliding formulation assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the sliding formulation assignments. Each tuple contains two entries:A region object or the SymbolicConstant GLOBAL specifying the surface to which the sliding formulation attribute is assigned.A SymbolicConstant specifying the overriding the smoothness value to be used for the first surface. Possible values of the SymbolicConstant are NONE and SMALL_SLIDING.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing sliding formulation assignments.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each sliding formulation assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The SlidingFormulationAssignment object has no members.



## Corresponding analysis keywords

- [CONTACT FORMULATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactformulation.htm?ContextScope=all#simakey-r-contactformulation), TYPE=SLIDING FORMULATION