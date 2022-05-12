from abaqusConstants import *
from .LoadState import LoadState

from __init__ import *
from __future__ import annotations


class ConnectorMomentState(LoadState):
    """The ConnectorMomentState object stores the propagating data for a connector moment in a
    step. One instance of this object is created internally by the ConnectorMoment object 
    for each step. The instance is also deleted internally by the ConnectorMoment object. 
    The ConnectorMomentState object has no constructor or methods. 
    The ConnectorMomentState object is derived from the LoadState object. 

    Attributes
    ----------
    m1: float
        A Float or a Complex specifying the connector moment component in the connector's local
        4-direction. Although **m1**, **m2**, and **m3** are optional arguments, at least one of them
        must be nonzero.
    m2: float
        A Float or a Complex specifying the connector moment component in the connector's local
        5direction.
    m3: float
        A Float or a Complex specifying the connector moment component in the connector's local
        6-direction.
    m1State: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the load component in the
        connector's local 4-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    m2State: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the load component in the
        connector's local 5-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    m3State: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the load component in the
        connector's local 6-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.
    status: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the :py:class:`~abaqus.Load.LoadState.LoadState` object. Possible
        values are:
            - NOT_YET_ACTIVE
            - CREATED
            - PROPAGATED
            - MODIFIED
            - DEACTIVATED
            - NO_LONGER_ACTIVE
            - TYPE_NOT_APPLICABLE
            - INSTANCE_NOT_APPLICABLE
            - BUILT_INTO_BASE_STATE
    amplitude: str
        A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import load
            mdb.models[name].steps[name].loadStates[name]

    The corresponding analysis keywords are:
        - CONNECTOR LOAD

    """

    # A Float or a Complex specifying the connector moment component in the connector's local
    # 4-direction. Although *m1*, *m2*, and *m3* are optional arguments, at least one of them
    # must be nonzero.
    m1: float = None

    # A Float or a Complex specifying the connector moment component in the connector's local
    # 5direction.
    m2: float = None

    # A Float or a Complex specifying the connector moment component in the connector's local
    # 6-direction.
    m3: float = None

    # A SymbolicConstant specifying the propagation state of the load component in the
    # connector's local 4-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    m1State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the load component in the
    # connector's local 5-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    m2State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the load component in the
    # connector's local 6-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    m3State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible
    # values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the LoadState object. Possible
    # values are:
    # - NOT_YET_ACTIVE
    # - CREATED
    # - PROPAGATED
    # - MODIFIED
    # - DEACTIVATED
    # - NO_LONGER_ACTIVE
    # - TYPE_NOT_APPLICABLE
    # - INSTANCE_NOT_APPLICABLE
    # - BUILT_INTO_BASE_STATE
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the load
    # has no amplitude reference.
    amplitude: str = ''
