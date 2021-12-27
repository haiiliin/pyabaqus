from abaqusConstants import *
from .AcousticMedium import AcousticMedium
from .BrittleCracking import BrittleCracking
from .CapPlasticity import CapPlasticity
from .CastIronPlasticity import CastIronPlasticity
from .ClayPlasticity import ClayPlasticity
from .Concrete import Concrete
from .ConcreteDamagedPlasticity import ConcreteDamagedPlasticity
from .Conductivity import Conductivity
from .Creep import Creep
from .CrushableFoam import CrushableFoam
from .DamageInitiation import DamageInitiation
from .Damping import Damping
from .DeformationPlasticity import DeformationPlasticity
from .Density import Density
from .Depvar import Depvar
from .Dielectric import Dielectric
from .Diffusivity import Diffusivity
from .DruckerPrager import DruckerPrager
from .Elastic import Elastic
from .ElectricalConductivity import ElectricalConductivity
from .Eos import Eos
from .Expansion import Expansion
from .FluidLeakoff import FluidLeakoff
from .GapFlow import GapFlow
from .GasketMembraneElastic import GasketMembraneElastic
from .GasketThicknessBehavior import GasketThicknessBehavior
from .GasketTransverseShearElastic import GasketTransverseShearElastic
from .Gel import Gel
from .HeatGeneration import HeatGeneration
from .Hyperelastic import Hyperelastic
from .Hyperfoam import Hyperfoam
from .Hypoelastic import Hypoelastic
from .InelasticHeatFraction import InelasticHeatFraction
from .JouleHeatFraction import JouleHeatFraction
from .LatentHeat import LatentHeat
from .LowDensityFoam import LowDensityFoam
from .MagneticPermeability import MagneticPermeability
from .MohrCoulombPlasticity import MohrCoulombPlasticity
from .MoistureSwelling import MoistureSwelling
from .MullinsEffect import MullinsEffect
from .Permeability import Permeability
from .Piezoelectric import Piezoelectric
from .Plastic import Plastic
from .PoreFluidExpansion import PoreFluidExpansion
from .PorousBulkModuli import PorousBulkModuli
from .PorousElastic import PorousElastic
from .PorousMetalPlasticity import PorousMetalPlasticity
from .Regularization import Regularization
from .Solubility import Solubility
from .Sorption import Sorption
from .SpecificHeat import SpecificHeat
from .Swelling import Swelling
from .UserDefinedField import UserDefinedField
from .UserMaterial import UserMaterial
from .UserOutputVariables import UserOutputVariables
from .Viscoelastic import Viscoelastic
from .Viscosity import Viscosity
from .Viscous import Viscous

