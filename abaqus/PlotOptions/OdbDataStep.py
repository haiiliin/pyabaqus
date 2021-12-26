from abaqusConstants import *
from .OdbDataFrameArray import OdbDataFrameArray


class OdbDataStep:

    """The OdbDataStep object. 

    Access
    ------
        - import visualization
        - session.odbData[name].steps[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An OdbDataFrameArray object specifying the list of frames. The list is read-only. 
    frames: OdbDataFrameArray = OdbDataFrameArray()

    def setValues(self, activateFrames: Boolean, update: Boolean = OFF):
        """This method modifies the OdbDataStep object.

        Parameters
        ----------
        activateFrames
            A Boolean specifying whether to activate all the frames in the step. 
        update
            A Boolean specifying whether to update the model. The default value is ON 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

