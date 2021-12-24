

class DrawingArea:

    """The DrawingArea object specifies the location and size of the drawing area used for 
    placement of viewports. 

    Access
    ------
        - session.drawingArea

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Float specifying the width in millimeters. 
    width: float = None

    # A Float specifying the height in millimeters. 
    height: float = None

    # A pair of Floats specifying the coordinates of the bottom left hand corner in 
    # millimeters. 
    origin: tuple[float] = ()

