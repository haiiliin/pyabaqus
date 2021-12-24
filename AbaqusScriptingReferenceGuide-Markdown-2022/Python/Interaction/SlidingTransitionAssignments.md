# SlidingTransitionAssignments object

The SlidingTransitionAssignment object stores the sliding transition assignment definition for surfaces in [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects. The SlidingTransitionAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].slidingTransitionAssignments
```

## changeValuesInStep(...)



This method allows you to modify sliding transition assignments already defined on surface pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the sliding transition assignments are to be modified.

- *index*

  An Int specifying the position of the sliding transition assignment whose value is to be modified.

- *value*

  A SymbolicConstant specifying the value of the smoothness of the surface-to-surface formulation on sliding to be assigned to the surface whose index is referenced. Possible values are ELEMENT_ORDER_SMOOTHING, LINEAR_SMOOTHING, and QUADRATIC_SMOOTHING.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows you to add sliding transition assignments to new surface pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the sliding transition assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the sliding transition assignments. Each tuple contains two entries:A region object or the SymbolicConstant GLOBAL specifying the surface to which the sliding transition attribute is assigned.A SymbolicConstant specifying the overriding the smoothness value to be used for the first surface. Possible values of the SymbolicConstant are ELEMENT_ORDER_SMOOTHING, LINEAR_SMOOTHING, and QUADRATIC_SMOOTHING.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing sliding transition assignments.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each sliding transition assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The SlidingTransitionAssignment object has no members.



## Corresponding analysis keywords

- [CONTACT FORMULATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactformulation.htm?ContextScope=all#simakey-r-contactformulation), TYPE=SLIDING TRANSITION