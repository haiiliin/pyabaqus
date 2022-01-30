from abaqusConstants import *


class PoreFluidExpansion:
    """The PoreFluidExpansion object specifies the thermal expansion coefficient for a
    hydraulic fluid. 

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].poreFluidExpansion
        - import odbMaterial
        - session.odbs[name].materials[name].poreFluidExpansion

    Table Data
    ----------
        - Mean coefficient of thermal expansion, α.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - EXPANSION

    """

    def __init__(self, table: tuple, zero: float = 0, temperatureDependency: Boolean = OFF,
                 dependencies: int = 0):
        """This method creates a PoreFluidExpansion object.

        Path
        ----
            - mdb.models[name].materials[name].PoreFluidExpansion
            - session.odbs[name].materials[name].PoreFluidExpansion

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        zero
            A Float specifying the value of θ0. The default value is 0.0. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A PoreFluidExpansion object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the PoreFluidExpansion object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Raises
        ------
            RangeError. 
        """
        pass
