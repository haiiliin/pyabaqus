# ShellSolidCoupling object

The ShellSolidCoupling object defines two surfaces to be tied together for the duration of a simulation.

The ShellSolidCoupling object is derived from the [Constraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].constraints[name]
```

## ShellSolidCoupling(...)



This method creates a ShellSolidCoupling object.



### Path

```
mdb.models[name].ShellSolidCoupling
```

### Required arguments

- *name*

  A String specifying the constraint repository key.

- *shellEdge*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the name of the shell edge surface.

- *solidFace*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the name of the solid surface.

### Optional arguments

- *positionToleranceMethod*

  A SymbolicConstant specifying the method used to determine the position tolerance. Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.

- *positionTolerance*

  A Float specifying the position tolerance. The default value is 0.0.The *positionTolerance* argument applies only when *positionToleranceMethod*=SPECIFIED.Note:Abaqus will not constrain nodes on the solid face region outside the position tolerance.

- *influenceDistanceMethod*

  A SymbolicConstant specifying the method used to determine the influence distance. Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.

- *influenceDistance*

  A Float specifying the influence distance. The *influenceDistance* argument applies only when *influenceDistanceMethod*=SPECIFIED. The default value is 0.0.

### Return value

A ShellSolidCoupling object.

### Exceptions

None.



## setValues(...)



This method modifies the ShellSolidCoupling object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ShellSolidCoupling ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shellsolidcouplingpyc.htm?ContextScope=all#simaker-shellsolidcouplingshellsolidcouplingpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The ShellSolidCoupling object has members with the same names and descriptions as the arguments to the [ShellSolidCoupling ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shellsolidcouplingpyc.htm?ContextScope=all#simaker-shellsolidcouplingshellsolidcouplingpyc)method.

In addition, the ShellSolidCoupling object has the following member:

- *suppressed*

  A Boolean specifying whether the constraint is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [SHELL TO SOLID COUPLING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shelltosolidcoupling.htm?ContextScope=all#simakey-r-shelltosolidcoupling)