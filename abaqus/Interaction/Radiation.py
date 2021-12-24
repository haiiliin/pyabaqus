

class Radiation:

    """The Radiation object specifies radiation for a contact interaction property. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactionProperties[name].radiation

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - GAP RADIATION

    """

    def __init__(self, mainEmissivity: float, secondaryEmissivity: float, table: tuple):
        """This method creates a Radiation object.

        Path
        ----
            - mdb.models[name].interactionProperties[name].Radiation

        Parameters
        ----------
        mainEmissivity
            A Float specifying the emissivity of the main surface. 
        secondaryEmissivity
            A Float specifying the emissivity of the secondary surface. 
        table
            A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap 
            clearance, dd. 

        Returns
        -------
            A Radiation object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the Radiation object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

