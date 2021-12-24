from ..Region.Region import Region
from ..UtilityAndView.Repository import Repository
from .Crack import Crack
from .Fastener import Fastener
from .Inertia import Inertia
from .SpringDashpot import SpringDashpot

class EngineeringFeature:

    """The EngineeringFeature object is a container for various specific engineering feature 
    repositories. The EngineeringFeature object has no explicit constructor or methods. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].engineeringFeatures
        - import assembly
        - mdb.models[name].rootAssembly.engineeringFeatures

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A repository of Inertia objects. 
    inertias: Repository[str, Inertia] = None

    # A repository of Crack objects. 
    cracks: Repository[str, Crack] = None

    # A repository of Fastener objects. 
    fasteners: Repository[str, Fastener] = None

    # A repository of SpringDashpot objects. 
    springDashpots: Repository[str, SpringDashpot] = None

    def assignSeam(self, regions: tuple[Region]):
        """This method creates a seam crack along an edge or a face.

        Parameters
        ----------
        regions
            A sequence of Region objects specifying the domain of the seam crack. The Region objects 
            must be faces or edges. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def deleteSeam(self, regions: tuple[Region]):
        """This method deletes a seam crack.

        Parameters
        ----------
        regions
            A sequence of Region objects specifying the domain of the seam crack. The Region objects 
            must be faces or edges. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

