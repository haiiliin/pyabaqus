# DirectDampingComponent object

A DirectDampingComponent object is used to define direct damping over a range of modes.

## Access

```
import step
mdb.models[name].steps[name].directDamping.components[i]
```

## Members

The DirectDampingComponent object has the following members:

- *start*

  An Int specifying the mode number of the lowest mode of a range.

- *end*

  An Int specifying the mode number of the highest mode of a range.

- *fraction*

  A Float specifying the fraction of critical damping.