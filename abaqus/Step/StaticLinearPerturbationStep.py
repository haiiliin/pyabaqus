from abaqusConstants import *
from .AnalysisStep import AnalysisStep
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
from ..UtilityAndView.Repository import Repository


class StaticLinearPerturbationStep(AnalysisStep):

    """The StaticLinearPerturbationStep object is used to indicate that the static step should 
    be analyzed as a linear perturbation load step. 
    The StaticLinearPerturbationStep object is derived from the AnalysisStep object. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - STATIC
        - STEP

    """

    # A String specifying the repository key. 
    name: str = ''

    # A SymbolicConstant specifying the type of solver. Possible values are DIRECT and 
    # ITERATIVE. The default value is DIRECT. 
    matrixSolver: SymbolicConstant = DIRECT

    # A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
    # UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    # A String specifying the name of the previous step. The new step appears after this step 
    # in the list of analysis steps. 
    previous: str = ''

    # A String specifying a description of the new step. The default value is an empty string. 
    description: str = ''

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
    fieldOutputRequestState: Repository[str, FieldOutputRequestState] = Repository[str, FieldOutputRequestState]()

    # A repository of HistoryOutputRequestState objects. 
    historyOutputRequestState: Repository[str, HistoryOutputRequestState] = Repository[str, HistoryOutputRequestState]()

    # A DiagnosticPrint object. 
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    # A Monitor object. 
    monitor: Monitor = None

    # A Restart object. 
    restart: Restart = Restart()

    # A repository of AdaptiveMeshConstraintState objects. 
    adaptiveMeshConstraintStates: Repository[str, AdaptiveMeshConstraintState] = Repository[str, AdaptiveMeshConstraintState]()

    # A repository of AdaptiveMeshDomain objects. 
    adaptiveMeshDomains: Repository[str, AdaptiveMeshDomain] = Repository[str, AdaptiveMeshDomain]()

    # A Control object. 
    control: Control = Control()

    # A SolverControl object. 
    solverControl: SolverControl = SolverControl()

    # A repository of BoundaryConditionState objects. 
    boundaryConditionStates: Repository[str, BoundaryConditionState] = Repository[str, BoundaryConditionState]()

    # A repository of InteractionState objects. 
    interactionStates: int = None

    # A repository of LoadState objects. 
    loadStates: Repository[str, LoadState] = Repository[str, LoadState]()

    # A repository of LoadCase objects. 
    loadCases: Repository[str, LoadCase] = Repository[str, LoadCase]()

    # A repository of PredefinedFieldState objects. 
    predefinedFieldStates: Repository[str, PredefinedFieldState] = Repository[str, PredefinedFieldState]()

    def __init__(self, name: str, previous: str, description: str = '', 
                 matrixSolver: SymbolicConstant = DIRECT, 
                 matrixStorage: SymbolicConstant = SOLVER_DEFAULT, maintainAttributes: Boolean = False):
        """This method creates a StaticLinearPerturbationStep object.

        Path
        ----
            - mdb.models[name].StaticLinearPerturbationStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and 
            ITERATIVE. The default value is DIRECT. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 

        Returns
        -------
            A StaticLinearPerturbationStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, description: str = '', matrixSolver: SymbolicConstant = DIRECT, 
                  matrixStorage: SymbolicConstant = SOLVER_DEFAULT):
        """This method modifies the StaticLinearPerturbationStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string. 
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and 
            ITERATIVE. The default value is DIRECT. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

