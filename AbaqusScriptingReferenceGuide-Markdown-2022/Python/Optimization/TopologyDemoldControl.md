# TopologyDemoldControl object

The TopologyDemoldControl object defines a topology demold control geometric restriction.

The TopologyDemoldControl object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## TopologyDemoldControl(...)



This method creates a TopologyDemoldControl object.



### Path

```
          mdb.models[name].optimizationTasks[name].TopologyDemoldControl
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the *pullDirection*. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int indicating the identifier of the [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all). The default value is None.

- *draftAngle*

  A Float specifying the draft angle. The default value is 0.0.

- *collisionCheckRegion*

  The SymbolicConstant DEMOLD_REGION or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the collision check region. If the value is DEMOLD_REGION, then the value of *region* is used as both the demold region and the collision check region. The default value is DEMOLD_REGION.

- *pointRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the point on a plane perpendicular to the pull direction, used to specify the central plane when *technique* is POINT.

- *pullDirection*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object of length 2 specifying the demold pull direction. Instead of through a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), each point may be specified through a tuple of coordinates.

- *technique*

  A SymbolicConstant specifying the demold technique. Possible values are AUTO, AUTO_TIGHT, POINT, SURFACE, and STAMP. The default value is AUTO.

### Return value

A TopologyDemoldControl object.

### Exceptions

None.



## setValues(...)



This method modifies the TopologyDemoldControl object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TopologyDemoldControl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologydemoldcontrolpyc.htm?ContextScope=all#simaker-topologydemoldcontroltopologydemoldcontrolpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The TopologyDemoldControl object has members with the same names and descriptions as the arguments to the [TopologyDemoldControl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologydemoldcontrolpyc.htm?ContextScope=all#simaker-topologydemoldcontroltopologydemoldcontrolpyc)method.