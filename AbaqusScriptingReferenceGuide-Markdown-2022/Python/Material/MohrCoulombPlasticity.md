# MohrCoulombPlasticity object

The MohrCoulombPlasticity object specifies the extended Mohr-Coulomb plasticity model.

## Access

```
import material
mdb.models[name].materials[name].mohrCoulombPlasticity
import odbMaterial
session.odbs[name].materials[name].mohrCoulombPlasticity
```

## MohrCoulombPlasticity(...)



This method creates a MohrCoulombPlasticity object.



### Path

```
mdb.models[name].materials[name].MohrCoulombPlasticity
session.odbs[name].materials[name].MohrCoulombPlasticity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *deviatoricEccentricity*

  None or a Float specifying the flow potential eccentricity in the deviatoric plane, e; 1/2 ≤ 1.0. If *deviatoricEccentricity*=None, Abaqus calculates the value using the specified Mohr-Coulomb angle of friction. The default value is None.

- *meridionalEccentricity*

  A Float specifying the flow potential eccentricity in the meridional plane, ϵϵ. The default value is 0.1.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *useTensionCutoff*

  A Boolean specifying whether tension cutoff specification is needed. The default value is OFF.

### Table data

The table data specify the following:

- Friction angle (given in degrees), ϕ, at high confining pressure in the p–Rm⁢c⁢q plane.
- Dilation angle, ψ, at high confining pressure in the p–Rm⁢w⁢q plane.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A MohrCoulombPlasticity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the MohrCoulombPlasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MohrCoulombPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mohrcoulombplasticitypyc.htm?ContextScope=all#simaker-mohrcoulombplasticitymohrcoulombplasticitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The MohrCoulombPlasticity object has members with the same names and descriptions as the arguments to the [MohrCoulombPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mohrcoulombplasticitypyc.htm?ContextScope=all#simaker-mohrcoulombplasticitymohrcoulombplasticitypyc)method.

In addition, the MohrCoulombPlasticity object can have the following members:

- *mohrCoulombHardening*

  A [MohrCoulombHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mohrcoulombhardeningpyc.htm?ContextScope=all) object.

- *tensionCutOff*

  A [TensionCutOff](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tensioncutoffpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [MOHR COULOMB](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-mohrcoulomb.htm?ContextScope=all#simakey-r-mohrcoulomb)