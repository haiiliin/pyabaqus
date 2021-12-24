# OdbRigidBody object

The Rigid body object is used to bind a set of elements and/or a set of nodes and/or an analytical surface with a reference node.

## Access

```
import odbAccess
session.odbs[name].parts[name].rigidBodies[i]
session.odbs[name].rootAssembly.instances[name].rigidBodies[i]
session.odbs[name].rootAssembly.rigidBodies[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.rigidBodies[i]
```

## RigidBody(...)



This method creates a OdbRigidBody object.



### Path

session.odbs[*name*].rootAssembly.instances[*name*].RigidBody

session.odbs[*name*].rootAssembly.RigidBody

### Required arguments

- *referenceNode*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the reference node set associated with the rigid body.

### Optional arguments

- *position*

  A SymbolicConstant specifying the specific location of the OdbRigidBody reference node relative to the rest of the rigid body. Possible values are INPUT and CENTER_OF_MASS. The default value is INPUT.

- *isothermal*

  A Boolean specifying specify whether the OdbRigidBody can have temperature gradients or be isothermal. This is used only for fully coupled thermal-stress analysis The default value is ON.

- *elements*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the element set whose motion is governed by the motion of rigid body reference node.

- *tieNodes*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the node set which have both translational and rotational degrees of freedom associated with the rigid body.

- *pinNodes*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the node set which have only translational degrees of freedom associated with the rigid body.

- *analyticSurface*

  An [AnalyticSurface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?ContextScope=all) object specifying the analytic surface whose motion is governed by the motion of rigid body reference node.

### Return value

An OdbRigidBody object.

### Exceptions

None.



## Members

The OdbRigidBody object has members with the same names and descriptions as the arguments to the [RigidBody ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbrigidbodypyc.htm?ContextScope=all#simaker-odbrigidbodyrigidbodypyc)method.