from abaqusConstants import *

class ConcreteCompressionDamage:

    """The ConcreteCompressionDamage object specifies hardening for the concrete damaged 
    plasticity model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].concreteDamagedPlasticity.concreteCompressionDamage
        - import odbMaterial
        - session.odbs[name].materials[name].concreteDamagedPlasticity.concreteCompressionDamage

    Table Data
    ----------
        - Compressive damage variable, dc.
        - Inelastic (crushing) strain, ϵci⁢n.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CONCRETE COMPRESSION DAMAGE

    """

    def __init__(self, table: tuple, tensionRecovery: float = 0, temperatureDependency: Boolean = OFF, 
                 dependencies: int = 0):
        """This method creates a ConcreteCompressionDamage object.

        Path
        ----
            - mdb.models[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionDamage
            - session.odbs[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionDamage

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        tensionRecovery
            A Float specifying the value of the stiffness recovery factor, wtwt, that determines the 
            amount of tension stiffness that is recovered as loading changes from compression to 
            tension. The default value is 0.0. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A ConcreteCompressionDamage object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the ConcreteCompressionDamage object.

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

