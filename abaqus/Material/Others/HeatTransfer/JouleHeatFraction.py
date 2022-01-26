class JouleHeatFraction:
    """The JouleHeatFraction object defines the fraction of electric energy released as heat.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].jouleHeatFraction
        - import odbMaterial
        - session.odbs[name].materials[name].jouleHeatFraction

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - JOULE HEAT FRACTION

    """

    def __init__(self, fraction: float = 1):
        """This method creates a JouleHeatFraction object.

        Path
        ----
            - mdb.models[name].materials[name].JouleHeatFraction
            - session.odbs[name].materials[name].JouleHeatFraction

        Parameters
        ----------
        fraction
            A Float specifying the fraction of electrical energy released as heat, including any 
            unit conversion factor. The default value is 1.0. 

        Returns
        -------
            A JouleHeatFraction object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the JouleHeatFraction object.

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
