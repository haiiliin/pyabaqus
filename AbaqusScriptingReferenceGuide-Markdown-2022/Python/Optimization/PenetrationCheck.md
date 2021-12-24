# PenetrationCheck object

The PenetrationCheck object defines a penetration check geometric restriction.

The PenetrationCheck object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

This page discusses:

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## PenetrationCheck(...)



This method creates a PenetrationCheck object.



### Path

```
          mdb.models[name].optimizationTasks[name].PenetrationCheck
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *penetrationCheckRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the penetration check region.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *presumeFeasibleRegionAtStart*

  A Boolean specifying whether to ignore the geometric restriction in the first design cycle. The default value is ON.

### Return value

A PenetrationCheck object.

### Exceptions

None.



## setValues(...)



This method modifies the PenetrationCheck object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PenetrationCheck ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-penetrationcheckpyc.htm?ContextScope=all#simaker-penetrationcheckpenetrationcheckpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The PenetrationCheck object has members with the same names and descriptions as the arguments to the [PenetrationCheck ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-penetrationcheckpyc.htm?ContextScope=all#simaker-penetrationcheckpenetrationcheckpyc)method.