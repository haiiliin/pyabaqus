from abaqus.Model.ModelBase import ModelBase
from abaqus.Part.Part import Part
from abaqusConstants import *


class PartModel(ModelBase):

    def Part(self, name: str, dimensionality: SymbolicConstant, type: SymbolicConstant,
             twist: Boolean = OFF):
        """This method creates a Part object and places it in the parts repository.

        Path
        ----
            - mdb.models[name].Part

        Parameters
        ----------
        name
            A String specifying the repository key.
        dimensionality
            A SymbolicConstant specifying the dimensionality of the part. Possible values are
            THREE_D, TWO_D_PLANAR, and AXISYMMETRIC.
        type
            A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE_BODY,
            EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE.
        twist
            A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only
            available when *dimensionality*=AXISYMMETRIC and *type*=DEFORMABLE_BODY). The default
            value is OFF.

        Returns
        -------
            A Part object.

        Exceptions
        ----------
            InvalidNameError.
        """
        self.parts[name] = part = Part(name, dimensionality, type, twist)
        return part
