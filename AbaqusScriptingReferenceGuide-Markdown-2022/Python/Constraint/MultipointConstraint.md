# MultipointConstraint object

The MultipointConstraint object defines a constraint between a group of MultipointConstraint nodes located on a region and a reference point.

The MultipointConstraint object is derived from the [Constraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].constraints[name]
```

## MultipointConstraint(...)



This method creates a MultipointConstraint object.



### Path

```
mdb.models[name].MultipointConstraint
```

### Required arguments

- *name*

  A String specifying the constraint repository key.

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surface on which the MultipointConstraint nodes are located.

- *controlPoint*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the constraint control point.

- *mpcType*

  A SymbolicConstant specifying the MPC type of the constraint. Possible values are BEAM_MPC, ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_MPC.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the initial orientation of the local coordinate system for the MultipointConstraint's degrees of freedom. If *localCsys*=None, the MultipointConstraint is defined in the global coordinate system. The default value is None.

- *userType*

  An Int specifying to differentiate between different constraint types in a user-defined MultipointConstraint. The default value is 0.The *userType* argument applies only when *mpcType*=USER_MPC.

- *userMode*

  A SymbolicConstant specifying the mode of the constraint when it is user-defined. Possible values are DOF_MODE_MPC and NODE_MODE_MPC. The default value is DOF_MODE_MPC.The *userMode* argument applies only when *mpcType*=USER_MPC.

### Return value

A MultipointConstraint object.

### Exceptions

None.



## setValues(...)



This method modifies the MultipointConstraint object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MultipointConstraint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-multipointconstraintpyc.htm?ContextScope=all#simaker-multipointconstraintmultipointconstraintpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The MultipointConstraint object has members with the same names and descriptions as the arguments to the [MultipointConstraint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-multipointconstraintpyc.htm?ContextScope=all#simaker-multipointconstraintmultipointconstraintpyc)method.

In addition, the MultipointConstraint object has the following member:

- *suppressed*

  A Boolean specifying whether the constraint is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [MPC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-mpc.htm?ContextScope=all#simakey-r-mpc)