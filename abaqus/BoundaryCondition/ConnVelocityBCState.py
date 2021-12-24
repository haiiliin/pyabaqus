from .BoundaryConditionState import BoundaryConditionState
from abaqusConstants import *

class ConnVelocityBCState(BoundaryConditionState):

    """The ConnVelocityBCState object stores the propagating data for a velocity boundary 
    condition in a step. One instance of this object is created internally by the 
    ConnVelocityBC object for each step. The instance is also deleted internally by the 
    ConnVelocityBC object. 
    The ConnVelocityBCState object has no constructor or methods. 
    The ConnVelocityBCState object is derived from the BoundaryConditionState object. 

    Access
    ------
        - import load
        - mdb.models[name].steps[name].boundaryConditionStates[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - CONNECTOR MOTION

    """

    # A Float specifying the velocity component in the connector's local 1-direction. 
    v1: float = None

    # A Float specifying the velocity component in the connector's local 2-direction. 
    v2: float = None

    # A Float specifying the velocity component in the connector's local 3-direction. 
    v3: float = None

    # A Float specifying the rotational velocity component in the connector's local 
    # 4-direction. 
    vr1: float = None

    # A Float specifying the rotational velocity component in the connector's local 
    # 5-direction. 
    vr2: float = None

    # A Float specifying the rotational velocity component in the connector's local 
    # 6-direction. 
    vr3: float = None

    # A SymbolicConstant specifying the propagation state of the velocity component in the 
    # connector's local 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and 
    # MODIFIED. 
    v1State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the velocity component in the 
    # connector's local 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and 
    # MODIFIED. 
    v2State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the velocity component in the 
    # connector's local 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and 
    # MODIFIED. 
    v3State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the rotational velocity component 
    # in the connector's local 4–direction. Possible values are UNSET, SET, UNCHANGED, FREED, 
    # and MODIFIED. 
    vr1State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the rotational velocity component 
    # in the connector's local 5–direction. Possible values are UNSET, SET, UNCHANGED, FREED, 
    # and MODIFIED. 
    vr2State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the rotational velocity component 
    # in the connector's local 6–direction. Possible values are UNSET, SET, UNCHANGED, FREED, 
    # and MODIFIED. 
    vr3State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the amplitude reference. Possible 
    # values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the BoundaryConditionState 
    # object. Possible values 
    # are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES 
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the 
    # boundary condition has no amplitude reference. 
    amplitude: str = ''

