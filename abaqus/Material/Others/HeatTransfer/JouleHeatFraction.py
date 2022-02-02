class JouleHeatFraction:
    """The JouleHeatFraction object defines the fraction of electric energy released as heat.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].jouleHeatFraction
        - import odbMaterial
        - session.odbs[name].materials[name].jouleHeatFraction

    Corresponding analysis keywords
    -------------------------------
        - JOULE HEAT FRACTION

    """

    def __init__(self, fraction: float = 1):
        """This method creates a JouleHeatFraction object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].JouleHeatFraction
            - session.odbs[name].materials[name].JouleHeatFraction
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

        Raises
        ------
            RangeError. 
        """
        pass
