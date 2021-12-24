# SelectedProbeValues object

The SelectedProbeValues object has no constructor. The SelectedProbeValues object is created when you import the Visualization module.

## Access

```
import visualization
session.selectedProbeValues
```

## Members

The SelectedProbeValues object has the following members:

- *length*

  An Int specifying the length of the *values* member.

- *fieldOutputAvailable*

  A Boolean specifying whether any probe values have been selected (as is necessary prior to writing to a file).

- *values*

  A tuple of tuples of Floats specifying the selected probe values.

- *lastValues*

  A tuple of Floats specifying the last sequence of the *values* member.