# RayleighDampingComponent object

A RayleighDampingComponent object is used to define Rayleigh damping over a range of modes.

## Access

```
import step
mdb.models[name].steps[name].rayleighDamping.components[i]
```

## Members

The RayleighDampingComponent object has the following members:

- *start*

  An Int specifying the mode number of the lowest mode of a range.

- *end*

  An Int specifying the mode number of the highest mode of a range.

- *alpha*

  A Float specifying the mass proportional damping, αM.

- *beta*

  A Float specifying the stiffness proportional damping, βM.