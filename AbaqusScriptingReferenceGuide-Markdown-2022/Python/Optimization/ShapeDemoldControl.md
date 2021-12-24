# ShapeDemoldControl object

The ShapeDemoldControl object defines a shape demold control geometric restriction.

The ShapeDemoldControl object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## ShapeDemoldControl(...)



This method creates a ShapeDemoldControl object.



### Path

```
          mdb.models[name].optimizationTasks[name].ShapeDemoldControl
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *pullDirection*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object of length 2 specifying the demold pull direction. Instead of through a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), each point might be specified through a tuple of coordinates.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *collisionCheckRegion*

  The SymbolicConstant DEMOLD_REGION or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the collision check region. If the value is DEMOLD_REGION, then the value of *region* is used as both the demold region and the collision check region. The default value is DEMOLD_REGION.

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the *pullDirection*. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int indicating the identifier of the [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all). The default value is None.

- *drawAngle*

  A Float specifying the draw angle. The default value is 0.0.

- *mainPointDetermination*

  A SymbolicConstant specifying the rule for assigning point priority. Possible values are MAXIMUM and MINIMUM. The default value is MAXIMUM.

- *presumeFeasibleRegionAtStart*

  A Boolean specifying whether to ignore the geometric restriction in the first design cycle. The default value is ON.

- *tolerance1*

  A Float specifying the geometric tolerance in the 1-direction. The default value is 0.01.

- *tolerance2*

  A Float specifying the geometric tolerance in the 2-direction. The default value is 0.01.

- *tolerance3*

  A Float specifying the geometric tolerance in the 3-direction. The default value is 0.01.

- *undercutTolerance*

  A Float specifying the undercut tolerance. The default value is 0.0.

### Return value

A ShapeDemoldControl object.

### Exceptions

None.



## setValues(...)



This method modifies the ShapeDemoldControl object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ShapeDemoldControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapedemoldcontrolpyc.htm?ContextScope=all#simaker-shapedemoldcontrolshapedemoldcontrolpyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The ShapeDemoldControl object has members with the same names and descriptions as the arguments to the [ShapeDemoldControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapedemoldcontrolpyc.htm?ContextScope=all#simaker-shapedemoldcontrolshapedemoldcontrolpyc) method.