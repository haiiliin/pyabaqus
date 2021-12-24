# Material object

A Material object is the object used to specify a material. The Material object stores the various settings that determine how a material behaves.

A material is created by combining one or more individual material options and sub options. A particular material option is associated with the Material object through a member. For example: the *acousticMedium* member may contain an AcousticMedium object. The alternative of having a MaterialOption abstract base class and a container of MaterialOptions was rejected because it would make it more difficult to enforce the fact that one Material object cannot contain two AcousticMedium objects, for example.

## Access

```
import material
mdb.models[name].materials[name]
import odbMaterial
session.odbs[name].materials[name]
```

## Material(...)



This method creates a Material object.



### Path

```
mdb.models[name].Material
session.odbs[name].Material
```

### Required arguments

- *name*

  A String specifying the name of the new material.

### Optional arguments

- *description*

  A String specifying user description of the material. The default value is an empty string.

- *materialIdentifier*

  A String specifying material identifier for customer use. The default value is an empty string.

### Return value

A Material object.

### Exceptions

InvalidNameError.



## materialsFromOdb(...)



This methods creates Material objects by reading an output database. The new materials are placed in the materials repository.



### Path

mdb.models[*name*].materialsFromOdb

### Required arguments

- *fileName*

  A String specifying the name of the output database file (including the .odb extension) to be read. This String can also be the full path to the output database file if it is located in another directory.

### Optional arguments

None.

### Return value

A list of Material objects.

### Exceptions

None.



## Members

