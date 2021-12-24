from ..Region.Region import Region
from .GeometricRestriction import GeometricRestriction

class BeadGrowth(GeometricRestriction):

    """The BeadGrowth object defines a growth geometric restriction. 
    The BeadGrowth object is derived from the GeometricRestriction object. 

    Access
    ------
        - import optimization
        - mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self, name: str, region: Region, beadGrowth: float = 0, shrink: float = 0):
        """This method creates a BeadGrowth object.

        Path
        ----
            -           mdb.models[name].optimizationTasks[name].BeadGrowth

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
        beadGrowth
            A Float specifying the maximum optimization displacement in the growth direction. Either 
            *beadGrowth* or *shrink* or both must be specified. The default value is 0.0. 
        shrink
            A Float specifying the maximum optimization displacement in the shrink direction. Either 
            *beadGrowth* or *shrink* or both must be specified The default value is 0.0. 

        Returns
        -------
            A BeadGrowth object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, beadGrowth: float = 0, shrink: float = 0):
        """This method modifies the BeadGrowth object.

        Parameters
        ----------
        beadGrowth
            A Float specifying the maximum optimization displacement in the growth direction. Either 
            *beadGrowth* or *shrink* or both must be specified. The default value is 0.0. 
        shrink
            A Float specifying the maximum optimization displacement in the shrink direction. Either 
            *beadGrowth* or *shrink* or both must be specified The default value is 0.0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

