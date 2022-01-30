from .Displayable import Displayable
from ..DisplayOptions.AssemblyDisplayOptions import AssemblyDisplayOptions
from ..DisplayOptions.PartDisplayOptions import PartDisplayOptions
from ..OdbDisplay.OdbDisplay import OdbDisplay
from ..UtilityAndView.View import View


class Layer:
    """Objects can be superimposed by displaying them in different layers of a viewport.

    Attributes
    ----------
    displayedObject: Displayable
        A Displayable object specifying the object to be displayed. The Displayable type is an
        abstract generalization. The concrete possible types are Part, Assembly,
        ConstrainedSketch, Odb, or XYPlot.
    view: View
        A View object specifying the object that controls viewing of the layer.
    odbDisplay: OdbDisplay
        An OdbDisplay object specifying the display options for the Odb object.
    partDisplay: PartDisplayOptions
        A PartDisplayOptions object specifying the display options for the Part object.
    assemblyDisplay: AssemblyDisplayOptions
        An AssemblyDisplayOptions object specifying the display options for the Assembly object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        session.viewports[name].layers[name]

    """

    # A Displayable object specifying the object to be displayed. The Displayable type is an 
    # abstract generalization. The concrete possible types are Part, Assembly, 
    # ConstrainedSketch, Odb, or XYPlot. 
    displayedObject: Displayable = Displayable()

    # A View object specifying the object that controls viewing of the layer. 
    view: View = None

    # An OdbDisplay object specifying the display options for the Odb object. 
    odbDisplay: OdbDisplay = OdbDisplay()

    # A PartDisplayOptions object specifying the display options for the Part object. 
    partDisplay: PartDisplayOptions = PartDisplayOptions()

    # An AssemblyDisplayOptions object specifying the display options for the Assembly object. 
    assemblyDisplay: AssemblyDisplayOptions = AssemblyDisplayOptions()

    def __init__(self, name: str, copyViewName: str = ''):
        """This method creates a Layer object in the Layer repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.viewports[name].Layer

        Parameters
        ----------
        name
            A String specifying the repository key. 
        copyViewName
            A String specifying the name of the layer to copy. 

        Returns
        -------
            A Layer object. . 
        """
        pass

    def moveBefore(self, name: str):
        """This method moves the layer object before another object in the layer repository.

        Parameters
        ----------
        name
            A String specifying the name of the other Layer object. 
        """
        pass

    def moveAfter(self, name: str):
        """This method moves the layer object after another object in the layer repository.

        Parameters
        ----------
        name
            A String specifying the name of the other Layer object. 
        """
        pass
