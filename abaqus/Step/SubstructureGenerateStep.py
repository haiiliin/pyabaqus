from abaqusConstants import *
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..LoadAndLoadCase.LoadCase import LoadCase
from ..LoadAndLoadCase.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..Region.Region import Region
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepMiscellaneous.SubstructureGenerateFrequencyArray import SubstructureGenerateFrequencyArray
from ..StepMiscellaneous.SubstructureGenerateModesArray import SubstructureGenerateModesArray
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.Repository import Repository


class SubstructureGenerateStep(AnalysisStep):

    """TheSubstructureGenerateStep object is used to generate a substructure. 
    The SubstructureGenerateStep object is derived from the AnalysisStep object. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - SUBSTRUCTURE GENERATE
        - STEP

    """

    # A String specifying the repository key. 
    name: str = ''

    # A SymbolicConstant specifying the subtructure recovery to be computed. Possible values 
    # are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL. 
    recoveryMatrix: SymbolicConstant = WHOLE_MODEL

    # A Float specifying the frequency at which to evaluate the frequency dependent 
    # properties. The default value is 0.0. 
    frequency: float = 0

    # A SymbolicConstant specifying the eigenmodes to be retained. Possible values are 
    # MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE. 
    retainedEigenmodesMethod: SymbolicConstant = NONE

    # A SymbolicConstant specifying the field to which the global damping factors should be 
    # applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is 
    # NONE. 
    globalDampingField: SymbolicConstant = NONE

    # A Float specifying the factor to create global Rayleigh mass proportional damping. The 
    # default value is 0.0. 
    alphaDampingRatio: float = 0

    # A Float specifying the factor to create global Rayleigh stiffness proportional damping. 
    # The default value is 0.0. 
    betaDampingRatio: float = 0

    # A Float specifying the factor to create frequency-independent stiffness proportional 
    # structural damping. The default value is 0.0. 
    structuralDampingRatio: float = 0

    # A SymbolicConstant specifying the damping control to include the viscous damping matrix. 
    # Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE. 
    viscousDampingControl: SymbolicConstant = NONE

    # A SymbolicConstant specifying the damping control to include the structural damping 
    # matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is 
    # NONE. 
    structuralDampingControl: SymbolicConstant = NONE

    # A String specifying the name of the previous step. The new step appears after this step 
    # in the list of analysis steps. 
    previous: str = ''

    # A String specifying a description of the new step. The default value is an empty string. 
    description: str = ''

    # A String specifying a unique identifier for the substructure. The default value is an 
    # empty string. 
    substructureIdentifier: str = ''

    # A Region object specifying the region for substructure recovery. This argument is 
    # required when *recoveryMatrix*=REGION. 
    recoveryRegion: Region = Region()

    # A SubstructureGenerateFrequencyArray object. 
    frequencyRange: SubstructureGenerateFrequencyArray = SubstructureGenerateFrequencyArray()

    # A SubstructureGenerateModesArray object. 
    modeRange: SubstructureGenerateModesArray = SubstructureGenerateModesArray()

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
    monitor: Monitor = Monitor()

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

    def __init__(self, name: str, previous: str, substructureIdentifier: int, description: str = '', 
                 recoveryMatrix: SymbolicConstant = WHOLE_MODEL, recoveryRegion: Region = Region(), 
                 computeGravityLoadVectors: Boolean = False, computeReducedMassMatrix: Boolean = False, 
                 computeReducedStructuralDampingMatrix: Boolean = False, 
                 computeReducedViscousDampingMatrix: Boolean = False, 
                 evaluateFrequencyDependentProperties: Boolean = False, frequency: float = 0, 
                 retainedEigenmodesMethod: SymbolicConstant = NONE, 
                 modeRange: SubstructureGenerateModesArray = SubstructureGenerateModesArray(), 
                 frequencyRange: SubstructureGenerateFrequencyArray = SubstructureGenerateFrequencyArray(), 
                 globalDampingField: SymbolicConstant = NONE, alphaDampingRatio: float = 0, 
                 betaDampingRatio: float = 0, structuralDampingRatio: float = 0, 
                 viscousDampingControl: SymbolicConstant = NONE, 
                 structuralDampingControl: SymbolicConstant = NONE):
        """This method creates a SubstructureGenerateStep object.

        Path
        ----
            - mdb.models[name].SubstructureGenerateStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        substructureIdentifier
            An Integer specifying a unique identifier for the substructure. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        recoveryMatrix
            A SymbolicConstant specifying the subtructure recovery to be computed. Possible values 
            are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL. 
        recoveryRegion
            A Region object specifying the region for substructure recovery. This argument is 
            required when *recoveryMatrix*=REGION. 
        computeGravityLoadVectors
            A Boolean specifying whether to compute the gravity load vectors. The default value is 
            False. 
        computeReducedMassMatrix
            A Boolean specifying whether to compute the reduced mass matrix. The default value is 
            False. 
        computeReducedStructuralDampingMatrix
            A Boolean specifying whether to compute the reduced structural damping matrix. The 
            default value is False. 
        computeReducedViscousDampingMatrix
            A Boolean specifying whether to compute the reduced viscous damping matrix. The default 
            value is False. 
        evaluateFrequencyDependentProperties
            A Boolean specifying whether to evaluate the frequency dependent properties. The default 
            value is False. 
        frequency
            A Float specifying the frequency at which to evaluate the frequency dependent 
            properties. The default value is 0.0. 
        retainedEigenmodesMethod
            A SymbolicConstant specifying the eigenmodes to be retained. Possible values are 
            MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE. 
        modeRange
            A SubstructureGenerateModesArray object. 
        frequencyRange
            A SubstructureGenerateFrequencyArray object. 
        globalDampingField
            A SymbolicConstant specifying the field to which the global damping factors should be 
            applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is 
            NONE. 
        alphaDampingRatio
            A Float specifying the factor to create global Rayleigh mass proportional damping. The 
            default value is 0.0. 
        betaDampingRatio
            A Float specifying the factor to create global Rayleigh stiffness proportional damping. 
            The default value is 0.0. 
        structuralDampingRatio
            A Float specifying the factor to create frequency-independent stiffness proportional 
            structural damping. The default value is 0.0. 
        viscousDampingControl
            A SymbolicConstant specifying the damping control to include the viscous damping matrix. 
            Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE. 
        structuralDampingControl
            A SymbolicConstant specifying the damping control to include the structural damping 
            matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is 
            NONE. 

        Returns
        -------
            A SubstructureGenerateStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, description: str = '', recoveryMatrix: SymbolicConstant = WHOLE_MODEL, 
                  recoveryRegion: Region = Region(), computeGravityLoadVectors: Boolean = False, 
                  computeReducedMassMatrix: Boolean = False, 
                  computeReducedStructuralDampingMatrix: Boolean = False, 
                  computeReducedViscousDampingMatrix: Boolean = False, 
                  evaluateFrequencyDependentProperties: Boolean = False, frequency: float = 0, 
                  retainedEigenmodesMethod: SymbolicConstant = NONE, 
                  modeRange: SubstructureGenerateModesArray = SubstructureGenerateModesArray(), 
                  frequencyRange: SubstructureGenerateFrequencyArray = SubstructureGenerateFrequencyArray(), 
                  globalDampingField: SymbolicConstant = NONE, alphaDampingRatio: float = 0, 
                  betaDampingRatio: float = 0, structuralDampingRatio: float = 0, 
                  viscousDampingControl: SymbolicConstant = NONE, 
                  structuralDampingControl: SymbolicConstant = NONE):
        """This method modifies the SubstructureGenerateStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string. 
        recoveryMatrix
            A SymbolicConstant specifying the subtructure recovery to be computed. Possible values 
            are WHOLE_MODEL, REGION, and NONE. The default value is WHOLE_MODEL. 
        recoveryRegion
            A Region object specifying the region for substructure recovery. This argument is 
            required when *recoveryMatrix*=REGION. 
        computeGravityLoadVectors
            A Boolean specifying whether to compute the gravity load vectors. The default value is 
            False. 
        computeReducedMassMatrix
            A Boolean specifying whether to compute the reduced mass matrix. The default value is 
            False. 
        computeReducedStructuralDampingMatrix
            A Boolean specifying whether to compute the reduced structural damping matrix. The 
            default value is False. 
        computeReducedViscousDampingMatrix
            A Boolean specifying whether to compute the reduced viscous damping matrix. The default 
            value is False. 
        evaluateFrequencyDependentProperties
            A Boolean specifying whether to evaluate the frequency dependent properties. The default 
            value is False. 
        frequency
            A Float specifying the frequency at which to evaluate the frequency dependent 
            properties. The default value is 0.0. 
        retainedEigenmodesMethod
            A SymbolicConstant specifying the eigenmodes to be retained. Possible values are 
            MODE_RANGE, FREQUENCY_RANGE, and NONE. The default value is NONE. 
        modeRange
            A SubstructureGenerateModesArray object. 
        frequencyRange
            A SubstructureGenerateFrequencyArray object. 
        globalDampingField
            A SymbolicConstant specifying the field to which the global damping factors should be 
            applied. Possible values are ALL, ACOUSTIC, MECHANICAL, and NONE. The default value is 
            NONE. 
        alphaDampingRatio
            A Float specifying the factor to create global Rayleigh mass proportional damping. The 
            default value is 0.0. 
        betaDampingRatio
            A Float specifying the factor to create global Rayleigh stiffness proportional damping. 
            The default value is 0.0. 
        structuralDampingRatio
            A Float specifying the factor to create frequency-independent stiffness proportional 
            structural damping. The default value is 0.0. 
        viscousDampingControl
            A SymbolicConstant specifying the damping control to include the viscous damping matrix. 
            Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is NONE. 
        structuralDampingControl
            A SymbolicConstant specifying the damping control to include the structural damping 
            matrix. Possible values are ELEMENT, FACTOR, COMBINED, and NONE. The default value is 
            NONE. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

