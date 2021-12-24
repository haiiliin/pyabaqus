# CapPlasticity object

The CapPlasticity object specifies the modified Drucker-Prager/Cap plasticity model.

## Access

```
import material
mdb.models[name].materials[name].capPlasticity
import odbMaterial
session.odbs[name].materials[name].capPlasticity
```

## CapPlasticity(...)



This method creates a CapPlasticity object.



### Path

```
mdb.models[name].materials[name].CapPlasticity
session.odbs[name].materials[name].CapPlasticity
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

- Material cohesion, d, in the p–t plane (Abaqus/Standard) or in the p–q plane (Abaqus/Explicit).
- Material angle of friction, β, in the p–t plane (Abaqus/Standard) or in the p–q plane (Abaqus/Explicit). Give the value in degrees.
- Cap eccentricity parameter, RR. Its value must be greater than zero (typically 0.0 <R< 1.0).
- Initial cap yield surface position, ε_vol^pl|0.
- Transition surface radius parameter, αα. The default value is 0.0 (i.e., no transition surface).
- (Not used in Abaqus/Explicit) K, the ratio of the flow stress in triaxial tension to the flow stress in triaxial compression. Possible values are 0.778 ≤K≤ 1.0. If the default value of 0.0 is accepted, Abaqus/Standard assumes K= 1.0.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CapPlasticity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the CapPlasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CapPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capplasticitypyc.htm?ContextScope=all#simaker-capplasticitycapplasticitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The CapPlasticity object has members with the same names and descriptions as the arguments to the [CapPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capplasticitypyc.htm?ContextScope=all#simaker-capplasticitycapplasticitypyc)method.

In addition, the CapPlasticity object can have the following members:

- *capCreepCohesion*

  A [CapCreepCohesion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capcreepcohesionpyc.htm?ContextScope=all) object.

- *capCreepConsolidation*

  A [CapCreepConsolidation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capcreepconsolidationpyc.htm?ContextScope=all) object.

- *capHardening*

  A [CapHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-caphardeningpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [CAP PLASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-capplasticity.htm?ContextScope=all#simakey-r-capplasticity)