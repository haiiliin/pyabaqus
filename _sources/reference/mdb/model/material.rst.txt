========
Material
========

The Material commands are used to define the materials in a model.

Create materials
-----------------

In Mdb
~~~~~~

.. automethod:: abaqus.Material.MaterialModel.MaterialModel.Material

In Odb
~~~~~~

.. automethod:: abaqus.Material.MaterialOdb.MaterialOdb.Material


Assign properties to the material
---------------------------------

.. automethod:: abaqus.Material.Material.Material.AcousticMedium

.. automethod:: abaqus.Material.Material.Material.BrittleCracking

.. automethod:: abaqus.Material.Material.Material.CapPlasticity

.. automethod:: abaqus.Material.Material.Material.CastIronPlasticity

.. automethod:: abaqus.Material.Material.Material.ClayPlasticity

.. automethod:: abaqus.Material.Material.Material.Concrete

.. automethod:: abaqus.Material.Material.Material.ConcreteDamagedPlasticity

.. automethod:: abaqus.Material.Material.Material.Conductivity

.. automethod:: abaqus.Material.Material.Material.Creep

.. automethod:: abaqus.Material.Material.Material.CrushableFoam

.. automethod:: abaqus.Material.Material.Material.Damping

.. automethod:: abaqus.Material.Material.Material.DeformationPlasticity

.. automethod:: abaqus.Material.Material.Material.Density

.. automethod:: abaqus.Material.Material.Material.Depvar

.. automethod:: abaqus.Material.Material.Material.Dielectric

.. automethod:: abaqus.Material.Material.Material.Diffusivity

.. automethod:: abaqus.Material.Material.Material.DruckerPrager

.. automethod:: abaqus.Material.Material.Material.Elastic

.. automethod:: abaqus.Material.Material.Material.ElectricalConductivity

.. automethod:: abaqus.Material.Material.Material.Eos

.. automethod:: abaqus.Material.Material.Material.Expansion

.. automethod:: abaqus.Material.Material.Material.FluidLeakoff

.. automethod:: abaqus.Material.Material.Material.GapFlow

.. automethod:: abaqus.Material.Material.Material.GasketMembraneElastic

.. automethod:: abaqus.Material.Material.Material.GasketThicknessBehavior

.. automethod:: abaqus.Material.Material.Material.GasketTransverseShearElastic

.. automethod:: abaqus.Material.Material.Material.Gel

.. automethod:: abaqus.Material.Material.Material.Hyperelastic

.. automethod:: abaqus.Material.Material.Material.Hyperfoam

.. automethod:: abaqus.Material.Material.Material.Hypoelastic

.. automethod:: abaqus.Material.Material.Material.InelasticHeatFraction

.. automethod:: abaqus.Material.Material.Material.JouleHeatFraction

.. automethod:: abaqus.Material.Material.Material.LatentHeat

.. automethod:: abaqus.Material.Material.Material.LowDensityFoam

.. automethod:: abaqus.Material.Material.Material.MagneticPermeability

.. automethod:: abaqus.Material.Material.Material.MohrCoulombPlasticity

.. automethod:: abaqus.Material.Material.Material.MoistureSwelling

.. automethod:: abaqus.Material.Material.Material.Permeability

.. automethod:: abaqus.Material.Material.Material.Piezoelectric

.. automethod:: abaqus.Material.Material.Material.Plastic

.. automethod:: abaqus.Material.Material.Material.PorousBulkModuli

.. automethod:: abaqus.Material.Material.Material.PorousElastic

.. automethod:: abaqus.Material.Material.Material.PorousMetalPlasticity

.. automethod:: abaqus.Material.Material.Material.Regularization

.. automethod:: abaqus.Material.Material.Material.Solubility

.. automethod:: abaqus.Material.Material.Material.Sorption

.. automethod:: abaqus.Material.Material.Material.SpecificHeat

.. automethod:: abaqus.Material.Material.Material.Swelling

.. automethod:: abaqus.Material.Material.Material.UserMaterial

.. automethod:: abaqus.Material.Material.Material.UserOutputVariables

.. automethod:: abaqus.Material.Material.Material.Viscoelastic

.. automethod:: abaqus.Material.Material.Material.Viscosity

.. automethod:: abaqus.Material.Material.Material.Viscous

.. automethod:: abaqus.Material.Material.Material.materialsFromOdb


Object features
---------------

Material
~~~~~~~~

.. autoclass:: abaqus.Material.Material.Material
    :members:
    :inherited-members:

