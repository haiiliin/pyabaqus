from .ConstrainedSketchGeometry import ConstrainedSketchGeometry

from __init__ import *
from __future__ import annotations


class Arc3Points(ConstrainedSketchGeometry):
    def __init__(self, point1: Tuple[float], point2: Tuple[float],
                 point3: Tuple[float]):
        """This method constructs an arc using a two endpoints and an intermediate third point on
        the arc.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].Arc3Points
        
        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint of the arc. 
        point2
            A pair of Floats specifying the second endpoint of the arc. 
        point3
            A pair of Floats specifying the third point on the arc. 

        Returns
        -------
            A ConstrainedSketchGeometry object (None if the arc cannot be created).
            
        """
        pass
