# RuleResult object

The RuleResult object contains result information corresponding to a [RemeshingRule](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-remeshingrulepyc.htm?ContextScope=all) object for an adaptivity iteration.

## Access

```
import job
mdb.adaptivityProcesses[name].iterations[i].ruleResults[name]
```

## RuleResult(...)



This method creates a RuleResult with data for a [RemeshingRule](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-remeshingrulepyc.htm?ContextScope=all) for a given adaptivity iteration.



### Path

```
mdb.adaptivityProcesses[name].iterations[i].RuleResult
```

### Required arguments

- *name*

  A String specifying the name of the Remeshing Rule to which these results correspond.

- *indicatorResults*

  A repository of [ErrorIndicatorResult](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-errorindicatorresultpyc.htm?ContextScope=all) objects specifying the calculated results from the sizing function corresponding to the error indicator variables for the Remeshing Rule.

- *numElems*

  An Int specifying the number of elements before remeshing in the region of the Remeshing Rule.

- *minSizeElemCount*

  An Int specifying the number of elements that were constrained to the minimum element size by the Remeshing Rule.

### Optional arguments

- *satisfiedVars*

  A sequence of Strings specifying the error indicator variables that have satisfied the Remeshing Rule.

### Return value

A RuleResult object.

### Exceptions

AbaqusException.



## Members

The RuleResult object has members with the same names and descriptions as the arguments to the [RuleResult ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ruleresultpyc.htm?ContextScope=all#simaker-ruleresultruleresultpyc)method.