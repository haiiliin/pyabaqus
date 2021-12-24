from .Behavior import Behavior
from .DataSet import DataSet

class Calibration:

    """A Calibration object is the object used to specify a material calibration. The 
    Calibration object stores the data that is used for specifying materials from test data. 

    Access
    ------
        - import calibration
        - mdb.models[name].calibrations[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A DataSet object. 
    dataSets: DataSet = None

    # A Behavior object. 
    behaviors: Behavior = None

    def __init__(self, name: str):
        """This method creates a Calibration object.

        Path
        ----
            -           mdb.models[name].Calibration

        Parameters
        ----------
        name
            A String specifying the name of the new calibration. 

        Returns
        -------
            A Calibration object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

