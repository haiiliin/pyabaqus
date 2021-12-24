# OdbDataStep object

The OdbDataStep object.

## Access

```
import visualization
session.odbData[name].steps[i]
```

## setValues(...)



This method modifies the OdbDataStep object.



### Required arguments

- *activateFrames*

  A Boolean specifying whether to activate all the frames in the step.

### Optional arguments

- *update*

  A Boolean specifying whether to update the model. The default value is ON

### Return value

None.

### Exceptions

None.



## Members

The OdbDataStep object has the following member:

- *frames*

  An [OdbDataFrameArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdataframepyc.htm?ContextScope=all) object specifying the list of frames. The list is read-only.