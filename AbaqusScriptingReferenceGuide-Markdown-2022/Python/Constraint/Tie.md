# Tie object

The Tie object defines two surfaces to be tied together for the duration of a simulation.

The Tie object is derived from the [Constraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].constraints[name]
```

## Tie(...)



This method creates a Tie object.



### Path

```
mdb.models[name].Tie
```

### Required arguments

- *name*

  A String specifying the constraint repository key.

- *main*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the name of the main surface.

- *secondary*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the name of the secondary surface.

### Optional arguments

- *adjust*

  A Boolean specifying whether initial positions of tied secondary nodes are adjusted to lie on the main surface. The default value is ON.

- *positionToleranceMethod*

  A SymbolicConstant specifying the method used to determine the position tolerance. Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.

- *positionTolerance*

  A Float specifying the position tolerance. The *positionTolerance* argument applies only when *positionToleranceMethod*=SPECIFIED. The default value is 0.0.

- *tieRotations*

  A Boolean specifying whether rotation degrees of freedom should be tied. The default value is ON.

- *constraintRatioMethod*

  A SymbolicConstant specifying the method used to determine the constraint ratio. Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.

- *constraintRatio*

  A Float specifying the fractional distance between the main reference surface and the secondary node at which the translational constraint should act. The *constraintRatio* argument applies only when *constraintRatioMethod*=SPECIFIED. The default value is 0.0.

- *constraintEnforcement*

  A SymbolicConstant specifying the discretization method. Possible values are SOLVER_DEFAULT, NODE_TO_SURFACE, and SURFACE_TO_SURFACE. The default value is SOLVER_DEFAULT.

- *thickness*

  A Boolean specifying whether shell element thickness is considered. The default value is ON.

### Return value

A Tie object.

### Exceptions

None.



## swapSurfaces()



This method switches the main and secondary surfaces of a tied constraint. This command is valid only during the step in which the interaction is created.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the Tie object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Tie](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tiepyc.htm?ContextScope=all#simaker-tietiepyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The Tie object has members with the same names and descriptions as the arguments to the [Tie](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tiepyc.htm?ContextScope=all#simaker-tietiepyc) method.

In addition, the Tie object has the following member:

- *suppressed*

  A Boolean specifying whether the constraint is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [TIE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-tie.htm?ContextScope=all#simakey-r-tie)