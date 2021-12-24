# ErrorIndicatorResult object

The ErrorIndicatorResult object contains result information corresponding to an error indicator variable in a [RemeshingRule](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-remeshingrulepyc.htm?ContextScope=all) object for an adaptivity iteration.

## Access

```
import job
mdb.adaptivityProcesses[name].iterations[i].ruleResults[name]\
.indicatorResults[name]
```

## ErrorIndicatorResult(...)



This method creates an ErrorIndicatorResult with data for an error indicator variable in a [RemeshingRule](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-remeshingrulepyc.htm?ContextScope=all) for a given adaptivity iteration.



### Path

```
mdb.adaptivityProcesses[name].iterations[i].ruleResults[name]\
.ErrorIndicatorResult
```

### Required arguments

- *name*

  A String specifying the name of the error indicator variable to which these results correspond.

- *results*

  A String-to-Float Dictionary specifying the calculated results from the sizing function corresponding to the error indicator variable represented by this ErrorIndicatorResult.

### Optional arguments

None.

### Return value

An ErrorIndicatorResult object.

### Exceptions

AbaqusException.



## Members

The ErrorIndicatorResult object has members with the same names and descriptions as the arguments to the [ErrorIndicatorResult ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-errorindicatorresultpyc.htm?ContextScope=all#simaker-errorindicatorresulterrorindicatorresultpyc)method.