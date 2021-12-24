# BeadGrowth object

The BeadGrowth object defines a growth geometric restriction.

The BeadGrowth object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## BeadGrowth(...)



This method creates a BeadGrowth object.



### Path

```
          mdb.models[name].optimizationTasks[name].BeadGrowth
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

- *beadGrowth*

  A Float specifying the maximum optimization displacement in the growth direction. Either *beadGrowth* or *shrink* or both must be specified. The default value is 0.0.

- *shrink*

  A Float specifying the maximum optimization displacement in the shrink direction. Either *beadGrowth* or *shrink* or both must be specified The default value is 0.0.

### Return value

A BeadGrowth object.

### Exceptions

None.



## setValues(...)



This method modifies the BeadGrowth object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BeadGrowth ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadgrowthpyc.htm?ContextScope=all#simaker-beadgrowthbeadgrowthpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The BeadGrowth object has members with the same names and descriptions as the arguments to the [BeadGrowth ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadgrowthpyc.htm?ContextScope=all#simaker-beadgrowthbeadgrowthpyc)method.