# UserOutputVariables object

The UserOutputVariables object specifies the number of user-defined output variables.

## Access

```
import material
mdb.models[name].materials[name].userOutputVariables
import odbMaterial
session.odbs[name].materials[name].userOutputVariables
```

## UserOutputVariables(...)



This method creates a UserOutputVariables object.



### Path

```
mdb.models[name].materials[name].UserOutputVariables
session.odbs[name].materials[name].UserOutputVariables
```

### Required arguments

None.

### Optional arguments

- *n*

  An Int specifying the number of user-defined variables required at each material point. The default value is 0.

### Return value

A UserOutputVariables object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the UserOutputVariables object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [UserOutputVariables ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-useroutputvariablespyc.htm?ContextScope=all#simaker-useroutputvariablesuseroutputvariablespyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The UserOutputVariables object has members with the same names and descriptions as the arguments to the [UserOutputVariables ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-useroutputvariablespyc.htm?ContextScope=all#simaker-useroutputvariablesuseroutputvariablespyc)method.



## Corresponding analysis keywords

- [USER OUTPUT VARIABLES](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-useroutputvariables.htm?ContextScope=all#simakey-r-useroutputvariables)