from abaqusConstants import *


class CyclicHardening:
    """The CyclicHardening object defines the evolution of the elastic domain for the nonlinear
    isotropic/kinematic hardening model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].Plastic.cyclicHardening
        - import odbMaterial
        - session.odbs[name].materials[name].Plastic.cyclicHardening

    Table Data
    ----------
        - Equivalent stress.
        - Q∞Q(only if *parameters*=ON).
        - Hardening parameter (only if *parameters*=ON).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CYCLIC HARDENING

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0,
                 parameters: Boolean = OFF):
        """This method creates a CyclicHardening object.

        Path
        ----
            - mdb.models[name].materials[name].Plastic.CyclicHardening
            - session.odbs[name].materials[name].Plastic.CyclicHardening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        parameters
            A Boolean specifying whether material parameters are to be input directly. The default 
            value is OFF. 

        Returns
        -------
            A CyclicHardening object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the CyclicHardening object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
