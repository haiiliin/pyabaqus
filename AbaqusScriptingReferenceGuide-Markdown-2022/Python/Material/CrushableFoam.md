# CrushableFoam object

The CrushableFoam object specifies the crushable foam plasticity model.

## Access

```
import material
mdb.models[name].materials[name].crushableFoam
import odbMaterial
session.odbs[name].materials[name].crushableFoam
```

## CrushableFoam(...)



This method creates a CrushableFoam object.



### Path

```
mdb.models[name].materials[name].CrushableFoam
session.odbs[name].materials[name].CrushableFoam
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *hardening*

  A SymbolicConstant specifying the type of hardening/softening definition. Possible values are VOLUMETRIC and ISOTROPIC. The default value is VOLUMETRIC.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *hardening*=VOLUMETRIC, the table data specify the following:

- Ratio, k, of initial yield stress in uniaxial compression, σc0, to initial yield stress in hydrostatic compression, p0cpc0; 0.0 <k< 3.0.
- Ratio, kt, of yield stress in hydrostatic tension, pt, to initial yield stress in hydrostatic compression, pc0. The default value is 1.0.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *hardening*=ISOTROPIC, the table data specify the following:

- Ratio, k, of initial yield stress in uniaxial compression, σ0cσc0, to initial yield stress in hydrostatic compression, p00; 0.0 ≤k≤ 3.0.
- Plastic Poisson's ratio.νpνp; -1≤νp≤0.5.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CrushableFoam object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the CrushableFoam object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CrushableFoam ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-crushablefoampyc.htm?ContextScope=all#simaker-crushablefoamcrushablefoampyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The CrushableFoam object has members with the same names and descriptions as the arguments to the [CrushableFoam ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-crushablefoampyc.htm?ContextScope=all#simaker-crushablefoamcrushablefoampyc)method.

In addition, the CrushableFoam object can have the following members:

- *crushableFoamHardening*

  A [CrushableFoamHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-crushablefoamhardeningpyc.htm?ContextScope=all) object.

- *rateDependent*

  A [RateDependent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ratedependentpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [CRUSHABLE FOAM](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-crushablefoam.htm?ContextScope=all#simakey-r-crushablefoam)