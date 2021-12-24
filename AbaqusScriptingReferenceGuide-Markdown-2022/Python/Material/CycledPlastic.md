# CycledPlastic object

The CycledPlastic object specifies cycled yield stress data for the ORNL constitutive model.

## Access

```
import material
mdb.models[name].materials[name].plastic.cycledPlastic
import odbMaterial
session.odbs[name].materials[name].plastic.cycledPlastic
```

## CycledPlastic(...)



This method creates a CycledPlastic object.



### Path

```
mdb.models[name].materials[name].plastic.CycledPlastic
session.odbs[name].materials[name].plastic.CycledPlastic
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

### Table data

- Yield stress.
- Plastic strain.
- Temperature, if the data depend on temperature.

### Return value

A CycledPlastic object.

### Exceptions

None.



## setValues(...)



This method modifies the CycledPlastic object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CycledPlastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cycledplasticpyc.htm?ContextScope=all#simaker-cycledplasticcycledplasticpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The CycledPlastic object has members with the same names and descriptions as the arguments to the [CycledPlastic ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cycledplasticpyc.htm?ContextScope=all#simaker-cycledplasticcycledplasticpyc)method.



## Corresponding analysis keywords

- [CYCLED PLASTIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cycledplastic.htm?ContextScope=all#simakey-r-cycledplastic)