class Gel:
    """The Gel object defines a swelling gel.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].gel
        - import odbMaterial
        - session.odbs[name].materials[name].gel

    Table Data
    ----------
        - Radius of gel particles when completely dry, radry.
        - Fully swollen radius of gel particles, raf.
        - Number of gel particles per unit volume, ka.
        - Relaxation time constant for long-term swelling of gel particles, τ1.

    Corresponding analysis keywords
    -------------------------------
        - GEL

    """

    def __init__(self, table: tuple):
        """This method creates a Gel object.

        Path
        ----
            - mdb.models[name].materials[name].Gel
            - session.odbs[name].materials[name].Gel

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 

        Returns
        -------
            A Gel object. . 
        """
        pass

    def setValues(self):
        """This method modifies the Gel object.

        Parameters
        ----------
        """
        pass
