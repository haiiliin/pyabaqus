from abaqusConstants import *


class Hypoelastic:
    """The Hypoelastic object specifies hypoelastic material properties.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].hypoelastic
        - import odbMaterial
        - session.odbs[name].materials[name].hypoelastic

    Table Data
    ----------
        - Instantaneous Young's modulus, E.
        - Instantaneous Poisson's ratio, ν.
        - First strain invariant, I1.
        - Second strain invariant, I2.
        - Third strain invariant, I3.

    Corresponding analysis keywords
    -------------------------------
        - HYPOELASTIC

    """

    def __init__(self, table: tuple, user: Boolean = OFF):
        """This method creates a Hypoelastic object.

        Path
        ----
            - mdb.models[name].materials[name].Hypoelastic
            - session.odbs[name].materials[name].Hypoelastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        user
            A Boolean specifying that hypoelasticity is defined by user subroutine UHYPEL. The 
            default value is OFF. 

        Returns
        -------
            A Hypoelastic object. . 
        """
        pass

    def setValues(self):
        """This method modifies the Hypoelastic object.

        Parameters
        ----------
        """
        pass
