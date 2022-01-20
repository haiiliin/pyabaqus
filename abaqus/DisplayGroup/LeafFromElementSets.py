from abaqusConstants import *
from .Leaf import Leaf


class LeafFromElementSets(Leaf):
    """The LeafFromElementSets object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromElementSets object is derived from the Leaf object. 

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

    def __init__(self, elementSets: tuple):
        """This method creates a Leaf object from a sequence of element sets.

        Path
        ----
            - LeafFromElementSets

        Parameters
        ----------
        elementSets
            A sequence of Strings specifying element sets or a String specifying a single element 
            set. 

        Returns
        -------
            A LeafFromElementSets object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__(DEFAULT_MODEL)
        pass
