
class ActivateElements:
    """The ActivateElements object is used turn on progressive element activation within a step
    definition. 

    Access
    ------
        - mdb.models[name].steps[name].activateElements[key]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - ActivateElements
        - ElementProgressiveActivation

    """

    def __init__(self, tableCollection: str, activation: str, eigenTimeConst: str = '',
                 expansionTimeConstant: str = ''):
        """This method creates an ActivateElements object.

        Path
        ----
            - mdb.models[name].ActivateElements

        Parameters
        ----------
        tableCollection
            A String specifying the name of the tableCollection object. 
        activation
            A string specifying the name of progressive element activation. 
        eigenTimeConst
            A Double specifying the time constant used to ramp up the eigenstrains at element 
            activation. 
        expansionTimeConstant
            A Double specifying the time constant used to ramp up the thermal strains at element 
            activation. 

        Returns
        -------
            An ActivateElements object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the ActivateElements object.

        Parameters
        ----------

        Returns
        -------

        Raises
        ------
            RangeError. 
        """
        pass
