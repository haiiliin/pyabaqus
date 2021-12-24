# ShapeRotationalSymmetry object

The ShapeRotationalSymmetry object defines a shape rotational symmetry geometric restriction.

The ShapeRotationalSymmetry object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## ShapeRotationalSymmetry(...)



This method creates a ShapeRotationalSymmetry object.



### Path

```
          mdb.models[name].optimizationTasks[name].ShapeRotationalSymmetry
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *clientDirection*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object of length 2 specifying the vector positioned at the *csys* origin, used as the axis of symmetry. Instead of through a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), each point might be specified through a tuple of coordinates.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied. When used with a [TopologyTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?ContextScope=all), there is no default value. When used with a [ShapeTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?ContextScope=all), the default value is MODEL.

### Optional arguments

- *allowNonSymmetricMesh*

  A Boolean specifying whether to allow a nonsymmetric mesh for this geometric restriction. The default value is TRUE.

- *angle*

  A Float specifying the segment size of the repeating pattern in degrees. If the *angle* value is 0, no repeating pattern is created. The default value is 0.0.

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

- *mainPoint*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the main point used when *mainPointDetermination* is SPECIFY. The default value is None.

- *mainPointDetermination*

  A SymbolicConstant specifying the rule for determining the main node. Possible values are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

- *presumeFeasibleRegionAtStart*

  A Boolean specifying whether to ignore the geometric restriction in the first design cycle. The default value is ON.

- *startPoint*

  A tuple of Floats representing the coordinates of a start point of the rotational symmetry.

- *tolerance1*

  A Float specifying the geometric tolerance in the 1-direction. The default value is 0.01.

- *tolerance2*

  A Float specifying the geometric tolerance in the 2-direction. The default value is 0.01.

- *tolerance3*

  A Float specifying the geometric tolerance in the 3-direction. The default value is 0.01.

### Return value

A ShapeRotationalSymmetry object.

### Exceptions

None.



## setValues(...)



This method modifies the ShapeRotationalSymmetry object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ShapeRotationalSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shaperotationalsymmetrypyc.htm?ContextScope=all#simaker-shaperotationalsymmetryshaperotationalsymmetrypyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The ShapeRotationalSymmetry object has members with the same names and descriptions as the arguments to the [ShapeRotationalSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shaperotationalsymmetrypyc.htm?ContextScope=all#simaker-shaperotationalsymmetryshaperotationalsymmetrypyc) method.