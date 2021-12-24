

class UserOutputVariables:

    """The UserOutputVariables object specifies the number of user-defined output variables. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].userOutputVariables
        - import odbMaterial
        - session.odbs[name].materials[name].userOutputVariables

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - USER OUTPUT VARIABLES

    """

    def __init__(self, n: int = 0):
        """This method creates a UserOutputVariables object.

        Path
        ----
            - mdb.models[name].materials[name].UserOutputVariables
            - session.odbs[name].materials[name].UserOutputVariables

        Parameters
        ----------
        n
            An Int specifying the number of user-defined variables required at each material point. 
            The default value is 0. 

        Returns
        -------
            A UserOutputVariables object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the UserOutputVariables object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

