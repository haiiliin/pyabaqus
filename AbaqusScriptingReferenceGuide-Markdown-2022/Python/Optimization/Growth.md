# Growth object

The Growth object defines a growth geometric restriction.

The Growth object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## Growth(...)



This method creates a Growth object.



### Path

```
          mdb.models[name].optimizationTasks[name].Growth
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *growth*

  A Float specifying the maximum optimization displacement in the growth direction. Either *growth* or *shrink* or both must be specified. The default value is 0.0.

- *presumeFeasibleRegionAtStart*

  A Boolean specifying whether to ignore the geometric restriction in the first design cycle. The default value is ON.

- *shrink*

  A Float specifying the maximum optimization displacement in the shrink direction. Either *growth* or *shrink* or both must be specified The default value is 0.0.

### Return value

A Growth object.

### Exceptions

None.



## setValues(...)



This method modifies the Growth object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Growth ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-growthpyc.htm?ContextScope=all#simaker-growthgrowthpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The Growth object has members with the same names and descriptions as the arguments to the [Growth ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-growthpyc.htm?ContextScope=all#simaker-growthgrowthpyc)method.