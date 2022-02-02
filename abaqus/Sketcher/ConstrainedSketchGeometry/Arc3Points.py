from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


class Arc3Points(ConstrainedSketchGeometry):

    def __init__(self, point1: tuple[float], point2: tuple[float], point3: tuple[float]):
        """This method constructs an arc using a two endpoints and an intermediate third point on
        the arc.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].sketches[name].Arc3Points
        point1
            A pair of Floats specifying the first endpoint of the arc. 
        point2
            A pair of Floats specifying the second endpoint of the arc. 
        point3
            A pair of Floats specifying the third point on the arc. 

        Returns
        -------
            A ConstrainedSketchGeometry object (None if the arc cannot be created). . 
            !img 
        """
        pass
