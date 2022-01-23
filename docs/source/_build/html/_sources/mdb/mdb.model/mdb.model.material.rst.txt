========
Material
========

The Material commands are used to define the materials in a model.


Attributes
----------

- **mdb.models[name].materials[name].acousticMedium**: An :py:class:`abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium` object.
- **mdb.models[name].materials[name].brittleCracking**: A :py:class:`abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking` object.
- **mdb.models[name].materials[name].capPlasticity**: A :py:class:`abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity` object.
- **mdb.models[name].materials[name].castIronPlasticity**: A :py:class:`abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity` object.
- **mdb.models[name].materials[name].clayPlasticity**: A :py:class:`abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity` object.
- **mdb.models[name].materials[name].concrete**: A :py:class:`abaqus.Material.Plastic.Concrete.Concrete.Concrete` object.
- **mdb.models[name].materials[name].concreteDamagedPlasticity**: A :py:class:`abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity` object.
- **mdb.models[name].materials[name].conductivity**: A :py:class:`abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity` object.
- **mdb.models[name].materials[name].creep**: A :py:class:`abaqus.Material.Plastic.Creep.Creep.Creep` object.
- **mdb.models[name].materials[name].crushableFoam**: A :py:class:`abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam` object.
- **mdb.models[name].materials[name].ductileDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].fldDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].flsdDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].johnsonCookDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].maxeDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].maxsDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].maxpeDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].maxpsDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].mkDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].msfldDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].quadeDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].quadsDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].shearDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].hashinDamageInitiation**: A :py:class:`abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation` object.
- **mdb.models[name].materials[name].damping**: A :py:class:`abaqus.Material.Others.Mechanical.Damping.Damping` object.
- **mdb.models[name].materials[name].deformationPlasticity**: A :py:class:`abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity` object.
- **mdb.models[name].materials[name].density**: A :py:class:`abaqus.Material.Density.Density.Density` object.
- **mdb.models[name].materials[name].depvar**: A :py:class:`abaqus.Material.Others.User.Depvar.Depvar` object.
- **mdb.models[name].materials[name].dielectric**: A :py:class:`abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric` object.
- **mdb.models[name].materials[name].diffusivity**: A :py:class:`abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity` object.
- **mdb.models[name].materials[name].druckerPrager**: A :py:class:`abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager` object.
- **mdb.models[name].materials[name].elastic**: An :py:class:`abaqus.Material.Elastic.Linear.Elastic.Elastic` object.
- **mdb.models[name].materials[name].electricalConductivity**: An :py:class:`abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity` object.
- **mdb.models[name].materials[name].eos**: An :py:class:`abaqus.Material.Eos.Eos.Eos` object.
- **mdb.models[name].materials[name].expansion**: An :py:class:`abaqus.Material.Others.Mechanical.Expansion.Expansion` object.
- **mdb.models[name].materials[name].fluidLeakoff**: A :py:class:`abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff` object.
- **mdb.models[name].materials[name].gapFlow**: A :py:class:`abaqus.Material.Gap.GapFlow.GapFlow` object.
- **mdb.models[name].materials[name].gasketThicknessBehavior**: A :py:class:`abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior` object.
- **mdb.models[name].materials[name].gasketTransverseShearElastic**: A :py:class:`abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic` object.
- **mdb.models[name].materials[name].gasketMembraneElastic**: A :py:class:`abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic` object.
- **mdb.models[name].materials[name].gel**: A :py:class:`abaqus.Material.Others.PoreFluidFlow.Gel.Gel` object.
- **mdb.models[name].materials[name].heatGeneration**: A :py:class:`abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration` object.
- **mdb.models[name].materials[name].hyperelastic**: A :py:class:`abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic` object.
- **mdb.models[name].materials[name].hyperfoam**: A :py:class:`abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam` object.
- **mdb.models[name].materials[name].hypoelastic**: A :py:class:`abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic` object.
- **mdb.models[name].materials[name].inelasticHeatFraction**: An :py:class:`abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction` object.
- **mdb.models[name].materials[name].jouleHeatFraction**: A :py:class:`abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction` object.
- **mdb.models[name].materials[name].latentHeat**: A :py:class:`abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat` object.
- **mdb.models[name].materials[name].lowDensityFoam**: A :py:class:`abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam` object.
- **mdb.models[name].materials[name].magneticPermeability**: A :py:class:`abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability` object.
- **mdb.models[name].materials[name].mohrCoulombPlasticity**: A :py:class:`abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity` object.
- **mdb.models[name].materials[name].moistureSwelling**: A :py:class:`abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling` object.
- **mdb.models[name].materials[name].mullinsEffect**: A :py:class:`abaqus.Material.TestData.MullinsEffect.MullinsEffect` object.
- **mdb.models[name].materials[name].permeability**: A :py:class:`abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability` object.
- **mdb.models[name].materials[name].piezoelectric**: A :py:class:`abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric` object.
- **mdb.models[name].materials[name].plastic**: A :py:class:`abaqus.Material.Plastic.Plastic.Plastic` object.
- **mdb.models[name].materials[name].poreFluidExpansion**: A :py:class:`abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion` object.
- **mdb.models[name].materials[name].porousBulkModuli**: A :py:class:`abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli` object.
- **mdb.models[name].materials[name].porousElastic**: A :py:class:`abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic` object.
- **mdb.models[name].materials[name].porousMetalPlasticity**: A :py:class:`abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity` object.
- **mdb.models[name].materials[name].regularization**: A :py:class:`abaqus.Material.Regularization.Regularization` object.
- **mdb.models[name].materials[name].solubility**: A :py:class:`abaqus.Material.Others.MassDiffusion.Solubility.Solubility` object.
- **mdb.models[name].materials[name].sorption**: A :py:class:`abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption` object.
- **mdb.models[name].materials[name].specificHeat**: A :py:class:`abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat` object.
- **mdb.models[name].materials[name].swelling**: A :py:class:`abaqus.Material.Plastic.Swelling.Swelling.Swelling` object.
- **mdb.models[name].materials[name].userDefinedField**: A :py:class:`abaqus.Material.Others.User.UserDefinedField.UserDefinedField` object.
- **mdb.models[name].materials[name].userMaterial**: A :py:class:`abaqus.Material.Others.User.UserMaterial.UserMaterial` object.
- **mdb.models[name].materials[name].userOutputVariables**: A :py:class:`abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables` object.
- **mdb.models[name].materials[name].viscoelastic**: A :py:class:`abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic` object.
- **mdb.models[name].materials[name].viscosity**: A :py:class:`abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity` object.
- **mdb.models[name].materials[name].viscous**: A :py:class:`abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous` object.



