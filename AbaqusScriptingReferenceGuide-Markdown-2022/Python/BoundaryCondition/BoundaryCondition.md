# BoundaryCondition object

The BoundaryCondition object is the abstract base type for other BoundaryCondition objects. The BoundaryCondition object has no explicit constructor. The methods and members of the BoundaryCondition object are common to all objects derived from the BoundaryCondition.

## Access

```
import load
mdb.models[name].boundaryConditions[name]
```

## deactivate(...)



This method deactivates the boundary condition in the specified step and all subsequent steps.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the boundary condition is deactivated.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## move(...)



This method moves the boundary condition state from one step to a different step.



### Required arguments

- *fromStepName*

  A String specifying the name of the step from which the boundary condition state is moved.

- *toStepName*

  A String specifying the name of the step to which the boundary condition state is moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## reset(...)



This method resets the boundary condition state of the specified step to the state of the previous analysis step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the boundary condition state is reset.

### Optional arguments

None.

### Return value

None.

### Exceptions

TextError.



## resume()



This method resumes the boundary condition that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the boundary condition.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## delete(...)



This method allows you to delete existing boundary conditions.



### Required arguments

- *indices*

  A sequence of Ints specifying the index of each boundary condition to delete.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The BoundaryCondition object can have the following members:

- *name*

  A String specifying the boundary condition repository key.

- *category*

  A SymbolicConstant specifying the category of the boundary condition. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the boundary condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.