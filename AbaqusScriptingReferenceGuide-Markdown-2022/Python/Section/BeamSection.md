# BeamSection object

The BeamSection object defines the properties of a beam section.

The BeamSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## BeamSection(...)



This method creates a BeamSection object.



### Path

```
mdb.models[name].BeamSection
session.odbs[name].BeamSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *integration*

  A SymbolicConstant specifying the integration method for the section. Possible values are BEFORE_ANALYSIS and DURING_ANALYSIS.

- *profile*

  A String specifying the name of the profile. This argument represents the start profile in case of *beamShape*=TAPERED.

### Optional arguments

- *poissonRatio*

  A Float specifying the Poisson's ratio of the section. The default value is 0.0.

- *thermalExpansion*

  A Boolean specifying whether to use thermal expansion data. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *density*

  None or a Float specifying the density of the section. The default value is None.

- *referenceTemperature*

  None or a Float specifying the reference temperature of the section. The default value is None.

- *temperatureVar*

  A SymbolicConstant specifying the temperature variation for the section. Possible values are LINEAR and INTERPOLATED. The default value is LINEAR.

- *alphaDamping*

  A Float specifying the αRαR factor to create mass proportional damping in direct-integration dynamics. The default value is 0.0.

- *betaDamping*

  A Float specifying the βRβR factor to create stiffness proportional damping in direct-integration dynamics. The default value is 0.0.

- *compositeDamping*

  A Float specifying the fraction of critical damping to be used in calculating composite damping factors for the modes (for use in modal dynamics). The default value is 0.0.

- *useFluidInertia*

  A Boolean specifying whether added mass effects will be simulated. The default value is OFF.

- *submerged*

  A SymbolicConstant specifying whether the section is either full submerged or half submerged. This argument applies only when *useFluidInertia* = True. Possible values are FULLY and HALF. The default value is FULLY.

- *fluidMassDensity*

  None or a Float specifying the mass density of the fluid. This argument applies only when *useFluidInertia* = True and must be specified in that case. The default value is None.

- *crossSectionRadius*

  None or a Float specifying the radius of the cylindrical cross-section. This argument applies only when *useFluidInertia* = True and must be specified in that case. The default value is None.

- *lateralMassCoef*

  A Float specifying the added mass coefficient, CACA, for lateral motions of the beam. This argument applies only when*useFluidInertia* = True. The default value is 1.0.

- *axialMassCoef*

  A Float specifying the added mass coefficient, C(A−E)C(A-E), for motions along the axis of the beam. This argument affects only the term added to the free end(s) of the beam, and applies only when *useFluidInertia* = True. The default value is 0.0.

- *massOffsetX*

  A Float specifying the local 1-coordinate of the center of the cylindrical cross-section with respect to the beam cross-section. This argument applies only when *useFluidInertia* = True. The default value is 0.0.

- *massOffsetY*

  A Float specifying the local 2-coordinate of the center of the cylindrical cross-section with respect to the beam cross-section. This argument applies only when *useFluidInertia* = True. The default value is 0.0.

- *beamShape*

  A SymbolicConstant specifying the change in cross-section of the beam along length. Possible values are CONSTANT and TAPERED. The default value is CONSTANT. This parameter is available for manipulating the model database but not for the ODB API.

- *material*

  A String specifying the name of the material. The default value is an empty string. The material is required when *integration* is "DURING_ANALYSIS".

- *table*

  A sequence of sequences of Floats specifying the items described below. The default value is an empty sequence.

- *outputPts*

  A sequence of pairs of Floats specifying the positions at which output is requested. The default value is an empty sequence.

- *centroid*

  A pair of Floats specifying the *X–Y* coordinates of the centroid. The default value is (0.0, 0.0).

- *shearCenter*

  A pair of Floats specifying the *X–Y* coordinates of the shear center. The default value is (0.0, 0.0).

- *profileEnd*

  A String specifying the name of the end profile. The type of the end profile must be same as that of the start profile. This argument is valid only when *beamShape*=TAPERED. The default value is an empty string. This parameter is available for manipulating the model database but not for the ODB API.

### Table data

The table data specify the following:

- E, the Young's modulus of the section.
- G, the torsional shear modulus of the section.
- Thermal expansion coefficient, if using thermal expansion.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A BeamSection object.

### Exceptions

None.



## setValues(...)



This method modifies the BeamSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [BeamSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beamsectionpyc.htm?ContextScope=all#simaker-beamsectionbeamsectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The BeamSection object has members with the same names and descriptions as the arguments to the [BeamSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beamsectionpyc.htm?ContextScope=all#simaker-beamsectionbeamsectionpyc)method.

In addition, the BeamSection object can have the following member:

- *beamTransverseShear*

  A [TransverseShearBeam](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-transverseshearbeampyc.htm?ContextScope=all) object specifying the transverse shear stiffness properties.



## Corresponding analysis keywords

- [BEAM GENERAL SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamgeneralsection.htm?ContextScope=all#simakey-r-beamgeneralsection)
- [BEAM SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamsection.htm?ContextScope=all#simakey-r-beamsection)
- [BEAM FLUID INERTIA](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamfluidinertia.htm?ContextScope=all#simakey-r-beamfluidinertia)
- [CENTROID](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-centroid.htm?ContextScope=all#simakey-r-centroid)
- [DAMPING](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damping.htm?ContextScope=all#simakey-r-damping)
- [SHEAR CENTER](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shearcenter.htm?ContextScope=all#simakey-r-shearcenter)
- [SECTION POINTS](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-sectionpoints.htm?ContextScope=all#simakey-r-sectionpoints)