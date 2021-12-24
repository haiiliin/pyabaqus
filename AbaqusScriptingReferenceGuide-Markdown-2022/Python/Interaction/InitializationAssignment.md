# InitializationAssignment object

The InitializationAssignment object stores the contact initialization assignment definition for domain pairs in a [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) or [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all#simaker-c-contactexppyc) object. The InitializationAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].initializationAssignments
```

## changeValuesInStep(...)



This method allows modification of contact initialization assignments to domain pairs already defined in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the contact initialization assignments are to be modified.

- *index*

  An Int specifying the position of the contact initialization assignment whose value is to be modified.

- *value*

  A String specifying the value of the contact initialization to be assigned to the domain pair whose index is referenced.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows addition of contact initialization assignments to new domain pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which new contact initialization assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the initializations assigned to each surface pair. Each tuple contains four entries (fourth entry is for Abaqus/Explicit and is optional):

  - A region object or the SymbolicConstant GLOBAL (for Abaqus/Standard only).
  - A region object or the SymbolicConstant SELF (for Abaqus/Standard only).
  - A String specifying a [StdInitialization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stdinitializationpyc.htm?ContextScope=all) or [ExpInitialization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expinitializationpyc.htm?ContextScope=all)object associated with this pair of regions.
  - A String specifying a secondary surface type. This entry is applicable only if the [ExpInitialization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expinitializationpyc.htm?ContextScope=all) object is defined with *overclosureType*=CLEARANCE and *adjustNodalCoords*=True.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing contact initialization assignments from a [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) or [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all#simaker-c-contactexppyc) object.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each contact initialization assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The InitializationAssignment object has no members.



## Corresponding analysis keywords

- [CONTACT INITIALIZATION ASSIGNMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactinitializationassignment.htm?ContextScope=all#simakey-r-contactinitializationassignment)