from abaqusConstants import *


class VoidNucleation:
    """The VoidNucleation object defines the nucleation of voids in a porous material.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].porousMetalPlasticity.voidNucleation
        - import odbMaterial
        - session.odbs[name].materials[name].porousMetalPlasticity.voidNucleation

    Table Data
    ----------
        - εN, the mean value of the nucleation-strain normal distribution.
        - sN, the standard deviation of the nucleation-strain normal distribution.
        - fN, the volume fraction of nucleating voids.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - VOID NUCLEATION

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a VoidNucleation object.

        Path
        ----
            - mdb.models[name].materials[name].porousMetalPlasticity.VoidNucleation
            - session.odbs[name].materials[name].porousMetalPlasticity\
            - .VoidNucleation

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
            A VoidNucleation object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the VoidNucleation object.

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
