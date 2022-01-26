from abaqusConstants import *


class ConcreteCompressionHardening:
    """The ConcreteCompressionHardening object specifies hardening for the concrete damaged
    plasticity model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].concreteDamagedPlasticity.concreteCompressionHardening
        - import odbMaterial
        - session.odbs[name].materials[name].concreteDamagedPlasticity.concreteCompressionHardening

    Table Data
    ----------
        - Yield stress in compression, σcσc.
        - Plastic (crushing) strain, ϵinc
        - Plastic (crushing) strain rate, ϵinc
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CONCRETE COMPRESSION HARDENING

    """

    def __init__(self, table: tuple, rate: Boolean = OFF, temperatureDependency: Boolean = OFF,
                 dependencies: int = 0):
        """This method creates a ConcreteCompressionHardening object.

        Path
        ----
            - mdb.models[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionHardening
            - session.odbs[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionHardening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        rate
            A Boolean specifying whether the data depend on rate. The default value is OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A ConcreteCompressionHardening object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the ConcreteCompressionHardening object.

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
