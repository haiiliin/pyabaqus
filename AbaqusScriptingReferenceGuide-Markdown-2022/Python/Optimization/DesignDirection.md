# DesignDirection object

The DesignDirection object defines a design direction geometric restriction.

The DesignDirection object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## DesignDirection(...)



This method creates a DesignDirection object.



### Path

```
          mdb.models[name].optimizationTasks[name].DesignDirection
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

- *mainPoint*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the main point used when *mainPointDetermination* is SPECIFY. The default value is None.

- *mainPointDetermination*

  A SymbolicConstant specifying the rule for assigning point priority. Possible values are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

- *movementRestriction*

  A SymbolicConstant specifying whether movement in the region should follow only the direction of the *mainPoint*, only the magnitude, or both the magnitude of the *mainPoint* and the directions specified by *u1*, *u2* and *u3*. Possible values are DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR.

- *presumeFeasibleRegionAtStart*

  A Boolean specifying whether to ignore the geometric restriction in the first design cycle. The default value is ON.

- *u1*

  A Boolean specifying whether movement in the region should follow the *masterPoint* in the 1-direction. This is used when *movementRestriction* is VECTOR. The default value is ON.

- *u2*

  A Boolean specifying whether movement in the region should follow the *masterPoint* in the 2-direction. This is used when *movementRestriction* is VECTOR. The default value is ON.

- *u3*

  A Boolean specifying whether movement in the region should follow the *masterPoint* in the 3-direction. This is used when *movementRestriction* is VECTOR. The default value is ON.

### Return value

A DesignDirection object.

### Exceptions

None.



## setValues(...)



This method modifies the DesignDirection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DesignDirection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designdirectionpyc.htm?ContextScope=all#simaker-designdirectiondesigndirectionpyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The DesignDirection object has members with the same names and descriptions as the arguments to the [DesignDirection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designdirectionpyc.htm?ContextScope=all#simaker-designdirectiondesigndirectionpyc) method.