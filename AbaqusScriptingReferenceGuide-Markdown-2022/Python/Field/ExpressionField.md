# ExpressionField object

The ExpressionField object defines a spatially varying field whose value is calculated from a user-supplied mathematical expression.

The ExpressionField object is derived from the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object.

## Access

```
import fields
mdb.models[name].analyticalFields[name]
```

## ExpressionField(...)



This method creates an ExpressionField object.



### Path

```
mdb.models[name].ExpressionField
```

### Required arguments

- *name*

  A String specifying the repository key.

- *expression*

  A String specifying the Python expression to evaluate in space. Variables are X, Y, and Z; R, Th, and Z; or R, Th, and P based on the selected coordinate system.

### Optional arguments

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the field. If *localCsys*=None, the field is defined in the global coordinate system. The default value is None.

- *description*

  A String specifying the description of the field. The default value is an empty string.

### Return value

An ExpressionField object.

### Exceptions

TextException.



## setValues(...)



This method modifies the ExpressionField object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ExpressionField ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expressionfieldpyc.htm?ContextScope=all#simaker-expressionfieldexpressionfieldpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The ExpressionField object has members with the same names and descriptions as the arguments to the [ExpressionField ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expressionfieldpyc.htm?ContextScope=all#simaker-expressionfieldexpressionfieldpyc)method.