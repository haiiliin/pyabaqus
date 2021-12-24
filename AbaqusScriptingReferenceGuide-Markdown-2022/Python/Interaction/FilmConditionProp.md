# FilmConditionProp object

The FilmConditionProp object is an interaction property that defines a film coefficient as a function of temperature and field variables.

The FilmConditionProp object is derived from the [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactionProperties[name]
```

## FilmConditionProp(...)



This method creates a FilmConditionProp object.



### Path

```
mdb.models[name].FilmConditionProp
```

### Required arguments

- *name*

  A String specifying the interaction property repository key.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *property*

  A sequence of sequences of Floats specifying the following:

  - The film coefficient, hh.
  - Temperature, if the data depend on temperature.
  - Value of the first field variable, if the data depend on field variables.
  - Value of the second field variable.
  - Etc.

### Return value

A FilmConditionProp object.

### Exceptions

None.



## setValues(...)



This method modifies the FilmConditionProp object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FilmConditionProp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionproppyc.htm?ContextScope=all#simaker-filmconditionpropfilmconditionproppyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The FilmConditionProp object has members with the same names and descriptions as the arguments to the [FilmConditionProp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filmconditionproppyc.htm?ContextScope=all#simaker-filmconditionpropfilmconditionproppyc)method.



## Corresponding analysis keywords

- [FILM PROPERTY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-filmproperty.htm?ContextScope=all#simakey-r-filmproperty)