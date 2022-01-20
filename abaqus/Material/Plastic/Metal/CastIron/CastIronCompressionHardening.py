from abaqusConstants import *


class CastIronCompressionHardening:
    """The CastIronCompressionHardening object specifies hardening for the Cast- Iron
    plasticity model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].castIronPlasticity.castIronCompressionHardening
        - import odbMaterial
        - session.odbs[name].materials[name].castIronPlasticity.castIronCompressionHardening

    Table Data
    ----------
        - Yield stress in compression, σcσc.
        - The absolute value of the corresponding Plastic strain.(The first tabular value entered must always be zero.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CAST IRON COMPRESSION HARDENING

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a CastIronCompressionHardening object.

        Path
        ----
            - mdb.models[name].materials[name].castIronPlasticity\
            - .CastIronCompressionHardening
            - session.odbs[name].materials[name].castIronPlasticity\
            - .CastIronCompressionHardening

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
            A CastIronCompressionHardening object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the CastIronCompressionHardening object.

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
