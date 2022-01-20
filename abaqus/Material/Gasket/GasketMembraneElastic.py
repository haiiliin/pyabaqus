from abaqusConstants import *


class GasketMembraneElastic:
    """The GasketMembraneElastic object defines the elastic parameters for the membrane shear
    behavior of a gasket. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].gasketMembraneElastic
        - import odbMaterial
        - session.odbs[name].materials[name].gasketMembraneElastic

    Table Data
    ----------
        - Young's modulus, E.
        - Poisson's ratio, ν.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - GASKET ELASTICITY

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a GasketMembraneElastic object.

        Path
        ----
            - mdb.models[name].materials[name].GasketMembraneElastic
            - session.odbs[name].materials[name].GasketMembraneElastic

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
            A GasketMembraneElastic object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the GasketMembraneElastic object.

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
