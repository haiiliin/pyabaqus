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
from .AnalysisStep import AnalysisStep
from abaqusConstants import *

class SteadyStateDirectStep(AnalysisStep):

    """The SteadyStateDirectStep object is used to calculate the linearized steady-state 
    response of the system to harmonic excitation in terms of the physical degrees of 
    freedom of the model. 
    The SteadyStateDirectStep object is derived from the AnalysisStep object. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - STEADY STATE DYNAMICS
        - STEP

    """

    # A String specifying the repository key. 
    name: str = ''

    # A SymbolicConstant specifying whether damping terms are to be ignored so that a real, 
    # rather than a complex, system matrix is factored. Possible values are REAL_ONLY and 
    # COMPLEX. The default value is COMPLEX. 
    factorization: SymbolicConstant = COMPLEX

    # A SymbolicConstant specifying whether a logarithmic or linear scale is used for output. 
    # Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC. 
    scale: SymbolicConstant = LOGARITHMIC

    # A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
    # UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    # A Boolean specifying whether to subdivide each frequency range using the 
    # eigenfrequencies of the system. The default value is OFF. 
    subdivideUsingEigenfrequencies: Boolean = OFF

    # A Boolean specifying whether to add to the damping matrix contributions due to friction 
    # effects. The default value is OFF. 
    frictionDamping: Boolean = OFF

    # A String specifying the name of the previous step. The new step appears after this step 
    # in the list of analysis steps. 
    previous: str = ''

    # A String specifying a description of the new step. The default value is an empty string. 
    description: str = ''

    # A SteadyStateDirectFrequencyArray object. 
    frequencyRange: SteadyStateDirectFrequencyArray = None

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
    fieldOutputRequestState: Repository[str, FieldOutputRequestState] = None

    # A repository of HistoryOutputRequestState objects. 
    historyOutputRequestState: Repository[str, HistoryOutputRequestState] = None

    # A DiagnosticPrint object. 
    diagnosticPrint: DiagnosticPrint = None

    # A Monitor object. 
    monitor: Monitor = None

    # A Restart object. 
    restart: Restart = None

    # A repository of AdaptiveMeshConstraintState objects. 
    adaptiveMeshConstraintStates: Repository[str, AdaptiveMeshConstraintState] = None

    # A repository of AdaptiveMeshDomain objects. 
    adaptiveMeshDomains: Repository[str, AdaptiveMeshDomain] = None

    # A Control object. 
    control: Control = None

    # A SolverControl object. 
    solverControl: SolverControl = None

    # A repository of BoundaryConditionState objects. 
    boundaryConditionStates: Repository[str, BoundaryConditionState] = None

    # A repository of InteractionState objects. 
    interactionStates: int = None

    # A repository of LoadState objects. 
    loadStates: Repository[str, LoadState] = None

    # A repository of LoadCase objects. 
    loadCases: Repository[str, LoadCase] = None

    # A repository of PredefinedFieldState objects. 
    predefinedFieldStates: Repository[str, PredefinedFieldState] = None

    def __init__(self, name: str, previous: str, frequencyRange: SteadyStateDirectFrequencyArray, 
                 description: str = '', factorization: SymbolicConstant = COMPLEX, 
                 scale: SymbolicConstant = LOGARITHMIC, matrixStorage: SymbolicConstant = SOLVER_DEFAULT, 
                 maintainAttributes: Boolean = False, subdivideUsingEigenfrequencies: Boolean = OFF, 
                 frictionDamping: Boolean = OFF):
        """This method creates a SteadyStateDirectStep object.

        Path
        ----
            - mdb.models[name].SteadyStateDirectStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        frequencyRange
            A SteadyStateDirectFrequencyArray object. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real, 
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and 
            COMPLEX. The default value is COMPLEX. 
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output. 
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the 
            eigenfrequencies of the system. The default value is OFF. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 

        Returns
        -------
            A SteadyStateDirectStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, description: str = '', factorization: SymbolicConstant = COMPLEX, 
                  scale: SymbolicConstant = LOGARITHMIC, matrixStorage: SymbolicConstant = SOLVER_DEFAULT, 
                  subdivideUsingEigenfrequencies: Boolean = OFF, frictionDamping: Boolean = OFF):
        """This method modifies the SteadyStateDirectStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string. 
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real, 
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and 
            COMPLEX. The default value is COMPLEX. 
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output. 
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the 
            eigenfrequencies of the system. The default value is OFF. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

