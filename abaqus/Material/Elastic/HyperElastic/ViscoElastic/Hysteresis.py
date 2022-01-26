
class Hysteresis:
    """The Hysteresis object specifies the creep part of the material model for the hysteretic
    behavior of elastomers. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].hyperelastic.hysteresis
        - import odbMaterial
        - session.odbs[name].materials[name].hyperelastic.hysteresis

    Table Data
    ----------
        - Stress scaling factor.
        - Creep parameter.
        - Effective stress exponent.
        - Creep strain exponent.

    Corresponding analysis keywords
    -------------------------------
        - HYSTERESIS

    """

    def __init__(self, table: tuple):
        """This method creates a Hysteresis object.

        Path
        ----
            - mdb.models[name].materials[name].hyperelastic.Hysteresis
            - session.odbs[name].materials[name].hyperelastic.Hysteresis

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 

        Returns
        -------
            A Hysteresis object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Hysteresis object.

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
