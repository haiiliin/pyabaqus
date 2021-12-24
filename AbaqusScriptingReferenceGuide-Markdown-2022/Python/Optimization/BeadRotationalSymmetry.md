# BeadRotationalSymmetry object

The BeadRotationalSymmetry object defines a bead rotational symmetry geometric restriction.

The BeadRotationalSymmetry object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## BeadRotationalSymmetry(...)



This method creates a BeadRotationalSymmetry object.



### Path

```
          mdb.models[name].optimizationTasks[name].BeadRotationalSymmetry
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *angle*

  A Float specifying the repeating segment size, an angle in degrees.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

- *axis*

  A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

### Return value

A BeadRotationalSymmetry object.

### Exceptions

None.



## setValues(...)



This method modifies the BeadRotationalSymmetry object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BeadRotationalSymmetry ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadrotationalsymmetrypyc.htm?ContextScope=all#simaker-beadrotationalsymmetrybeadrotationalsymmetrpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The BeadRotationalSymmetry object has members with the same names and descriptions as the arguments to the [BeadRotationalSymmetry ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadrotationalsymmetrypyc.htm?ContextScope=all#simaker-beadrotationalsymmetrybeadrotationalsymmetrpyc)method.