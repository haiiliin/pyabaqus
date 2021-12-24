# FeatureOptions object

The FeatureOptions object stores the options that control the behavior of feature regeneration for all features in a model.

## Access

```
import part
mdb.models[name].featureOptions
```

## setValues(...)



This method modifies the FeatureOptions object for the specified model.



### Required arguments

None.

### Optional arguments

- *checkSelfIntersection*

  A Boolean specifying whether Abaqus/CAE should perform self-intersection checks while regenerating features. The default value is ON.

- *autoCaching*

  A Boolean specifying whether geometric states should be automatically cached. The default value is ON.

- *maxCachedStates*

  An Int specifying the maximum number of caches to be stored with each part or with the assembly. The default value is 5.

### Return value

None.

### Exceptions

None.



## Members

The FeatureOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featureoptionspyc.htm?ContextScope=all#simaker-featureoptionssetvaluespyc)method.