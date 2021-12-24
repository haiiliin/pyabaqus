# DruckerPrager object

The DruckerPrager object specifies the extended Drucker-Prager plasticity model.

## Access

```
import material
mdb.models[name].materials[name].druckerPrager
import odbMaterial
session.odbs[name].materials[name].druckerPrager
```

## DruckerPrager(...)



This method creates a DruckerPrager object.



### Path

```
mdb.models[name].materials[name].DruckerPrager
session.odbs[name].materials[name].DruckerPrager
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *shearCriterion*

  A SymbolicConstant specifying the yield criterion. Possible values are LINEAR, HYPERBOLIC, and EXPONENTIAL. The default value is LINEAR.This argument applies only to Abaqus/Standard analyses. Only the linear Drucker-Prager model is available in Abaqus/Explicit analyses.

- *eccentricity*

  A Float specifying the flow potential eccentricity, ϵϵ, a small positive number that defines the rate at which the hyperbolic flow potential approaches its asymptote. The default value is 0.1.This argument applies only to Abaqus/Standard analyses.

- *testData*

  A Boolean specifying whether the material constants for the exponent model are to be computed by Abaqus/Standard from triaxial test data at different levels of confining pressure. The default value is OFF.This argument is valid only if *shearCriterion*=EXPONENTIAL.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *shearCriterion*=LINEAR (the only option allowed in an Abaqus/Explicit analysis), the table data specify the following:

- Material angle of friction, β, in the p–t plane. Give the value in degrees.
- KK, the ratio of the flow stress in triaxial tension to the flow stress in triaxial compression. 0.778≤K≤1.0. If the default value of 0.0 is accepted, a value of 1.0 is assumed.
- Dilation angle, ψ, in the p–t plane. Give the value in degrees.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *shearCriterion*=HYPERBOLIC, the table data specify the following:

- Material angle of friction, β, at high confining pressure in the p–q plane. Give the value in degrees.
- Initial hydrostatic tension strength, pt|0.
- Dilation angle, ψ, at high confining pressure in the p–q plane. Give the value in degrees.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *shearCriterion*=EXPONENTIAL, the table data specify the following:

- Dilation angle, ψ, at high confining pressure in the p–q plane. Give the value in degrees.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A DruckerPrager object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the DruckerPrager object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DruckerPrager ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragerpyc.htm?ContextScope=all#simaker-druckerpragerdruckerpragerpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The DruckerPrager object has members with the same names and descriptions as the arguments to the [DruckerPrager ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragerpyc.htm?ContextScope=all#simaker-druckerpragerdruckerpragerpyc)method.

In addition, the DruckerPrager object can have the following members:

- *druckerPragerCreep*

  A [DruckerPragerCreep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragercreeppyc.htm?ContextScope=all) object.

- *druckerPragerHardening*

  A [DruckerPragerHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragerhardeningpyc.htm?ContextScope=all) object.

- *rateDependent*

  A [RateDependent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ratedependentpyc.htm?ContextScope=all) object.

- *triaxialTestData*

  A [TriaxialTestData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-triaxialtestdatapyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [DRUCKER PRAGER](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-druckerprager.htm?ContextScope=all#simakey-r-druckerprager)