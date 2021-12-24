# SizingClusterAreas object

The SizingClusterAreas object defines a sizing cluster areas geometric restriction.

The SizingClusterAreas object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## SizingClusterAreas(...)



This method creates a SizingClusterAreas object.



### Path

```
          mdb.models[name].optimizationTasks[name].SizingClusterAreas
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *regions*

  Tuple of [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects specifying the regions to which the geometric restriction is applied.

### Return value

A SizingClusterAreas object.

### Exceptions

None.



## setValues(...)



This method modifies the SizingClusterAreas object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SizingClusterAreas ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingclusterareaspyc.htm?ContextScope=all#simaker-sizingclusterareassizingclusterareaspyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The SizingClusterAreas object has members with the same names and descriptions as the arguments to the [SizingClusterAreas ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingclusterareaspyc.htm?ContextScope=all#simaker-sizingclusterareassizingclusterareaspyc)method.