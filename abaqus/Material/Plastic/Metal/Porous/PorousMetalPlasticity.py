from abaqusConstants import *
from .PorousFailureCriteria import PorousFailureCriteria
from abaqus.Material.Plastic.Metal.Porous.VoidNucleation import VoidNucleation


class PorousMetalPlasticity:
    """The PorousMetalPlasticity object specifies a porous metal plasticity model.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].porousMetalPlasticity
        - import odbMaterial
        - session.odbs[name].materials[name].porousMetalPlasticity

    Table Data
    ----------
        - q1.
        - q2.
        - q3.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - POROUS METAL PLASTICITY

    """

    # A PorousFailureCriteria object. 
    porousFailureCriteria: PorousFailureCriteria = PorousFailureCriteria()

    # A VoidNucleation object. 
    voidNucleation: VoidNucleation = VoidNucleation(((),))

    def __init__(self, table: tuple, relativeDensity: float = None, temperatureDependency: Boolean = OFF,
                 dependencies: int = 0):
        """This method creates a PorousMetalPlasticity object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].PorousMetalPlasticity
            - session.odbs[name].materials[name].PorousMetalPlasticity
        table
            A sequence of sequences of Floats specifying the items described below. 
        relativeDensity
            None or a Float specifying the initial relative density of the material, r0. The default 
            value is None. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A PorousMetalPlasticity object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the PorousMetalPlasticity object.

        Raises
        ------
            RangeError. 
        """
        pass
