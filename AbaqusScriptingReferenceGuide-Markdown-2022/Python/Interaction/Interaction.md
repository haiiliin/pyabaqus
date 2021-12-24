# Interaction object

The Interaction object is the abstract base type for other Interaction objects. The Interaction object has no explicit constructor. Each of the Interaction objects has the following methods:

- deactivate
- move
- reset
- resume
- suppress
- delete

The methods are described below.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## deactivate(...)



This method deactivates the interaction in the specified step and all its subsequent steps.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is deactivated.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## move(...)



This method moves an interaction from one step to another.



### Required arguments

- *fromStepName*

  A String specifying the name of the step from which to move the interaction.

- *toStepName*

  A String specifying the name of the step to which to move the interaction.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## reset(...)



This method reactivates an interaction that was deactivated previously. The reset method is available during the step in which the interaction was deactivated originally.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is reactivated.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## resume()



This method resumes an interaction that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses an interaction.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



This method allows you to delete existing interactions.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each interaction to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Interaction object has the following member:

- *name*

  A String specifying the repository key.