The Material object has members with the same names and descriptions as the arguments to the [Material ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialpyc.htm?ContextScope=all#simaker-materialmaterialpyc)method.

In addition, the Material object can have the following members:

- *acousticMedium*

  An [AcousticMedium](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticmediumpyc.htm?ContextScope=all) object.

- *brittleCracking*

  A [BrittleCracking](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-brittlecrackingpyc.htm?ContextScope=all) object.

- *capPlasticity*

  A [CapPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-capplasticitypyc.htm?ContextScope=all) object.

- *castIronPlasticity*

  A [CastIronPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-castironplasticitypyc.htm?ContextScope=all) object.

- *clayPlasticity*

  A [ClayPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-clayplasticitypyc.htm?ContextScope=all) object.

- *concrete*

  A [Concrete](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretepyc.htm?ContextScope=all) object.

- *concreteDamagedPlasticity*

  A [ConcreteDamagedPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretedamagedplasticitypyc.htm?ContextScope=all) object.

- *conductivity*

  A [Conductivity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conductivitypyc.htm?ContextScope=all) object.

- *creep*

  A [Creep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-creeppyc.htm?ContextScope=all) object.

- *crushableFoam*

  A [CrushableFoam](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-crushablefoampyc.htm?ContextScope=all) object.

- *ductileDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *fldDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *flsdDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *johnsonCookDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *maxeDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *maxsDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *maxpeDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *maxpsDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *mkDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *msfldDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *quadeDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *quadsDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *shearDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *hashinDamageInitiation*

  A [DamageInitiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all) object.

- *damping*

  A [Damping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dampingpyc.htm?ContextScope=all) object.

- *deformationPlasticity*

  A [DeformationPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-deformationplasticitypyc.htm?ContextScope=all) object.

- *density*

  A [Density](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-densitypyc.htm?ContextScope=all) object.

- *depvar*

  A [Depvar](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-depvarpyc.htm?ContextScope=all) object.

- *dielectric*

  A [Dielectric](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dielectricpyc.htm?ContextScope=all) object.

- *diffusivity*

  A [Diffusivity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diffusivitypyc.htm?ContextScope=all) object.

- *druckerPrager*

  A [DruckerPrager](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-druckerpragerpyc.htm?ContextScope=all) object.

- *elastic*

  An [Elastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticpyc.htm?ContextScope=all) object.

- *electricalConductivity*

  An [ElectricalConductivity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-electricalconductivitypyc.htm?ContextScope=all) object.

- *eos*

  An [Eos](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eospyc.htm?ContextScope=all) object.

- *expansion*

  An [Expansion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expansionpyc.htm?ContextScope=all) object.

- *fluidLeakoff*

  A [FluidLeakoff](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidleakoffpyc.htm?ContextScope=all) object.

- *gapFlow*

  A [GapFlow](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapflowpyc.htm?ContextScope=all) object.

- *gasketThicknessBehavior*

  A [GasketThicknessBehavior](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gasketthicknessbehaviorpyc.htm?ContextScope=all) object.

- *gasketTransverseShearElastic*

  A [GasketTransverseShearElastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gaskettransverseshearelasticpyc.htm?ContextScope=all) object.

- *gasketMembraneElastic*

  A [GasketMembraneElastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gasketmembraneelasticpyc.htm?ContextScope=all) object.

- *gel*

  A [Gel](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gelpyc.htm?ContextScope=all) object.

- *heatGeneration*

  A [HeatGeneration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-heatgenerationpyc.htm?ContextScope=all) object.

- *hyperelastic*

  A [Hyperelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hyperelasticpyc.htm?ContextScope=all) object.

- *hyperfoam*

  A [Hyperfoam](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hyperfoampyc.htm?ContextScope=all) object.

- *hypoelastic*

  A [Hypoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hypoelasticpyc.htm?ContextScope=all) object.

- *inelasticHeatFraction*

  An [InelasticHeatFraction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inelasticheatfractionpyc.htm?ContextScope=all) object.

- *jouleHeatFraction*

  A [JouleHeatFraction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jouleheatfractionpyc.htm?ContextScope=all) object.

- *latentHeat*

  A [LatentHeat](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-latentheatpyc.htm?ContextScope=all) object.

- *lowDensityFoam*

  A [LowDensityFoam](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lowdensityfoampyc.htm?ContextScope=all) object.

- *magneticPermeability*

  A [MagneticPermeability](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-magneticpermeabilitypyc.htm?ContextScope=all) object.

- *mohrCoulombPlasticity*

  A [MohrCoulombPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mohrcoulombplasticitypyc.htm?ContextScope=all) object.

- *moistureSwelling*

  A [MoistureSwelling](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-moistureswellingpyc.htm?ContextScope=all) object.

- *mullinsEffect*

  A [MullinsEffect](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mullinseffectpyc.htm?ContextScope=all) object.

- *permeability*

  A [Permeability](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-permeabilitypyc.htm?ContextScope=all) object.

- *piezoelectric*

  A [Piezoelectric](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-piezoelectricpyc.htm?ContextScope=all) object.

- *plastic*

  A [Plastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-plasticpyc.htm?ContextScope=all) object.

- *poreFluidExpansion*

  A [PoreFluidExpansion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porefluidexpansionpyc.htm?ContextScope=all) object.

- *porousBulkModuli*

  A [PorousBulkModuli](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousbulkmodulipyc.htm?ContextScope=all) object.

- *porousElastic*

  A [PorousElastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porouselasticpyc.htm?ContextScope=all) object.

- *porousMetalPlasticity*

  A [PorousMetalPlasticity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousmetalplasticitypyc.htm?ContextScope=all) object.

- *regularization*

  A [Regularization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regularizationpyc.htm?ContextScope=all) object.

- *solubility*

  A [Solubility](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solubilitypyc.htm?ContextScope=all) object.

- *sorption*

  A [Sorption](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sorptionpyc.htm?ContextScope=all) object.

- *specificHeat*

  A [SpecificHeat](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-specificheatpyc.htm?ContextScope=all) object.

- *swelling*

  A [Swelling](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-swellingpyc.htm?ContextScope=all) object.

- *userDefinedField*

  A [UserDefinedField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-userdefinedfieldpyc.htm?ContextScope=all) object.

- *userMaterial*

  A [UserMaterial](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-usermaterialpyc.htm?ContextScope=all) object.

- *userOutputVariables*

  A [UserOutputVariables](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-useroutputvariablespyc.htm?ContextScope=all) object.

- *viscoelastic*

  A [Viscoelastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscoelasticpyc.htm?ContextScope=all) object.

- *viscosity*

  A [Viscosity](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscositypyc.htm?ContextScope=all) object.

- *viscous*

  A [Viscous](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viscouspyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [MATERIAL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-material.htm?ContextScope=all#simakey-r-material)