# TopologyMillingControl object

The TopologyMillingControl object defines a topology milling control geometric restriction.

The TopologyMillingControl object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## TopologyMillingControl(...)



This method creates a TopologyMillingControl object.



### Path

```
          mdb.models[name].optimizationTasks[name].TopologyMillingControl
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *millingDirections*

  A tuple of [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects of length 2 specifying the milling directions. Each point can be specified through a tuple of coordinates instead of through a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all).

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the *millingDirections*. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int indicating the identifier of the [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all). The default value is None.

- *millingCheckRegion*

  The SymbolicConstant MILLING_REGION or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the milling check region. If the value is MILLING_REGION, the value of *region* is used as both the milling control region and the milling check region. The default value is MILLING_REGION.

- *radius*

  A Float specifying the radius for the collision check during the removal of the elements for the milling criteria.

### Return value

A TopologyMillingControl object.

### Exceptions

None.



## setValues(...)



This method modifies the TopologyMillingControl object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TopologyMillingControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymillingcontrolpyc.htm?ContextScope=all#simaker-topologymillingcontroltopologymillingcontrolpyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The TopologyMillingControl object has members with the same names and descriptions as the arguments to the [TopologyMillingControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymillingcontrolpyc.htm?ContextScope=all#simaker-topologymillingcontroltopologymillingcontrolpyc) method.