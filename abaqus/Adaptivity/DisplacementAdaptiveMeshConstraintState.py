from abaqusConstants import *
from .AdaptiveMeshConstraintState import AdaptiveMeshConstraintState


class DisplacementAdaptiveMeshConstraintState(AdaptiveMeshConstraintState):

    """The DisplacementAdaptiveMeshConstraintState object stores the propagating data for an 
    Arbitrary Lagrangian Eularian (ALE) style displacement/rotation adaptive mesh constraint 
    in a step. One instance of this object is created internally by the 
    DisplacementAdaptiveMeshConstraint object for each step. The instance is also deleted 
    internally by the DisplacementAdaptiveMeshConstraint object. 
    The DisplacementAdaptiveMeshConstraintState object has no constructor or methods. 
    The DisplacementAdaptiveMeshConstraintState object is derived from the 
    AdaptiveMeshConstraintState object. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].adaptiveMeshConstraintStates[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - ADAPTIVE MESH CONSTRAINT

    """

    # A Float or a Complex specifying the displacement component in the 1-direction. 
    u1: float = None

    # A Float or a Complex specifying the displacement component in the 2-direction. 
    u2: float = None

    # A Float or a Complex specifying the displacement component in the 3-direction. 
    u3: float = None

    # A Float or a Complex specifying the rotational displacement component about the 
    # 1-direction. 
    ur1: float = None

    # A Float or a Complex specifying the rotational displacement component about the 
    # 2-direction. 
    ur2: float = None

    # A Float or a Complex specifying the rotational displacement component about the 
    # 3-direction. 
    ur3: float = None

    # A SymbolicConstant specifying the propagation state of the displacement component in the 
    # 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    u1State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the displacement component in the 
    # 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    u2State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the displacement component in the 
    # 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    u3State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the rotational displacement 
    # component about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and 
    # MODIFIED. 
    ur1State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the rotational displacement 
    # component about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and 
    # MODIFIED. 
    ur2State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the rotational displacement 
    # component about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and 
    # MODIFIED. 
    ur3State: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the amplitude reference. Possible 
    # values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState 
    # object. Possible values 
    # are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES 
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the 
    # adaptive mesh constraint has no amplitude reference. 
    amplitude: str = ''

