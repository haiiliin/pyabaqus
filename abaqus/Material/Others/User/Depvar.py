class Depvar:
    """The Depvar object specifies solution-dependent state variables.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].depvar
        - import odbMaterial
        - session.odbs[name].materials[name].depvar

    Corresponding analysis keywords
    -------------------------------
        - DEPVAR

    """

    def __init__(self, deleteVar: int = 0, n: int = 0):
        """This method creates a Depvar object.

        Path
        ----
            - mdb.models[name].materials[name].Depvar
            - session.odbs[name].materials[name].Depvar

        Parameters
        ----------
        deleteVar
            An Int specifying the state variable number controlling the element deletion flag. The 
            default value is 0.This argument applies only to Abaqus/Explicit analyses. 
        n
            An Int specifying the number of solution-dependent state variables required at each 
            integration point. The default value is 0. 

        Returns
        -------
            A Depvar object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Depvar object.

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