Density
~~~~~~~


Density
*******

.. autoclass:: abaqus.Material.Density.Density.Density

    .. automethod:: __init__

Elastic
~~~~~~~


HyperElastic
************


Hyperelastic
''''''''''''

.. autoclass:: abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic
    
    .. automethod:: __init__

HyperFoam
'''''''''


Hyperfoam
`````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.HyperFoam.Hyperfoam.Hyperfoam
    
    .. automethod:: __init__

ViscoElastic
''''''''''''


CombinedTestData
````````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData.CombinedTestData
    
    .. automethod:: __init__

Hysteresis
``````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Hysteresis.Hysteresis
    
    .. automethod:: __init__

Viscoelastic
````````````

.. autoclass:: abaqus.Material.Elastic.HyperElastic.ViscoElastic.Viscoelastic.Viscoelastic
    
    .. automethod:: __init__

HypoElastic
***********


Hypoelastic
'''''''''''

.. autoclass:: abaqus.Material.Elastic.HypoElastic.Hypoelastic.Hypoelastic
    
    .. automethod:: __init__

Linear
******


Elastic
'''''''

.. autoclass:: abaqus.Material.Elastic.Linear.Elastic.Elastic
    
    .. automethod:: __init__

FailStrain
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStrain.FailStrain
    
    .. automethod:: __init__

FailStress
''''''''''

.. autoclass:: abaqus.Material.Elastic.Linear.FailStress.FailStress
    
    .. automethod:: __init__

LowDensityFoam
**************


LowDensityFoam
''''''''''''''

.. autoclass:: abaqus.Material.Elastic.LowDensityFoam.LowDensityFoam.LowDensityFoam
    
    .. automethod:: __init__

Porous
******


PorousElastic
'''''''''''''

.. autoclass:: abaqus.Material.Elastic.Porous.PorousElastic.PorousElastic
    
    .. automethod:: __init__

SuperElastic
************


SuperElasticity
'''''''''''''''

.. autoclass:: abaqus.Material.Elastic.SuperElastic.SuperElasticity.SuperElasticity
    
    .. automethod:: __init__

Eos
~~~


DetonationPoint
***************

.. autoclass:: abaqus.Material.Eos.DetonationPoint.DetonationPoint
    
    .. automethod:: __init__

Eos
***

.. autoclass:: abaqus.Material.Eos.Eos.Eos
    
    .. automethod:: __init__

EosCompaction
*************

.. autoclass:: abaqus.Material.Eos.EosCompaction.EosCompaction
    
    .. automethod:: __init__

evaluateMaterial
~~~~~~~~~~~~~~~~

.. automodule:: abaqus.Material.evaluateMaterial
    :members:

Gap
~~~


GapConductance
**************

.. autoclass:: abaqus.Material.Gap.GapConductance.GapConductance
    
    .. automethod:: __init__

GapConvection
*************

.. autoclass:: abaqus.Material.Gap.GapConvection.GapConvection
    
    .. automethod:: __init__

GapFlow
*******

.. autoclass:: abaqus.Material.Gap.GapFlow.GapFlow
    
    .. automethod:: __init__

GapRadiation
************

.. autoclass:: abaqus.Material.Gap.GapRadiation.GapRadiation
    
    .. automethod:: __init__

Gasket
~~~~~~


ContactArea
***********

.. autoclass:: abaqus.Material.Gasket.ContactArea.ContactArea
    
    .. automethod:: __init__

GasketMembraneElastic
*********************

.. autoclass:: abaqus.Material.Gasket.GasketMembraneElastic.GasketMembraneElastic
    
    .. automethod:: __init__

GasketThicknessBehavior
***********************

.. autoclass:: abaqus.Material.Gasket.GasketThicknessBehavior.GasketThicknessBehavior
    
    .. automethod:: __init__

GasketTransverseShearElastic
****************************

.. autoclass:: abaqus.Material.Gasket.GasketTransverseShearElastic.GasketTransverseShearElastic
    
    .. automethod:: __init__

Multiscale
~~~~~~~~~~


MeanFieldHomogenization
***********************

.. autoclass:: abaqus.Material.Multiscale.MeanFieldHomogenization.MeanFieldHomogenization
    
    .. automethod:: __init__

MeanFieldInclusion
******************

.. autoclass:: abaqus.Material.Multiscale.MeanFieldInclusion.MeanFieldInclusion
    
    .. automethod:: __init__

MeanFieldMatrix
***************

