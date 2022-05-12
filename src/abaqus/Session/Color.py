from __init__ import *
from __future__ import annotations


class Color:
    """The Color object contains the RGB definition of a system color.

    Attributes
    ----------
    name: str
        A String specifying the name of the color.
    rgb: float
        A Tuple of three Floats specifying the RGB value of the color. The Float values must be
        between 0.0 and 1.0.

    Notes
    -----
        This object can be accessed by:
            session.colors[name]

    """

    # A String specifying the name of the color.
    name: str = ''

    # A Tuple of three Floats specifying the RGB value of the color. The Float values must be
    # between 0.0 and 1.0.
    rgb: float = None

    def setByRGB(self, rgb: Tuple):
        """This method changes the RGB value of a user-defined color. However, users cannot define
        colors, and this method does not modify system-defined colors.
        
        Parameters
        ----------
        rgb
            A sequence of three Floats specifying the RGB value of the color. The Float values must 
            be between 0.0 and 1.0. 
        """
        pass
