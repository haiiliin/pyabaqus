# SizingPointSymmetry object

The SizingPointSymmetry object defines a sizing point symmetry geometric restriction.

The SizingPointSymmetry object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## SizingPointSymmetry(...)



This method creates a SizingPointSymmetry object.



### Path

```
          mdb.models[name].optimizationTasks[name].SizingPointSymmetry
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the position of the symmetry point defined as the origin of a local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

- *ignoreFrozenArea*

  A Boolean specifying whether to ignore frozen areas. The default value is OFF.

### Return value

A SizingPointSymmetry object.

### Exceptions

None.



## setValues(...)



This method modifies the SizingPointSymmetry object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SizingPointSymmetry ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingpointsymmetrypyc.htm?ContextScope=all#simaker-sizingpointsymmetrysizingpointsymmetrypyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The SizingPointSymmetry object has members with the same names and descriptions as the arguments to the [SizingPointSymmetry ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingpointsymmetrypyc.htm?ContextScope=all#simaker-sizingpointsymmetrysizingpointsymmetrypyc)method.