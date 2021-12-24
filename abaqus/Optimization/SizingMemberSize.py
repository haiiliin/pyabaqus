from ..Region.Region import Region
from .GeometricRestriction import GeometricRestriction

class SizingMemberSize(GeometricRestriction):

    """The SizingMemberSize object defines a sizing member size geometric restriction. 
    The SizingMemberSize object is derived from the GeometricRestriction object. 

    Access
    ------
        - import optimization
        - mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self, name: str, region: Region, minWidth: float):
        """This method creates a SizingMemberSize object.

        Path
        ----
            -           mdb.models[name].optimizationTasks[name].SizingMemberSize

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
        minWidth
            A Float specifying the min width. 

        Returns
        -------

        Exceptions
        ----------
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the sizingMemberSize object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

