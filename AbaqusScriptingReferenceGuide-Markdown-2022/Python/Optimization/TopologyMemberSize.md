# TopologyMemberSize object

The TopologyMemberSize object defines a topology member size geometric restriction.

The TopologyMemberSize object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## TopologyMemberSize(...)



This method creates a TopologyMemberSize object.



### Path

```
          mdb.models[name].optimizationTasks[name].TopologyMemberSize
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *maxThickness*

  A Float specifying the maximum thickness. The default value is 0.0.

- *minThickness*

  A Float specifying the minimum thickness. The default value is 0.0.

- *separation*

  A Float specifying the minimum gap. The default value is 0.0.

- *sizeRestriction*

  A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an envelope of both. Possible values are ENVELOPE, MAXIMUM, and MINIMUM. The default value is MINIMUM.

### Return value

A TopologyMemberSize object.

### Exceptions

None.



## setValues(...)



This method modifies the TopologyMemberSize object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TopologyMemberSize ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymembersizepyc.htm?ContextScope=all#simaker-topologymembersizetopologymembersizepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The TopologyMemberSize object has members with the same names and descriptions as the arguments to the [TopologyMemberSize ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymembersizepyc.htm?ContextScope=all#simaker-topologymembersizetopologymembersizepyc)method.