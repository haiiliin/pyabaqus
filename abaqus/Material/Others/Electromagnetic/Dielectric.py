from abaqusConstants import *


class Dielectric:
    """The Dielectric object specifies dielectric material properties.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].dielectric
        - import odbMaterial
        - session.odbs[name].materials[name].dielectric

    Table Data
    ----------
        If *type*=ISOTROPIC, the table data specify the following:
        - Dielectric constant.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=ORTHOTROPIC, the table data specify the following:
        - Dφ11.
        - Dφ2φ.
        - Dφ3φ.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=ANISOTROPIC, the table data specify the following:
        - Dφ11.
        - Dφ12.
        - Dφ22.
        - Dφ13.
        - Dφ23.
        - Dφ33.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - DIELECTRIC

    """

    def __init__(self, table: tuple, type: SymbolicConstant = ISOTROPIC, frequencyDependency: Boolean = OFF,
                 temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a Dielectric object.

        Path
        ----
            - mdb.models[name].materials[name].Dielectric
            - session.odbs[name].materials[name].Dielectric

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        type
            A SymbolicConstant specifying the dielectric behavior. Possible values are ISOTROPIC, 
            ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC. 
        frequencyDependency
            A Boolean specifying whether the data depend on frequency. The default value is OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A Dielectric object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the Dielectric object.

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
