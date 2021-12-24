# PolarityAssignments object

The PolarityAssignments object stores the polarity assignment definition for surfaces in [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) objects. The PolarityAssignments object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].polarityAssignments
```

## changeValuesInStep(...)



This method allows you to modify polarity assignments already defined on surface pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the main-secondary assignments are to be modified.

- *index*

  An Int specifying the position of the polarity assignment whose value is to be modified.

- *value*

  A SymbolicConstant specifying the value of the polarity to be assigned to the surface whose index is referenced. Possible values are SPOS, SNEG, and TWO_SIDED.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows you to add polarity assignments to new surface pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the polarity assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the polarity assignments. Each tuple contains two entries:

  - A region object or the SymbolicConstant GLOBAL specifying the surface to which the polarity attribute is assigned.
  - A SymbolicConstant specifying the overriding polarity value to be used for the first surface. Possible values of the SymbolicConstant are SPOS, SNEG, and TWO_SIDED.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing polarity assignments.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each polarity assignment to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The PolarityAssignments object has no members.



## Corresponding analysis keywords

- [CONTACT FORMULATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactformulation.htm?ContextScope=all#simakey-r-contactformulation), TYPE=POLARITY