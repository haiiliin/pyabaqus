# FailStrain object

The FailStrain object defines parameters for strain-based failure measures.

## Access

```
import material
mdb.models[name].materials[name].elastic.failStrain
import odbMaterial
session.odbs[name].materials[name].elastic.failStrain
```

## FailStrain(...)



This method creates a FailStrain object.



### Path

```
mdb.models[name].materials[name].elastic.FailStrain
session.odbs[name].materials[name].elastic.FailStrain
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- Tensile strain limit in fiber direction, Xεt.
- Compressive strain limit in fiber direction, Xεc.
- Tensile strain limit in transverse direction, Yεt.
- Compressive strain limit in transverse direction, Yεc.
- Shear strain limit in the X–Y plane, Sε.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A FailStrain object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the FailStrain object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FailStrain ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failstrainpyc.htm?ContextScope=all#simaker-failstrainfailstrainpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The FailStrain object has members with the same names and descriptions as the arguments to the [FailStrain ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failstrainpyc.htm?ContextScope=all#simaker-failstrainfailstrainpyc)method.



## Corresponding analysis keywords

- [FAIL STRAIN](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-failstrain.htm?ContextScope=all#simakey-r-failstrain)