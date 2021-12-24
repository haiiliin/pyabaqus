# CompositeLayup object

The CompositeLayup object is used to specify a composite layup on a part.

## Access

```
import part
mdb.models[name].parts[name].compositeLayups[i]
```

## CompositeLayup(...)



This method creates a CompositeLayup object.



### Path

mdb.models[*name*].parts[*name*].CompositeLayup

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *description*

  A String specifying a description of the composite layup.

- *offsetType*

  A SymbolicConstant specifying the method used to define the shell offset. If *offsetType*=OFFSET_FIELD the *offsetField* argument is required. This member is valid only if *elementType*=SHELL. Possible values are SINGLE_VALUE, MIDDLE_SURFACE, TOP_SURFACE, BOTTOM_SURFACE, OFFSET_FIELD, and GLOBAL. The default value is GLOBAL.

- *offsetField*

  A String specifying The name of the field specifying the offset. This member is valid only if *elementType*=SHELL. The default value is an empty string.

- *offsetValues*

  A Float specifying The offset of the shell section. This member is valid only if *elementType*=SHELL. The default value is 0.0.

- *elementType*

  A SymbolicConstant specifying the type of element in the composite layup. Possible values are SHELL, CONTINUUM_SHELL, and SOLID. The default value is SHELL.

- *symmetric*

  A Boolean specifying whether or not the layup should be made symmetric by the analysis. The default value is OFF.

### Return value

A CompositeLayup object.

### Exceptions

AbaqusException.



## suppress()



This method suppresses a composite layup.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## resume()



This method resumes a composite layup that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## deletePlies()



This method deletes all of the plies from a composite layup.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the CompositeLayup object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CompositeLayup ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositelayuppyc.htm?ContextScope=all#simaker-compositelayupcompositelayuppyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The CompositeLayup object has members with the same names and descriptions as the arguments to the [CompositeLayup ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositelayuppyc.htm?ContextScope=all#simaker-compositelayupcompositelayuppyc)method.

In addition, the CompositeLayup object has the following members:

- *section*

  A [GeometryShellSection](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometryshellsectionpyc.htm?ContextScope=all) object.

- *orientation*

  A [MaterialOrientation](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialorientationpyc.htm?ContextScope=all) object.

- *plies*

  A [CompositePlyArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositeplypyc.htm?ContextScope=all) object specifying the plies that make up this composite layup.



## Corresponding analysis keywords

- [SHELL SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shellsection.htm?ContextScope=all#simakey-r-shellsection)
- [SHELL GENERAL SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shellgeneralsection.htm?ContextScope=all#simakey-r-shellgeneralsection)
- [SOLID SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-solidsection.htm?ContextScope=all#simakey-r-solidsection)