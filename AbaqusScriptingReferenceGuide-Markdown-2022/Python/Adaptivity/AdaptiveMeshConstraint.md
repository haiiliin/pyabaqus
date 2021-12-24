# AdaptiveMeshConstraint object

The AdaptiveMeshConstraint object is the abstract base type for other Arbitrary Lagrangian Eularian (ALE) style AdaptiveMeshConstraint objects. The AdaptiveMeshConstraint object has no explicit constructor. The methods and members of the AdaptiveMeshConstraint object are common to all objects derived from the AdaptiveMeshConstraint object.

## Access

```
import step
mdb.models[name].adaptiveMeshConstraints[name]
```

## deactivate(...)



This method deactivates the adaptive mesh constraint in the specified step and all subsequent steps.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the adaptive mesh constraint is deactivated.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## move(...)



This method moves the adaptive mesh constraint state from one step to a different step.



### Required arguments

- *fromStepName*

  A String specifying the name of the step from which the adaptive mesh constraint state is moved.

- *toStepName*

  A String specifying the name of the step to which the adaptive mesh constraint state is moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## reset(...)



This method resets the adaptive mesh constraint state of the specified step to the state of the previous analysis step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the adaptive mesh constraint state is reset.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## resume()



This method resumes the adaptive mesh constraint that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the adaptive mesh constraint.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



This method allows you to delete existing adaptive mesh constraints.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each adaptive mesh constraint to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The AdaptiveMeshConstraint object can have the following members:

- *name*

  A String specifying the adaptive mesh constraint repository key.

- *category*

  A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the adaptive mesh constraint is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the adaptive mesh constraint's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.