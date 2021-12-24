from .CohesiveBehavior import CohesiveBehavior
from .ContactDamage import ContactDamage
from .ContactDamping import ContactDamping
from .ContactTangentialBehavior import ContactTangentialBehavior
from .FractureCriterion import FractureCriterion
from .GapElectricalConductance import GapElectricalConductance
from .GapHeatGeneration import GapHeatGeneration
from .GeometricProperties import GeometricProperties
from .InteractionProperty import InteractionProperty
from .NormalBehavior import NormalBehavior
from .Radiation import Radiation
from .ThermalConductance import ThermalConductance

class ContactProperty(InteractionProperty):

    """The ContactProperty object defines a contact interaction property. 
    The ContactProperty object is derived from the InteractionProperty object. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactionProperties[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - SURFACE INTERACTION

    """

    # A ContactTangentialBehavior object. 
    tangentialBehavior: ContactTangentialBehavior = None

    # A NormalBehavior object. 
    normalBehavior: NormalBehavior = None

    # A ContactDamping object. 
    damping: ContactDamping = None

    # A ContactDamage object. 
    damage: ContactDamage = None

    # A FractureCriterion object. 
    fractureCriterion: FractureCriterion = None

    # A CohesiveBehavior object. 
    cohesiveBehavior: CohesiveBehavior = None

    # A ThermalConductance object. 
    thermalConductance: ThermalConductance = None

    # A GapHeatGeneration object. 
    heatGeneration: GapHeatGeneration = None

    # A Radiation object. 
    radiation: Radiation = None

    # A GeometricProperties object. 
    geometricProperties: GeometricProperties = None

    # A GapElectricalConductance object. 
    electricalConductance: GapElectricalConductance = None

    def __init__(self, name: str):
        """This method creates a ContactProperty object.

        Path
        ----
            - mdb.models[name].ContactProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 

        Returns
        -------
            A ContactProperty object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