.. autoclass:: abaqus.Material.Multiscale.MeanFieldMatrix.MeanFieldMatrix
    
    .. automethod:: __init__

MeanFieldVoid
*************

.. autoclass:: abaqus.Material.Multiscale.MeanFieldVoid.MeanFieldVoid
    
    .. automethod:: __init__

Others
~~~~~~


Acoustic
********


AcousticMedium
''''''''''''''

.. autoclass:: abaqus.Material.Others.Acoustic.AcousticMedium.AcousticMedium
    
    .. automethod:: __init__

Electromagnetic
***************


Dielectric
''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Dielectric.Dielectric
    
    .. automethod:: __init__

ElectricalConductivity
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.ElectricalConductivity.ElectricalConductivity
    
    .. automethod:: __init__

MagneticPermeability
''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.MagneticPermeability.MagneticPermeability
    
    .. automethod:: __init__

Piezoelectric
'''''''''''''

.. autoclass:: abaqus.Material.Others.Electromagnetic.Piezoelectric.Piezoelectric
    
    .. automethod:: __init__

HeatTransfer
************


Conductivity
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity
    
    .. automethod:: __init__

HeatGeneration
''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.HeatGeneration.HeatGeneration
    
    .. automethod:: __init__

InelasticHeatFraction
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.InelasticHeatFraction.InelasticHeatFraction
    
    .. automethod:: __init__

JouleHeatFraction
'''''''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.JouleHeatFraction.JouleHeatFraction
    
    .. automethod:: __init__

LatentHeat
''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.LatentHeat.LatentHeat
    
    .. automethod:: __init__

SpecificHeat
''''''''''''

.. autoclass:: abaqus.Material.Others.HeatTransfer.SpecificHeat.SpecificHeat
    
    .. automethod:: __init__

Hydrodynamic
************


MassDiffusion
*************


Diffusivity
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Diffusivity.Diffusivity
    
    .. automethod:: __init__

PressureEffect
''''''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.PressureEffect.PressureEffect
    
    .. automethod:: __init__

Solubility
''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.Solubility.Solubility
    
    .. automethod:: __init__

SoretEffect
'''''''''''

.. autoclass:: abaqus.Material.Others.MassDiffusion.SoretEffect.SoretEffect
    
    .. automethod:: __init__

Mechanical
**********


Damping
'''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Damping.Damping
    
    .. automethod:: __init__

Expansion
'''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.Expansion.Expansion
    
    .. automethod:: __init__

PoreFluidExpansion
''''''''''''''''''

.. autoclass:: abaqus.Material.Others.Mechanical.PoreFluidExpansion.PoreFluidExpansion
    
    .. automethod:: __init__

Viscosity
'''''''''


Trs
```

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Trs.Trs
    
    .. automethod:: __init__

Viscosity
`````````

.. autoclass:: abaqus.Material.Others.Mechanical.Viscosity.Viscosity.Viscosity
    
    .. automethod:: __init__

PoreFluidFlow
*************


FluidLeakoff
''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.FluidLeakoff.FluidLeakoff
    
    .. automethod:: __init__

Gel
'''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Gel.Gel
    
    .. automethod:: __init__

MoistureSwelling
''''''''''''''''


MoistureSwelling
````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.MoistureSwelling.MoistureSwelling.MoistureSwelling
    
    .. automethod:: __init__

Permeability
''''''''''''


Permeability
````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.Permeability.Permeability
    
    .. automethod:: __init__

SaturationDependence
````````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.SaturationDependence.SaturationDependence
    
    .. automethod:: __init__

VelocityDependence
``````````````````

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Permeability.VelocityDependence.VelocityDependence
    
    .. automethod:: __init__

PorousBulkModuli
''''''''''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.PorousBulkModuli.PorousBulkModuli
    
    .. automethod:: __init__

Sorption
''''''''

.. autoclass:: abaqus.Material.Others.PoreFluidFlow.Sorption.Sorption
    
    .. automethod:: __init__

User
****


Depvar
''''''

.. autoclass:: abaqus.Material.Others.User.Depvar.Depvar
    
    .. automethod:: __init__

UserDefinedField
''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserDefinedField.UserDefinedField
    
    .. automethod:: __init__

UserMaterial
''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserMaterial.UserMaterial
    
    .. automethod:: __init__

UserOutputVariables
'''''''''''''''''''

.. autoclass:: abaqus.Material.Others.User.UserOutputVariables.UserOutputVariables
    
    .. automethod:: __init__

Plastic
~~~~~~~


Concrete
********


BrittleCracking
'''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking
    
    .. automethod:: __init__

