# BeadPenetrationCheck object

The BeadPenetrationCheck object defines a penetration check geometric restriction.

The BeadPenetrationCheck object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## BeadPenetrationCheck(...)



This method creates a BeadPenetrationCheck object.



### Path

```
          mdb.models[name].optimizationTasks[name].BeadPenetrationCheck
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *beadPenetrationCheckRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the penetration check region.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

None.

### Return value

A BeadPenetrationCheck object.

### Exceptions

None.



## setValues(...)



This method modifies the BeadPenetrationCheck object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BeadPenetrationCheck ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpenetrationcheckpyc.htm?ContextScope=all#simaker-beadpenetrationcheckbeadpenetrationcheckpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The BeadPenetrationCheck object has members with the same names and descriptions as the arguments to the [BeadPenetrationCheck ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpenetrationcheckpyc.htm?ContextScope=all#simaker-beadpenetrationcheckbeadpenetrationcheckpyc)method.