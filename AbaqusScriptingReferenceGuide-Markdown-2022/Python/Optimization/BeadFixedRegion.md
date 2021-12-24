# BeadFixedRegion object

The BeadFixedRegion object defines a fixed region geometric restriction.

The BeadFixedRegion object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## BeadFixedRegion(...)



This method creates a BeadFixedRegion object.



### Path

```
          mdb.models[name].optimizationTasks[name].BeadFixedRegion
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

- *u1*

  A Boolean specifying whether to fix the region in the 1-direction. The default value is OFF.

- *u2*

  A Boolean specifying whether to fix the region in the 2-direction. The default value is OFF.

- *u3*

  A Boolean specifying whether to fix the region in the 3-direction. The default value is OFF.

### Return value

A BeadFixedRegion object.

### Exceptions

None.



## setValues(...)



This method modifies the BeadFixedRegion object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BeadFixedRegion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadfixedregionpyc.htm?ContextScope=all#simaker-beadfixedregionbeadfixedregionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The BeadFixedRegion object has members with the same names and descriptions as the arguments to the [BeadFixedRegion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadfixedregionpyc.htm?ContextScope=all#simaker-beadfixedregionbeadfixedregionpyc)method.