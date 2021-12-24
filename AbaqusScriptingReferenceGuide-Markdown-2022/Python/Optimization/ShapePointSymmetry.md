# ShapePointSymmetry object

The ShapePointSymmetry object defines a shape point symmetry geometric restriction.

The ShapePointSymmetry object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## ShapePointSymmetry(...)



This method creates a ShapePointSymmetry object.



### Path

```
          mdb.models[name].optimizationTasks[name].ShapePointSymmetry
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the symmetry point represented as the origin of a local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

- *mainPointDetermination*

  A SymbolicConstant specifying the rule for determining the main node. Possible values are MAXIMUM and MINIMUM. The default value is MAXIMUM.

- *presumeFeasibleRegionAtStart*

  A Boolean specifying whether to ignore the geometric restriction in the first design cycle. The default value is ON.

- *tolerance1*

  A Float specifying the geometric tolerance in the 1-direction. The default value is 0.01.

- *tolerance2*

  A Float specifying the geometric tolerance in the 2-direction. The default value is 0.01.

- *tolerance3*

  A Float specifying the geometric tolerance in the 3-direction. The default value is 0.01.

### Return value

A ShapePointSymmetry object.

### Exceptions

None.



## setValues(...)



This method modifies the ShapePointSymmetry object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ShapePointSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapepointsymmetrypyc.htm?ContextScope=all#simaker-shapepointsymmetryshapepointsymmetrypyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The ShapePointSymmetry object has members with the same names and descriptions as the arguments to the [ShapePointSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapepointsymmetrypyc.htm?ContextScope=all#simaker-shapepointsymmetryshapepointsymmetrypyc) method.