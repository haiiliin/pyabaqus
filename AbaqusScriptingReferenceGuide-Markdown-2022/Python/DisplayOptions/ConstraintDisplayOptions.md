# ConstraintDisplayOptions object

The ConstraintDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when

```
session.viewports[name].assemblyDisplay.constraints=ON
```

The ConstraintDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.

## Access

```
session.viewports[name].assemblyDisplay.constraintOptions
session.viewports[name].layers[name].assemblyDisplay.constraintOptions
```

## setValues(...)



This method modifies the ConstraintDisplayOptions object.



### Required arguments

None.

### Optional arguments

- *constraintEquation*

  A Boolean specifying whether constraint equation symbols are shown. The default value is ON.

- *tieConstraint*

  A Boolean specifying whether tie constraint symbols are shown. The default value is ON.

- *rigidBodyConstraint*

  A Boolean specifying whether rigid body constraint symbols are shown. The default value is ON.

- *displayBodyConstraint*

  A Boolean specifying whether display body constraint symbols are shown. The default value is ON.

- *couplingConstrain*

  A Boolean specifying whether coupling constraint symbols are shown. The default value is ON.

### Return value

None.

### Exceptions

None.



## Members

The ConstraintDisplayOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintdisplayoptionspyc.htm?ContextScope=all#simaker-constraintdisplayoptionssetvaluespyc)method.