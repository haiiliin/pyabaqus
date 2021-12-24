# SizingFrozenArea object

The SizingFrozenArea object defines a sizing frozen area geometric restriction.

The SizingFrozenArea object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## SizingFrozenArea (...)



This method creates a SizingFrozenArea object.



### Path

```
          mdb.models[name].optimizationTasks[name].SizingFrozenArea
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

### Optional arguments

None.

### Return value

A SizingFrozenArea object.

### Exceptions

None.



## setValues(...)



This method modifies the SizingFrozenArea object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SizingFrozenArea ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingfrozenareapyc.htm?ContextScope=all#simaker-sizingfrozenareasizingfrozenareapyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The SizingFrozenArea object has members with the same names and descriptions as the arguments to the [SizingFrozenArea ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingfrozenareapyc.htm?ContextScope=all#simaker-sizingfrozenareasizingfrozenareapyc)method.