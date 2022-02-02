from abaqusConstants import *


class Solubility:
    """The Solubility object specifies solubility.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].solubility
        - import odbMaterial
        - session.odbs[name].materials[name].solubility

    Table Data
    ----------
        - Solubility.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - SOLUBILITY

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a Solubility object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].Solubility
            - session.odbs[name].materials[name].Solubility
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A Solubility object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Solubility object.

        Raises
        ------
            RangeError. 
        """
        pass
