from abaqusConstants import *
from .XYData import XYData

"""This method writes an XYData object to a user-defined ASCII file. 

Access
------

Table Data
----------

Corresponding analysis keywords
-------------------------------

"""


def writeXYRepor(fileName: str, xyData: tuple[XYData], appendMode: Boolean = ON):
    """This method writes an XYData object to a user-defined ASCII file.

    Path
    ----
        - session.writeXYReport

    Parameters
    ----------
    fileName
        A String specifying the name of the file to which *X–Y* data will be written. 
    xyData
        A sequence of XYData objects to be written to the output file. 
    appendMode
        A Boolean specifying whether to append the *X–Y* data to the existing file. The default 
        value is ON. 

    Returns
    -------
        None. 

    Exceptions
    ----------
        None. 
    """
    pass
