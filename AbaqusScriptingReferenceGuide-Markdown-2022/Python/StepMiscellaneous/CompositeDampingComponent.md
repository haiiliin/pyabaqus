# CompositeDampingComponent object

A CompositeDampingComponent object is used to define composite damping over a range of modes.

## Access

```
import step
mdb.models[name].steps[name].compositeDamping.components[i]
```

## Members

The CompositeDampingComponent object has the following members:

- *start*

  An Int specifying the mode number of the lowest mode of a range.

- *end*

  An Int specifying the mode number of the highest mode of a range.