class BaseMaterial:

    """A Material object is the object used to specify a material. The Material object stores 
    the various settings that determine how a material behaves. 
    A material is created by combining one or more individual material options and sub 
    options. A particular material option is associated with the Material object through a 
    member. For example: the *acousticMedium* member may contain an AcousticMedium object. 
    The alternative of having a MaterialOption abstract base class and a container of 
    MaterialOptions was rejected because it would make it more difficult to enforce the fact 
    that one Material object cannot contain two AcousticMedium objects, for example. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name]
        - import odbMaterial
        - session.odbs[name].materials[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - MATERIAL

    """

    # An AcousticMedium object. 
    acousticMedium: AcousticMedium = AcousticMedium()

    # A BrittleCracking object. 
    brittleCracking: BrittleCracking = BrittleCracking(((), ))

    # A CapPlasticity object. 
    capPlasticity: CapPlasticity = CapPlasticity(((), ))

    # A CastIronPlasticity object. 
    castIronPlasticity: CastIronPlasticity = CastIronPlasticity(((), ))

    # A ClayPlasticity object. 
    clayPlasticity: ClayPlasticity = ClayPlasticity(((), ))

    # A Concrete object. 
    concrete: Concrete = Concrete(((), ))

    # A ConcreteDamagedPlasticity object. 
    concreteDamagedPlasticity: ConcreteDamagedPlasticity = ConcreteDamagedPlasticity(((), ))

    # A Conductivity object. 
    conductivity: Conductivity = Conductivity(((), ))

    # A Creep object. 
    creep: Creep = Creep(((), ))

    # A CrushableFoam object. 
    crushableFoam: CrushableFoam = CrushableFoam(((), ))

    # A DamageInitiation object. 
    ductileDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    fldDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    flsdDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    johnsonCookDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    maxeDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    maxsDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    maxpeDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    maxpsDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    mkDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    msfldDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    quadeDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    quadsDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    shearDamageInitiation: DamageInitiation = DamageInitiation()

    # A DamageInitiation object. 
    hashinDamageInitiation: DamageInitiation = DamageInitiation()

    # A Damping object. 
    damping: Damping = Damping()

    # A DeformationPlasticity object. 
    deformationPlasticity: DeformationPlasticity = DeformationPlasticity(((), ))

    # A Density object. 
    density: Density = Density(((), ))

    # A Depvar object. 
    depvar: Depvar = Depvar()

    # A Dielectric object. 
    dielectric: Dielectric = Dielectric(((), ))

    # A Diffusivity object. 
    diffusivity: Diffusivity = Diffusivity(((), ))

    # A DruckerPrager object. 
    druckerPrager: DruckerPrager = DruckerPrager(((), ))

    # An Elastic object. 
    elastic: Elastic = Elastic(((), ))

    # An ElectricalConductivity object. 
    electricalConductivity: ElectricalConductivity = ElectricalConductivity(((), ))

    # An Eos object. 
    eos: Eos = Eos()

    # An Expansion object. 
    expansion: Expansion = Expansion()

    # A FluidLeakoff object. 
    fluidLeakoff: FluidLeakoff = FluidLeakoff()

    # A GapFlow object. 
    gapFlow: GapFlow = GapFlow(((), ))

    # A GasketThicknessBehavior object. 
    gasketThicknessBehavior: GasketThicknessBehavior = GasketThicknessBehavior(((), ))

    # A GasketTransverseShearElastic object. 
    gasketTransverseShearElastic: GasketTransverseShearElastic = GasketTransverseShearElastic(((), ))

    # A GasketMembraneElastic object. 
    gasketMembraneElastic: GasketMembraneElastic = GasketMembraneElastic(((), ))

    # A Gel object. 
    gel: Gel = Gel(((), ))

    # A HeatGeneration object. 
    heatGeneration: HeatGeneration = HeatGeneration()

    # A Hyperelastic object. 
    hyperelastic: Hyperelastic = Hyperelastic(((), ))

    # A Hyperfoam object. 
    hyperfoam: Hyperfoam = Hyperfoam()

    # A Hypoelastic object. 
    hypoelastic: Hypoelastic = Hypoelastic(((), ))

    # An InelasticHeatFraction object. 
    inelasticHeatFraction: InelasticHeatFraction = InelasticHeatFraction()

    # A JouleHeatFraction object. 
    jouleHeatFraction: JouleHeatFraction = JouleHeatFraction()

    # A LatentHeat object. 
    latentHeat: LatentHeat = LatentHeat(((), ))

    # A LowDensityFoam object. 
    lowDensityFoam: LowDensityFoam = LowDensityFoam()

    # A MagneticPermeability object. 
    magneticPermeability: MagneticPermeability = MagneticPermeability(((), ), ((), ), ((), ))

    # A MohrCoulombPlasticity object. 
    mohrCoulombPlasticity: MohrCoulombPlasticity = MohrCoulombPlasticity(((), ))

    # A MoistureSwelling object. 
    moistureSwelling: MoistureSwelling = MoistureSwelling(((), ))

    # A MullinsEffect object. 
    mullinsEffect: MullinsEffect = MullinsEffect()

    # A Permeability object. 
    permeability: Permeability = Permeability(0, 0, ((), ))

    # A Piezoelectric object. 
    piezoelectric: Piezoelectric = Piezoelectric(((), ))

    # A Plastic object. 
    plastic: Plastic = Plastic(((), ))

    # A PoreFluidExpansion object. 
    poreFluidExpansion: PoreFluidExpansion = PoreFluidExpansion(((), ))

    # A PorousBulkModuli object. 
    porousBulkModuli: PorousBulkModuli = PorousBulkModuli(((), ))

    # A PorousElastic object. 
    porousElastic: PorousElastic = PorousElastic(((), ))

    # A PorousMetalPlasticity object. 
    porousMetalPlasticity: PorousMetalPlasticity = PorousMetalPlasticity(((), ))

    # A Regularization object. 
    regularization: Regularization = Regularization()

    # A Solubility object. 
    solubility: Solubility = Solubility(((), ))

    # A Sorption object. 
    sorption: Sorption = Sorption(((), ))

    # A SpecificHeat object. 
    specificHeat: SpecificHeat = SpecificHeat(((), ))

    # A Swelling object. 
    swelling: Swelling = Swelling(((), ))

    # A UserDefinedField object. 
    userDefinedField: UserDefinedField = UserDefinedField()

    # A UserMaterial object. 
    userMaterial: UserMaterial = UserMaterial()

    # A UserOutputVariables object. 
    userOutputVariables: UserOutputVariables = UserOutputVariables()

    # A Viscoelastic object. 
    viscoelastic: Viscoelastic = Viscoelastic(FREQUENCY, ((), ))

    # A Viscosity object. 
    viscosity: Viscosity = Viscosity(((), ))

    # A Viscous object. 
    viscous: Viscous = Viscous(((), ))

    def __init__(self, name: str, description: str = '', materialIdentifier: str = ''):
        """This method creates a Material object.

        Path
        ----
            - mdb.models[name].Material
            - session.odbs[name].Material

        Parameters
        ----------
        name
            A String specifying the name of the new material. 
        description
            A String specifying user description of the material. The default value is an empty 
            string. 
        materialIdentifier
            A String specifying material identifier for customer use. The default value is an empty 
            string. 

        Returns
        -------
            A Material object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def materialsFromOdb(self, fileName: str):
        """This methods creates Material objects by reading an output database. The new materials
        are placed in the materials repository.

        Path
        ----
            - mdb.models[*name*].materialsFromOdb

        Parameters
        ----------
        fileName
            A String specifying the name of the output database file (including the .odb extension) 
            to be read. This String can also be the full path to the output database file if it is 
            located in another directory. 

        Returns
        -------
            A list of Material objects. 

        Exceptions
        ----------
            None. 
        """
        pass

