# RemeshingRule object

The RemeshingRule object controls the adaptive remeshing resizing and the error indicators written to the output database for a specified region of the model.

## Access

```
import mesh
mdb.models[name].remeshingRules[name]
```

## RemeshingRule(...)



This method creates a RemeshingRule object.



### Path

```
mdb.models[name].RemeshingRule
```

### Required arguments

- *name*

  A String specifying the name of the object.

- *stepName*

  A String specifying the name of the step in which resizing should occur for this rule.

- *variables*

  A sequence of Strings specifying the output request variables that Abaqus will use as error indicators.

### Optional arguments

- *description*

  A String specifying a descriptive string for this rule. The default value is an empty string.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region in which Abaqus will remesh and generate output. The SymbolicConstant MODEL represents the entire applicable model. The default value is MODEL.

- *sizingMethod*

  A SymbolicConstant specifying the method for calculating the new mesh sizes. The SymbolicConstant DEFAULT indicates that Abaqus will use the default calculation method for each individual variable. Possible values are DEFAULT, UNIFORM_ERROR, and MINIMUM_MAXIMUM. The default value is DEFAULT.

- *errorTarget*

  A Float specifying the target error percentage for each variable in the region. A value of 0.0 indicates that Abaqus will use automated error target reduction for the region. You use the *errorTarget* argument when *sizingMethod*=UNIFORM_ERROR. The default value is 0.0.

- *maxSolutionErrorTarget*

  A Float specifying the target error percentage at the location of the maximum solution value in the region. A value of 0.0 indicates that Abaqus will use automated error target reduction for the region. You use the *maxSolutionErrorTarget* argument when *sizingMethod*=MINIMUM_MAXIMUM. The default value is 0.0.

- *minSolutionErrorTarget*

  A Float specifying the target error percentage at the location of the minimum solution value in the region. A value of 0.0 indicates that Abaqus will use automated error target reduction for the region. You use the *minSolutionErrorTarget* argument when *sizingMethod*=MINIMUM_MAXIMUM. The default value is 0.0.

- *meshBias*

  An Int specifying an indication of how much Abaqus will bias the mesh toward the location of the maximum solution value in the region. The higher the value, the more the mesh will bias towards the location of the maximum solution value. You use the *meshBias* argument when *sizingMethod*=MINIMUM_MAXIMUM. The default value is 0.0.

- *minElementSize*

  A Float specifying the minimum size of any single element. The default value is 0.0.

- *maxElementSize*

  A Float specifying the maximum size of any single element. The default value is 0.0.

- *outputFrequency*

  A SymbolicConstant specifying the frequency with which the error indicators are saved to the output database file (.odb). Possible values are LAST_INCREMENT and ALL_INCREMENTS. The default value is LAST_INCREMENT.

- *specifyMinSize*

  A Boolean specifying an indication of whether to use a user-supplied minimum element size or to calculate a characteristic minimum element size. The default value is OFF.

- *specifyMaxSize*

  A Boolean specifying an indication of whether to use a user-supplied maximum element size or to calculate a characteristic maximum element size. The default value is ON.

- *coarseningFactor*

  A SymbolicConstant or an Int specifying an indication of the upper limit on the element growth from one remeshing iteration to the next. Possible values are DEFAULT_LIMIT and NOT_ALLOWED. The default value is DEFAULT_LIMIT.

- *refinementFactor*

  A SymbolicConstant or an Int specifying an indication of the upper limit on element shrinkage from one remeshing iteration to the next. Possible values are DEFAULT_LIMIT and NOT_ALLOWED. The default value is DEFAULT_LIMIT.

- *elementCountLimit*

  None or an Int specifying an approximate limit on the number of elements that will be created during remeshing. Use None to indicate there is not upper limit. The default value is None.

### Return value

A RemeshingRule object.

### Exceptions

AbaqusException.



## resume()



This method resumes the remeshing rule that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the remeshing rule. Abaqus will not remesh regions where the rules are suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the RemeshingRule object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [RemeshingRule ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-remeshingrulepyc.htm?ContextScope=all#simaker-remeshingruleremeshingrulepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The RemeshingRule object has members with the same names and descriptions as the arguments to the [RemeshingRule ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-remeshingrulepyc.htm?ContextScope=all#simaker-remeshingruleremeshingrulepyc)method.

In addition, the RemeshingRule object has the following member:

- *suppressed*

  A Boolean specifying whether the remeshing rule is suppressed. Remeshing of the remeshing rule's region will not occur if you suppress a rule. The default value is OFF.