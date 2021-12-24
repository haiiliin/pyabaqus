# GeometricRestriction object

The GeometricRestriction object is the abstract base type for other GeometricRestriction objects. The GeometricRestriction object has no explicit constructor. The methods and members of the GeometricRestriction object are common to all objects derived from GeometricRestriction.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## Members

The GeometricRestriction object can have the following members:

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.