# DisplacementAdaptiveMeshConstraint object

The AdaptivityProcess object defines a series of jobs that will be submitted for analysis. Abaqus performs adaptive remeshing between each job.

## Access

```
import step
mdb.models[name].adaptiveMeshConstraints[name]
```

## DisplacementAdaptiveMeshConstraint(...)



This method creates a DisplacementAdaptiveMeshConstraint object.



### Path

```
mdb.models[name].DisplacementAdaptiveMeshConstraint
```

### Required arguments

- *name*

  A String specifying the adaptive mesh constraint repository key.

- *createStepName*

  A String specifying the name of the step in which the adaptive mesh constraint is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the adaptive mesh constraint is applied.

### Optional arguments

- *u1*

  A Float or a SymbolicConstant specifying the displacement component in the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.Note:Although *u1*, *u2*, *u3*, *ur1*, *ur2*, and *ur3* are optional arguments, at least one of them must be specified.

- *u2*

  A Float or a SymbolicConstant specifying the displacement component in the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *u3*

  A Float or a SymbolicConstant specifying the displacement component in the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *ur1*

  A Float or a SymbolicConstant specifying the rotational displacement component about the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *ur2*

  A Float or a SymbolicConstant specifying the rotational displacement component about the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *ur3*

  A Float or a SymbolicConstant specifying the rotational displacement component about the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

- *amplitude*

  A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the adaptive mesh constraint has no amplitude reference. The default value is UNSET. You should provide the *amplitude* argument only if it is valid for the specified step.

- *motionType*

  A SymbolicConstant specifying the mesh motion in relation to the underlying material. Possible values are INDEPENDENT, FOLLOW and USER_DEFINED. The default value is INDEPENDENT.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the adaptive mesh constraint's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.

### Return value

A DisplacementAdaptiveMeshConstraint object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing DisplacementAdaptiveMeshConstraint object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DisplacementAdaptiveMeshConstraint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementadaptivemeshconstraintpyc.htm?ContextScope=all#simaker-displacementadaptivemeshconstraintdisplacementadaptpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing DisplacementAdaptiveMeshConstraint object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the adaptive mesh constraint is modified.

### Optional arguments

- *u1*

  A Float or a SymbolicConstant specifying the displacement component in the 1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *u2*

  A Float or a SymbolicConstant specifying the displacement component in the 2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *u3*

  A Float or a SymbolicConstant specifying the displacement component in the 3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *ur1*

  A Float or a SymbolicConstant specifying the rotational displacement component about the 1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *ur2*

  A Float or a SymbolicConstant specifying the rotational displacement component about the 2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *ur3*

  A Float or a SymbolicConstant specifying the rotational displacement component about the 3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

- *amplitude*

  A String or a SymbolicConstant specifying the name of the amplitude reference. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the amplitude is propagated from the previous analysis step. FREED should be used if the adaptive mesh constraint is changed to have no amplitude reference. You should provide the *amplitude* argument only if it is valid for the specified step.

### Return value

None.

### Exceptions

None.



## Members

The DisplacementAdaptiveMeshConstraint object can have the following members:

- *name*

  A String specifying the adaptive mesh constraint repository key.

- *category*

  A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible values are MECHANICAL and THERMAL.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the adaptive mesh constraint is applied.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the adaptive mesh constraint's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.