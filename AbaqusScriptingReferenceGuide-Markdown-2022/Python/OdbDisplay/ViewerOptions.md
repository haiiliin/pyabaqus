# ViewerOptions object

The ViewerOptions object specifies options to set the result caching parameters. The ViewerOptions object has no constructor. Abaqus creates the *viewerOptions* member when a session is started.

## Access

```
import visualization
session.viewerOptions
```

## setValues(...)



This method modifies the ViewerOptions object.



### Required arguments

None.

### Optional arguments

- *primaryVariableCaching*

  A Boolean specifying whether results are currently cached. Caching improves the performance of subsequent access. The default value is ON.

- *deformedVariableCaching*

  A Boolean specifying whether deformation vectors are currently cached. Caching improves the performance of subsequent access. The default value is ON.

- *cutVariableCaching*

  A Boolean specifying whether the values used for displaying cut models are currently cached. Caching improves the performance of subsequent access. The default value is ON.

- *odbUpdateChecking*

  A Boolean specifying whether the current .odb file should be checked for updates. Setting *odbUpdateChecking* to OFF can improve Viewer performance when accessing data from a remote file. The default value is ON.

- *odbUpdateCheckInterval*

  An Int specifying the minimum time between status checks (in seconds). The default value is 0.

### Return value

None.

### Exceptions

None.



## Members

The ViewerOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vieweroptionspyc.htm?ContextScope=all#simaker-vieweroptionssetvaluespyc)method.