from abaqusConstants import *
from .CastIronCompressionHardening import CastIronCompressionHardening
from .CastIronTensionHardening import CastIronTensionHardening


class CastIronPlasticity:

    """The CastIronPlasticity object specifies the Cast Iron plasticity model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].castIronPlasticity
        - import odbMaterial
        - session.odbs[name].materials[name].castIronPlasticity

    Table Data
    ----------
        The table data specify the following:
        - Plastic Poisson's ratio, νp⁢l (dimensionless).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CAST IRON PLASTICITY

    """

    # A CastIronTensionHardening object. 
    castIronTensionHardening: CastIronTensionHardening = None

    # A CastIronCompressionHardening object. 
    castIronCompressionHardening: CastIronCompressionHardening = None

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a CastIronPlasticity object.

        Path
        ----
            - mdb.models[name].materials[name].CastIronPlasticity
            - session.odbs[name].materials[name].CastIronPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A CastIronPlasticity object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the CastIronPlasticity object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

