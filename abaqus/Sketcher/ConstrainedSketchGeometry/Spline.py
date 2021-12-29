from abaqusConstants import *
from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


class Spline(ConstrainedSketchGeometry):

    def __init__(self, points: tuple, constrainPoints: Boolean = True):
        """This method creates a spline curve running through a sequence of points.

        Path
        ----
            - mdb.models[name].sketches[name].Spline

        Parameters
        ----------
        points
            A sequence of pairs of Floats specifying the points through which the spline passes. 
        constrainPoints
            A Boolean that determines whether the points given are to constrained to always remain 
            on the __init__. The default is True. For a large sequence of *points*, significant 
            performance gains may be achieved by setting the value to False. 

        Returns
        -------
            A ConstrainedSketchGeometry object (None if the spline cannot be created). 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass
