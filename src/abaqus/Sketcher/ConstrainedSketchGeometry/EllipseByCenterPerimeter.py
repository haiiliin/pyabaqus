from .ConstrainedSketchGeometry import ConstrainedSketchGeometry

from __init__ import *
from __future__ import annotations


class EllipseByCenterPerimeter(ConstrainedSketchGeometry):
    def __init__(self, center: Tuple[float], axisPoint1: Tuple[float],
                 axisPoint2: Tuple[float]):
        """This method constructs an ellipse using a center point, a major axis point, and a minor
        axis point. The ellipse is added to the geometry repository of the ConstrainedSketch
        object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].EllipseByCenterPerimeter
        
        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the ellipse. 
        axisPoint1
            A pair of Floats specifying the major or minor axis point of the ellipse. 
        axisPoint2
            A pair of Floats specifying the minor or major axis point of the ellipse. 

        Returns
        -------
            A ConstrainedSketchGeometry object (None if the ellipse cannot be created).
            
        """
        pass
