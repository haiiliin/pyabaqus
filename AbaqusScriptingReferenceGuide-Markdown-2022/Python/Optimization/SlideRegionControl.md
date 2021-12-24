# SlideRegionControl object

The SlideRegionControl object defines a slide region control geometric restriction.

The SlideRegionControl object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## SlideRegionControl(...)



This method creates a SlideRegionControl object.



### Path

```
          mdb.models[name].optimizationTasks[name].SlideRegionControl
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *clientDirection*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object of length 2 specifying the axis of revolution. Instead of through a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), each point may be specified through a tuple of coordinates. This is used when *approach* is TURN.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *approach*

  A SymbolicConstant specifying the restriction approach. The SymbolicConstant FREE_FORM indicates a free-form slide region, and the SymbolicConstant TURN indicates that the restriction should conserve a turnable surface. Possible values are FREE_FORM and TURN. The default value is FREE_FORM.

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. This is used when *approach* is TURN. The default value is None.

- *freeFormRegion*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the free-form region. This is used when *approach* is FREE_FORM. The default value is None.

- *presumeFeasibleRegionAtStart*

  A Boolean specifying whether to ignore the geometric restriction in the first design cycle. The default value is ON.

- *revolvedRegion*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to revolve into a slide region. This is used when *approach* is TURN. The default value is None.

- *tolerance1*

  A Float specifying the geometric tolerance in the 1-direction. This is used when *approach* is TURN. The default value is 0.01.

- *tolerance2*

  A Float specifying the geometric tolerance in the 2-direction. This is used when *approach* is TURN. The default value is 0.01.

- *tolerance3*

  A Float specifying the geometric tolerance in the 3-direction. This is used when *approach* is TURN. The default value is 0.01.

### Return value

A SlideRegionControl object.

### Exceptions

None.



## setValues(...)



This method modifies the SlideRegionControl object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SlideRegionControl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-slideregioncontrolpyc.htm?ContextScope=all#simaker-slideregioncontrolslideregioncontrolpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The SlideRegionControl object has members with the same names and descriptions as the arguments to the [SlideRegionControl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-slideregioncontrolpyc.htm?ContextScope=all#simaker-slideregioncontrolslideregioncontrolpyc)method.