=====
Model
=====

Model commands are used to create Abaqus/CAE models. A finished model contains all the data that Abaqus/CAE needs to create and submit an analysis to Abaqus/Standard or Abaqus/Explicit. Models are stored in a model database.

Attributes
----------

- **mdb.models[name].name**: A String specifying the repository key.
- **mdb.models[name].stefanBoltzmann**: None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
- **mdb.models[name].absoluteZero**: None or a Float specifying the absolute zero constant. The default value is None.
- **mdb.models[name].waveFormulation**: A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value is NOT_SET.
- **mdb.models[name].universalGas**: None or a Float specifying the universal gas constant. The default value is None.
- **mdb.models[name].noPartsInputFile**: A Boolean specifying whether an input file should be written without parts and assemblies. The default value is OFF.
- **mdb.models[name].restartIncrement**: An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. To select the end of the step use the SymbolicConstant STEP_END.
- **mdb.models[name].endRestartStep**: A Boolean specifying that the step specified by **restartStep** should be terminated at the increment specified by **restartIncrement**.
- **mdb.models[name].shellToSolid**: A Boolean specifying that a shell global model drives a solid submodel.
- **mdb.models[name].lastChangedCount**: A Float specifying the time stamp that indicates when the model was last changed.
- **mdb.models[name].description**: A String specifying the purpose and contents of the Model object. The default value is an empty string.
- **mdb.models[name].restartJob**: A String specifying the name of the job that generated the restart data.
- **mdb.models[name].restartStep**: A String specifying the name of the step where the restart analysis will start.
- **mdb.models[name].globalJob**: A String specifying the name of the job that generated the results for the global model.
- **mdb.models[name].copyConstraints**: A boolean specifying the status of constraints created in a model, in the model which instances this model.
- **mdb.models[name].copyConnectors**: A boolean specifying the status of connectors created in a model, in the model which instances this model.
- **mdb.models[name].copyInteractions**: A boolean specifying the status of interactions created in a model, in the model which instances this model.
- **mdb.models[name].keywordBlock**: A :py:class:`abaqus.Model.KeywordBlock.KeywordBlock` object.
- **mdb.models[name].rootAssembly**: An :py:class:`abaqus.Assembly.Assembly.Assembly` object.
- **mdb.models[name].amplitudes**: A repository of :py:class:`abaqus.Amplitude.Amplitude.Amplitude` objects.
- **mdb.models[name].profiles**: A repository of :py:class:`abaqus.BeamSectionProfile.Profile.Profile` objects.
- **mdb.models[name].boundaryConditions**: A repository of :py:class:`abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition` objects.
- **mdb.models[name].constraints**: A repository of :py:class:`abaqus.Constraint.Constraint.Constraint` objects.
- **mdb.models[name].analyticalFields**: A repository of :py:class:`abaqus.Field.AnalyticalField.AnalyticalField` objects.
- **mdb.models[name].discreteFields**: A repository of :py:class:`abaqus.Field.DiscreteField.DiscreteField` objects.
- **mdb.models[name].predefinedFields**: A repository of :py:class:`abaqus.PredefinedField.PredefinedField.PredefinedField` objects.
- **mdb.models[name].interactions**: A repository of :py:class:`abaqus.Interaction.Interaction.Interaction` objects.
- **mdb.models[name].interactionProperties**: A repository of :py:class:`abaqus.Interaction.ContactProperty.ContactProperty` objects.
- **mdb.models[name].contactControls**: A repository of :py:class:`abaqus.Interaction.ContactControl.ContactControl` objects.
- **mdb.models[name].contactInitializations**: A repository of :py:class:`abaqus.Interaction.ContactInitialization.ContactInitialization` objects.
- **mdb.models[name].contactStabilizations**: A repository of :py:class:`abaqus.Interaction.ContactStabilization.ContactStabilization` objects.
- **mdb.models[name].linkedInstances**: A tuple of tuples of Strings specifying the linked child PartInstance name in the current model to the corresponding parent PartInstance name in a different model.
- **mdb.models[name].linkedParts**: A tuple of tuples of Strings specifying the linked child Part name in the current model to the corresponding parent Part name in a different model.
- **mdb.models[name].loads**: A repository of :py:class:`abaqus.LoadAndLoadCase.Load.Load` objects.
- **mdb.models[name].materials**: A repository of :py:class:`abaqus.Material.Material.Material` objects.
- **mdb.models[name].calibrations**: A repository of :py:class:`abaqus.BoundaryCondition.Calibration.Calibration` objects.
- **mdb.models[name].sections**: A repository of :py:class:`abaqus.Section.Section.Section` objects.
- **mdb.models[name].remeshingRules**: A repository of :py:class:`abaqus.Adaptivity.RemeshingRule.RemeshingRule` objects.
- **mdb.models[name].sketches**: A repository of :py:class:`abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch` objects.
- **mdb.models[name].parts**: A repository of :py:class:`abaqus.Part.Part.Part` objects.
- **mdb.models[name].steps**: A repository of :py:class:`abaqus.Step.Step.Step` objects.
- **mdb.models[name].featureOptions**: A :py:class:`abaqus.Feature.FeatureOptions.FeatureOptions` object.
- **mdb.models[name].adaptiveMeshConstraints**: A repository of :py:class:`abaqus.Adaptivity.AdaptiveMeshConstraint.AdaptiveMeshConstraint` objects.
- **mdb.models[name].adaptiveMeshControls**: A repository of :py:class:`abaqus.Adaptivity.AdaptiveMeshControl.AdaptiveMeshControl` objects.
- **mdb.models[name].timePoints**: A repository of :py:class:`abaqus.StepOutput.TimePoint.TimePoint` objects.
- **mdb.models[name].filters**: A repository of :py:class:`abaqus.Filter.Filter.Filter` objects.
- **mdb.models[name].integratedOutputSections**: A repository of :py:class:`abaqus.StepOutput.IntegratedOutputSection.IntegratedOutputSection` objects.
- **mdb.models[name].fieldOutputRequests**: A repository of :py:class:`abaqus.StepOutput.FieldOutputRequest.FieldOutputRequest` objects.
- **mdb.models[name].historyOutputRequests**: A repository of :py:class:`abaqus.StepOutput.HistoryOutputRequest.HistoryOutputRequest` objects.
- **mdb.models[name].optimizationTasks**: A repository of :py:class:`abaqus.Optimization.OptimizationTask.OptimizationTask` objects.
- **mdb.models[name].tableCollections**: A repository of :py:class:`abaqus.TableCollection.TableCollection.TableCollection` objects.
- **mdb.models[name].eventSeriesTypes**: A repository of :py:class:`abaqus.TableCollection.EventSeriesType.EventSeriesType` objects.
- **mdb.models[name].eventSeriesDatas**: A repository of :py:class:`abaqus.TableCollection.EventSeriesData.EventSeriesData` objects.



