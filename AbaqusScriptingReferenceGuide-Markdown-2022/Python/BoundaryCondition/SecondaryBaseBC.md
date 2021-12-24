# SecondaryBaseBC object

The SecondaryBaseBC object stores the data for a secondary base boundary condition.

The SecondaryBaseBC object is derived from the [BoundaryCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].boundaryConditions[name]
```

## SecondaryBaseBC(...)



This method creates a SecondaryBaseBC object.



### Path

```
mdb.models[name].SecondaryBaseBC
```

### Required arguments

- *name*

  A String specifying the boundary condition repository key.

- *createStepName*

  A String specifying the name of the step in which the boundary condition is created.

- *regions*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied. Note that the usual *region* is ignored. The default value is MODEL.

- *dofs*

  A sequence of sequences of Ints specifying the constrained degrees-of-freedom.

### Optional arguments

None.

### Return value

A SecondaryBaseBC object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing SecondaryBaseBC object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SecondaryBaseBC ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-secondarybasebcpyc.htm?ContextScope=all#simaker-secondarybasebcsecondarybasebcpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing SecondaryBaseBC object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the boundary condition is modified.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The SecondaryBaseBC object can have the following members:

- *name*

  A String specifying the boundary condition repository key.

- *dofs*

  A tuple of tuples of Ints specifying the constrained degrees-of-freedom.

- *regions*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied. Note that the usual *region* is ignored. The default value is MODEL.

- *category*

  A SymbolicConstant specifying the category of the boundary condition. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the boundary condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.