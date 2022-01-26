from abaqusConstants import *


class DruckerPragerHardening:
    """The DruckerPragerHardening object specifies hardening for Drucker-Prager plasticity
    models. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].druckerPrager.druckerPragerHardening
        - import odbMaterial
        - session.odbs[name].materials[name].druckerPrager.druckerPragerHardening

    Table Data
    ----------
        - Yield stress.
        - Absolute value of the corresponding Plastic strain. (The first tabular value entered must always be zero.)
        - Equivalent Plastic strain rate, ˙¯εpl, for which this hardening curve applies.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - DRUCKER PRAGER HARDENING

    """

    def __init__(self, table: tuple, type: SymbolicConstant = COMPRESSION, rate: Boolean = OFF,
                 temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a DruckerPragerHardening object.

        Path
        ----
            - mdb.models[name].materials[name].druckerPrager.DruckerPragerHardening
            - session.odbs[name].materials[name].druckerPrager\
            - .DruckerPragerHardening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        type
            A SymbolicConstant specifying the type of data defining the hardening behavior. Possible 
            values are COMPRESSION, TENSION, and SHEAR. The default value is COMPRESSION. 
        rate
            A Boolean specifying whether the data depend on rate. The default value is OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A DruckerPragerHardening object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the DruckerPragerHardening object.

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
