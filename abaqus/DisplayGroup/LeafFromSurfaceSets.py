from .Leaf import Leaf
from abaqusConstants import *

class LeafFromSurfaceSets(Leaf):

    """The LeafFromSurfaceSets object can be used whenever a Leaf object is expected as an 
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromSurfaceSets object is derived from the Leaf object. 

    Access
    ------
        - import displayGroupOdbToolset

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, surfaceSets: tuple):
        """This method creates a Leaf object from a sequence of surface sets.

        Path
        ----
            - LeafFromSurfaceSets

        Parameters
        ----------
        surfaceSets
            A sequence of Strings specifying surface sets, or a String specifying a single surface 
            set. 

        Returns
        -------
            A LeafFromSurfaceSets object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

