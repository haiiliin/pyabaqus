from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import ConstrainedSketchGeometry


class FixedConstraint(ConstrainedSketchConstraint):

    def __init__(self, entity: ConstrainedSketchGeometry):
        """This method creates a fixed constraint. This constraint applies to a
        ConstrainedSketchGeometry object or a ConstrainedSketchVertex object and constrains them to be fixed in
        space. Both the location and the shape of the sketch geometry is fixed.

        Path
        ----
            - mdb.models[name].sketches[name].FixedConstraint

        Parameters
        ----------
        entity
            A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the item to fix in
            space. 

        Returns
        -------
            A ConstrainedSketchConstraint object. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass
