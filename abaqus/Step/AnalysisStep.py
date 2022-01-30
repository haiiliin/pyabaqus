from abaqusConstants import *
from .Step import Step
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..LoadAndLoadCase.LoadCase import LoadCase
from ..LoadAndLoadCase.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart


class AnalysisStep(Step):
    """The AnalysisStep object is the abstract base type for other Step objects, except the
    InitialStep object. It has no explicit constructor, no methods, and has only inherited 
    members. 
    The AnalysisStep object is derived from the Step object. 

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    explicit: SymbolicConstant
        A SymbolicConstant specifying whether the step has an explicit procedure type
        (**procedureType=ANNEAL**, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    perturbation: Boolean
        A Boolean specifying whether the step has a perturbation procedure type.
    nonmechanical: Boolean
        A Boolean specifying whether the step has a mechanical procedure type.
    procedureType: SymbolicConstant
        A SymbolicConstant specifying the Abaqus procedure. Possible values are:
        - ANNEAL
        - BUCKLE
        - COMPLEX_FREQUENCY
        - COUPLED_TEMP_DISPLACEMENT
        - COUPLED_THERMAL_ELECTRIC
        - DIRECT_CYCLIC
        - DYNAMIC_IMPLICIT
        - DYNAMIC_EXPLICIT
        - DYNAMIC_SUBSPACE
        - DYNAMIC_TEMP_DISPLACEMENT
        - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
        - FREQUENCY
        - GEOSTATIC
        - HEAT_TRANSFER
        - MASS_DIFFUSION
        - MODAL_DYNAMICS
        - RANDOM_RESPONSE
        - RESPONSE_SPECTRUM
        - SOILS
        - STATIC_GENERAL
        - STATIC_LINEAR_PERTURBATION
        - STATIC_RIKS
        - STEADY_STATE_DIRECT
        - STEADY_STATE_MODAL
        - STEADY_STATE_SUBSPACE
        - VISCO
    suppressed: Boolean
        A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    fieldOutputRequestState: dict[str, FieldOutputRequestState]
        A repository of FieldOutputRequestState objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState]
        A repository of HistoryOutputRequestState objects.
    diagnosticPrint: DiagnosticPrint
        A DiagnosticPrint object.
    monitor: Monitor
        A Monitor object.
    restart: Restart
        A Restart object.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState]
        A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain]
        A repository of AdaptiveMeshDomain objects.
    control: Control
        A Control object.
    solverControl: SolverControl
        A SolverControl object.
    boundaryConditionStates: dict[str, BoundaryConditionState]
        A repository of BoundaryConditionState objects.
    interactionStates: int
        A repository of InteractionState objects.
    loadStates: dict[str, LoadState]
        A repository of LoadState objects.
    loadCases: dict[str, LoadCase]
        A repository of LoadCase objects.
    predefinedFieldStates: dict[str, PredefinedFieldState]
        A repository of PredefinedFieldState objects.

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name]

    """

    # A String specifying the repository key. 
    name: str = ''

    # A SymbolicConstant specifying whether the step has an explicit procedure type 
    # (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT). 
    explicit: SymbolicConstant = None

    # A Boolean specifying whether the step has a perturbation procedure type. 
    perturbation: Boolean = OFF

    # A Boolean specifying whether the step has a mechanical procedure type. 
    nonmechanical: Boolean = OFF

    # A SymbolicConstant specifying the Abaqus procedure. Possible values are: 
    # - ANNEAL 
    # - BUCKLE 
    # - COMPLEX_FREQUENCY 
    # - COUPLED_TEMP_DISPLACEMENT 
    # - COUPLED_THERMAL_ELECTRIC 
    # - DIRECT_CYCLIC 
    # - DYNAMIC_IMPLICIT 
    # - DYNAMIC_EXPLICIT 
    # - DYNAMIC_SUBSPACE 
    # - DYNAMIC_TEMP_DISPLACEMENT 
    # - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL 
    # - FREQUENCY 
    # - GEOSTATIC 
    # - HEAT_TRANSFER 
    # - MASS_DIFFUSION 
    # - MODAL_DYNAMICS 
    # - RANDOM_RESPONSE 
    # - RESPONSE_SPECTRUM 
    # - SOILS 
    # - STATIC_GENERAL 
    # - STATIC_LINEAR_PERTURBATION 
    # - STATIC_RIKS 
    # - STEADY_STATE_DIRECT 
    # - STEADY_STATE_MODAL 
    # - STEADY_STATE_SUBSPACE 
    # - VISCO 
    procedureType: SymbolicConstant = None

    # A Boolean specifying whether the step is suppressed or not. The default value is OFF. 
    suppressed: Boolean = OFF

    # A repository of FieldOutputRequestState objects. 
    fieldOutputRequestState: dict[str, FieldOutputRequestState] = dict[str, FieldOutputRequestState]()

    # A repository of HistoryOutputRequestState objects. 
    historyOutputRequestState: dict[str, HistoryOutputRequestState] = dict[str, HistoryOutputRequestState]()

    # A DiagnosticPrint object. 
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    # A Monitor object. 
    monitor: Monitor = None

    # A Restart object. 
    restart: Restart = Restart()

    # A repository of AdaptiveMeshConstraintState objects. 
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState] = dict[
        str, AdaptiveMeshConstraintState]()

    # A repository of AdaptiveMeshDomain objects. 
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain] = dict[str, AdaptiveMeshDomain]()

    # A Control object. 
    control: Control = Control()

    # A SolverControl object. 
    solverControl: SolverControl = SolverControl()

    # A repository of BoundaryConditionState objects. 
    boundaryConditionStates: dict[str, BoundaryConditionState] = dict[str, BoundaryConditionState]()

    # A repository of InteractionState objects. 
    interactionStates: int = None

    # A repository of LoadState objects. 
    loadStates: dict[str, LoadState] = dict[str, LoadState]()

    # A repository of LoadCase objects. 
    loadCases: dict[str, LoadCase] = dict[str, LoadCase]()

    # A repository of PredefinedFieldState objects. 
    predefinedFieldStates: dict[str, PredefinedFieldState] = dict[str, PredefinedFieldState]()
