# ContactPropertyAssignment object

The ContactPropertyAssignment object stores the contact property assignment definition for domain pairs in [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) and [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects. The ContactPropertyAssignment object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].contactPropertyAssignments
```

## changeValuesInStep(...)



This method allows modification of contact property assignments to domain pairs already defined in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the contact property assignments are to be modified.

- *index*

  An Int specifying the position of the contact property assignment whose value is to be modified.

- *value*

  A String specifying the value of the contact property to be assigned to the domain pair whose index is referenced.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## appendInStep(...)



This method allows addition of contact property assignments to new domain pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which new contact property assignments are to be defined.

- *assignments*

  A sequence of tuples specifying the properties assigned to each surface pair. Each tuple contains three entries:A region or a material object or the SymbolicConstant GLOBAL.A region or a material object or the SymbolicConstant SELF. When used with a [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) object, this parameter can also be a string that references an Eulerian material surface.A String specifying a [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object associated with this pair of regions.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



The delete method allows you to delete existing contact property assignments.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each contact property assignment to delete. The *indices* and *surfPair* arguments are mutually exclusive.

- *surfPair*

  A sequence of tuples specifying the surface pair of each contact property assignment to delete. Each tuple contains two entries:A region or a material object or the SymbolicConstant GLOBAL.A region or a material object or the SymbolicConstant SELF. When used with a [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) object, this parameter can also be a string that references an Eulerian material surface.*surfPair* and *indices* arguments are mutually exclusive.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The ContactPropertyAssignment object has no members.



## Corresponding analysis keywords

- [CONTACT PROPERTY ASSIGNMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactpropertyassignment.htm?ContextScope=all#simakey-r-contactpropertyassignment)