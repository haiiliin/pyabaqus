# MdbDataStep object

The MdbDataStep object.It corresponds to same named step in the cae model.

## Access

```
import visualization
session.mdbData[name].steps[i]
```

## Members

The MdbDataStep object has the following member:

- *frames*

  A [MdbDataFrameArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbdataframepyc.htm?ContextScope=all) object specifying the list of frames. The list is read-only. There is only one frame in a step.