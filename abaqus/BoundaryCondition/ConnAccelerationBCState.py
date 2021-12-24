from .BoundaryConditionState import BoundaryConditionState
from abaqusConstants import *

class ConnAccelerationBCState(BoundaryConditionState):

    """The ConnAccelerationBCState object stores the propagating data of a connector 
    acceleration boundary condition in a step. One instance of this object is created 
    internally by the ConnAccelerationBC object for each step. The instance is also deleted 
    internally by the ConnAccelerationBC object. 
    The ConnAccelerationBCState object has no constructor or methods. 
    The ConnAccelerationBCState object is derived from the BoundaryConditionState object. 

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

    # A Float specifying the connector acceleration component in the connector's local 
    # 1-direction. 
    a1: float = None

    # A Float specifying the connector acceleration component in the connector's local 
    # 2-direction. 
    a2: float = None

    # A Float specifying the connector acceleration component in the connector's local 
    # 3-direction. 
    a3: float = None

    # A Float specifying the connector acceleration component in the connector's local 
    # 4-direction. 
    ar1: float = None

    # A Float specifying the connector acceleration component in the connector's local 
    # 5-direction. 
    ar2: float = None

    # A Float specifying the connector acceleration component in the connector's local 
    # 6-direction. 
    ar3: float = None

    # A SymbolicConstant specifying the propagation state of the connector acceleration 
    # component in the connector's local 1-direction. Possible values are UNSET, SET, 
    # UNCHANGED, FREED, and MODIFIED. 
    a1State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the connector acceleration 
    # component in the connector's local 2-direction. Possible values are UNSET, SET, 
    # UNCHANGED, FREED, and MODIFIED. 
    a2State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the connector acceleration 
    # component in the connector's local 3-direction. Possible values are UNSET, SET, 
    # UNCHANGED, FREED, and MODIFIED. 
    a3State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the connector acceleration 
    # component in the connector's local 4-direction. Possible values are UNSET, SET, 
    # UNCHANGED, FREED, and MODIFIED. 
    ar1State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the connector acceleration 
    # component in the connector's local 5-direction. Possible values are UNSET, SET, 
    # UNCHANGED, FREED, and MODIFIED. 
    ar2State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the connector acceleration 
    # component in the connector's local 6-direction. Possible values are UNSET, SET, 
    # UNCHANGED, FREED, and MODIFIED. 
    ar3State: SymbolicConstant = None

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

