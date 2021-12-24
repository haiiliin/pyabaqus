# InertiaReliefState object

The InertiaReliefState object stores the propagating data for an inertia relief load in a step. One instance of this object is created internally by the [InertiaRelief](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiareliefpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [InertiaRelief](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiareliefpyc.htm?ContextScope=all) object.

The InertiaReliefState object has no constructor or methods.

The InertiaReliefState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The InertiaReliefState object has the following members:

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

- *u1State*

  A SymbolicConstant specifying the propagation state of the Boolean that identifies the local 1-direction as a free direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *u2State*

  A SymbolicConstant specifying the propagation state of the Boolean that identifies the local 2-direction as a free direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *u3State*

  A SymbolicConstant specifying the propagation state of the Boolean that identifies the local the 3-direction as a free direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *ur1State*

  A SymbolicConstant specifying the propagation state of the Boolean that identifies rotation about the local 1-direction as a free direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *ur2State*

  A SymbolicConstant specifying the propagation state of the Boolean that identifies the rotation about the local the 2-direction as a free direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *ur3State*

  A SymbolicConstant specifying the propagation state of the Boolean that identifies the rotation about the local the 3-direction as a free direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *fixed*

  A Boolean specifying whether the inertia relief loading should remain fixed at the current loading at the start of the step. The default value is OFF.

- *fixedState*

  A SymbolicConstant specifying the propagation state of the Boolean that identifies whether the inertia relief load should remain fixed at current level at the start of the step. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *referencePointState*

  A SymbolicConstant specifying the propagation state of the reference point of the inertia relief load. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *referencePoint*

  A tuple of Floats specifying the point about which rotations are defined. The point can be specified only for certain combinations of free directions. The *referencePoint* argument can be one of the following:

  - The *X*, *Y* and *Z*-coordinates of a fixed rotation point.
  - A point on the rotation axis.
  - A point on the symmetry line.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *status*

  A SymbolicConstant specifying the propagation state of the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - BUILT_INTO_BASE_STATE

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the load has no amplitude reference.



## Corresponding analysis keywords

- [INERTIA RELIEF](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-inertiarelief.htm?ContextScope=all#simakey-r-inertiarelief)