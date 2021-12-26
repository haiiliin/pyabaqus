from abaqusConstants import *
from .Constraint import Constraint


class Equation(Constraint):

    """The Equation object defines a linear multi-point constraint between a set of degrees of 
    freedom. 
    The Equation object is derived from the Constraint object. 

    Access
    ------
        - import interaction
        - mdb.models[name].constraints[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - EQUATION

    """

    # A Boolean specifying whether the constraint is suppressed or not. The default value is 
    # OFF. 
    suppressed: Boolean = OFF

    def __init__(self, name: str, terms: tuple):
        """This method creates an Equation object.

        Path
        ----
            - mdb.models[name].Equation

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        terms
            A sequence of (Float, String, Int, Int) sequences specifying a coefficient, Set name, 
            degree of freedom, and coordinate system ID. The coordinate system ID is optional. 

        Returns
        -------
            An Equation object. 

        Exceptions
        ----------
            - If *terms* does not contain more than one entry: 
              Equation must have two or more terms. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the Equation object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            - If *terms* does not contain more than one entry: 
              Equation must have two or more terms. 
        """
        pass

