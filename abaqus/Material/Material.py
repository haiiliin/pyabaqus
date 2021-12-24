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

class Material:

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
    acousticMedium: AcousticMedium = None

    # A BrittleCracking object. 
    brittleCracking: BrittleCracking = None

    # A CapPlasticity object. 
    capPlasticity: CapPlasticity = None

    # A CastIronPlasticity object. 
    castIronPlasticity: CastIronPlasticity = None

    # A ClayPlasticity object. 
    clayPlasticity: ClayPlasticity = None

    # A Concrete object. 
    concrete: Concrete = None

    # A ConcreteDamagedPlasticity object. 
    concreteDamagedPlasticity: ConcreteDamagedPlasticity = None

    # A Conductivity object. 
    conductivity: Conductivity = None

    # A Creep object. 
    creep: Creep = None

    # A CrushableFoam object. 
    crushableFoam: CrushableFoam = None

    # A DamageInitiation object. 
    ductileDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    fldDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    flsdDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    johnsonCookDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    maxeDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    maxsDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    maxpeDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    maxpsDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    mkDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    msfldDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    quadeDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    quadsDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    shearDamageInitiation: DamageInitiation = None

    # A DamageInitiation object. 
    hashinDamageInitiation: DamageInitiation = None

    # A Damping object. 
    damping: Damping = None

    # A DeformationPlasticity object. 
    deformationPlasticity: DeformationPlasticity = None

    # A Density object. 
    density: Density = None

    # A Depvar object. 
    depvar: Depvar = None

    # A Dielectric object. 
    dielectric: Dielectric = None

    # A Diffusivity object. 
    diffusivity: Diffusivity = None

    # A DruckerPrager object. 
    druckerPrager: DruckerPrager = None

    # An Elastic object. 
    elastic: Elastic = None

    # An ElectricalConductivity object. 
    electricalConductivity: ElectricalConductivity = None

    # An Eos object. 
    eos: Eos = None

    # An Expansion object. 
    expansion: Expansion = None

    # A FluidLeakoff object. 
    fluidLeakoff: FluidLeakoff = None

    # A GapFlow object. 
    gapFlow: GapFlow = None

    # A GasketThicknessBehavior object. 
    gasketThicknessBehavior: GasketThicknessBehavior = None

    # A GasketTransverseShearElastic object. 
    gasketTransverseShearElastic: GasketTransverseShearElastic = None

    # A GasketMembraneElastic object. 
    gasketMembraneElastic: GasketMembraneElastic = None

    # A Gel object. 
    gel: Gel = None

    # A HeatGeneration object. 
    heatGeneration: HeatGeneration = None

    # A Hyperelastic object. 
    hyperelastic: Hyperelastic = None

    # A Hyperfoam object. 
    hyperfoam: Hyperfoam = None

    # A Hypoelastic object. 
    hypoelastic: Hypoelastic = None

    # An InelasticHeatFraction object. 
    inelasticHeatFraction: InelasticHeatFraction = None

    # A JouleHeatFraction object. 
    jouleHeatFraction: JouleHeatFraction = None

    # A LatentHeat object. 
    latentHeat: LatentHeat = None

    # A LowDensityFoam object. 
    lowDensityFoam: LowDensityFoam = None

    # A MagneticPermeability object. 
    magneticPermeability: MagneticPermeability = None

    # A MohrCoulombPlasticity object. 
    mohrCoulombPlasticity: MohrCoulombPlasticity = None

    # A MoistureSwelling object. 
    moistureSwelling: MoistureSwelling = None

    # A MullinsEffect object. 
    mullinsEffect: MullinsEffect = None

    # A Permeability object. 
    permeability: Permeability = None

    # A Piezoelectric object. 
    piezoelectric: Piezoelectric = None

    # A Plastic object. 
    plastic: Plastic = None

    # A PoreFluidExpansion object. 
    poreFluidExpansion: PoreFluidExpansion = None

    # A PorousBulkModuli object. 
    porousBulkModuli: PorousBulkModuli = None

    # A PorousElastic object. 
    porousElastic: PorousElastic = None

    # A PorousMetalPlasticity object. 
    porousMetalPlasticity: PorousMetalPlasticity = None

    # A Regularization object. 
    regularization: Regularization = None

    # A Solubility object. 
    solubility: Solubility = None

    # A Sorption object. 
    sorption: Sorption = None

    # A SpecificHeat object. 
    specificHeat: SpecificHeat = None

    # A Swelling object. 
    swelling: Swelling = None

    # A UserDefinedField object. 
    userDefinedField: UserDefinedField = None

    # A UserMaterial object. 
    userMaterial: UserMaterial = None

    # A UserOutputVariables object. 
    userOutputVariables: UserOutputVariables = None

    # A Viscoelastic object. 
    viscoelastic: Viscoelastic = None

    # A Viscosity object. 
    viscosity: Viscosity = None

    # A Viscous object. 
    viscous: Viscous = None

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

