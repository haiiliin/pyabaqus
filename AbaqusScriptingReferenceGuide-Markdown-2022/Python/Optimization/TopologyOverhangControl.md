# TopologyOverhangControl object

The TopologyOverhangControl object defines a topology overhang control geometric restriction.

The TopologyOverhangControl object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## TopologyOverhangControl(...)



This method creates a TopologyOverhangControl object.



### Path

```
          mdb.models[name].optimizationTasks[name].TopologyOverhangControl
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *pullDirection*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object of length 2 specifying the overhang control print direction. Instead of through a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), each point can be specified through a tuple of coordinates.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the *pullDirection*. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int indicating the identifier of the [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all). The default value is None.

- *draftAngle*

  A Float specifying the overhang angle. The default value is 45.0.

- *overhangCheckRegion*

  The SymbolicConstant OVERHANG_REGION or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the overhang check region. If the value is OVERHANG_REGION, the value of *region* is used as both the overhang control region and the overhang check region. The default value is OVERHANG_REGION.

- *pointRegion*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the point on a plane perpendicular to the *pullDirection* that is used to specify the base plane when *technique* is POINT.

- *radius*

  A Float specifying the radius to define the size of the cones that are used in the internal check for the overhang criteria.

- *technique*

  A SymbolicConstant specifying the overhang control technique used to define the base plane. Possible values are AUTO, POINT, and NONE. The default value is AUTO.

### Return value

A TopologyOverhangControl object.

### Exceptions

None.



## setValues(...)



This method modifies the TopologyOverhangControl object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TopologyOverhangControl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyoverhangcontrolpyc.htm?ContextScope=all#simaker-topologyoverhangcontroltopologyoverhangcontrolpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The TopologyOverhangControl object has members with the same names and descriptions as the arguments to the [TopologyOverhangControl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyoverhangcontrolpyc.htm?ContextScope=all#simaker-topologyoverhangcontroltopologyoverhangcontrolpyc)method.