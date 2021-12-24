# Model object

Abaqus creates a Model object named `Model-1` when a session is started.

## Access

```
mdb.models[name]
```

## Model(...)



This method creates a Model object.



### Path

```
mdb.Model
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *description*

  A String specifying the purpose and contents of the Model object. The default value is an empty string.

- *stefanBoltzmann*

  None or a Float specifying the Stefan-Boltzmann constant. The default value is None.

- *absoluteZero*

  None or a Float specifying the absolute zero constant. The default value is None.

- *waveFormulation*

  A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value is NOT_SET.

- *modelType*

  A SymbolicConstant specifying the analysis model type. Possible values are STANDARD_EXPLICIT and ELECTROMAGNETIC. The default is STANDARD_EXPLICIT.

- *universalGas*

  None or a Float specifying the universal gas constant. The default value is None.

- *copyConstraints*

  A boolean specifying whether to copy the constraints created in the model to the model that instances this model. The default value is ON.

- *copyConnectors*

  A boolean specifying whether to copy the connectors created in the model to the model that instances this model. The default value is ON.

- *copyInteractions*

  A boolean specifying whether to copy the interactions created in the model to the model that instances this model. The default value is ON.

### Return value

A Model object.

### Exceptions

None.



## ModelFromInputFile(...)



This method creates a Model object by reading the keywords in an input file and creating the corresponding Abaqus/CAE objects.



### Path

```
mdb.ModelFromInputFile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *inputFileName*

  A String specifying the name of the input file (including the .inp extension) to be parsed into the new model. This String can also be the full path to the input file if it is located in another directory.

### Optional arguments

None.

### Return value

A Model object.

### Exceptions

None.



## ModelFromOdbFile(...)



This method creates a Model object by reading an output database and creating any corresponding Abaqus/CAE objects.



### Path

```
mdb.ModelFromOdbFile
```

### Required arguments

- *name*

  A String specifying the repository key.

- *odbFileName*

  A String specifying the name of the output database file (including the .odb extension) to be read into the new model. This String can also be the full path to the output database file if it is located in another directory.

### Optional arguments

None.

### Return value

A Model object.

### Exceptions

None.



## ModelFromNastranFile(...)



This method creates a Model object by reading the keywords in a Nastran bulk data file or Nastran input file and creating any corresponding Abaqus/CAE objects. The default values is discussed in following and can be defined alternatively in the Abaqus environment file as the one used for the translator from Nastran to Abaqus. For more information, see [Translating Nastran data to Abaqus files](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEEXCRefMap/simaexc-c-nasabaproc.htm?ContextScope=all).



### Path

```
mdb.ModelFromNastranFile
```

### Required arguments

- *modelName*

  A String specifying the repository key.

- *inputFileName*

  A String specifying the name of the Nastran input file (including the .bdf, .dat, .nas, .nastran, .blk, .bulk extension) to be read into the new model. This String can also be the full path to the Nastran input file if it is located in another directory.

### Optional arguments

- *sectionConsolidation*

  A SymbolicConstant specifying the method used to create shell section. Possible values are PRESERVE_SECTION, GROUP_BY_MATERIAL, and NONE. If PRESERVE_SECTION is used, an Abaqus section is created corresponding to each shell property ID. If GROUP_BY_MATERIAL is used, a single Abaqus section is created for all homogeneous elements referencing the same material. In both cases, material orientations and offsets are created using discrete fields. If NONE is used, a separate shell section is created for each combination of orientation, material offset, and/or thickness. The default is PRESERVE_SECTION.

- *preIntegratedShell*

  A Boolean specifying whether the pre-integrated shell section is created in default for shell element. The default value is OFF.

- *weightMassScaling*

  A Boolean specifying whether the value on the Nastran data line PARAM, WTMASS is used as a multiplier for all density, mass, and rotary inertia values created in the Abaqus input file. The default value is ON.

