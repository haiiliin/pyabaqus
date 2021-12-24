# BeadPointSymmetry object

The BeadPointSymmetry object defines a point symmetry geometric restriction.

The BeadPointSymmetry object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## BeadPointSymmetry(...)



This method creates a BeadPointSymmetry object.



### Path

```
          mdb.models[name].optimizationTasks[name].BeadPointSymmetry
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

- *csys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the position of the symmetry point defined as the origin of a local coordinate system. If *csys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

### Return value

A BeadPointSymmetry object.

### Exceptions

None.



## setValues(...)



This method modifies the BeadPointSymmetry object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BeadPointSymmetry ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpointsymmetrypyc.htm?ContextScope=all#simaker-beadpointsymmetrybeadpointsymmetrypyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The BeadPointSymmetry object has members with the same names and descriptions as the arguments to the [BeadPointSymmetry ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpointsymmetrypyc.htm?ContextScope=all#simaker-beadpointsymmetrybeadpointsymmetrypyc)method.