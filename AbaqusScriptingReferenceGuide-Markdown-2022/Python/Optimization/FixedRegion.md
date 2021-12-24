# FixedRegion object

The FixedRegion object defines a fixed region geometric restriction.

The FixedRegion object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## FixedRegion(...)



This method creates a FixedRegion object.



### Path

```
          mdb.models[name].optimizationTasks[name].FixedRegion
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

- *presumeFeasibleRegionAtStart*

  A Boolean specifying whether to ignore the geometric restriction in the first design cycle. The default value is ON.

- *u1*

  A Boolean specifying whether to fix the region in the 1-direction. The default value is OFF.

- *u2*

  A Boolean specifying whether to fix the region in the 2-direction. The default value is OFF.

- *u3*

  A Boolean specifying whether to fix the region in the 3-direction. The default value is OFF.

### Return value

A FixedRegion object.

### Exceptions

None.



## setValues(...)



This method modifies the FixedRegion object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FixedRegion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fixedregionpyc.htm?ContextScope=all#simaker-fixedregionfixedregionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The FixedRegion object has members with the same names and descriptions as the arguments to the [FixedRegion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fixedregionpyc.htm?ContextScope=all#simaker-fixedregionfixedregionpyc)method.