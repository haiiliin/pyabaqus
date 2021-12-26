from .MdbDataFrameArray import MdbDataFrameArray

class MdbDataStep:

    """The MdbDataStep object.It corresponds to same named step in the cae model. 

    Access
    ------
        - import visualization
        - session.mdbData[name].steps[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A MdbDataFrameArray object specifying the list of frames. The list is read-only. There 
    # is only one frame in a step. 
    frames: MdbDataFrameArray = MdbDataFrameArray()

