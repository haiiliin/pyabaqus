from .DGCommonOptions import DGCommonOptions
from .DGContourOptions import DGContourOptions
from .DGDisplayBodyOptions import DGDisplayBodyOptions
from .DGOrientationOptions import DGOrientationOptions
from .DGSuperimposeOptions import DGSuperimposeOptions
from .DGSymbolOptions import DGSymbolOptions

class OdbDisplayOptions:

    """The OdbDisplayOptions object stores the display options associated with an OdbInstance 
    object. This object does not have a constructor. Abaqus creates the OdbDisplayOptions 
    object when an OdbInstance object is created using the display options associated with 
    the current viewport at the time of creation. 

    Access
    ------
        - import assembly
        - session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions
        - session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions
        - import visualization
        - session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions
        - import part
        - session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions
        - session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions
        - session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A DGCommonOptions object. 
    commonOptions: DGCommonOptions = None

    # A DGSuperimposeOptions object. 
    superimposeOptions: DGSuperimposeOptions = None

    # A DGContourOptions object. 
    contourOptions: DGContourOptions = None

    # A DGSymbolOptions object. 
    symbolOptions: DGSymbolOptions = None

    # A DGOrientationOptions object. 
    materialOrientationOptions: DGOrientationOptions = None

    # A DGDisplayBodyOptions object. 
    displayBodyOptions: DGDisplayBodyOptions = None

