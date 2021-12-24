# InertiaRelief object

The InertiaRelief object defines an inertia relief load.

The InertiaRelief object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## InertiaRelief(...)



This method creates an InertiaRelief object.



### Path

```
mdb.models[name].InertiaRelief
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created.

### Optional arguments

- *u1*

  A Boolean specifying the 1-direction as a free direction.Note:Although *u1*, *u2*, *u3*, *ur1*, *ur2*, and *ur3* are optional arguments, at least one of them must be specified. Further, any specified set of free directions cannot include only two rotational degrees of freedom.

- *u2*

  A Boolean specifying the 2-direction as a free direction.

- *u3*

  A Boolean specifying the 3-direction as a free direction.

- *ur1*

  A Boolean specifying the rotation about the 1–direction as a free direction.

- *ur2*

  A Boolean specifying the rotation about the 2–direction as a free direction.

- *ur3*

  A Boolean specifying the rotation about the 3–direction as a free direction.

- *referencePoint*

  A sequence of Floats specifying the *X*, *Y* and *Z*-coordinates of a fixed rotation point or a point on the rotation axis or a point on the symmetry line, about which rotations are defined. Such a point must be specified only for certain combinations of free directions.

- *localCoordinates*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the rigid body degrees of freedom for the inertia relief load. If *localCoordinates*=None, the free directions are defined in the global coordinate system. When this member is queried, it returns an Int. The default value is None.

### Return value

An InertiaRelief object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing InertiaRelief object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [InertiaRelief ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiareliefpyc.htm?ContextScope=all#simaker-inertiareliefinertiareliefpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing InertiaRelief object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *u1*

  A Boolean specifying the 1-direction as a free direction.

- *u2*

  A Boolean specifying the 2-direction as a free direction.

- *u3*

  A Boolean specifying the 3-direction as a free direction.

- *ur1*

  A Boolean specifying the rotation about the 1–direction as a free direction.

- *ur2*

  A Boolean specifying the rotation about the 2–direction as a free direction.

- *ur3*

  A Boolean specifying the rotation about the 3–direction as a free direction.

- *referencePoint*

  A sequence of Floats specifying the point about which rotations are defined. The point can be specified only for certain combinations of free directions. The *referencePoint* argument can be one of the following:

  - The *X*, *Y* and *Z*-coordinates of a fixed rotation point.
  - A point on the rotation axis.
  - A point on the symmetry line.

- *fixed*

  A Boolean specifying whether the inertia relief loading should remain fixed at the current loading at the start of the step. The default value is OFF.

### Return value

None.

### Exceptions

None.



## Members

The InertiaRelief object can have the following members:

- *name*

  A String specifying the load repository key.

- *localCoordinates*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the rigid body degrees of freedom for the inertia relief load. If *localCoordinates*=None, the free directions are defined in the global coordinate system. When this member is queried, it returns an Int. The default value is None.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.