BrittleFailure
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure
    
    .. automethod:: __init__

BrittleShear
''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.BrittleShear.BrittleShear
    
    .. automethod:: __init__

Concrete
''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.Concrete.Concrete
    
    .. automethod:: __init__

ConcreteCompressionDamage
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionDamage.ConcreteCompressionDamage
    
    .. automethod:: __init__

ConcreteCompressionHardening
''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteCompressionHardening.ConcreteCompressionHardening
    
    .. automethod:: __init__

ConcreteDamagedPlasticity
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteDamagedPlasticity.ConcreteDamagedPlasticity
    
    .. automethod:: __init__

ConcreteTensionDamage
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionDamage.ConcreteTensionDamage
    
    .. automethod:: __init__

ConcreteTensionStiffening
'''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ConcreteTensionStiffening.ConcreteTensionStiffening
    
    .. automethod:: __init__

FailureRatios
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.FailureRatios.FailureRatios
    
    .. automethod:: __init__

ShearRetention
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.ShearRetention.ShearRetention
    
    .. automethod:: __init__

TensionStiffening
'''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.Concrete.TensionStiffening.TensionStiffening
    
    .. automethod:: __init__

Creep
*****


Creep
'''''

.. autoclass:: abaqus.Material.Plastic.Creep.Creep.Creep
    
    .. automethod:: __init__

CriticalStateClay
*****************


ClayHardening
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayHardening.ClayHardening
    
    .. automethod:: __init__

ClayPlasticity
''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CriticalStateClay.ClayPlasticity.ClayPlasticity
    
    .. automethod:: __init__

CrushableFoam
*************


CrushableFoam
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoam.CrushableFoam
    
    .. automethod:: __init__

CrushableFoamHardening
''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.CrushableFoam.CrushableFoamHardening.CrushableFoamHardening
    
    .. automethod:: __init__

DruckerPrager
*************


Extended
''''''''


DruckerPrager
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPrager.DruckerPrager
    
    .. automethod:: __init__

DruckerPragerCreep
``````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerCreep.DruckerPragerCreep
    
    .. automethod:: __init__

DruckerPragerHardening
``````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.DruckerPragerHardening.DruckerPragerHardening
    
    .. automethod:: __init__

TriaxialTestData
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.Extended.TriaxialTestData.TriaxialTestData
    
    .. automethod:: __init__

ModifiedCap
'''''''''''


CapCreepCohesion
````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepCohesion.CapCreepCohesion
    
    .. automethod:: __init__

CapCreepConsolidation
`````````````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapCreepConsolidation.CapCreepConsolidation
    
    .. automethod:: __init__

CapHardening
````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapHardening.CapHardening
    
    .. automethod:: __init__

CapPlasticity
`````````````

.. autoclass:: abaqus.Material.Plastic.DruckerPrager.ModifiedCap.CapPlasticity.CapPlasticity
    
    .. automethod:: __init__

Metal
*****


Annealing
'''''''''


AnnealTemperature
`````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Annealing.AnnealTemperature.AnnealTemperature
    
    .. automethod:: __init__

CastIron
''''''''


CastIronCompressionHardening
````````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening
    
    .. automethod:: __init__

CastIronPlasticity
``````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronPlasticity.CastIronPlasticity
    
    .. automethod:: __init__

CastIronTensionHardening
````````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.CastIron.CastIronTensionHardening.CastIronTensionHardening
    
    .. automethod:: __init__

Cyclic
''''''


CycledPlastic
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CycledPlastic.CycledPlastic
    
    .. automethod:: __init__

CyclicHardening
```````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Cyclic.CyclicHardening.CyclicHardening
    
    .. automethod:: __init__

Deformation
'''''''''''


DeformationPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Deformation.DeformationPlasticity.DeformationPlasticity
    
    .. automethod:: __init__

ORNL
''''


Ornl
````

.. autoclass:: abaqus.Material.Plastic.Metal.ORNL.Ornl.Ornl
    
    .. automethod:: __init__

Porous
''''''


PorousFailureCriteria
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousFailureCriteria.PorousFailureCriteria
    
    .. automethod:: __init__

PorousMetalPlasticity
`````````````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.PorousMetalPlasticity.PorousMetalPlasticity
    
    .. automethod:: __init__

VoidNucleation
``````````````

.. autoclass:: abaqus.Material.Plastic.Metal.Porous.VoidNucleation.VoidNucleation
    
    .. automethod:: __init__

RateDependent
'''''''''''''


RateDependent
`````````````

.. autoclass:: abaqus.Material.Plastic.Metal.RateDependent.RateDependent.RateDependent
    
    .. automethod:: __init__

TwoLayerViscoPlasticity
'''''''''''''''''''''''