Create materials
-----------------

In Mdb
~~~~~~

.. autoclass:: abaqus.Material.MaterialModel.MaterialModel
    :members:

In Odb
~~~~~~

.. autoclass:: abaqus.Material.MaterialOdb.MaterialOdb
    :members:


Assign properties to the material
---------------------------------

.. autoclass:: abaqus.Material.Material.Material
    :members:


Object features
---------------

Density
*******

.. autoclass:: abaqus.Material.Density.Density.Density
    :members:



Hyperelastic
''''''''''''

.. autoclass:: abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic
    :members:


Hyperfoam
`````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam
    :members:


CombinedTestData
````````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData
    :members:

Hysteresis
``````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis
    :members:

Viscoelastic
````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic
    :members:


Hypoelastic
'''''''''''

.. autoclass:: abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic
    :members:


Elastic
'''''''

.. autoclass:: abaqus.Material.Elastic.Linear.Elastic.Elastic
    :members:

FailStrain
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStrain.FailStrain
    :members:

FailStress
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStress.FailStress
    :members:


LowDensityFoam
''''''''''''''

.. autoclass:: abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam
    :members:


PorousElastic
'''''''''''''

.. autoclass:: abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic
    :members:


SuperElasticity
'''''''''''''''

.. autoclass:: abaqus.Material.Elastic.SuperElastic.SuperElasticity.SuperElasticity
    :members:


DetonationPoint
***************

.. autoclass:: abaqus.Material.Eos.DetonationPoint.DetonationPoint
    :members:

Eos
***

.. autoclass:: abaqus.Material.Eos.Eos.Eos
    :members:

EosCompaction
*************

.. autoclass:: abaqus.Material.Eos.EosCompaction.EosCompaction
    :members:

evaluateMaterial
****************

.. autoclass:: abaqus.Material.evaluateMaterial.evaluateMaterial
    :members:


GapConductance
**************

.. autoclass:: abaqus.Material.Gap.GapConductance.GapConductance
    :members:

GapConvection
*************

.. autoclass:: abaqus.Material.Gap.GapConvection.GapConvection
    :members:

GapFlow
*******

.. autoclass:: abaqus.Material.Gap.GapFlow.GapFlow
    :members:

GapRadiation
************

.. autoclass:: abaqus.Material.Gap.GapRadiation.GapRadiation
    :members:


ContactArea
***********

.. autoclass:: abaqus.Material.Gasket.ContactArea.ContactArea
    :members:

GasketMembraneElastic
*********************

.. autoclass:: abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic
    :members:

GasketThicknessBehavior
***********************

.. autoclass:: abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior
    :members:

GasketTransverseShearElastic
****************************

.. autoclass:: abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic
    :members:

Material
********

.. autoclass:: abaqus.Material.Material.Material
    :members:

MaterialBase
************

.. autoclass:: abaqus.Material.MaterialBase.MaterialBase
    :members:

MaterialModel
*************

.. autoclass:: abaqus.Material.MaterialModel.MaterialModel
    :members:

MaterialOdb
***********

.. autoclass:: abaqus.Material.MaterialOdb.MaterialOdb
    :members:


MeanFieldHomogenization
***********************

.. autoclass:: abaqus.Material.Multiscale.MeanFieldHomogenization.MeanFieldHomogenization
    :members:

MeanFieldInclusion
******************

.. autoclass:: abaqus.Material.Multiscale.MeanFieldInclusion.MeanFieldInclusion
    :members:

MeanFieldMatrix
***************

.. autoclass:: abaqus.Material.Multiscale.MeanFieldMatrix.MeanFieldMatrix
    :members:

MeanFieldVoid
*************

.. autoclass:: abaqus.Material.Multiscale.MeanFieldVoid.MeanFieldVoid
    :members:



AcousticMedium
''''''''''''''

.. autoclass:: abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium
    :members:


Dielectric
''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric
    :members:

ElectricalConductivity
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity
    :members:

MagneticPermeability
''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability
    :members:

Piezoelectric
'''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric
    :members:


Conductivity
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity
    :members:

HeatGeneration
''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration
    :members:

InelasticHeatFraction
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction
    :members:

JouleHeatFraction
'''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction
    :members:

LatentHeat
''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat
    :members:

SpecificHeat
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat
    :members:



Diffusivity
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity
    :members:

PressureEffect
''''''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect
    :members:

Solubility
''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Solubility.Solubility
    :members:

SoretEffect
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect
    :members:


Damping
'''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Damping.Damping
    :members:

Expansion
'''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Expansion.Expansion
    :members:

PoreFluidExpansion
''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion
    :members:


Trs
```

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs
    :members:

