class LatentHeat:
    """The LatentHeat object specifies a material's latent heat.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].latentHeat
        - import odbMaterial
        - session.odbs[name].materials[name].latentHeat

    Table Data
    ----------
        - Latent heat per unit mass.
        - Solidus temperature.
        - Liquidus temperature.

    Corresponding analysis keywords
    -------------------------------
        - LATENT HEAT

    """

    def __init__(self, table: tuple):
        """This method creates a LatentHeat object.

        Path
        ----
            - mdb.models[name].materials[name].LatentHeat
            - session.odbs[name].materials[name].LatentHeat

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 

        Returns
        -------
            A LatentHeat object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the LatentHeat object.

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
