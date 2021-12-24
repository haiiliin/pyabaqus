# PointMassInertia object

The PointMassInertia object defines point masses and point rotary inertia on a part or an assembly region.

The PointMassInertia object is derived from the [Inertia](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiapyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.inertias[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]
```

## PointMassInertia(...)



This method creates a PointMassInertia object.



### Path

```
mdb.models[name].parts[name].engineeringFeatures.PointMassInertia
mdb.models[name].rootAssembly.engineeringFeatures.PointMassInertia
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the mass or rotary inertia is applied.

### Optional arguments

- *mass*

  A Float specifying the mass magnitude for isotropic mass. This parameter cannot be specified when anisotropic mass terms are specified. The default value is 0.0.

- *mass1*

  A Float specifying the mass in the 1-direction for anisotropic mass. This parameter cannot be specified when isotropic mass is also specified. The default value is 0.0.

- *mass2*

  A Float specifying the mass in the 2-direction for anisotropic mass. This parameter cannot be specified when isotropic mass is also specified. The default value is 0.0.

- *mass3*

  A Float specifying the mass in the 3-direction for anisotropic mass. This parameter cannot be specified when isotropic mass is also specified. The default value is 0.0.

- *i11*

  A Float specifying the rotary inertia about the local 1-axis, I11I11. The default value is 0.0.

- *i22*

  A Float specifying the rotary inertia about the local 2-axis, I22I22. The default value is 0.0.

- *i33*

  A Float specifying the rotary inertia about the local 3-axis, I33I33. The default value is 0.0.

- *i12*

  A Float specifying the product of inertia, I12I12. The default value is 0.0.

- *i13*

  A Float specifying the product of inertia, I13I13. The default value is 0.0.

- *i23*

  A Float specifying the product of inertia, I23I23. The default value is 0.0.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system for the anisotropic mass terms (when specified), and the rotary inertia (when specified). If *localCsys*=None, the anisotropic mass and rotary inertia data are defined in the global coordinate system. The default value is None.

- *alpha*

  A Float specifying the alpha damping magnitude. The default value is 0.0.This argument applies only to Abaqus/Standard analyses.

- *composite*

  A Float specifying the composite damping magnitude. The default value is 0.0.This argument applies only to Abaqus/Standard analyses.

### Return value

A PointMassInertia object.

### Exceptions

None.



## setValues(...)



This method modifies the PointMassInertia object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PointMassInertia ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pointmassinertiapyc.htm?ContextScope=all#simaker-pointmassinertiapointmassinertiapyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The PointMassInertia object has members with the same names and descriptions as the arguments to the [PointMassInertia ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pointmassinertiapyc.htm?ContextScope=all#simaker-pointmassinertiapointmassinertiapyc)method.

In addition, the PointMassInertia object has the following member:

- *suppressed*

  A Boolean specifying whether the inertia is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [MASS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-mass.htm?ContextScope=all#simakey-r-mass), [ROTARY INERTIA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-rotaryinertia.htm?ContextScope=all#simakey-r-rotaryinertia)