# FrozenArea object

The FrozenArea object defines a frozen area geometric restriction.

The FrozenArea object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## FrozenArea(...)



This method creates a FrozenArea object.



### Path

```
          mdb.models[name].optimizationTasks[name].FrozenArea
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

### Optional arguments

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Return value

A FrozenArea object.

### Exceptions

None.



## setValues(...)



This method modifies the FrozenArea object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FrozenArea ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-frozenareapyc.htm?ContextScope=all#simaker-frozenareafrozenareapyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The FrozenArea object has members with the same names and descriptions as the arguments to the [FrozenArea ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-frozenareapyc.htm?ContextScope=all#simaker-frozenareafrozenareapyc)method.