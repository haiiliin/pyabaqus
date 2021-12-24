# Stress object

The Stress object stores the data for an initial stress predefined field.

The Stress object is derived from the [PredefinedField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].predefinedFields[name]
```

## Stress(...)



This method creates a Stress predefined field object.



### Path

```
mdb.models[name].Stress
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the predefined field is applied. Region is ignored if the predefined field has *distributionType*=FROM_FILE.

### Optional arguments

- *distributionType*

  A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM and FROM_FILE. The default value is UNIFORM.

- *sigma11*

  A Float specifying the first principal component of the stress.

- *sigma22*

  A Float specifying the second principal component of the stress.

- *sigma33*

  A Float specifying the third principal component of the stress.

- *sigma12*

  A Float specifying the first shear component of the stress.

- *sigma13*

  A Float specifying the second shear component of the stress.

- *sigma23*

  A Float specifying the third shear component of the stress.

### Return value

A Stress object.

### Exceptions

None.



## setValues(...)



This method modifies the Stress object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Stress](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stresspyc.htm?ContextScope=all#simaker-stressstresspyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The Stress object has members with the same names and descriptions as the arguments to the [Stress](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stresspyc.htm?ContextScope=all#simaker-stressstresspyc) method.



## Corresponding analysis keywords

- [INITIAL CONDITIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-initialconditions.htm?ContextScope=all#simakey-r-initialconditions), TYPE=STRESS