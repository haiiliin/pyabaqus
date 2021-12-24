from ..PlotOptions.BasicOptions import BasicOptions
from ..PlotOptions.FreeBodyOptions import FreeBodyOptions
from ..PlotOptions.StreamOptions import StreamOptions
from ..PlotOptions.ViewCutOptions import ViewCutOptions
from .CommonOptions import CommonOptions
from .ContourOptions import ContourOptions
from .DisplayBodyOptions import DisplayBodyOptions
from .OrientationOptions import OrientationOptions
from .SuperimposeOptions import SuperimposeOptions
from .SymbolOptions import SymbolOptions

class DefaultOdbDisplay:

    """The DefaultOdbDisplay object is a limited-functionality version of the OdbDisplay 
    object. 

    Access
    ------
        - import visualization
        - session.defaultOdbDisplay

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A BasicOptions object. 
    basicOptions: BasicOptions = None

    # A CommonOptions object. 
    commonOptions: CommonOptions = None

    # A ContourOptions object. 
    contourOptions: ContourOptions = None

    # A DisplayBodyOptions object. 
    displayBodyOptions: DisplayBodyOptions = None

    # A FreeBodyOptions object. 
    freeBodyOptions: FreeBodyOptions = None

    # A StreamOptions object. 
    streamOptions: StreamOptions = None

    # An OrientationOptions object. 
    materialOrientationOptions: OrientationOptions = None

    # A SuperimposeOptions object. 
    superimposeOptions: SuperimposeOptions = None

    # A SymbolOptions object. 
    symbolOptions: SymbolOptions = None

    # A ViewCutOptions object. 
    viewCutOptions: ViewCutOptions = None

