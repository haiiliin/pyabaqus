from abaqusConstants import *
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..LoadAndLoadCase.LoadCase import LoadCase
from ..LoadAndLoadCase.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.CompositeDamping import CompositeDamping
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.DirectDamping import DirectDamping
from ..StepMiscellaneous.DirectDampingByFrequency import DirectDampingByFrequency
from ..StepMiscellaneous.RayleighDamping import RayleighDamping
from ..StepMiscellaneous.RayleighDampingByFrequency import RayleighDampingByFrequency
from ..StepMiscellaneous.ResponseSpectrumComponentArray import ResponseSpectrumComponentArray
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepMiscellaneous.StructuralDamping import StructuralDamping
from ..StepMiscellaneous.StructuralDampingByFrequency import StructuralDampingByFrequency
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.Repository import Repository


class ResponseSpectrumStep(AnalysisStep):

    """The ResponseSpectrumStep object is used to calculate estimates of peak values of 
    displacements and stresses based on user-supplied response spectra and on the natural 
    modes of the system. 
    The ResponseSpectrumStep object is derived from the AnalysisStep object. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - RESPONSE SPECTRUM
        - STEP

    """

    # A String specifying the repository key. 
    name: str = ''

    # A SymbolicConstant specifying the order and method used to sum the components. Possible 
    # values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM, 
    # MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and 
    # MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION. 
    comp: SymbolicConstant = SINGLE_DIRECTION

    # A SymbolicConstant specifying the method used to sum the components. Possible values are 
    # ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS. 
    sum: SymbolicConstant = ABS

    # A String specifying the name of the previous step. The new step appears after this step 
    # in the list of analysis steps. 
    previous: str = ''

    # A String specifying a description of the new step. The default value is an empty string. 
    description: str = ''

    # A ResponseSpectrumComponentArray object. 
    components: ResponseSpectrumComponentArray = None

    # A DirectDamping object. 
    directDamping: DirectDamping = None

    # A CompositeDamping object. 
    compositeDamping: CompositeDamping = None

    # A RayleighDamping object. 
    rayleighDamping: RayleighDamping = None

    # A DirectDampingByFrequency object. 
    directDampingByFrequency: DirectDampingByFrequency = None

    # A RayleighDampingByFrequency object. 
    rayleighDampingByFrequency: RayleighDampingByFrequency = None

    # A StructuralDamping object. 
    structuralDamping: StructuralDamping = None

    # A StructuralDampingByFrequency object. 
    structuralDampingByFrequency: StructuralDampingByFrequency = None

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

    def __init__(self, name: str, previous: str, components: ResponseSpectrumComponentArray, 
                 description: str = '', comp: SymbolicConstant = SINGLE_DIRECTION, 
                 sum: SymbolicConstant = ABS, directDamping: DirectDamping = None, 
                 compositeDamping: CompositeDamping = None, rayleighDamping: RayleighDamping = None, 
                 directDampingByFrequency: DirectDampingByFrequency = None, 
                 rayleighDampingByFrequency: RayleighDampingByFrequency = None, 
                 maintainAttributes: Boolean = False):
        """This method creates a ResponseSpectrumStep object.

        Path
        ----
            - mdb.models[name].ResponseSpectrumStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        components
            A ResponseSpectrumComponentArray object. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        comp
            A SymbolicConstant specifying the order and method used to sum the components. Possible 
            values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM, 
            MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and 
            MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION. 
        sum
            A SymbolicConstant specifying the method used to sum the components. Possible values are 
            ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS. 
        directDamping
            A DirectDamping object. 
        compositeDamping
            A CompositeDamping object. 
        rayleighDamping
            A RayleighDamping object. 
        directDampingByFrequency
            A DirectDampingByFrequency object. 
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 

        Returns
        -------
            A ResponseSpectrumStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, description: str = '', comp: SymbolicConstant = SINGLE_DIRECTION, 
                  sum: SymbolicConstant = ABS, directDamping: DirectDamping = None, 
                  compositeDamping: CompositeDamping = None, rayleighDamping: RayleighDamping = None, 
                  directDampingByFrequency: DirectDampingByFrequency = None, 
                  rayleighDampingByFrequency: RayleighDampingByFrequency = None):
        """This method modifies the ResponseSpectrumStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string. 
        comp
            A SymbolicConstant specifying the order and method used to sum the components. Possible 
            values are SINGLE_DIRECTION, MULTIPLE_DIRECTION_ABSOLUTE_SUM, 
            MULTIPLE_DIRECTION_SRSS_SUM, MULTIPLE_DIRECTION_THIRTY_PERCENT_RULE, and 
            MULTIPLE_DIRECTION_FORTY_PERCENT_RULE. The default value is SINGLE_DIRECTION. 
        sum
            A SymbolicConstant specifying the method used to sum the components. Possible values are 
            ABS, CQC, NRL, SRSS, TENP, DSC, and GRP. The default value is ABS. 
        directDamping
            A DirectDamping object. 
        compositeDamping
            A CompositeDamping object. 
        rayleighDamping
            A RayleighDamping object. 
        directDampingByFrequency
            A DirectDampingByFrequency object. 
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

