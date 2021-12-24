# MainSecondaryAssignment object

The MainSecondaryAssignment object stores the main-secondary assignment definition for surfaces in [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) and [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects. The MainSecondaryAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].mainSecondaryAssignments
```

## changeValuesInStep(...)



This method allows modification of main-secondary assignments already defined on surface pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the main-secondary assignments are to be modified.

- *index*

  An Int specifying the position of the main-secondary assignment whose value is to be modified.

- *value*

  A SymbolicConstant specifying the value of the main-secondary role to be assigned to the surface whose index is referenced. Possible values are MAIN, SECONDARY, and BALANCED. The SymbolicConstant BALANCED can be specified only in an Abaqus/Standard analysis.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows addition of main-secondary assignments to new surface pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the main-secondary assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the main-secondary assignments. Each tuple contains two entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the main-secondary attribute is assigned.
  - A SymbolicConstant specifying the overriding main-secondary value to be used for the first surface. Possible values of the SymbolicConstant are MAIN, SECONDARY, and BALANCED. The SymbolicConstant BALANCED can be specified only in an Abaqus/Standard analysis.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing main-secondary assignments.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each main-secondary assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The MainSecondaryAssignment object has no members.



## Corresponding analysis keywords

- [CONTACT FORMULATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactformulation.htm?ContextScope=all#simakey-r-contactformulation), TYPE=PURE MAIN-SECONDARY
- [CONTACT FORMULATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactformulation.htm?ContextScope=all#simakey-r-contactformulation), TYPE=MAIN SECONDARY ROLES