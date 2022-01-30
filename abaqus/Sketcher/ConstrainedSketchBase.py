from .ConstrainedSketchConstraint.ConstrainedSketchConstraint import ConstrainedSketchConstraint
from .ConstrainedSketchDimension.ConstrainedSketchDimension import ConstrainedSketchDimension
from .ConstrainedSketchOptions.ConstrainedSketchImageOptions import ConstrainedSketchImageOptions
from .ConstrainedSketchOptions.ConstrainedSketchOptions import ConstrainedSketchOptions
from .ConstrainedSketchParameter.ConstrainedSketchParameter import ConstrainedSketchParameter
from .ConstrainedSketchVertex.ConstrainedSketchVertexArray import ConstrainedSketchVertexArray
from ..Amplitude.ConstrainedSketchGeometryArray import ConstrainedSketchGeometryArray


class ConstrainedSketchBase:
    """A ConstrainedSketch object contains the entities that are used to create a sketch. The
    objects include ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository,
    such as Line, Arc, and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and ConstrainedSketchParameter objects are
    contained in their respective repositories. 

    Attributes
    ----------
    constraints: dict[str, ConstrainedSketchConstraint]
        A repository of ConstrainedSketchConstraint objects.
    dimensions: dict[str, ConstrainedSketchDimension]
        A repository of ConstrainedSketchDimension objects.
    geometry: ConstrainedSketchGeometryArray
        A ConstrainedSketchGeometryArray object specifying the sketch geometry, such as lines,
        arcs, circles, and splines.
    parameters: dict[str, ConstrainedSketchParameter]
        A repository of ConstrainedSketchParameter objects specifying sketch parameters, which
        may be associated with dimensions.
    sketchOptions: ConstrainedSketchOptions
        A ConstrainedSketchOptions object specifying the sketch option settings.
    vertices: ConstrainedSketchVertexArray
        A ConstrainedSketchVertexArray object.
    imageOptions: ConstrainedSketchImageOptions
        A ConstrainedSketchImageOptions object.

    Notes
    -----
        This object can be accessed by:
        - import sketch
        - mdb.models[name].sketches[name]

    """

    # A repository of ConstrainedSketchConstraint objects. 
    constraints: dict[str, ConstrainedSketchConstraint] = dict[str, ConstrainedSketchConstraint]()

    # A repository of ConstrainedSketchDimension objects. 
    dimensions: dict[str, ConstrainedSketchDimension] = dict[str, ConstrainedSketchDimension]()

    # A ConstrainedSketchGeometryArray object specifying the sketch geometry, such as lines, 
    # arcs, circles, and splines. 
    geometry: ConstrainedSketchGeometryArray = ConstrainedSketchGeometryArray()

    # A repository of ConstrainedSketchParameter objects specifying sketch parameters, which 
    # may be associated with dimensions. 
    parameters: dict[str, ConstrainedSketchParameter] = dict[str, ConstrainedSketchParameter]()

    # A ConstrainedSketchOptions object specifying the sketch option settings. 
    sketchOptions: ConstrainedSketchOptions = ConstrainedSketchOptions()

    # A ConstrainedSketchVertexArray object. 
    vertices: ConstrainedSketchVertexArray = ConstrainedSketchVertexArray()

    # A ConstrainedSketchImageOptions object. 
    imageOptions: ConstrainedSketchImageOptions = ConstrainedSketchImageOptions()
