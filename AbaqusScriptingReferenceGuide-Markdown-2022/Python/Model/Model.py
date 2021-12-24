from abaqusConstants import *


class Model:

    """Abaqus creates a Model object named `Model-1` when a session is started. 

    Access
    ------
        - ```
        - mdb.models[name]
        - ```

    Corresponding analysis keywords
    -------------------------------
        - PHYSICAL CONSTANTS

    """

    # A String specifying the repository key. 
    name: str = ''

    # None or a Float specifying the Stefan-Boltzmann constant. The default value is None. 
    stefanBoltzmann: float = None

    # None or a Float specifying the absolute zero constant. The default value is None. 
    absoluteZero: float = None

    # A SymbolicConstant specifying the type of incident wave formulation to be used in 
    # acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value 
    # is NOT_SET. 
    waveFormulation: SymbolicConstant = NOT_SET

    # None or a Float specifying the universal gas constant. The default value is None. 
    universalGas: float = None

    # A Boolean specifying whether an input file should be written without parts and 
    # assemblies. The default value is OFF. 
    noPartsInputFile: Boolean = OFF

    # An Int specifying the increment, interval, iteration or cycle where the restart analysis 
    # will start. To select the end of the step use the SymbolicConstant STEP_END. 
    restartIncrement: SymbolicConstant = None

    # A Boolean specifying that the step specified by *restartStep* should be terminated at 
    # the increment specified by *restartIncrement*. 
    endRestartStep: Boolean = OFF

    # A Boolean specifying that a shell global model drives a solid submodel. 
    shellToSolid: Boolean = OFF

    # A Float specifying the time stamp that indicates when the model was last changed. 
    lastChangedCount: float = None

    # A String specifying the purpose and contents of the Model object. The default value is 
    # an empty string. 
    description: str = ''

    # A String specifying the name of the job that generated the restart data. 
    restartJob: str = ''

    # A String specifying the name of the step where the restart analysis will start. 
    restartStep: str = ''

    # A String specifying the name of the job that generated the results for the global model. 
    globalJob: str = ''

    # A boolean specifying the status of constraints created in a model, in the model which 
    # instances this model. 
    copyConstraints: str = ''

    # A boolean specifying the status of connectors created in a model, in the model which 
    # instances this model. 
    copyConnectors: str = ''

    # A boolean specifying the status of interactions created in a model, in the model which 
    # instances this model. 
    copyInteractions: str = ''

    # A KeywordBlock object. 
    keywordBlock: KeywordBlock = None

    # An Assembly object. 
    rootAssembly: Assembly = None

    # A repository of Amplitude objects. 
    amplitudes: Repository[str, Amplitude] = None

    # A repository of Profile objects. 
    profiles: Repository[str, Profile] = None

    # A repository of BoundaryCondition objects. 
    boundaryConditions: Repository[str, BoundaryCondition] = None

    # A repository of Constraint objects. 
    constraints: Repository[str, Constraint] = None

    # A repository of AnalyticalField objects. 
    analyticalFields: Repository[str, AnalyticalField] = None

    # A repository of DiscreteField objects. 
    discreteFields: Repository[str, DiscreteField] = None

    # A repository of PredefinedField objects. 
    predefinedFields: Repository[str, PredefinedField] = None

    # A repository of Interaction objects. 
    interactions: int = None

    # A repository of InteractionProperty objects. 
    interactionProperties: int = None

    # A repository of ContactControl objects. 
    contactControls: Repository[str, ContactControl] = None

    # A repository of ContactInitialization objects. 
    contactInitializations: Repository[str, ContactInitialization] = None

    # A repository of ContactStabilization objects. 
    contactStabilizations: Repository[str, ContactStabilization] = None

    # A tuple of tuples of Strings specifying the linked child PartInstance name in the 
    # current model to the corresponding parent PartInstance name in a different model. 
    linkedInstances: tuple = ()

    # A tuple of tuples of Strings specifying the linked child Part name in the current model 
    # to the corresponding parent Part name in a different model. 
    linkedParts: tuple = ()

    # A repository of Load objects. 
    loads: Repository[str, Load] = None

    # A repository of Material objects. 
    materials: Repository[str, Material] = None

    # A repository of Calibration objects. 
    calibrations: Repository[str, Calibration] = None

    # A repository of Section objects. 
    sections: Repository[str, Section] = None

    # A repository of RemeshingRule objects. 
    remeshingRules: Repository[str, RemeshingRule] = None

    # A repository of ConstrainedSketch objects. 
    sketches: Repository[str, ConstrainedSketch] = None

    # A repository of Part objects. 
    parts: Repository[str, Part] = None

    # A repository of Step objects. 
    steps: Repository[str, Step] = None

    # A FeatureOptions object. 
    featureOptions: FeatureOptions = None

    # A repository of AdaptiveMeshConstraint objects. 
    adaptiveMeshConstraints: Repository[str, AdaptiveMeshConstraint] = None

    # A repository of AdaptiveMeshControl objects. 
    adaptiveMeshControls: Repository[str, AdaptiveMeshControl] = None

    # A repository of TimePoint objects. 
    timePoints: Repository[str, TimePoint] = None

    # A repository of Filter objects. 
    filters: Repository[str, Filter] = None

    # A repository of IntegratedOutputSection objects. 
    integratedOutputSections: int = None

    # A repository of FieldOutputRequest objects. 
    fieldOutputRequests: Repository[str, FieldOutputRequest] = None

    # A repository of HistoryOutputRequest objects. 
    historyOutputRequests: Repository[str, HistoryOutputRequest] = None

    # A repository of OptimizationTask objects. 
    optimizationTasks: Repository[str, OptimizationTask] = None

    # A repository of TableCollection objects. 
    tableCollections: Repository[str, TableCollection] = None

    # A repository of EventSeriesType objects. 
    eventSeriesTypes: Repository[str, EventSeriesType] = None

    # A repository of EventSeriesData objects. 
    eventSeriesDatas: Repository[str, EventSeriesData] = None

    def __init__(self, name: str, description: str = '', stefanBoltzmann: float = None, 
                 absoluteZero: float = None, waveFormulation: SymbolicConstant = NOT_SET, 
                 modelType: SymbolicConstant = STANDARD_EXPLICIT, universalGas: float = None, 
                 copyConstraints: str = ON, copyConnectors: str = ON, copyInteractions: str = ON):
        """This method creates a Model object.

        Path
        ----
            - ```
            - mdb.Model
            - ```

        Parameters
        ----------
        name
            A String specifying the repository key. 
        description
            A String specifying the purpose and contents of the Model object. The default value is 
            an empty string. 
        stefanBoltzmann
            None or a Float specifying the Stefan-Boltzmann constant. The default value is None. 
        absoluteZero
            None or a Float specifying the absolute zero constant. The default value is None. 
        waveFormulation
            A SymbolicConstant specifying the type of incident wave formulation to be used in 
            acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value 
            is NOT_SET. 
        modelType
            A SymbolicConstant specifying the analysis model type. Possible values are 
            STANDARD_EXPLICIT and ELECTROMAGNETIC. The default is STANDARD_EXPLICIT. 
        universalGas
            None or a Float specifying the universal gas constant. The default value is None. 
        copyConstraints
            A boolean specifying whether to copy the constraints created in the model to the model 
            that instances this model. The default value is ON. 
        copyConnectors
            A boolean specifying whether to copy the connectors created in the model to the model 
            that instances this model. The default value is ON. 
        copyInteractions
            A boolean specifying whether to copy the interactions created in the model to the model 
            that instances this model. The default value is ON. 

        Returns
        -------
            A Model object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def ModelFromInputFile(self, name: str, inputFileName: str):
        """This method creates a Model object by reading the keywords in an input file and creating
        the corresponding Abaqus/CAE objects.

        Path
        ----
            - ```
            - mdb.ModelFromInputFile
            - ```

        Parameters
        ----------
        name
            A String specifying the repository key. 
        inputFileName
            A String specifying the name of the input file (including the .inp extension) to be 
            parsed into the new model. This String can also be the full path to the input file if it 
            is located in another directory. 

        Returns
        -------
            A Model object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def ModelFromOdbFile(self, name: str, odbFileName: str):
        """This method creates a Model object by reading an output database and creating any
        corresponding Abaqus/CAE objects.

        Path
        ----
            - ```
            - mdb.ModelFromOdbFile
            - ```

        Parameters
        ----------
        name
            A String specifying the repository key. 
        odbFileName
            A String specifying the name of the output database file (including the .odb extension) 
            to be read into the new model. This String can also be the full path to the output 
            database file if it is located in another directory. 

        Returns
        -------
            A Model object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def ModelFromNastranFile(self, modelName: str, inputFileName: str, 
                             sectionConsolidation: SymbolicConstant = PRESERVE_SECTION, 
                             preIntegratedShell: Boolean = OFF, weightMassScaling: Boolean = ON, 
                             loadCases: Boolean = ON, coupleBeamOffsets: Boolean = ON, cbar: str = B31, 
                             cquad4: str = S4, chexa: str = C3D8I, ctetra: str = C3D10, 
                             keepTranslatedFiles: Boolean = ON):
        """This method creates a Model object by reading the keywords in a Nastran bulk data file
        or Nastran input file and creating any corresponding Abaqus/CAE objects. The default
        values is discussed in following and can be defined alternatively in the Abaqus
        environment file as the one used for the translator from Nastran to Abaqus. For more
        information, see [Translating Nastran data to Abaqus
        files](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEEXCRefMap/simaexc-c-nasabaproc.htm?ContextScope=all).

        Path
        ----
            - ```
            - mdb.ModelFromNastranFile
            - ```

        Parameters
        ----------
        modelName
            A String specifying the repository key. 
        inputFileName
            A String specifying the name of the Nastran input file (including the .bdf, .dat, .nas, 
            .nastran, .blk, .bulk extension) to be read into the new model. This String can also be 
            the full path to the Nastran input file if it is located in another directory. 
        sectionConsolidation
            A SymbolicConstant specifying the method used to create shell section. Possible values 
            are PRESERVE_SECTION, GROUP_BY_MATERIAL, and NONE. If PRESERVE_SECTION is used, an 
            Abaqus section is created corresponding to each shell property ID. If GROUP_BY_MATERIAL 
            is used, a single Abaqus section is created for all homogeneous elements referencing the 
            same material. In both cases, material orientations and offsets are created using 
            discrete fields. If NONE is used, a separate shell section is created for each 
            combination of orientation, material offset, and/or thickness. The default is 
            PRESERVE_SECTION. 
        preIntegratedShell
            A Boolean specifying whether the pre-integrated shell section is created in default for 
            shell element. The default value is OFF. 
        weightMassScaling
            A Boolean specifying whether the value on the Nastran data line PARAM, WTMASS is used as 
            a multiplier for all density, mass, and rotary inertia values created in the Abaqus 
            input file. The default value is ON. 
        loadCases
            A Boolean specifying whether each SUBCASE for linear static analyses is translated to a 
            [LOAD 
            CASE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-loadcase.htm?ContextScope=all#simakey-r-loadcase) 
            option, and all such [LOAD 
            CASE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-loadcase.htm?ContextScope=all#simakey-r-loadcase) 
            options are grouped in a single STEP option. The default value is ON. 
        coupleBeamOffsets
            A Boolean specifying whether to translate the beam element connectivity to newly created 
            nodes at the offset location and rigidly coupling the new and original nodes. If not, 
            beam element offsets are translated to the CENTROID and [SHEAR 
            CENTER](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shearcenter.htm?ContextScope=all#simakey-r-shearcenter) 
            options, which are suboptions of the [BEAM GENERAL 
            SECTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamgeneralsection.htm?ContextScope=all#simakey-r-beamgeneralsection) 
            option. The default value is ON. When the beam element references a PBARL or PBEAML 
            property or if the beam offset has a significant component in the direction of the beam 
            axis, the setting for this argument is always ON. 
        cbar
            A String specifying the 2-node beam that is created from CBAR and CBEAM elements. 
            Possible values are B31 and B33. The default is B31. 
        cquad4
            A String specifying the 4-node shell that is created from CQUAD4 elements. Possible 
            values are S4 and S4R. The default is S4. If a reduced-integration element is chosen, 
            the enhanced hourglass formulation is applied automatically. 
        chexa
            A String specifying the 8-node brick that is created from CHEXA elements. Possible 
            values are C3D8I, C3D8 and C3D8R. The default is C3D8I. If a reduced-integration element 
            is chosen, the enhanced hourglass formulation is applied automatically. 
        ctetra
            A String specifying the 10-node tetrahedron that is created from CTETRA elements. 
            Possible values are C3D10 and C3D10M. The default is C3D10. 
        keepTranslatedFiles
            A Boolean specifying whether to keep the generated Abaqus input file after the model is 
            created from the Nastran input file. The default value is ON. 

        Returns
        -------
            A Model object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self, description: str = '', noPartsInputFile: Boolean = OFF, absoluteZero: float = None, 
                  stefanBoltzmann: float = None, waveFormulation: SymbolicConstant = NOT_SET, 
                  universalGas: float = None, restartJob: str = '', restartStep: str = '', 
                  restartIncrement: SymbolicConstant = None, endRestartStep: Boolean = OFF, 
                  globalJob: str = '', shellToSolid: Boolean = OFF, copyConstraints: Boolean = OFF, 
                  copyConnectors: Boolean = OFF, copyInteractions: Boolean = OFF):
        """This method modifies the Model object.

        Parameters
        ----------
        description
            A String specifying the purpose and contents of the Model object. The default value is 
            an empty string. 
        noPartsInputFile
            A Boolean specifying whether an input file should be written without parts and 
            assemblies. The default value is OFF. 
        absoluteZero
            None or a Float specifying the absolute zero constant. The default value is None. 
        stefanBoltzmann
            None or a Float specifying the Stefan-Boltzmann constant. The default value is None. 
        waveFormulation
            A SymbolicConstant specifying the type of incident wave formulation to be used in 
            acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value 
            is NOT_SET. 
        universalGas
            None or a Float specifying the universal gas constant. The default value is None. 
        restartJob
            A String specifying the name of the job that generated the restart data. 
        restartStep
            A String specifying the name of the step where the restart analysis will start. 
        restartIncrement
            An Int specifying the increment, interval, iteration or cycle where the restart analysis 
            will start. To select the end of the step use the SymbolicConstant STEP_END. 
        endRestartStep
            A Boolean specifying that the step specified by *restartStep* should be terminated at 
            the increment specified by *restartIncrement*. 
        globalJob
            A String specifying the name of the job that generated the results for the global model. 
        shellToSolid
            A Boolean specifying that a shell global model drives a solid submodel. 
        copyConstraints
            A Boolean specifying whether to copy the constraints created in the model to the model 
            that instances this model. 
        copyConnectors
            A Boolean specifying whether to copy the connectors created in the model to the model 
            that instances this model 
        copyInteractions
            A Boolean specifying whether to copy the interactions created in the model to the model 
            that instances this model. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
