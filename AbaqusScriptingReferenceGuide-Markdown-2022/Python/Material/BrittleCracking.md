# BrittleCracking object

The BrittleCracking object specifies cracking and postcracking properties for the brittle cracking material model.

## Access

```
import material
mdb.models[name].materials[name].brittleCracking
import odbMaterial
session.odbs[name].materials[name].brittleCracking
```

## BrittleCracking(...)



This method creates a BrittleCracking object.



### Path

```
mdb.models[name].materials[name].BrittleCracking
session.odbs[name].materials[name].BrittleCracking
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *type*

  A SymbolicConstant specifying the type of postcracking behavior. Possible values are STRAIN, DISPLACEMENT, and GFI. The default value is STRAIN.

### Table data

If *type*=STRAIN the table data specify the following:

- Remaining direct stress after cracking.
- Direct cracking strain.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT the table data specify the following:

- Remaining direct stress after cracking.
- Direct cracking displacement.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=GFI the table data specify the following:

- Failure stress.
- Mode I fracture energy.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A BrittleCracking object.

### Exceptions

None.



## setValues(...)



This method modifies the BrittleCracking object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BrittleCracking ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-brittlecrackingpyc.htm?ContextScope=all#simaker-brittlecrackingbrittlecrackingpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The BrittleCracking object has members with the same names and descriptions as the arguments to the [BrittleCracking ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-brittlecrackingpyc.htm?ContextScope=all#simaker-brittlecrackingbrittlecrackingpyc)method.

In addition, the BrittleCracking object can have the following members:

- *brittleShear*

  A [BrittleShear](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-brittleshearpyc.htm?ContextScope=all) object.

- *brittleFailure*

  A [BrittleFailure](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-brittlefailurepyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [BRITTLE CRACKING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-brittlecracking.htm?ContextScope=all#simakey-r-brittlecracking)