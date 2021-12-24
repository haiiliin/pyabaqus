from .PlyStackPlotOptions import PlyStackPlotOptions

class DetailPlotOptions:

    """The DetailPlotOptions object stores values and attributes associated with a Viewport 
    object. The DetailPlotOptions object has no constructor command. Abaqus creates the 
    *detailPlotOptions* member whenever a Viewport is created. 

    Access
    ------
        - session.viewports[name].detailPlotOptions

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A PlyStackPlotOptions object. 
    plyStackPlotOptions: PlyStackPlotOptions = None