Viscous
```````

.. autoclass:: abaqus.Material.Plastic.Metal.TwoLayerViscoPlasticity.Viscous.Viscous
    
    .. automethod:: __init__

MohrCoulomb
***********


MohrCoulombHardening
''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombHardening.MohrCoulombHardening
    
    .. automethod:: __init__

MohrCoulombPlasticity
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.MohrCoulombPlasticity.MohrCoulombPlasticity
    
    .. automethod:: __init__

TensionCutOff
'''''''''''''

.. autoclass:: abaqus.Material.Plastic.MohrCoulomb.TensionCutOff.TensionCutOff
    
    .. automethod:: __init__

Plastic
*******

.. autoclass:: abaqus.Material.Plastic.Plastic.Plastic
    
    .. automethod:: __init__

Potential
*********

.. autoclass:: abaqus.Material.Plastic.Potential.Potential
    
    .. automethod:: __init__

SuperElastic
************


SuperElasticHardening
'''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardening.SuperElasticHardening
    
    .. automethod:: __init__

SuperElasticHardeningModifications
''''''''''''''''''''''''''''''''''

.. autoclass:: abaqus.Material.Plastic.SuperElastic.SuperElasticHardeningModifications.SuperElasticHardeningModifications
    
    .. automethod:: __init__

Swelling
********


Swelling
''''''''

.. autoclass:: abaqus.Material.Plastic.Swelling.Swelling.Swelling
    
    .. automethod:: __init__

TensileFailure
**************

.. autoclass:: abaqus.Material.Plastic.TensileFailure.TensileFailure
    
    .. automethod:: __init__

ProgressiveDamageFailure
~~~~~~~~~~~~~~~~~~~~~~~~


DamageEvolution
***************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageEvolution.DamageEvolution
    
    .. automethod:: __init__

DamageInitiation
****************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageInitiation.DamageInitiation
    
    .. automethod:: __init__

DamageStabilization
*******************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilization.DamageStabilization
    
    .. automethod:: __init__

DamageStabilizationCohesive
***************************

.. autoclass:: abaqus.Material.ProgressiveDamageFailure.DamageStabilizationCohesive.DamageStabilizationCohesive
    
    .. automethod:: __init__

Ratios
~~~~~~

.. autoclass:: abaqus.Material.Ratios.Ratios
    
    .. automethod:: __init__

Regularization
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Material.Regularization.Regularization
    
    .. automethod:: __init__

TestData
~~~~~~~~


BiaxialTestData
***************

.. autoclass:: abaqus.Material.TestData.BiaxialTestData.BiaxialTestData
    
    .. automethod:: __init__

BiaxialTestDataArray
********************

.. autoclass:: abaqus.Material.TestData.BiaxialTestDataArray.BiaxialTestDataArray
    
    .. automethod:: __init__

MullinsEffect
*************

.. autoclass:: abaqus.Material.TestData.MullinsEffect.MullinsEffect
    
    .. automethod:: __init__

PlanarTestData
**************

.. autoclass:: abaqus.Material.TestData.PlanarTestData.PlanarTestData
    
    .. automethod:: __init__

PlanarTestDataArray
*******************

.. autoclass:: abaqus.Material.TestData.PlanarTestDataArray.PlanarTestDataArray
    
    .. automethod:: __init__

ShearTestData
*************

.. autoclass:: abaqus.Material.TestData.ShearTestData.ShearTestData
    
    .. automethod:: __init__

SimpleShearTestData
*******************

.. autoclass:: abaqus.Material.TestData.SimpleShearTestData.SimpleShearTestData
    
    .. automethod:: __init__

UniaxialTestData
****************

.. autoclass:: abaqus.Material.TestData.UniaxialTestData.UniaxialTestData
    
    .. automethod:: __init__

UniaxialTestDataArray
*********************

.. autoclass:: abaqus.Material.TestData.UniaxialTestDataArray.UniaxialTestDataArray
    
    .. automethod:: __init__

VolumetricTestData
******************

.. autoclass:: abaqus.Material.TestData.VolumetricTestData.VolumetricTestData
    
    .. automethod:: __init__