Create models
--------------

.. autoclass:: abaqus.Mdb.Mdb.Mdb
    :members:


Object features
---------------

Basic Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Model.ModelBase.ModelBase
    :members:

ALE Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptivityModel.AdaptivityModel
    :members:


Assembly Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Assembly.AssemblyModel.AssemblyModel
    :members:


Amplitude Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Amplitude.AmplitudeModel.AmplitudeModel
    :members:


Boundary Condition Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel
    :members:


Calibration Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Calibration.CalibrationModel.CalibrationModel
    :members:


Constraint Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Constraint.ConstraintModel.ConstraintModel
    :members:


Filter Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Filter.FilterModel.FilterModel
    :members:


Interaction Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Interaction.InteractionModel.InteractionModel
    :members:


Load Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Load.LoadModel.LoadModel
    :members:


Material Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Material.MaterialModel.MaterialModel
    :members:


Optimization Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel
    :members:


Part Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Part.PartModel.PartModel
    :members:


Predefined Field Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel
    :members:


Beam Section Profile Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel
    :members:


Output Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.StepOutput.OutputModel.OutputModel
    :members:


Section Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Section.SectionModel.SectionModel
    :members:


Sketch Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Sketch.SketchModel.SketchModel
    :members:


Step Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.StepModel.StepModel
    :members:


Table Collection Features of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.TableCollection.TableCollectionModel.TableCollectionModel
    :members:

KeywordBlock
~~~~~~~~~~~~

.. autoclass:: abaqus.Model.KeywordBlock.KeywordBlock
    :members: