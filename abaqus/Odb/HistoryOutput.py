from abaqusConstants import *

class HistoryOutput:

    """The HistoryOutput object contains the history output at a point for the specified 
    variable. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].steps[name].historyRegions[name].historyOutputs[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A tuple of pairs of Floats specifying the pairs (*frameValue*, *value*) where 
    # *frameValue* is either time, frequency, or mode and *value* is the value of the 
    # specified variable at *frameValue*. (This value depends on the type of the variable.) 
    data: float = None

    # A tuple of pairs of Floats specifying the imaginary portion of a specified complex 
    # variable at each frame value (time, frequency, or mode). The pairs have the form 
    # (*frameValue*, *value*). 
    conjugateData: float = None

    def __init__(self, name: str, description: str, type: SymbolicConstant, 
                 validInvariants: SymbolicConstant = None):
        """This method creates a HistoryOutput object.

        Path
        ----
            - session.odbs[name].steps[name].historyRegions[name].HistoryOutput

        Parameters
        ----------
        name
            A String specifying the output variable name. 
        description
            A String specifying the output variable. 
        type
            A SymbolicConstant specifying the output type. Only SCALAR is currently supported. 
        validInvariants
            A sequence of SymbolicConstants specifying which invariants should be calculated for 
            this field. Possible values are MAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL, 
            MID_PRINCIPAL, and MIN_PRINCIPAL. The default value is an empty sequence. 

        Returns
        -------
            A HistoryOutput object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def addData(self, data: tuple):
        """This method adds data to the *data* member of the HistoryOutput object.

        Parameters
        ----------
        data
            A sequence of pairs of Floats specifying the pairs (*frameValue*, *value*) where 
            *frameValue* is either time, frequency, or mode and *value* is the value of the 
            specified variable at *frameValue*. (This value depends on the type of the variable.) 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

