from abaqusConstants import *
from .Amplitude import Amplitude


class SmoothStepAmplitude(Amplitude):

    """The SmoothStepAmplitude object defines an amplitude that ramps up or down smoothly from 
    one data point to another. 
    The SmoothStepAmplitude object is derived from the Amplitude object. 

    Access
    ------
        - import amplitude
        - mdb.models[name].amplitudes[name]
        - import odbAmplitude
        - session.odbs[name].amplitudes[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - AMPLITUDE

    """

    def __init__(self, name: str, data: tuple, timeSpan: SymbolicConstant = STEP):
        """This method creates a SmoothStepAmplitude object.

        Path
        ----
            - mdb.models[name].SmoothStepAmplitude
            - session.odbs[name].SmoothStepAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        data
            A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible 
            values for time/frequency are positive numbers. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A SmoothStepAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, timeSpan: SymbolicConstant = STEP):
        """This method modifies the SmoothStepAmplitude object.

        Parameters
        ----------
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

