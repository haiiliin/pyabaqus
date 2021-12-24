# TopologyCyclicSymmetry object

The TopologyCyclicSymmetry object defines a topology cyclic symmetry geometric restriction.

The TopologyCyclicSymmetry object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## TopologyCyclicSymmetry(...)



This method creates a TopologyCyclicSymmetry object.



### Path

```
          mdb.models[name].optimizationTasks[name].TopologyCyclicSymmetry
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

- *translation*

  A Float specifying the translation distance.

### Optional arguments

- *axis*

  A SymbolicConstant specifying the translation direction defined along an axis positioned at the *csys* origin. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

- *ignoreFrozenArea*

  A Boolean specifying whether to ignore frozen areas. The default value is OFF.

### Return value

A TopologyCyclicSymmetry object.

### Exceptions

None.



## setValues(...)



This method modifies the TopologyCyclicSymmetry object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TopologyCyclicSymmetry ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologycyclicsymmetrypyc.htm?ContextScope=all#simaker-topologycyclicsymmetrytopologycyclicsymmetrypyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The TopologyCyclicSymmetry object has members with the same names and descriptions as the arguments to the [TopologyCyclicSymmetry ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologycyclicsymmetrypyc.htm?ContextScope=all#simaker-topologycyclicsymmetrytopologycyclicsymmetrypyc)method.