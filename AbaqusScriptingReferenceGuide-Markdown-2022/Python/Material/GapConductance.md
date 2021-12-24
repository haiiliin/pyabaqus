# GapConductance object

The GapConductance object specifies conductive heat transfer between closely adjacent (or contacting) surfaces.

## Access

```
import material
mdb.models[name].materials[name].gapConductance
import odbMaterial
session.odbs[name].materials[name].gapConductance
```

## GapConductance(...)



This method creates a GapConductance object.



### Path

```
mdb.models[name].materials[name].GapConductance
session.odbs[name].materials[name].GapConductance
```

### Optional arguments

- *pressureDependency*

  A Boolean specifying whether the data depend on pressure. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Table data

- Gap Conductance or Cohesive Separation.
- Gap Clearance, Gap Pressure (if optional parameter pressureDependency is used), or Closure, c (for coupled temperature-displacement gasket elements).
- Average Temperature if the data depend on temperature.
- Mass Flow Rate per unit area if the data depend on the average mass flow rate.
- Value of the first field variable if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A GapConductance object.



## setValues(...)



This method modifies the GapConductance object.



### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GapConductance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapconductancepyc.htm?ContextScope=all#simaker-gapconductancegapconductancepyc) method.



## Members

The GapConductance object has members with the same names and descriptions as the arguments to the [GapConductance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapconductancepyc.htm?ContextScope=all#simaker-gapconductancegapconductancepyc) method.



## Corresponding analysis keywords

- [GAP CONDUCTANCE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gapconductance.htm?ContextScope=all#simakey-r-gapconductance)