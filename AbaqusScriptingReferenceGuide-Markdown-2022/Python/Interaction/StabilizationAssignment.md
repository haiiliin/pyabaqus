# StabilizationAssignment object

The StabilizationAssignment object stores the contact stabilization assignment definition for domain pairs in a [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) object. The StabilizationAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].stabilizationAssignments
```

## changeValuesInStep(...)



This method allows modification of contact stabilization assignments to domain pairs already defined in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the contact stabilization assignments are to be modified.

- *index*

  An Int specifying the position of the contact stabilization assignment whose value is to be modified.

- *value*

  A String specifying the value of the contact stabilization to be assigned to the domain pair whose index is referenced.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows addition of contact stabilization assignments to new domain pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which new contact stabilization assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the stabilizations assigned to each surface pair. Each tuple contains three entries:

  - A region object or the SymbolicConstant GLOBAL.
  - A region object or the SymbolicConstant SELF.
  - A String specifying a [StdStabilization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdstabilizationpyc.htm?ContextScope=all) object associated with this pair of regions.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing contact stabilization assignments from a [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) object.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each contact stabilization assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The StabilizationAssignment object has no members.



## Corresponding analysis keywords

- [CONTACT STABILIZATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactstabilization.htm?ContextScope=all#simakey-r-contactstabilization)