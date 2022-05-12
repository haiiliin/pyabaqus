from abaqusConstants import *
from .BoundaryConditionState import BoundaryConditionState

from __init__ import *
from __future__ import annotations


class MaterialFlowBCState(BoundaryConditionState):
    """The MaterialFlowBCState object stores the propagating data for a connector material flow
    boundary condition in a step. One instance of this object is created internally by the 
    MaterialFlowBC object for each step. The instance is also deleted internally by the 
    MaterialFlowBC object. 
    The MaterialFlowBCState object has no constructor or methods. 
    The MaterialFlowBCState object is derived from the BoundaryConditionState object. 

    Attributes
    ----------
    magnitude: float
        A Float specifying the material flow magnitude.
    magnitudeState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the material flow magnitude.
        Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    status: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the :py:class:`~abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState` object. Possible values are:
        NOT_YET_ACTIVE
        CREATED
        PROPAGATED
        MODIFIED
        DEACTIVATED
        NO_LONGER_ACTIVE
        TYPE_NOT_APPLICABLE
        INSTANCE_NOT_APPLICABLE
        PROPAGATED_FROM_BASE_STATE
        MODIFIED_FROM_BASE_STATE
        DEACTIVATED_FROM_BASE_STATE
        BUILT_INTO_MODES
    amplitude: str
        A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

    The corresponding analysis keywords are:
        - BOUNDARY

    """

    # A Float specifying the material flow magnitude.
    magnitude: float = None

    # A SymbolicConstant specifying the propagation state of the material flow magnitude.
    # Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    magnitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    # values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:
    # NOT_YET_ACTIVE
    # CREATED
    # PROPAGATED
    # MODIFIED
    # DEACTIVATED
    # NO_LONGER_ACTIVE
    # TYPE_NOT_APPLICABLE
    # INSTANCE_NOT_APPLICABLE
    # PROPAGATED_FROM_BASE_STATE
    # MODIFIED_FROM_BASE_STATE
    # DEACTIVATED_FROM_BASE_STATE
    # BUILT_INTO_MODES
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the
    # boundary condition has no amplitude reference.
    amplitude: str = ''
