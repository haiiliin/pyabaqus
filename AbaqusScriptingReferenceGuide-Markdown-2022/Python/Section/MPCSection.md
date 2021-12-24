# MPCSection object

The MPCSection object defines the properties of a multi-point constraint section.

The MPCSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## MPCSection(...)



This method creates a MPCSection object.



### Path

```
mdb.models[name].MPCSection
session.odbs[name].MPCSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *mpcType*

  A SymbolicConstant specifying the MPC type of the section. Possible values are BEAM_MPC, ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_DEFINED.

### Optional arguments

- *userMode*

  A SymbolicConstant specifying the mode of the MPC when it is user-defined. Possible values are DOF_MODE and NODE_MODE. The default value is DOF_MODE.The *userMode* argument applies only when *mpcType*=USER_DEFINED.

- *userType*

  An Int specifying to differentiate between different constraint types in a user-defined MPCSection. The default value is 0.The *userType* argument applies only when *mpcType*=USER_DEFINED.

### Return value

A MPCSection object.

### Exceptions

RangeError and InvalidNameError.



## Members

The MPCSection object has members with the same names and descriptions as the arguments to the [MPCSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mpcsectionpyc.htm?ContextScope=all#simaker-mpcsectionmpcsectionpyc)method.



## Corresponding analysis keywords

- [MPC](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-mpc.htm?ContextScope=all#simakey-r-mpc)