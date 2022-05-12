from abaqusConstants import *
from .Constraint import Constraint
from ..Region.Region import Region

from __init__ import *
from __future__ import annotations


class Tie(Constraint):
    """The Tie object defines two surfaces to be tied together for the duration of a
    simulation. 
    The Tie object is derived from the ConstrainedSketchConstraint object.

    Attributes
    ----------
    suppressed: Boolean
        A Boolean specifying whether the constraint is suppressed or not. The default value is
        OFF.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].constraints[name]

    The corresponding analysis keywords are:
        - TIE

    """

    # A Boolean specifying whether the constraint is suppressed or not. The default value is
    # OFF.
    suppressed: Boolean = OFF

    def __init__(self,
                 name: str,
                 main: Region,
                 secondary: Region,
                 adjust: Boolean = ON,
                 positionToleranceMethod: SymbolicConstant = COMPUTED,
                 positionTolerance: float = 0,
                 tieRotations: Boolean = ON,
                 constraintRatioMethod: SymbolicConstant = DEFAULT,
                 constraintRatio: float = 0,
                 constraintEnforcement: SymbolicConstant = SOLVER_DEFAULT,
                 thickness: Boolean = ON):
        """This method creates a Tie object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Tie
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        main
            A Region object specifying the name of the main surface. 
        secondary
            A Region object specifying the name of the secondary surface. 
        adjust
            A Boolean specifying whether initial positions of tied secondary nodes are adjusted to 
            lie on the main surface. The default value is ON. 
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance. 
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED. 
        positionTolerance
            A Float specifying the position tolerance. The *positionTolerance* argument applies only 
            when *positionToleranceMethod*=SPECIFIED. The default value is 0.0. 
        tieRotations
            A Boolean specifying whether rotation degrees of freedom should be tied. The default 
            value is ON. 
        constraintRatioMethod
            A SymbolicConstant specifying the method used to determine the constraint ratio. 
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT. 
        constraintRatio
            A Float specifying the fractional distance between the main reference surface and the 
            secondary node at which the translational constraint should act. The *constraintRatio* 
            argument applies only when *constraintRatioMethod*=SPECIFIED. The default value is 0.0. 
        constraintEnforcement
            A SymbolicConstant specifying the discretization method. Possible values are 
            SOLVER_DEFAULT, NODE_TO_SURFACE, and SURFACE_TO_SURFACE. The default value is 
            SOLVER_DEFAULT. 
        thickness
            A Boolean specifying whether shell element thickness is considered. The default value is 
            ON. 

        Returns
        -------
            A Tie object.
        """
        super().__init__()
        pass

    def swapSurfaces(self):
        """This method switches the main and secondary surfaces of a tied constraint. This command
        is valid only during the step in which the interaction is created.
        """
        pass

    def setValues(self,
                  adjust: Boolean = ON,
                  positionToleranceMethod: SymbolicConstant = COMPUTED,
                  positionTolerance: float = 0,
                  tieRotations: Boolean = ON,
                  constraintRatioMethod: SymbolicConstant = DEFAULT,
                  constraintRatio: float = 0,
                  constraintEnforcement: SymbolicConstant = SOLVER_DEFAULT,
                  thickness: Boolean = ON):
        """This method modifies the Tie object.
        
        Parameters
        ----------
        adjust
            A Boolean specifying whether initial positions of tied secondary nodes are adjusted to 
            lie on the main surface. The default value is ON. 
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance. 
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED. 
        positionTolerance
            A Float specifying the position tolerance. The *positionTolerance* argument applies only 
            when *positionToleranceMethod*=SPECIFIED. The default value is 0.0. 
        tieRotations
            A Boolean specifying whether rotation degrees of freedom should be tied. The default 
            value is ON. 
        constraintRatioMethod
            A SymbolicConstant specifying the method used to determine the constraint ratio. 
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT. 
        constraintRatio
            A Float specifying the fractional distance between the main reference surface and the 
            secondary node at which the translational constraint should act. The *constraintRatio* 
            argument applies only when *constraintRatioMethod*=SPECIFIED. The default value is 0.0. 
        constraintEnforcement
            A SymbolicConstant specifying the discretization method. Possible values are 
            SOLVER_DEFAULT, NODE_TO_SURFACE, and SURFACE_TO_SURFACE. The default value is 
            SOLVER_DEFAULT. 
        thickness
            A Boolean specifying whether shell element thickness is considered. The default value is 
            ON. 
        """
        pass