- *loadCases*

  A Boolean specifying whether each SUBCASE for linear static analyses is translated to a [LOAD CASE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-loadcase.htm?ContextScope=all#simakey-r-loadcase) option, and all such [LOAD CASE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-loadcase.htm?ContextScope=all#simakey-r-loadcase) options are grouped in a single [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step) option. The default value is ON.

- *coupleBeamOffsets*

  A Boolean specifying whether to translate the beam element connectivity to newly created nodes at the offset location and rigidly coupling the new and original nodes. If not, beam element offsets are translated to the [CENTROID](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-centroid.htm?ContextScope=all#simakey-r-centroid) and [SHEAR CENTER](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-shearcenter.htm?ContextScope=all#simakey-r-shearcenter) options, which are suboptions of the [BEAM GENERAL SECTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-beamgeneralsection.htm?ContextScope=all#simakey-r-beamgeneralsection) option. The default value is ON. When the beam element references a PBARL or PBEAML property or if the beam offset has a significant component in the direction of the beam axis, the setting for this argument is always ON.

- *cbar*

  A String specifying the 2-node beam that is created from CBAR and CBEAM elements. Possible values are B31 and B33. The default is B31.

- *cquad4*

  A String specifying the 4-node shell that is created from CQUAD4 elements. Possible values are S4 and S4R. The default is S4. If a reduced-integration element is chosen, the enhanced hourglass formulation is applied automatically.

- *chexa*

  A String specifying the 8-node brick that is created from CHEXA elements. Possible values are C3D8I, C3D8 and C3D8R. The default is C3D8I. If a reduced-integration element is chosen, the enhanced hourglass formulation is applied automatically.

- *ctetra*

  A String specifying the 10-node tetrahedron that is created from CTETRA elements. Possible values are C3D10 and C3D10M. The default is C3D10.

- *keepTranslatedFiles*

  A Boolean specifying whether to keep the generated Abaqus input file after the model is created from the Nastran input file. The default value is ON.

### Return value

A Model object.

### Exceptions

None.



## setValues(...)



This method modifies the Model object.



### Required arguments

None.

### Optional arguments

- *description*

  A String specifying the purpose and contents of the Model object. The default value is an empty string.

- *noPartsInputFile*

  A Boolean specifying whether an input file should be written without parts and assemblies. The default value is OFF.

- *absoluteZero*

  None or a Float specifying the absolute zero constant. The default value is None.

- *stefanBoltzmann*

  None or a Float specifying the Stefan-Boltzmann constant. The default value is None.

- *waveFormulation*

  A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value is NOT_SET.

- *universalGas*

  None or a Float specifying the universal gas constant. The default value is None.

- *restartJob*

  A String specifying the name of the job that generated the restart data.

- *restartStep*

  A String specifying the name of the step where the restart analysis will start.

- *restartIncrement*

  An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. To select the end of the step use the SymbolicConstant STEP_END.

- *endRestartStep*

  A Boolean specifying that the step specified by *restartStep* should be terminated at the increment specified by *restartIncrement*.

- *globalJob*

  A String specifying the name of the job that generated the results for the global model.

- *shellToSolid*

  A Boolean specifying that a shell global model drives a solid submodel.

- *copyConstraints*

  A Boolean specifying whether to copy the constraints created in the model to the model that instances this model.

- *copyConnectors*

  A Boolean specifying whether to copy the connectors created in the model to the model that instances this model

- *copyInteractions*

  A Boolean specifying whether to copy the interactions created in the model to the model that instances this model.

### Return value

None.

### Exceptions

None.



## Members

The Model object can have the following members:

- *name*

  A String specifying the repository key.

- *stefanBoltzmann*

  None or a Float specifying the Stefan-Boltzmann constant. The default value is None.

- *absoluteZero*

  None or a Float specifying the absolute zero constant. The default value is None.

- *waveFormulation*

  A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value is NOT_SET.

- *universalGas*

  None or a Float specifying the universal gas constant. The default value is None.

- *noPartsInputFile*

  A Boolean specifying whether an input file should be written without parts and assemblies. The default value is OFF.

- *restartIncrement*

  An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. To select the end of the step use the SymbolicConstant STEP_END.

- *endRestartStep*

  A Boolean specifying that the step specified by *restartStep* should be terminated at the increment specified by *restartIncrement*.

- *shellToSolid*

  A Boolean specifying that a shell global model drives a solid submodel.

- *lastChangedCount*

  A Float specifying the time stamp that indicates when the model was last changed.

- *description*

  A String specifying the purpose and contents of the Model object. The default value is an empty string.

- *restartJob*

  A String specifying the name of the job that generated the restart data.

- *restartStep*

  A String specifying the name of the step where the restart analysis will start.

- *globalJob*

  A String specifying the name of the job that generated the results for the global model.

- *copyConstraints*

  A boolean specifying the status of constraints created in a model, in the model which instances this model.

- *copyConnectors*

  A boolean specifying the status of connectors created in a model, in the model which instances this model.

- *copyInteractions*

  A boolean specifying the status of interactions created in a model, in the model which instances this model.

- *keywordBlock*

  A [KeywordBlock](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-keywordblockpyc.htm?ContextScope=all) object.

- *rootAssembly*

  An [Assembly](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?ContextScope=all) object.

- *amplitudes*

  A repository of [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) objects.

- *profiles*

  A repository of [Profile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) objects.

- *boundaryConditions*

  A repository of [BoundaryCondition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?ContextScope=all) objects.

- *constraints*

  A repository of [Constraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintpyc.htm?ContextScope=all) objects.

- *analyticalFields*

  A repository of [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) objects.

- *discreteFields*

  A repository of [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) objects.

- *predefinedFields*

  A repository of [PredefinedField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldpyc.htm?ContextScope=all) objects.

- *interactions*

  A repository of [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) objects.

- *interactionProperties*

  A repository of [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) objects.

- *contactControls*

  A repository of [ContactControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactcontrolpyc.htm?ContextScope=all) objects.

- *contactInitializations*

  A repository of [ContactInitialization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactinitializationpyc.htm?ContextScope=all) objects.

- *contactStabilizations*

  A repository of [ContactStabilization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstabilizationpyc.htm?ContextScope=all) objects.

- *linkedInstances*

  A tuple of tuples of Strings specifying the linked child PartInstance name in the current model to the corresponding parent PartInstance name in a different model.

- *linkedParts*

  A tuple of tuples of Strings specifying the linked child Part name in the current model to the corresponding parent Part name in a different model.

- *loads*

  A repository of [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) objects.

- *materials*

  A repository of [Material](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialpyc.htm?ContextScope=all) objects.

- *calibrations*

  A repository of [Calibration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-calibrationpyc.htm?ContextScope=all) objects.

- *sections*

  A repository of [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) objects.

- *remeshingRules*

  A repository of [RemeshingRule](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-remeshingrulepyc.htm?ContextScope=all) objects.

- *sketches*

  A repository of [ConstrainedSketch](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) objects.

- *parts*

  A repository of [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) objects.

- *steps*

  A repository of [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) objects.

- *featureOptions*

  A [FeatureOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featureoptionspyc.htm?ContextScope=all) object.

- *adaptiveMeshConstraints*

  A repository of [AdaptiveMeshConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshconstraintpyc.htm?ContextScope=all) objects.

- *adaptiveMeshControls*

  A repository of [AdaptiveMeshControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshcontrolpyc.htm?ContextScope=all) objects.

- *timePoints*

  A repository of [TimePoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-timepointpyc.htm?ContextScope=all) objects.

- *filters*

  A repository of [Filter](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filterpyc.htm?ContextScope=all) objects.

- *integratedOutputSections*

  A repository of [IntegratedOutputSection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-integratedoutputsectionpyc.htm?ContextScope=all) objects.

- *fieldOutputRequests*

  A repository of [FieldOutputRequest](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?ContextScope=all) objects.

- *historyOutputRequests*

  A repository of [HistoryOutputRequest](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?ContextScope=all) objects.

- *optimizationTasks*

  A repository of [OptimizationTask](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationtaskpyc.htm?ContextScope=all) objects.

- *tableCollections*

  A repository of [TableCollection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tableCollectionpyc.htm?ContextScope=all#simaker-c-tableCollectionpyc) objects.

- *eventSeriesTypes*

  A repository of [EventSeriesType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eventseriestypepyc.htm?ContextScope=all#simaker-c-eventseriestypepyc) objects.

- *eventSeriesDatas*

  A repository of [EventSeriesData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eventseriespyc.htm?ContextScope=all#simaker-c-eventseriespyc) objects.



## Corresponding analysis keywords

- [PHYSICAL CONSTANTS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-physicalconstants.htm?ContextScope=all#simakey-r-physicalconstants)