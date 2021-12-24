# SizingMemberSize object

The SizingMemberSize object defines a sizing member size geometric restriction.

The SizingMemberSize object is derived from the [GeometricRestriction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
      
```

## SizingMemberSize(...)



This method creates a SizingMemberSize object.



### Path

```
          mdb.models[name].optimizationTasks[name].SizingMemberSize
        
```

### Required arguments

- *name*

  A String specifying the geometric restriction repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the geometric restriction is applied.

- *minWidth*

  A Float specifying the min width.



## setValues(...)



This method modifies the sizingMemberSize object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [sizingMemberSize ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingmembersizepyc.htm?ContextScope=all#simaker-sizingmembersizesizingmembersizepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The sizingMemberSize object has members with the same names and descriptions as the arguments to the [sizingMemberSize ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingmembersizepyc.htm?ContextScope=all#simaker-sizingmembersizesizingmembersizepyc)method.