Viscosity
`````````

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity
    :members:


FluidLeakoff
''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff
    :members:

Gel
'''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel
    :members:


MoistureSwelling
````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling
    :members:


Permeability
````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability
    :members:

SaturationDependence
````````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence
    :members:

VelocityDependence
``````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence
    :members:

PorousBulkModuli
````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli
    :members:

Sorption
````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption
    :members:


Depvar
''''''

.. autoclass:: abaqus.Material.Others.User.Depvar.Depvar
    :members:

UserDefinedField
''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField
    :members:

UserMaterial
''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial
    :members:

UserOutputVariables
'''''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables
    :members:



BrittleCracking
'''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking
    :members:

BrittleFailure
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure
    :members:

BrittleShear
''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear
    :members:

Concrete
''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete
    :members:

ConcreteCompressionDamage
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage
    :members:

ConcreteCompressionHardening
''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening
    :members:

ConcreteDamagedPlasticity
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity
    :members:

ConcreteTensionDamage
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage
    :members:

ConcreteTensionStiffening
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening
    :members:

FailureRatios
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios
    :members:

ShearRetention
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention
    :members:

TensionStiffening
'''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening
    :members:


Creep
'''''

.. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep
    :members:


ClayHardening
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening
    :members:

ClayPlasticity
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity
    :members:


CrushableFoam
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam
    :members:

CrushableFoamHardening
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening
    :members:



DruckerPrager
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager
    :members:

DruckerPragerCreep
``````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep
    :members:

DruckerPragerHardening
``````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening
    :members:

TriaxialTestData
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData
    :members:


CapCreepCohesion
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion
    :members:

CapCreepConsolidation
`````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation
    :members:

CapHardening
````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening
    :members:

CapPlasticity
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity
    :members:



AnnealTemperature
`````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature
    :members:


CastIronCompressionHardening
````````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening
    :members:

CastIronPlasticity
``````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity
    :members:

CastIronTensionHardening
````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening
    :members:


CycledPlastic
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic
    :members:

CyclicHardening
```````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening
    :members:


DeformationPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity
    :members:


Ornl
````

.. autoclass:: abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl
    :members:


PorousFailureCriteria
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria
    :members:

PorousMetalPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity
    :members:

VoidNucleation
``````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation
    :members:


RateDependent
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent
    :members:


Viscous
```````

.. autoclass:: abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous
    :members:


MohrCoulombHardening
''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening
    :members:

MohrCoulombPlasticity
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity
    :members:

TensionCutOff
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff
    :members:

Plastic
'''''''

.. autoclass:: abaqus.Material.Plastic.Plastic.Plastic
    :members:

Potential
'''''''''

.. autoclass:: abaqus.Material.Plastic.Potential.Potential
    :members:


SuperElasticHardening
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening
    :members:

SuperElasticHardeningModifications
''''''''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications
    :members:


Swelling
''''''''

.. autoclass:: abaqus.Material.Plastic.Swelling.Swelling.Swelling
    :members:

TensileFailure
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.TensileFailure.TensileFailure
    :members:


DamageEvolution
***************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution
    :members:

DamageInitiation
****************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation
    :members:

DamageStabilization
*******************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilization.DamageStabilization
    :members:

DamageStabilizationCohesive
***************************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilizationCohesive.DamageStabilizationCohesive
    :members:

Ratios
******

.. autoclass:: abaqus.Material.Ratios.Ratios
    :members:

Regularization
**************

.. autoclass:: abaqus.Material.Regularization.Regularization
    :members:


BiaxialTestData
***************

.. autoclass:: abaqus.Material.TestData.BiaxialTestData.BiaxialTestData
    :members:

BiaxialTestDataArray
********************

.. autoclass:: abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray
    :members:

MullinsEffect
*************

.. autoclass:: abaqus.Material.TestData.MullinsEffect.MullinsEffect
    :members:

PlanarTestData
**************

.. autoclass:: abaqus.Material.TestData.PlanarTestData.PlanarTestData
    :members:

PlanarTestDataArray
*******************

.. autoclass:: abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray
    :members:

ShearTestData
*************

.. autoclass:: abaqus.Material.TestData.ShearTestData.ShearTestData
    :members:

SimpleShearTestData
*******************

.. autoclass:: abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData
    :members:

UniaxialTestData
****************

.. autoclass:: abaqus.Material.TestData.UniaxialTestData.UniaxialTestData
    :members:

UniaxialTestDataArray
*********************

.. autoclass:: abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray
    :members:

VolumetricTestData
******************

.. autoclass:: abaqus.Material.TestData.VolumetricTestData.VolumetricTestData
    :members:
