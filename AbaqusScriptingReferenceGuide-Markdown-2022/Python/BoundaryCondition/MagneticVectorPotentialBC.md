# MagneticVectorPotentialBC object

The MagneticVectorPotentialBC object stores the data for a magnetic vector potential boundary condition.

The MagneticVectorPotentialBC object is derived from the [BoundaryCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].boundaryConditions[name]
```

## MagneticVectorPotentialBC(...)



This method creates a MagneticVectorPotentialBC object.



### Path

```
mdb.models[name].MagneticVectorPotentialBC
```

### Required arguments

- *name*

  A String specifying the boundary condition repository key.

- *createStepName*

  A String specifying the name of the step in which the boundary condition is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

### Optional arguments

- *component1*

  A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET

- *component2*

  A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *component3*

  A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *distributionType*

  A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the boundary condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.

### Return value

A MagneticVectorPotentialBC object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing MagneticVectorPotentialBC object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MagneticVectorPotentialBC ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-magneticvectorpotentialbcpyc.htm?ContextScope=all#simaker-magneticvectorpotentialbcmagneticvectorpotentialbcpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing MagneticVectorPotentialBC object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the boundary condition is modified.

### Optional arguments

- *component1*

  A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 1-direction. Possible values for the SymbolicConstant are SET and UNCHANGED.

- *component2*

  A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 2-direction. Possible values for the SymbolicConstant are SET and UNCHANGED.

- *component3*

  A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 3-direction. Possible values for the SymbolicConstant areSET and UNCHANGED.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the boundary condition is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The MagneticVectorPotentialBC object can have the following members:

- *name*

  A String specifying the boundary condition repository key.

- *distributionType*

  A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.

- *category*

  A SymbolicConstant specifying the category of the boundary condition. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the boundary condition is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the boundary condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.