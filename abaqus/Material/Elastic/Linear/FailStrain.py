from abaqusConstants import *


class FailStrain:
    """The FailStrain object defines parameters for strain-based failure measures.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].elastic.failStrain
        - import odbMaterial
        - session.odbs[name].materials[name].elastic.failStrain

    Table Data
    ----------
        - Tensile strain limit in fiber direction, Xεt.
        - Compressive strain limit in fiber direction, Xεc.
        - Tensile strain limit in transverse direction, Yεt.
        - Compressive strain limit in transverse direction, Yεc.
        - Shear strain limit in the X–Y plane, Sε.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - FAIL STRAIN

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a FailStrain object.

        Path
        ----
            - mdb.models[name].materials[name].elastic.FailStrain
            - session.odbs[name].materials[name].elastic.FailStrain

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
            A FailStrain object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the FailStrain object.

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
