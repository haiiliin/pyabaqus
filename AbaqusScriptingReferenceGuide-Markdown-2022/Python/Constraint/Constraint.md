# Constraint object

The Constraint object is the abstract base type for other Constraint objects. The Constraint object has no explicit constructor. The members of the Constraint object are common to all objects derived from the Constraint.

## Access

```
import interaction
mdb.models[name].constraints[name]
```

## resume()



This method resumes the constraint that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the constraint.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



This method allows you to delete existing constraints.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each constraint to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Constraint object has the following members:

- *name*

  A String specifying the constraint repository key.

- *suppressed*

  A Boolean specifying whether the constraint is suppressed or not. The default value is OFF.