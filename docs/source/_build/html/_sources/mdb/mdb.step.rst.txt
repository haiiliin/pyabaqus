====
Step
====

The Step commands described in this chapter are used to create and configure analysis steps. Step commands (output) describes the commands used to create and configure output requests and integrated output sections and the commands to configure diagnostic printing, monitoring, and restart. Step commands (miscellaneous) describes the commands used to configure controls, damping, and frequency tables.

Attributes
----------

- **mdb.models[name].steps[name].name**: A String specifying the repository key.
- **mdb.models[name].steps[name].explicit**: A SymbolicConstant specifying whether the step has an explicit procedure type (**procedureType**=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
- **mdb.models[name].steps[name].perturbation**: A Boolean specifying whether the step has a perturbation procedure type.
- **mdb.models[name].steps[name].nonmechanical**: A Boolean specifying whether the step has a mechanical procedure type.
- **mdb.models[name].steps[name].procedureType**: A SymbolicConstant specifying the Abaqus procedure. Possible values are: 
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
- **mdb.models[name].steps[name].suppressed**: A Boolean specifying whether the step is suppressed or not. The default value is OFF.
- **mdb.models[name].steps[name].fieldOutputRequestState**: A repository of :py:class:`abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState` objects.
- **mdb.models[name].steps[name].historyOutputRequestState**: A repository of :py:class:`abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState` objects.
- **mdb.models[name].steps[name].diagnosticPrint**: A :py:class:`abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
- **mdb.models[name].steps[name].monitor**: A :py:class:`abaqus.StepOutput.Monitor.Monitor` object.
- **mdb.models[name].steps[name].restart**: A :py:class:`abaqus.StepOutput.Restart.Restart` object.
- **mdb.models[name].steps[name].adaptiveMeshConstraintStates**: A repository of :py:class:`abaqus.Adaptivity.AdaptiveMeshConstraintState.AdaptiveMeshConstraintState` objects.
- **mdb.models[name].steps[name].adaptiveMeshDomains**: A repository of :py:class:`abaqus.Adaptivity.AdaptiveMeshDomain.AdaptiveMeshDomain` objects.
- **mdb.models[name].steps[name].control**: A :py:class:`abaqus.StepMiscellaneous.Control.Control` object.
- **mdb.models[name].steps[name].solverControl**: A :py:class:`abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
- **mdb.models[name].steps[name].boundaryConditionStates**: A repository of :py:class:`abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState` objects.
- **mdb.models[name].steps[name].interactionStates**: A repository of :py:class:`abaqus.Interaction.InteractionState.InteractionState` objects.
- **mdb.models[name].steps[name].loadStates**: A repository of :py:class:`abaqus.LoadAndLoadCase.LoadState.LoadState` objects.
- **mdb.models[name].steps[name].loadCases**: A repository of :py:class:`abaqus.LoadAndLoadCase.LoadCase.LoadCase` objects.
- **mdb.models[name].steps[name].predefinedFieldStates**: A repository of :py:class:`abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState` objects.
- **mdb.models[name].steps[name].activateElements**: A repository of :py:class:`abaqus.TableCollection.ActivateElements.ActivateElements` objects.



Create steps
------------

.. autoclass:: abaqus.Step.StepModel.StepModel
    :members:

Object features
---------------

Basic features of the Step
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.Step.Step
    :members:

.. autoclass:: abaqus.Step.StepBase.StepBase
    :members:

ALE features of the Step
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptivityStep.AdaptivityStep
    :members:

Output features of the Step
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.StepOutput.OutputStep.OutputStep
    :members:

Table Collection features of the Step
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.TableCollection.TableCollectionStep.TableCollectionStep
    :members:

AnalysisStep
~~~~~~~~~~~~

.. autoclass:: abaqus.Step.AnalysisStep.AnalysisStep
    :members:

AnnealStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.AnnealStep.AnnealStep
    :members:

BuckleStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.BuckleStep.BuckleStep
    :members:

ComplexFrequencyStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ComplexFrequencyStep.ComplexFrequencyStep
    :members:

CoupledTempDisplacementStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledTempDisplacementStep.CoupledTempDisplacementStep
    :members:

CoupledThermalElectricalStructuralStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledThermalElectricalStructuralStep.CoupledThermalElectricalStructuralStep
    :members:

CoupledThermalElectricStep
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledThermalElectricStep.CoupledThermalElectricStep
    :members:

DirectCyclicStep
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.DirectCyclicStep.DirectCyclicStep
    :members:

EmagTimeHarmonicStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.EmagTimeHarmonicStep.EmagTimeHarmonicStep
    :members:

ExplicitDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ExplicitDynamicsStep.ExplicitDynamicsStep
    :members:

FrequencyStep
~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.FrequencyStep.FrequencyStep
    :members:

GeostaticStep
~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.GeostaticStep.GeostaticStep
    :members:

HeatTransferStep
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.HeatTransferStep.HeatTransferStep
    :members:

ImplicitDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ImplicitDynamicsStep.ImplicitDynamicsStep
    :members:

InitialStep
~~~~~~~~~~~

.. autoclass:: abaqus.Step.InitialStep.InitialStep
    :members:

MassDiffusionStep
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.MassDiffusionStep.MassDiffusionStep
    :members:

ModalDynamicsStep
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ModalDynamicsStep.ModalDynamicsStep
    :members:

RandomResponseStep
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.RandomResponseStep.RandomResponseStep
    :members:

ResponseSpectrumStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ResponseSpectrumStep.ResponseSpectrumStep
    :members:

SoilsStep
~~~~~~~~~

.. autoclass:: abaqus.Step.SoilsStep.SoilsStep
    :members:

StaticLinearPerturbationStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticLinearPerturbationStep.StaticLinearPerturbationStep
    :members:

StaticRiksStep
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticRiksStep.StaticRiksStep
    :members:

StaticStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticStep.StaticStep
    :members:

SteadyStateDirectStep
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateDirectStep.SteadyStateDirectStep
    :members:

SteadyStateModalStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateModalStep.SteadyStateModalStep
    :members:

SteadyStateSubspaceStep
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateSubspaceStep.SteadyStateSubspaceStep
    :members:

SubspaceDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SubspaceDynamicsStep.SubspaceDynamicsStep
    :members:

SubstructureGenerateStep
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SubstructureGenerateStep.SubstructureGenerateStep
    :members:

TempDisplacementDynamicsStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep
    :members:

ViscoStep
~~~~~~~~~

.. autoclass:: abaqus.Step.ViscoStep.ViscoStep
    :members:
