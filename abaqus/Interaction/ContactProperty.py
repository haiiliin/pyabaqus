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
    tangentialBehavior: ContactTangentialBehavior = ContactTangentialBehavior()

    # A NormalBehavior object. 
    normalBehavior: NormalBehavior = NormalBehavior()

    # A ContactDamping object. 
    damping: ContactDamping = ContactDamping()

    # A ContactDamage object. 
    damage: ContactDamage = ContactDamage()

    # A FractureCriterion object. 
    fractureCriterion: FractureCriterion = FractureCriterion()

    # A CohesiveBehavior object. 
    cohesiveBehavior: CohesiveBehavior = CohesiveBehavior()

    # A ThermalConductance object. 
    thermalConductance: ThermalConductance = ThermalConductance()

    # A GapHeatGeneration object. 
    heatGeneration: GapHeatGeneration = GapHeatGeneration()

    # A Radiation object. 
    radiation: Radiation = Radiation()

    # A GeometricProperties object. 
    geometricProperties: GeometricProperties = GeometricProperties()

    # A GapElectricalConductance object. 
    electricalConductance: GapElectricalConductance = GapElectricalConductance()

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

