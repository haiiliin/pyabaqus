from abaqusConstants import *


class CastIronTensionHardening:
    """The CastIronTensionHardening object specifies hardening for the Cast- Iron plasticity
    model. 

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].castIronPlasticity.castIronTensionHardening
        - import odbMaterial
        - session.odbs[name].materials[name].castIronPlasticity.castIronTensionHardening

    Table Data
    ----------
        - Yield stress in uniaxial tension, σt.
        - The absolute value of the corresponding Plastic strain.(The first tabular value entered must always be zero.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CAST IRON TENSION HARDENING

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a CastIronTensionHardening object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].castIronPlasticity\
            - .CastIronTensionHardening
            - session.odbs[name].materials[name].castIronPlasticity\
            - .CastIronTensionHardening
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A CastIronTensionHardening object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the CastIronTensionHardening object.

        Raises
        ------
            RangeError. 
        """
        pass
