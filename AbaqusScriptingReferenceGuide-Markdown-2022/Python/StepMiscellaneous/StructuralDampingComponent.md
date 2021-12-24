# StructuralDampingComponent object

A StructuralDampingComponent object is used to define structural damping over a range of modes.

## Access

```
import step
mdb.models[name].steps[name].structuralDamping.components[i]
```

## Members

The StructuralDampingComponent object has the following members:

- *start*

  An Int specifying the mode number of the lowest mode of a range.

- *end*

  An Int specifying the mode number of the highest mode of a range.

- *factor*

  A Float specifying the damping factor, s.