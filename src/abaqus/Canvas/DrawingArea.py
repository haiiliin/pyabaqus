from __init__ import *
from __future__ import annotations


class DrawingArea:
    """The DrawingArea object specifies the location and size of the drawing area used for
    placement of viewports. 

    Attributes
    ----------
    width: float
        A Float specifying the width in millimeters.
    height: float
        A Float specifying the height in millimeters.
    origin: Tuple[float]
        A pair of Floats specifying the coordinates of the bottom left hand corner in
        millimeters.

    Notes
    -----
        This object can be accessed by:
            session.drawingArea

    """

    # A Float specifying the width in millimeters.
    width: float = None

    # A Float specifying the height in millimeters.
    height: float = None

    # A pair of Floats specifying the coordinates of the bottom left hand corner in
    # millimeters.
    origin: Tuple[float] = ()
