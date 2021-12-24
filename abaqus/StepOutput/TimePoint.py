

class TimePoint:

    """The TimePoint object defines time points at which data are written to the output 
    database or restart files. 

    Access
    ------
        - import step
        - mdb.models[name].timePoints[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - TIME POINTS

    """

    def __init__(self, name: str, points: tuple):
        """This method creates a TimePoint object.

        Path
        ----
            - mdb.models[name].TimePoint

        Parameters
        ----------
        name
            A String specifying the repository key. 
        points
            A sequence of sequences of Floats specifying time points at which data are written to 
            the output database or restart files. 

        Returns
        -------
            A TimePoint object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the TimePoint object.

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

