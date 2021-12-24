from ..Region.Region import Region
from .GeometricRestriction import GeometricRestriction

class SizingFrozenArea(GeometricRestriction):

    """The SizingFrozenArea object defines a sizing frozen area geometric restriction. 
    The SizingFrozenArea object is derived from the GeometricRestriction object. 

    Access
    ------
        - import optimization
        - mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self, name: str, region: Region):
        """This method creates a SizingFrozenArea object.

        Path
        ----
            -           mdb.models[name].optimizationTasks[name].SizingFrozenArea

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 

        Returns
        -------
            A SizingFrozenArea object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the SizingFrozenArea object.

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

