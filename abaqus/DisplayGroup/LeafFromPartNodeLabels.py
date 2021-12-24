from ..Part.Part import Part
from .Leaf import Leaf
from abaqusConstants import *

class LeafFromPartNodeLabels(Leaf):

    """The LeafFromPartNodeLabels object can be used whenever a Leaf object is expected as an 
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromPartNodeLabels object is derived from the Leaf object. 

    Access
    ------
        - import displayGroupMdbToolset

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, part: Part, nodeLabels: tuple):
        """This method creates a Leaf object from a sequence of Strings specifying node labels.
        Leaf objects specify the items in a display group.

        Path
        ----
            - LeafFromPartNodeLabels

        Parameters
        ----------
        part
            A Part object. 
        nodeLabels
            A sequence of Strings specifying node labels. 

        Returns
        -------
            A LeafFromPartNodeLabels object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

