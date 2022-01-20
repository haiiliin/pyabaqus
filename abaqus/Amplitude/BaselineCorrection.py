class BaselineCorrection:
    """The BaselineCorrection object modifies an acceleration history to minimize the overall
    drift of the displacement obtained from the time integration of the given acceleration. 

    Access
    ------
        - import amplitude
        - mdb.models[name].amplitudes[name].baselineCorrection
        - import odbAmplitude
        - session.odbs[name].amplitudes[name].baselineCorrection

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - BASELINE CORRECTION

    """

    def __init__(self, intervals: tuple = ()):
        """This method creates a BaselineCorrection object.

        Path
        ----
            - mdb.models[name].amplitudes[name].BaselineCorrection
            - session.odbs[name].amplitudes[name].BaselineCorrection

        Parameters
        ----------
        intervals
            A sequence of Floats specifying the correction time interval end points. Possible values 
            are positive and monotonically increasing Floats. The default value is an empty 
            sequence. 

        Returns
        -------
            A BaselineCorrection object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the BaselineCorrection object.

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
