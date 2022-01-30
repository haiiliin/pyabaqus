from .CommonOptions import CommonOptions
from .ContourOptions import ContourOptions
from .DisplayBodyOptions import DisplayBodyOptions
from .OrientationOptions import OrientationOptions
from .SuperimposeOptions import SuperimposeOptions
from .SymbolOptions import SymbolOptions
from ..PlotOptions.BasicOptions import BasicOptions
from ..PlotOptions.FreeBodyOptions import FreeBodyOptions
from ..PlotOptions.StreamOptions import StreamOptions
from ..PlotOptions.ViewCutOptions import ViewCutOptions


class DefaultOdbDisplay:
    """The DefaultOdbDisplay object is a limited-functionality version of the OdbDisplay
    object. 

    Attributes
    ----------
    basicOptions: BasicOptions
        A BasicOptions object.
    commonOptions: CommonOptions
        A CommonOptions object.
    contourOptions: ContourOptions
        A ContourOptions object.
    displayBodyOptions: DisplayBodyOptions
        A DisplayBodyOptions object.
    freeBodyOptions: FreeBodyOptions
        A FreeBodyOptions object.
    streamOptions: StreamOptions
        A StreamOptions object.
    materialOrientationOptions: OrientationOptions
        An OrientationOptions object.
    superimposeOptions: SuperimposeOptions
        A SuperimposeOptions object.
    symbolOptions: SymbolOptions
        A SymbolOptions object.
    viewCutOptions: ViewCutOptions
        A ViewCutOptions object.

    Notes
    -----
        This object can be accessed by:
        - import visualization
        - session.defaultOdbDisplay

    """

    # A BasicOptions object. 
    basicOptions: BasicOptions = BasicOptions()

    # A CommonOptions object. 
    commonOptions: CommonOptions = CommonOptions()

    # A ContourOptions object. 
    contourOptions: ContourOptions = ContourOptions()

    # A DisplayBodyOptions object. 
    displayBodyOptions: DisplayBodyOptions = DisplayBodyOptions()

    # A FreeBodyOptions object. 
    freeBodyOptions: FreeBodyOptions = FreeBodyOptions()

    # A StreamOptions object. 
    streamOptions: StreamOptions = StreamOptions()

    # An OrientationOptions object. 
    materialOrientationOptions: OrientationOptions = OrientationOptions()

    # A SuperimposeOptions object. 
    superimposeOptions: SuperimposeOptions = SuperimposeOptions()

    # A SymbolOptions object. 
    symbolOptions: SymbolOptions = SymbolOptions()

    # A ViewCutOptions object. 
    viewCutOptions: ViewCutOptions = ViewCutOptions()
