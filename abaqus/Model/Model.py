import typing

from abaqusConstants import *
from ..Amplitude.ActuatorAmplitude import ActuatorAmplitude
from ..Amplitude.CorrelationArray import CorrelationArray
from ..Amplitude.DecayAmplitude import DecayAmplitude
from ..Amplitude.EquallySpacedAmplitude import EquallySpacedAmplitude
from ..Amplitude.ModulatedAmplitude import ModulatedAmplitude
from ..Amplitude.PeriodicAmplitude import PeriodicAmplitude
from ..Amplitude.PsdDefinition import PsdDefinition
from ..Amplitude.SmoothStepAmplitude import SmoothStepAmplitude
from ..Amplitude.SolutionDependentAmplitude import SolutionDependentAmplitude
from ..Amplitude.SpectrumAmplitude import SpectrumAmplitude
from ..Amplitude.TabularAmplitude import TabularAmplitude
from ..Assembly.Model import Model as AssemblyModel
from ..Assembly.PartInstance import PartInstance
from ..Assembly.PartInstanceArray import PartInstanceArray
from ..BasicGeometry.ModelDot import ModelDot
from ..BasicGeometry.ModelDotArray import ModelDotArray
from ..BoundaryCondition.AccelerationBC import AccelerationBC
from ..BoundaryCondition.AccelerationBaseMotionBC import AccelerationBaseMotionBC
from ..BoundaryCondition.AcousticPressureBC import AcousticPressureBC
from ..BoundaryCondition.Calibration import Calibration
from ..BoundaryCondition.ConcentrationBC import ConcentrationBC
from ..BoundaryCondition.ConnAccelerationBC import ConnAccelerationBC
from ..BoundaryCondition.ConnDisplacementBC import ConnDisplacementBC
from ..BoundaryCondition.ConnVelocityBC import ConnVelocityBC
from ..BoundaryCondition.DisplacementBC import DisplacementBC
from ..BoundaryCondition.DisplacementBaseMotionBC import DisplacementBaseMotionBC
from ..BoundaryCondition.ElectricPotentialBC import ElectricPotentialBC
from ..BoundaryCondition.EulerianBC import EulerianBC
from ..BoundaryCondition.EulerianMotionBC import EulerianMotionBC
from ..BoundaryCondition.FluidCavityPressureBC import FluidCavityPressureBC
from ..BoundaryCondition.MagneticVectorPotentialBC import MagneticVectorPotentialBC
from ..BoundaryCondition.MaterialFlowBC import MaterialFlowBC
from ..BoundaryCondition.PorePressureBC import PorePressureBC
from ..BoundaryCondition.RetainedNodalDofsBC import RetainedNodalDofsBC
from ..BoundaryCondition.SecondaryBaseBC import SecondaryBaseBC
from ..BoundaryCondition.SubmodelBC import SubmodelBC
from ..BoundaryCondition.TemperatureBC import TemperatureBC
from ..BoundaryCondition.VelocityBC import VelocityBC
from ..BoundaryCondition.VelocityBaseMotionBC import VelocityBaseMotionBC
from ..Connector.ConnectorBehaviorOptionArray import ConnectorBehaviorOptionArray
from ..Constraint.AdjustPoints import AdjustPoints
from ..Constraint.Coupling import Coupling
from ..Constraint.DisplayBody import DisplayBody
from ..Constraint.EmbeddedRegion import EmbeddedRegion
from ..Constraint.Equation import Equation
from ..Constraint.MultipointConstraint import MultipointConstraint
from ..Constraint.RigidBody import RigidBody
from ..Constraint.ShellSolidCoupling import ShellSolidCoupling
from ..Constraint.Tie import Tie
from ..Datum.DatumAxis import DatumAxis
from ..Interaction.AcousticImpedance import AcousticImpedance
from ..Interaction.AcousticImpedanceProp import AcousticImpedanceProp
from ..Interaction.ActuatorSensor import ActuatorSensor
from ..Interaction.ActuatorSensorProp import ActuatorSensorProp
from ..Interaction.CavityRadiation import CavityRadiation
from ..Interaction.CavityRadiationProp import CavityRadiationProp
from ..Interaction.ConcentratedFilmCondition import ConcentratedFilmCondition
from ..Interaction.ConcentratedRadiationToAmbient import ConcentratedRadiationToAmbient
from ..Interaction.ContactExp import ContactExp
from ..Interaction.ContactProperty import ContactProperty
from ..Interaction.ContactPropertyAssignment import ContactPropertyAssignment
from ..Interaction.ContactStd import ContactStd
from ..Interaction.CyclicSymmetry import CyclicSymmetry
from ..Interaction.ElasticFoundation import ElasticFoundation
from ..Interaction.ExpContactControl import ExpContactControl
from ..Interaction.ExpInitialization import ExpInitialization
from ..Interaction.FilmCondition import FilmCondition
from ..Interaction.FilmConditionProp import FilmConditionProp
from ..Interaction.FluidCavity import FluidCavity
from ..Interaction.FluidCavityProperty import FluidCavityProperty
from ..Interaction.FluidExchange import FluidExchange
from ..Interaction.FluidExchangeProperty import FluidExchangeProperty
from ..Interaction.FluidInflator import FluidInflator
from ..Interaction.FluidInflatorProperty import FluidInflatorProperty
from ..Interaction.IncidentWave import IncidentWave
from ..Interaction.IncidentWaveProperty import IncidentWaveProperty
from ..Interaction.InitializationAssignment import InitializationAssignment
from ..Interaction.MainSecondaryAssignment import MainSecondaryAssignment
from ..Interaction.Model import Model as InteractionModel
from ..Interaction.ModelChange import ModelChange
from ..Interaction.PressurePenetration import PressurePenetration
from ..Interaction.RadiationToAmbient import RadiationToAmbient
from ..Interaction.RegionPairs import RegionPairs
from ..Interaction.SelfContactExp import SelfContactExp
from ..Interaction.SelfContactStd import SelfContactStd
from ..Interaction.SlidingFormulationAssignment import SlidingFormulationAssignment
from ..Interaction.SlidingTransitionAssignments import SlidingTransitionAssignments
from ..Interaction.SmoothingAssignment import SmoothingAssignment
from ..Interaction.StabilizationAssignment import StabilizationAssignment
from ..Interaction.StdContactControl import StdContactControl
from ..Interaction.StdInitialization import StdInitialization
from ..Interaction.StdStabilization import StdStabilization
from ..Interaction.StdXplCosimulation import StdXplCosimulation
from ..Interaction.SurfaceBeamSmoothingAssignment import SurfaceBeamSmoothingAssignment
from ..Interaction.SurfaceCrushTriggerAssignment import SurfaceCrushTriggerAssignment
from ..Interaction.SurfaceFeatureAssignment import SurfaceFeatureAssignment
from ..Interaction.SurfaceFrictionAssignment import SurfaceFrictionAssignment
from ..Interaction.SurfaceOffsetAssignment import SurfaceOffsetAssignment
from ..Interaction.SurfaceThicknessAssignment import SurfaceThicknessAssignment
from ..Interaction.SurfaceToSurfaceContactExp import SurfaceToSurfaceContactExp
from ..Interaction.SurfaceToSurfaceContactStd import SurfaceToSurfaceContactStd
from ..Interaction.SurfaceVertexCriteriaAssignment import SurfaceVertexCriteriaAssignment
from ..Interaction.XFEMCrackGrowth import XFEMCrackGrowth
from ..LoadAndLoadCase.BodyCharge import BodyCharge
from ..LoadAndLoadCase.BodyConcentrationFlux import BodyConcentrationFlux
from ..LoadAndLoadCase.BodyCurrent import BodyCurrent
from ..LoadAndLoadCase.BodyCurrentDensity import BodyCurrentDensity
from ..LoadAndLoadCase.BodyForce import BodyForce
from ..LoadAndLoadCase.BodyHeatFlux import BodyHeatFlux
from ..LoadAndLoadCase.BoltLoad import BoltLoad
from ..LoadAndLoadCase.ConcCharge import ConcCharge
from ..LoadAndLoadCase.ConcConcFlux import ConcConcFlux
from ..LoadAndLoadCase.ConcCurrent import ConcCurrent
from ..LoadAndLoadCase.ConcPoreFluid import ConcPoreFluid
from ..LoadAndLoadCase.ConcentratedForce import ConcentratedForce
from ..LoadAndLoadCase.ConcentratedHeatFlux import ConcentratedHeatFlux
from ..LoadAndLoadCase.ConnectorForce import ConnectorForce
from ..LoadAndLoadCase.ConnectorMoment import ConnectorMoment
from ..LoadAndLoadCase.CoriolisForce import CoriolisForce
from ..LoadAndLoadCase.Gravity import Gravity
from ..LoadAndLoadCase.InertiaRelief import InertiaRelief
from ..LoadAndLoadCase.InwardVolAccel import InwardVolAccel
from ..LoadAndLoadCase.LineLoad import LineLoad
from ..LoadAndLoadCase.LoadCase import LoadCase
from ..LoadAndLoadCase.Moment import Moment
from ..LoadAndLoadCase.PEGLoad import PEGLoad
from ..LoadAndLoadCase.PipePressure import PipePressure
from ..LoadAndLoadCase.Pressure import Pressure
from ..LoadAndLoadCase.RotationalBodyForce import RotationalBodyForce
from ..LoadAndLoadCase.ShellEdgeLoad import ShellEdgeLoad
from ..LoadAndLoadCase.SubmodelSB import SubmodelSB
from ..LoadAndLoadCase.SubstructureLoad import SubstructureLoad
from ..LoadAndLoadCase.SurfaceCharge import SurfaceCharge
from ..LoadAndLoadCase.SurfaceConcentrationFlux import SurfaceConcentrationFlux
from ..LoadAndLoadCase.SurfaceCurrent import SurfaceCurrent
from ..LoadAndLoadCase.SurfaceCurrentDensity import SurfaceCurrentDensity
from ..LoadAndLoadCase.SurfaceHeatFlux import SurfaceHeatFlux
from ..LoadAndLoadCase.SurfacePoreFluid import SurfacePoreFluid
from ..LoadAndLoadCase.SurfaceTraction import SurfaceTraction
from ..Material.Material import Material
from ..Part.Part import Part
from ..PredefinedField.Field import Field
from ..PredefinedField.FluidCavityPressure import FluidCavityPressure
from ..PredefinedField.InitialState import InitialState
from ..PredefinedField.KinematicHardening import KinematicHardening
from ..PredefinedField.MaterialAssignment import MaterialAssignment
from ..PredefinedField.Stress import Stress
from ..PredefinedField.Temperature import Temperature
from ..PredefinedField.Velocity import Velocity
from ..Region.Region import Region
from ..Region.RegionArray import RegionArray
from ..Section.AcousticInfiniteSection import AcousticInfiniteSection
from ..Section.AcousticInterfaceSection import AcousticInterfaceSection
from ..Section.BeamSection import BeamSection
from ..Section.CohesiveSection import CohesiveSection
from ..Section.CompositeShellSection import CompositeShellSection
from ..Section.CompositeSolidSection import CompositeSolidSection
from ..Section.ConnectorSection import ConnectorSection
from ..Section.EulerianSection import EulerianSection
from ..Section.GasketSection import GasketSection
from ..Section.GeneralStiffnessSection import GeneralStiffnessSection
from ..Section.HomogeneousShellSection import HomogeneousShellSection
from ..Section.HomogeneousSolidSection import HomogeneousSolidSection
from ..Section.MPCSection import MPCSection
from ..Section.MembraneSection import MembraneSection
from ..Section.PEGSection import PEGSection
from ..Section.SectionLayerArray import SectionLayerArray
from ..Section.SurfaceSection import SurfaceSection
from ..Section.TrussSection import TrussSection
from ..Sketcher.ConstrainedSketch import ConstrainedSketch
from ..Step.AnnealStep import AnnealStep
from ..Step.BuckleStep import BuckleStep
from ..Step.ComplexFrequencyStep import ComplexFrequencyStep
from ..Step.CoupledTempDisplacementStep import CoupledTempDisplacementStep
from ..Step.CoupledThermalElectricStep import CoupledThermalElectricStep
from ..Step.CoupledThermalElectricalStructuralStep import CoupledThermalElectricalStructuralStep
from ..Step.DirectCyclicStep import DirectCyclicStep
from ..Step.EmagTimeHarmonicStep import EmagTimeHarmonicStep
from ..Step.ExplicitDynamicsStep import ExplicitDynamicsStep
from ..Step.FrequencyStep import FrequencyStep
from ..Step.GeostaticStep import GeostaticStep
from ..Step.HeatTransferStep import HeatTransferStep
from ..Step.ImplicitDynamicsStep import ImplicitDynamicsStep
from ..Step.MassDiffusionStep import MassDiffusionStep
from ..Step.ModalDynamicsStep import ModalDynamicsStep
from ..Step.RandomResponseStep import RandomResponseStep
from ..Step.ResponseSpectrumStep import ResponseSpectrumStep
from ..Step.SoilsStep import SoilsStep
from ..Step.StaticLinearPerturbationStep import StaticLinearPerturbationStep
from ..Step.StaticRiksStep import StaticRiksStep
from ..Step.StaticStep import StaticStep
from ..Step.SteadyStateDirectStep import SteadyStateDirectStep
from ..Step.SteadyStateModalStep import SteadyStateModalStep
from ..Step.SteadyStateSubspaceStep import SteadyStateSubspaceStep
from ..Step.SubspaceDynamicsStep import SubspaceDynamicsStep
from ..Step.SubstructureGenerateStep import SubstructureGenerateStep
from ..Step.TempDisplacementDynamicsStep import TempDisplacementDynamicsStep
from ..Step.ViscoStep import ViscoStep
from ..StepMiscellaneous.CompositeDamping import CompositeDamping
from ..StepMiscellaneous.DirectDamping import DirectDamping
from ..StepMiscellaneous.DirectDampingByFrequency import DirectDampingByFrequency
from ..StepMiscellaneous.EmagTimeHarmonicFrequencyArray import EmagTimeHarmonicFrequencyArray
from ..StepMiscellaneous.MassScalingArray import MassScalingArray
from ..StepMiscellaneous.RandomResponseFrequencyArray import RandomResponseFrequencyArray
from ..StepMiscellaneous.RayleighDamping import RayleighDamping
from ..StepMiscellaneous.RayleighDampingByFrequency import RayleighDampingByFrequency
from ..StepMiscellaneous.ResponseSpectrumComponentArray import ResponseSpectrumComponentArray
from ..StepMiscellaneous.SteadyStateDirectFrequencyArray import SteadyStateDirectFrequencyArray
from ..StepMiscellaneous.SteadyStateModalFrequencyArray import SteadyStateModalFrequencyArray
from ..StepMiscellaneous.SteadyStateSubspaceFrequencyArray import SteadyStateSubspaceFrequencyArray
from ..StepMiscellaneous.StructuralDamping import StructuralDamping
from ..StepMiscellaneous.StructuralDampingByFrequency import StructuralDampingByFrequency
from ..StepMiscellaneous.SubstructureGenerateFrequencyArray import SubstructureGenerateFrequencyArray
from ..StepMiscellaneous.SubstructureGenerateModesArray import SubstructureGenerateModesArray
from ..StepOutput.FieldOutputRequest import FieldOutputRequest
from ..StepOutput.HistoryOutputRequest import HistoryOutputRequest


class PolarityAssignments:
    pass


class Model(InteractionModel, AssemblyModel):

    def ActuatorAmplitude(self, name: str, timeSpan: SymbolicConstant = STEP) -> ActuatorAmplitude:
        """This method creates a ActuatorAmplitude object.

        Path
        ----
            - mdb.models[name].ActuatorAmplitude
            - session.odbs[name].ActuatorAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            An ActuatorAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = ActuatorAmplitude(name, timeSpan)
        return amplitude

    def DecayAmplitude(self, name: str, initial: float, maximum: float, start: float, decayTime: float,
                       timeSpan: SymbolicConstant = STEP) -> DecayAmplitude:
        """This method creates a DecayAmplitude object.

        Path
        ----
            - mdb.models[name].DecayAmplitude
            - session.odbs[name].DecayAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        initial
            A Float specifying the constant A0A0. 
        maximum
            A Float specifying the coefficient AA. 
        start
            A Float specifying the starting time t0t0. Possible values are non-negative numbers. 
        decayTime
            A Float specifying the decay time tdtd. Possible values are non-negative numbers. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A DecayAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = DecayAmplitude(name, initial, maximum, start, decayTime, timeSpan)
        return amplitude

    def EquallySpacedAmplitude(self, name: str, fixedInterval: float, data: tuple, begin: float = 0,
                               smooth: typing.Union[SymbolicConstant, float] = SOLVER_DEFAULT,
                               timeSpan: SymbolicConstant = STEP) -> EquallySpacedAmplitude:
        """This method creates an EquallySpacedAmplitude object.

        Path
        ----
            - mdb.models[name].EquallySpacedAmplitude
            - session.odbs[name].EquallySpacedAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        fixedInterval
            A Float specifying the fixed time interval at which the amplitude data are given. 
            Possible values are positive numbers. 
        data
            A sequence of Floats specifying the amplitude values. 
        begin
            A Float specifying the time at which the first amplitude data are given. Possible values 
            are non-negative numbers. The default value is 0.0. 
        smooth
            The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. 
            Possible float values are 0 ≤≤ *smoothing* ≤≤ 0.5. If *smooth*=SOLVER_DEFAULT, the 
            default degree of smoothing will be determined by the solver. The default value is 
            SOLVER_DEFAULT. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            An EquallySpacedAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = EquallySpacedAmplitude(name, fixedInterval, data, begin, smooth, timeSpan)
        return amplitude

    def ModulatedAmplitude(self, name: str, initial: float, magnitude: float, start: float, frequency1: float,
                           frequency2: float, timeSpan: SymbolicConstant = STEP) -> ModulatedAmplitude:
        """This method creates a ModulatedAmplitude object.

        Path
        ----
            - mdb.models[name].ModulatedAmplitude
            - session.odbs[name].ModulatedAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        initial
            A Float specifying the constant A0A0. 
        magnitude
            A Float specifying the coefficient AA. 
        start
            A Float specifying the starting time t0t0. Possible values are non-negative numbers. 
        frequency1
            A Float specifying the circular frequency 1 (ω1ω1). Possible values are positive 
            numbers. 
        frequency2
            A Float specifying the circular frequency 2 (ω2ω2). Possible values are positive 
            numbers. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A ModulatedAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = ModulatedAmplitude(name, initial, magnitude, start, frequency1, frequency2,
                                                               timeSpan)
        return amplitude

    def PeriodicAmplitude(self, name: str, frequency: float, start: float, a_0: float, data: tuple,
                          timeSpan: SymbolicConstant = STEP) -> PeriodicAmplitude:
        """This method creates a PeriodicAmplitude object.

        Path
        ----
            - mdb.models[name].PeriodicAmplitude
            - session.odbs[name].PeriodicAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        frequency
            A Float specifying the circular frequency ωω. Possible values are positive numbers. 
        start
            A Float specifying the starting time t0t0. Possible values are positive numbers. 
        a_0
            A Float specifying the constant A0A0. 
        data
            A sequence of pairs of Floats specifying AiAi and BiBi pairs. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A PeriodicAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = PeriodicAmplitude(name, frequency, start, a_0, data, timeSpan)
        return amplitude

    def PsdDefinition(self, name: str, data: tuple, unitType: SymbolicConstant = FORCE,
                      referenceGravityAcceleration: float = 1, referenecePower: float = 0,
                      user: Boolean = OFF, timeSpan: SymbolicConstant = STEP, amplitude: str = '') -> PsdDefinition:
        """This method creates a PsdDefinition object.

        Path
        ----
            - mdb.models[name].PsdDefinition
            - session.odbs[name].PsdDefinition

        Parameters
        ----------
        name
            A String specifying the repository key. 
        data
            A sequence of sequences of Floats specifying the real part of the frequency function, 
            the imaginary part of the frequency function, and the frequency or frequency band number 
            values, depending on the value of *unitType*. 
        unitType
            A SymbolicConstant specifying the type of units for specifying the frequency function. 
            FORCE implies power units. BASE implies gravity used to define base motion. DB implies 
            decibel units. Possible values are FORCE, BASE, and DB. The default value is FORCE. 
        referenceGravityAcceleration
            A Float specifying the reference gravity acceleration. This argument applies when 
            *unitType* = BASE. The default value is 1.0. 
        referenecePower
            A Float specifying the reference power value, in load units squared. This argument 
            applies when *unitType* = DB. The default value is 0.0. 
        user
            A Boolean specifying whether the frequency function is defined in user subroutine UPSD. 
            If specified, then *data* is not applicable, and the *unitType* value must not be DB. 
            The default value is OFF. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 
        amplitude
            A String specifying the name of the amplitude that describes the dynamic event used to 
            define the cross-spectral density frequency function. The default value is an empty 
            string. 

        Returns
        -------
            A PsdDefinition object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = PsdDefinition(name, data, unitType, referenceGravityAcceleration,
                                                          referenecePower, user, timeSpan, amplitude)
        return amplitude

    def SmoothStepAmplitude(self, name: str, data: tuple, timeSpan: SymbolicConstant = STEP) -> SmoothStepAmplitude:
        """This method creates a SmoothStepAmplitude object.

        Path
        ----
            - mdb.models[name].SmoothStepAmplitude
            - session.odbs[name].SmoothStepAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        data
            A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible 
            values for time/frequency are positive numbers. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A SmoothStepAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = SmoothStepAmplitude(name, data, timeSpan)
        return amplitude

    def SolutionDependentAmplitude(self, name: str, initial: float = 1, minimum: float = 0, maximum: float = 1000,
                                   timeSpan: SymbolicConstant = STEP) -> SolutionDependentAmplitude:
        """This method creates a SolutionDependentAmplitude object.

        Path
        ----
            - mdb.models[name].SolutionDependentAmplitude
            - session.odbs[name].SolutionDependentAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        initial
            A Float specifying the initial amplitude value. Possible values are those between 
            *minimum* and *maximum*. The default value is 1.0. 
        minimum
            A Float specifying the minimum amplitude value. Possible values are those smaller than 
            *maximum* and *initial*. The default value is 0.1. 
        maximum
            A Float specifying the maximum amplitude value. Possible values are those larger than 
            *minimum* and *initial*. The default value is 1000.0. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A SolutionDependentAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = SolutionDependentAmplitude(name, initial, minimum, maximum, timeSpan)
        return amplitude

    def SpectrumAmplitude(self, name: str, method: SymbolicConstant, data: tuple,
                          specificationUnits: SymbolicConstant = ACCELERATION,
                          eventUnits: SymbolicConstant = EVENT_ACCELERATION,
                          solution: SymbolicConstant = ABSOLUTE_VALUE, timeIncrement: float = 0,
                          gravity: float = 1, criticalDamping: Boolean = OFF, timeSpan: SymbolicConstant = STEP,
                          amplitude: str = '') -> SpectrumAmplitude:
        """This method creates a SpectrumAmplitude object.

        Path
        ----
            - mdb.models[name].SpectrumAmplitude
            - session.odbs[name].SpectrumAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        method
            A SymbolicConstant specifying the method for specifying the spectrum. Possible values 
            are DEFINE and CALCULATE. 
        data
            A sequence of sequences of Floats specifying the magnitude, frequency, and damping 
            values. 
        specificationUnits
            A SymbolicConstant specifying the units used for specifying the spectrum. Possible 
            values are DISPLACEMENT, VELOCITY, ACCELERATION, and GRAVITY. The default value is 
            ACCELERATION. 
        eventUnits
            A SymbolicConstant specifying the units used to describe the dynamic event in the 
            amplitude used for the calculation. Possible values are EVENT_DISPLACEMENT, 
            EVENT_VELOCITY, EVENT_ACCELERATION, and EVENT_GRAVITY. The default value is 
            EVENT_ACCELERATION. 
        solution
            A SymbolicConstant specifying the solution method for the dynamic equations. Possible 
            values are ABSOLUTE_VALUE and RELATIVE_VALUE. The default value is ABSOLUTE_VALUE. 
        timeIncrement
            A Float specifying the implicit time increment used to calculate the spectrum. This 
            argument is required when the *method* = CALCULATE. The default value is 0.0. 
        gravity
            A Float specifying the acceleration due to gravity. This argument applies only when 
            *specificationUnits* = GRAVITY or*eventUnits* = GRAVITY. The default value is 1.0. 
        criticalDamping
            A Boolean specifying whether to calculate the spectrum for only the specified range of 
            critical damping values or a list of values. If *criticalDamping* = ON, the spectrum is 
            calculated only for the specified range of critical damping values. If *criticalDamping* 
            = OFF, the spectrum is calculated for a list of damping values. The default value is 
            OFF. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 
        amplitude
            A String specifying the name of the amplitude that describes the dynamic event used to 
            calculate the spectrum. The default value is an empty string. 

        Returns
        -------
            A SpectrumAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = SpectrumAmplitude(name, method, data, specificationUnits, eventUnits,
                                                              solution, timeIncrement, gravity, criticalDamping,
                                                              timeSpan, amplitude)
        return amplitude

    def TabularAmplitude(self, name: str, data: tuple, smooth: typing.Union[SymbolicConstant, float] = SOLVER_DEFAULT,
                         timeSpan: SymbolicConstant = STEP) -> TabularAmplitude:
        """This method creates a TabularAmplitude object.

        Path
        ----
            - mdb.models[name].TabularAmplitude
            - session.odbs[name].TabularAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        data
            A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible 
            values for time/frequency are positive numbers. 
        smooth
            The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. 
            Possible float values are between 0 and 0.5. If *smooth*=SOLVER_DEFAULT, the default 
            degree of smoothing will be determined by the solver. The default value is 
            SOLVER_DEFAULT. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A TabularAmplitude object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.amplitudes[name] = amplitude = TabularAmplitude(name, data, smooth, timeSpan)
        return amplitude

    def AccelerationBaseMotionBC(self, name: str, createStepName: str, dof: SymbolicConstant,
                                 amplitudeScaleFactor: float = 1,
                                 centerOfRotation: tuple = (), correlation: CorrelationArray = None,
                                 secondaryBase: str = '', useComplex: Boolean = OFF,
                                 amplitude: str = UNSET) -> AccelerationBaseMotionBC:
        """This method creates a AccelerationBaseMotionBC object.

        Path
        ----
            - mdb.models[name].AccelerationBaseMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        dof
            A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the 
            SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1. 
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0. 
        centerOfRotation
            A ModelDot object specifying a tuple containing one center of rotation. The default 
            value is the global origin. This argument applies only when *dof*=UR1, UR2, or UR3. 
        correlation
            A CorrelationArray object. 
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary 
            condition. The default value is an empty string. 
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base 
            motion record given by amplitude definition. The default value is OFF. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 

        Returns
        -------
            An AccelerationBaseMotionBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = AccelerationBaseMotionBC(name, createStepName, dof,
                                                                                     amplitudeScaleFactor,
                                                                                     centerOfRotation, correlation,
                                                                                     secondaryBase, useComplex,
                                                                                     amplitude)
        return boundaryCondition

    def AccelerationBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                       a1: typing.Union[SymbolicConstant, float] = UNSET,
                       a2: typing.Union[SymbolicConstant, float] = UNSET,
                       a3: typing.Union[SymbolicConstant, float] = UNSET,
                       ar1: typing.Union[SymbolicConstant, float] = UNSET,
                       ar2: typing.Union[SymbolicConstant, float] = UNSET,
                       ar3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                       localCsys: str = None, distributionType: SymbolicConstant = UNIFORM) -> AccelerationBC:
        """This method creates an AccelerationBC object.

        Path
        ----
            - mdb.models[name].AccelerationBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the 1-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is 
            UNSET.Note:Although *a1*, *a2*, *a3*, *ar1*, *ar2*, and *ar3* are optional arguments, at 
            least one of them must be specified. 
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the 2-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the 3-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 

        Returns
        -------
            An AccelerationBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = AccelerationBC(name, createStepName, region, fieldName, a1,
                                                                           a2, a3, ar1, ar2, ar3, amplitude, localCsys,
                                                                           distributionType)
        return boundaryCondition

    def AcousticPressureBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                           magnitude: float = 0, distributionType: SymbolicConstant = UNIFORM,
                           amplitude: str = UNSET, fixed: Boolean = OFF) -> AcousticPressureBC:
        """This method creates a AcousticPressureBC object.

        Path
        ----
            - mdb.models[name].AcousticPressureBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        magnitude
            A Float specifying the acoustic pressure magnitude. The default value is 0. The 
            *magnitude* argument is optional if *distributionType*=USER_DEFINED. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 

        Returns
        -------
            An AcousticPressureBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = AcousticPressureBC(name, createStepName, region, fieldName,
                                                                               magnitude, distributionType, amplitude,
                                                                               fixed)
        return boundaryCondition

    def Calibration(self, name: str) -> Calibration:
        """This method creates a Calibration object.

        Path
        ----
            -           mdb.models[name].Calibration

        Parameters
        ----------
        name
            A String specifying the name of the new calibration. 

        Returns
        -------
            A Calibration object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        self.boundaryConditions[name] = boundaryCondition = Calibration(name)
        return boundaryCondition

    def ConcentrationBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                        magnitude: float = 0, distributionType: SymbolicConstant = UNIFORM,
                        amplitude: str = UNSET, fixed: Boolean = OFF) -> ConcentrationBC:
        """This method creates a ConcentrationBC object.

        Path
        ----
            - mdb.models[name].ConcentrationBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        magnitude
            A Float specifying the concentration magnitude. The default value is 0. The *magnitude* 
            argument is optional if *distributionType*=USER_DEFINED. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 

        Returns
        -------
            A ConcentrationBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = ConcentrationBC(name, createStepName, region, fieldName,
                                                                            magnitude, distributionType, amplitude,
                                                                            fixed)
        return boundaryCondition

    def ConnAccelerationBC(self, name: str, createStepName: str, region: str = '', fastenerName: str = '',
                           fastenerSetName: str = '', a1: typing.Union[SymbolicConstant, float] = UNSET,
                           a2: typing.Union[SymbolicConstant, float] = UNSET,
                           a3: typing.Union[SymbolicConstant, float] = UNSET,
                           ar1: typing.Union[SymbolicConstant, float] = UNSET,
                           ar2: typing.Union[SymbolicConstant, float] = UNSET,
                           ar3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                           distributionType: SymbolicConstant = UNIFORM) -> ConnAccelerationBC:
        """This method creates an ConnAccelerationBC object on a wire region. Alternatively, the
        boundary condition may also be applied to a wire set referenced from an assembled
        fastener template model.

        Path
        ----
            - mdb.models[name].ConnAccelerationBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            The wire region to which the boundary condition is applied. This argument is not valid 
            when *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition 
            will be applied. This argument is not valid when *region* is specified. When this 
            argument is specified, *fastenerSetName* must also be specified. The default value is an 
            empty string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary 
            condition will be applied. This argument is not valid when *region* is specified. When 
            this argument is specified, *fastenerName* must also be specified. The default value is 
            an empty string. 
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET.Note:Although *a1*, *a2*, *a3*, *ar1*, *ar2*, and *ar3* are 
            optional arguments, at least one of them must be specified. 
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET. 
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET. 
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 

        Returns
        -------
            A ConnAccelerationBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = ConnAccelerationBC(name, createStepName, region,
                                                                               fastenerName, fastenerSetName, a1, a2,
                                                                               a3, ar1, ar2, ar3, amplitude,
                                                                               distributionType)
        return boundaryCondition

    def ConnDisplacementBC(self, name: str, createStepName: str, region: str = '', fastenerName: str = '',
                           fastenerSetName: str = '', u1: typing.Union[SymbolicConstant, float] = UNSET,
                           u2: typing.Union[SymbolicConstant, float] = UNSET,
                           u3: typing.Union[SymbolicConstant, float] = UNSET,
                           ur1: typing.Union[SymbolicConstant, float] = UNSET,
                           ur2: typing.Union[SymbolicConstant, float] = UNSET,
                           ur3: typing.Union[SymbolicConstant, float] = UNSET, fixed: Boolean = OFF,
                           amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM,
                           buckleCase: SymbolicConstant = NOT_APPLICABLE) -> ConnDisplacementBC:
        """This method creates a ConnDisplacementBC object on a wire region. Alternatively, the
        boundary condition may also be applied to a wire set referenced from an assembled
        fastener template model.

        Path
        ----
            - mdb.models[name].ConnDisplacementBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            The wire region to which the boundary condition is applied. This argument is not valid 
            when *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition 
            will be applied. This argument is not valid when *region* is specified. When this 
            argument is specified, *fastenerSetName* must also be specified. The default value is an 
            empty string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary 
            condition will be applied. This argument is not valid when *region* is specified. When 
            this argument is specified, *fastenerName* must also be specified. The default value is 
            an empty string. 
        u1
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 
            connector's local 1-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET.Note:Although *u1*, *u2*, *u3*, *ur1*, *ur2*, and *ur3* 
            are optional arguments, at least one of them must be specified. 
        u2
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 
            connector's local 2-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        u3
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 
            connector's local 3-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ur1
            A Float, a Complex, or a SymbolicConstant specifying the rotational component in the 
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ur2
            A Float, a Complex, or a SymbolicConstant specifying the rotational component in the 
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ur3
            A Float, a Complex, or a SymbolicConstant specifying the rotational component in the 
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 

        Returns
        -------
            A ConnDisplacementBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = ConnDisplacementBC(name, createStepName, region,
                                                                               fastenerName, fastenerSetName, u1, u2,
                                                                               u3, ur1, ur2, ur3, fixed, amplitude,
                                                                               distributionType, buckleCase)
        return boundaryCondition

    def ConnVelocityBC(self, name: str, createStepName: str, region: str = '', fastenerName: str = '',
                       fastenerSetName: str = '', v1: typing.Union[SymbolicConstant, float] = UNSET,
                       v2: typing.Union[SymbolicConstant, float] = UNSET,
                       v3: typing.Union[SymbolicConstant, float] = UNSET,
                       vr1: typing.Union[SymbolicConstant, float] = UNSET,
                       vr2: typing.Union[SymbolicConstant, float] = UNSET,
                       vr3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                       distributionType: SymbolicConstant = UNIFORM) -> ConnVelocityBC:
        """This method creates a ConnVelocityBC object on a wire region. Alternatively, the
        boundary condition may also be applied to a wire set referenced from an assembled
        fastener template model.

        Path
        ----
            - mdb.models[name].ConnVelocityBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            The wire region to which the boundary condition is applied. This argument is not valid 
            when *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition 
            will be applied. This argument is not valid when *region* is specified. When this 
            argument is specified, *fastenerSetName* must also be specified. The default value is an 
            empty string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary 
            condition will be applied. This argument is not valid when *region* is specified. When 
            this argument is specified, *fastenerName* must also be specified. The default value is 
            an empty string. 
        v1
            A Float or a SymbolicConstant specifying the velocity component in the connector's local 
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET.Note:Although *v1*, *v2*, *v3*, *vr1*, *vr2*, and *vr3* are optional 
            arguments, at least one of them must be specified. 
        v2
            A Float or a SymbolicConstant specifying the velocity component in the connector's local 
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        v3
            A Float or a SymbolicConstant specifying the velocity component in the connector's local 
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component in the 
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component in the 
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component in the 
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 

        Returns
        -------
            A ConnVelocityBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = ConnVelocityBC(name, createStepName, region, fastenerName,
                                                                           fastenerSetName, v1, v2, v3, vr1, vr2, vr3,
                                                                           amplitude, distributionType)
        return boundaryCondition

    def DisplacementBaseMotionBC(self, name: str, createStepName: str, dof: SymbolicConstant,
                                 amplitudeScaleFactor: float = 1,
                                 centerOfRotation: tuple = (), correlation: CorrelationArray = None,
                                 secondaryBase: str = '', useComplex: Boolean = OFF,
                                 amplitude: str = UNSET) -> DisplacementBaseMotionBC:
        """This method creates a DisplacementBaseMotionBC object.

        Path
        ----
            - mdb.models[name].DisplacementBaseMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        dof
            A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the 
            SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1. 
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0. 
        centerOfRotation
            A ModelDot object specifying a tuple containing one center of rotation. The default 
            value is the global origin. This argument applies only when *dof*=UR1, UR2, or UR3. 
        correlation
            A CorrelationArray object. 
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary 
            condition. The default value is an empty string. 
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base 
            motion record given by amplitude definition. The default value is OFF. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 

        Returns
        -------
            A DisplacementBaseMotionBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = DisplacementBaseMotionBC(name, createStepName, dof,
                                                                                     amplitudeScaleFactor,
                                                                                     centerOfRotation, correlation,
                                                                                     secondaryBase, useComplex,
                                                                                     amplitude)
        return boundaryCondition

    def DisplacementBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                       u1: typing.Union[SymbolicConstant, float] = UNSET,
                       u2: typing.Union[SymbolicConstant, float] = UNSET,
                       u3: typing.Union[SymbolicConstant, float] = UNSET,
                       ur1: typing.Union[SymbolicConstant, float] = UNSET,
                       ur2: typing.Union[SymbolicConstant, float] = UNSET,
                       ur3: typing.Union[SymbolicConstant, float] = UNSET, fixed: Boolean = OFF,
                       amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM,
                       localCsys: str = None, buckleCase: SymbolicConstant = NOT_APPLICABLE) -> DisplacementBC:
        """This method creates a DisplacementBC object.

        Path
        ----
            - mdb.models[name].DisplacementBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated 
            with this boundary condition. The *fieldName* argument applies only when 
            *distributionType*=FIELD or *distributionType*=DISCRETE_FIELD. The default value is an 
            empty string. 
        u1
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET.Note:Although *u1*, *u2*, *u3*, *ur1*, *ur2*, and *ur3* are optional 
            arguments, at least one of them must be specified. 
        u2
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        u3
            A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        ur1
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement 
            component about the 1-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ur2
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement 
            component about the 2-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ur3
            A Float, a Complex, or a SymbolicConstant specifying the rotational displacement 
            component about the 3-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, FIELD, and DISCRETE_FIELD. The default value 
            is UNIFORM. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 

        Returns
        -------
            A DisplacementBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = DisplacementBC(name, createStepName, region, fieldName, u1,
                                                                           u2, u3, ur1, ur2, ur3, fixed, amplitude,
                                                                           distributionType, localCsys, buckleCase)
        return boundaryCondition

    def ElectricPotentialBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                            magnitude: float = 0, distributionType: SymbolicConstant = UNIFORM,
                            amplitude: str = UNSET, fixed: Boolean = OFF) -> ElectricPotentialBC:
        """This method creates an ElectricPotentialBC object.

        Path
        ----
            - mdb.models[name].ElectricPotentialBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        magnitude
            A Float specifying the electrical potential magnitude. The default value is 0. The 
            *magnitude* argument is optional if *distributionType*=USER_DEFINED. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 

        Returns
        -------
            An ElectricPotentialBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = ElectricPotentialBC(name, createStepName, region, fieldName,
                                                                                magnitude, distributionType, amplitude,
                                                                                fixed)
        return boundaryCondition

    def EulerianBC(self, name: str, createStepName: str, region: Region, definition: SymbolicConstant = INFLOW,
                   inflowType: SymbolicConstant = FREE, outflowType: SymbolicConstant = ZERO_PRESSURE) -> EulerianBC:
        """This method creates a EulerianBC object.

        Path
        ----
            - mdb.models[name].EulerianBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        definition
            A SymbolicConstant specifying the flow conditions to be defined. Possible values are 
            INFLOW, OUTFLOW, and BOTH. The default value is INFLOW. 
        inflowType
            A SymbolicConstant specifying the control of material flow into the Eulerian domain. 
            Possible values are FREE, NONE, and VOID. The default value is FREE. 
        outflowType
            A SymbolicConstant specifying the control of flow of material out of the Eulerian 
            domain. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The 
            default value is ZERO_PRESSURE. 

        Returns
        -------
            An EulerianBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = EulerianBC(name, createStepName, region, definition,
                                                                       inflowType, outflowType)
        return boundaryCondition

    def EulerianMotionBC(self, name: str, createStepName: str, instanceName: str, followRegion: Boolean = ON,
                         region: Region = Region(), materialName: str = '',
                         ctrPosition1: SymbolicConstant = FREE, posPosition1: SymbolicConstant = FREE,
                         negPosition1: SymbolicConstant = FREE, expansionRatio1: float = None,
                         contractRatio1: float = 0, ctrPosition2: SymbolicConstant = FREE,
                         posPosition2: SymbolicConstant = FREE, negPosition2: SymbolicConstant = FREE,
                         expansionRatio2: float = None, contractRatio2: float = 0,
                         ctrPosition3: SymbolicConstant = FREE, posPosition3: SymbolicConstant = FREE,
                         negPosition3: SymbolicConstant = FREE, expansionRatio3: float = None,
                         contractRatio3: float = 0, allowContraction: Boolean = ON, aspectLimit: float = 10,
                         vmaxFactor: float = 1, volThreshold: float = 0, bufferSize: float = 2) -> EulerianMotionBC:
        """This method creates an EulerianMotionBC object.

        Path
        ----
            - mdb.models[name].EulerianMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        instanceName
            A String specifying the name of the Eulerian part instance. 
        followRegion
            A Boolean specifying whether the mesh will follow a regular surface region or an 
            Eulerian surface. The default value is ON. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        materialName
            A String specifying the name of the Eulerian surface to follow. This argument applies 
            only when *followRegion*=False. 
        ctrPosition1
            A SymbolicConstant specifying the 1-direction translational constraint on the center of 
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE. 
        posPosition1
            A SymbolicConstant specifying the translational constraint on the positive (maximum) 
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default 
            value is FREE. 
        negPosition1
            A SymbolicConstant specifying the translational constraint on the negative (minimum) 
            bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default 
            value is FREE. 
        expansionRatio1
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 
            1 direction. If *expansionRatio1*=None, then there is no upper limit. The default value 
            is None. 
        contractRatio1
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 1 
            direction. The default value is 0.0. 
        ctrPosition2
            A SymbolicConstant specifying the 2-direction translational constraint on the center of 
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE. 
        posPosition2
            A SymbolicConstant specifying the translational constraint on the positive (maximum) 
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default 
            value is FREE. 
        negPosition2
            A SymbolicConstant specifying the translational constraint on the negative (minimum) 
            bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default 
            value is FREE. 
        expansionRatio2
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 
            2 direction. If *expansionRatio2*=None, then there is no upper limit. The default value 
            is None. 
        contractRatio2
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 2 
            direction. The default value is 0.0. 
        ctrPosition3
            A SymbolicConstant specifying the 3-direction translational constraint on the center of 
            the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE. 
        posPosition3
            A SymbolicConstant specifying the translational constraint on the positive (maximum) 
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default 
            value is FREE. 
        negPosition3
            A SymbolicConstant specifying the translational constraint on the negative (minimum) 
            bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default 
            value is FREE. 
        expansionRatio3
            None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 
            3 direction. If *expansionRatio3*=None, then there is no upper limit. The default value 
            is None. 
        contractRatio3
            A Float specifying the lower bounds on the allowable scaling of the mesh in the 3 
            direction. The default value is 0.0. 
        allowContraction
            A Boolean specifying whether the mesh is allowed to contract . The default value is ON. 
        aspectLimit
            A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh 
            aspects, 1-2, 2-3, 3-1). The default value is 10.0. 
        vmaxFactor
            A Float specifying the multiplier for the mesh nodal velocity limit. The default value 
            is 1.01. 
        volThreshold
            A Float specifying the lower bounds on the volume fraction when determining which nodes 
            to include in the surface bounding box calculation for an Eulerian material surface. 
            This argument applies only when *followRegion*=False. The default value is 0.5. 
        bufferSize
            None or a Float specifying the buffer between the surface box and the Eulerian section 
            mesh bounding box. The default value is 2.0. 

        Returns
        -------
            An EulerianMotionBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = EulerianMotionBC(name, createStepName, instanceName,
                                                                             followRegion, region, materialName,
                                                                             ctrPosition1, posPosition1, negPosition1,
                                                                             expansionRatio1, contractRatio1,
                                                                             ctrPosition2, posPosition2, negPosition2,
                                                                             expansionRatio2, contractRatio2,
                                                                             ctrPosition3, posPosition3, negPosition3,
                                                                             expansionRatio3, contractRatio3,
                                                                             allowContraction, aspectLimit, vmaxFactor,
                                                                             volThreshold, bufferSize)
        return boundaryCondition

    def FluidCavityPressureBC(self, name: str, createStepName: str, fluidCavity: str, magnitude: float = 0,
                              amplitude: str = UNSET, fixed: Boolean = OFF) -> FluidCavityPressureBC:
        """This method creates a FluidCavityPressureBC object.

        Path
        ----
            - mdb.models[name].FluidCavityPressureBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction. 
        magnitude
            A Float specifying the fluid cavity pressure magnitude. The default value is 0. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 

        Returns
        -------
            A FluidCavityPressureBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = FluidCavityPressureBC(name, createStepName, fluidCavity,
                                                                                  magnitude, amplitude, fixed)
        return boundaryCondition

    def MagneticVectorPotentialBC(self, name: str, createStepName: str, region: Region,
                                  component1: SymbolicConstant = None,
                                  component2: SymbolicConstant = UNSET, component3: SymbolicConstant = UNSET,
                                  amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM,
                                  localCsys: str = None) -> MagneticVectorPotentialBC:
        """This method creates a MagneticVectorPotentialBC object.

        Path
        ----
            - mdb.models[name].MagneticVectorPotentialBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        component1
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET 
        component2
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        component3
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A MagneticVectorPotentialBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = MagneticVectorPotentialBC(name, createStepName, region,
                                                                                      component1, component2,
                                                                                      component3, amplitude,
                                                                                      distributionType, localCsys)
        return boundaryCondition

    def MaterialFlowBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                       magnitude: float = 0, distributionType: SymbolicConstant = UNIFORM,
                       amplitude: str = UNSET, fixed: Boolean = OFF) -> MaterialFlowBC:
        """This method creates a MaterialFlowBC object.

        Path
        ----
            - mdb.models[name].MaterialFlowBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        magnitude
            A Float specifying the material flow magnitude. The default value is 0. The *magnitude* 
            argument is optional if *distributionType*=USER_DEFINED. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 

        Returns
        -------
            A MaterialFlowBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = MaterialFlowBC(name, createStepName, region, fieldName,
                                                                           magnitude, distributionType, amplitude,
                                                                           fixed)
        return boundaryCondition

    def PorePressureBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                       magnitude: float = 0, distributionType: SymbolicConstant = UNIFORM,
                       amplitude: str = UNSET, fixed: Boolean = OFF) -> PorePressureBC:
        """This method creates a PorePressureBC object.

        Path
        ----
            - mdb.models[name].PorePressureBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        magnitude
            A Float specifying the pore pressure magnitude. The default value is 0. The *magnitude* 
            argument is optional if *distributionType*=USER_DEFINED. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 

        Returns
        -------
            A PorePressureBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = PorePressureBC(name, createStepName, region, fieldName,
                                                                           magnitude, distributionType, amplitude,
                                                                           fixed)
        return boundaryCondition

    def RetainedNodalDofsBC(self, name: str, createStepName: str, region: Region, u1: Boolean = OFF, u2: Boolean = OFF,
                            u3: Boolean = OFF, ur1: Boolean = OFF, ur2: Boolean = OFF,
                            ur3: Boolean = OFF) -> RetainedNodalDofsBC:
        """This method creates a RetainedNodalDofsBC object.

        Path
        ----
            - mdb.models[name].RetainedNodalDofsBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        u1
            A Boolean specifying whether to retain the degree of freedom in the 1-direction. The 
            default value is OFF indicating that the degree of freedom is not retained. 
        u2
            A Boolean specifying whether to retain the degree of freedom in the 2-direction. The 
            default value is OFF indicating that the degree of freedom is not retained. 
        u3
            A Boolean specifying whether to retain the degree of freedom in the 3-direction. The 
            default value is OFF indicating that the degree of freedom is not retained. 
        ur1
            A Boolean specifying whether to retain the rotational degree of freedom about the 
            1-direction. The default value is OFF indicating that the degree of freedom is not 
            retained. 
        ur2
            A Boolean specifying whether to retain the rotational degree of freedom about the 
            2-direction. The default value is OFF indicating that the degree of freedom is not 
            retained. 
        ur3
            A Boolean specifying whether to retain the rotational degree of freedom about the 
            3-direction. The default value is OFF indicating that the degree of freedom is not 
            retained. 

        Returns
        -------
            A RetainedNodalDofsBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = RetainedNodalDofsBC(name, createStepName, region, u1, u2,
                                                                                u3, ur1, ur2, ur3)
        return boundaryCondition

    def SecondaryBaseBC(self, name: str, createStepName: str, regions: RegionArray, dofs: tuple) -> SecondaryBaseBC:
        """This method creates a SecondaryBaseBC object.

        Path
        ----
            - mdb.models[name].SecondaryBaseBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        regions
            A RegionArray object specifying the region to which the boundary condition is applied. 
            Note that the usual *region* is ignored. The default value is MODEL. 
        dofs
            A sequence of sequences of Ints specifying the constrained degrees-of-freedom. 

        Returns
        -------
            A SecondaryBaseBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = SecondaryBaseBC(name, createStepName, regions, dofs)
        return boundaryCondition

    def SubmodelBC(self, name: str, createStepName: str, region: Region, dof: tuple, globalStep: str,
                   timeScale: Boolean, shellThickness: float, globalDrivingRegion: str = '',
                   absoluteExteriorTolerance: float = None, exteriorTolerance: float = 0,
                   localCsys: str = None, globalIncrement: int = 0, centerZoneSize: float = None,
                   intersectionOnly: Boolean = OFF) -> SubmodelBC:
        """This method creates a SubmodelBC object.

        Path
        ----
            - mdb.models[name].SubmodelBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        dof
            A sequence of Ints specifying the degrees of freedom to which the boundary condition is 
            applied. 
        globalStep
            A String specifying the step in the global model from which Abaqus reads the values of 
            the variables that will drive the submodel analysis. The String indicates the position 
            of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates 
            the first step. 
        timeScale
            A Boolean specifying whether to scale the time variable for the driven nodes' amplitude 
            functions to match the submodel analysis step time. The default value is OFF. 
        shellThickness
            A Float specifying the thickness of the shell in the global model. This argument is 
            required for shell-to-solid submodeling and is not applicable to other submodels. The 
            default value is 0.0. 
        globalDrivingRegion
            A String specifying the element set in the global model that will be searched for 
            elements whose responses will be used to drive the submodel. An empty string indicates 
            that the entire global model will be searched. The default value is an empty string. 
        absoluteExteriorTolerance
            None or a Float specifying the absolute value by which a driven node of the submodel can 
            lie outside the region of the elements of the global model. The default value is None. 
        exteriorTolerance
            None or a Float specifying the fraction of the average element size in the global model 
            by which a driven node of the submodel can lie outside the region of the elements of the 
            global model. The default value is 0.05. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        globalIncrement
            An Int specifying the increment number in the global model step from which the solution 
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the 
            solution from the last increment will be used. The *globalIncrement* argument is 
            applicable only for linear perturbation steps. The default value is 0. 
        centerZoneSize
            A Float specifying the thickness of the center zone size around the shell midsurface. 
            The default value is None. 
        intersectionOnly
            A Boolean specifying whether to ignore driven nodes that lie outside the region of 
            elements of the global model after accounting for the exterior search tolerance. The 
            default value is OFF. 

        Returns
        -------
            A SubmodelBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = SubmodelBC(name, createStepName, region, dof, globalStep,
                                                                       timeScale, shellThickness, globalDrivingRegion,
                                                                       absoluteExteriorTolerance, exteriorTolerance,
                                                                       localCsys, globalIncrement, centerZoneSize,
                                                                       intersectionOnly)
        return boundaryCondition

    def TemperatureBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                      magnitude: float = 0, dof: tuple = (), amplitude: str = UNSET,
                      distributionType: SymbolicConstant = UNIFORM, fixed: Boolean = OFF) -> TemperatureBC:
        """This method creates a TemperatureBC object.

        Path
        ----
            - mdb.models[name].TemperatureBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        magnitude
            A Float specifying the temperature magnitude. The default value is 0. 
        dof
            A sequence of Ints specifying the degrees of freedom to which the boundary condition is 
            applied. The default value is (11,). 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is OFF. 

        Returns
        -------
            A TemperatureBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = TemperatureBC(name, createStepName, region, fieldName,
                                                                          magnitude, dof, amplitude, distributionType,
                                                                          fixed)
        return boundaryCondition

    def VelocityBaseMotionBC(self, name: str, createStepName: str, dof: SymbolicConstant,
                             amplitudeScaleFactor: float = 1,
                             centerOfRotation: tuple = (), correlation: CorrelationArray = None,
                             secondaryBase: str = '', useComplex: Boolean = OFF,
                             amplitude: str = UNSET) -> VelocityBaseMotionBC:
        """This method creates a VelocityBaseMotionBC object.

        Path
        ----
            - mdb.models[name].VelocityBaseMotionBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        dof
            A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the 
            SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1. 
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0. 
        centerOfRotation
            A ModelDot object specifying a tuple containing one center of rotation. The default 
            value is the global origin. This argument applies only when *dof*=UR1, UR2, or UR3. 
        correlation
            A CorrelationArray object. 
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary 
            condition. The default value is an empty string. 
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base 
            motion record given by amplitude definition. The default value is OFF. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 

        Returns
        -------
            A VelocityBaseMotionBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = VelocityBaseMotionBC(name, createStepName, dof,
                                                                                 amplitudeScaleFactor, centerOfRotation,
                                                                                 correlation, secondaryBase, useComplex,
                                                                                 amplitude)
        return boundaryCondition

    def VelocityBC(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                   v1: typing.Union[SymbolicConstant, float] = UNSET,
                   v2: typing.Union[SymbolicConstant, float] = UNSET,
                   v3: typing.Union[SymbolicConstant, float] = UNSET,
                   vr1: typing.Union[SymbolicConstant, float] = UNSET,
                   vr2: typing.Union[SymbolicConstant, float] = UNSET,
                   vr3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                   localCsys: str = None, distributionType: SymbolicConstant = UNIFORM) -> VelocityBC:
        """This method creates a VelocityBC object.

        Path
        ----
            - mdb.models[name].VelocityBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is 
            UNSET.Note:Although *v1*, *v2*, *v3*, *vr1*, *vr2*, and *vr3* are optional arguments, at 
            least one of them must be specified. 
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 

        Returns
        -------
            A VelocityBC object. 

        Exceptions
        ----------
            None. 
        """
        self.boundaryConditions[name] = boundaryCondition = VelocityBC(name, createStepName, region, fieldName, v1, v2,
                                                                       v3, vr1, vr2, vr3, amplitude, localCsys,
                                                                       distributionType)
        return boundaryCondition

    def AdjustPoints(self, name: str, surface: Region, controlPoints: Region) -> AdjustPoints:
        """This method creates an AdjustPoints object.

        Path
        ----
            - mdb.models[name].AdjustPoints

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        surface
            A Region object specifying the surface to which the *controlPoints* are adjusted. 
        controlPoints
            A Region object specifying the constraint control points. 

        Returns
        -------
            An AdjustPoints object. 

        Exceptions
        ----------
            None. 
        """
        self.constraints[name] = constraint = AdjustPoints(name, surface, controlPoints)
        return constraint

    def Coupling(self, name: str, surface: Region, controlPoint: Region,
                 influenceRadius: typing.Union[SymbolicConstant, float], couplingType: SymbolicConstant,
                 adjust: Boolean = OFF, localCsys: str = None, u1: Boolean = ON, u2: Boolean = ON,
                 u3: Boolean = ON, ur1: Boolean = ON, ur2: Boolean = ON, ur3: Boolean = ON,
                 weightingMethod: SymbolicConstant = UNIFORM) -> Coupling:
        """This method creates a Coupling object.

        Path
        ----
            - mdb.models[name].Coupling

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        surface
            A Region object specifying the surface on which the coupling nodes are located. 
        controlPoint
            A Region object specifying the constraint control point. 
        influenceRadius
            The SymbolicConstant WHOLE_SURFACE or a Float specifying the influence radius. 
        couplingType
            A SymbolicConstant specifying the coupling constraint type. Possible values are 
            KINEMATIC, DISTRIBUTING, and STRUCTURAL. 
        adjust
            A Boolean specifying if the control point will be adjusted (moved) to the surface. The 
            point will be adjusted in the direction normal to the specified surface. The default 
            value is OFF. 
        localCsys
            None or a DatumCsys object specifying the initial orientation of the local coordinate 
            system for the coupling's degrees of freedom. If *localCsys*=None, the coupling is 
            defined in the global coordinate system. The default value is None. 
        u1
            A Boolean specifying if the displacement component in the 1-direction is constrained to 
            the reference node for a kinematic coupling constraint. The default value is ON.The *u1* 
            argument applies only when *couplingType*=KINEMATIC. 
        u2
            A Boolean specifying if the displacement component in the 2-direction is constrained to 
            the reference node for a kinematic coupling constraint. The default value is ON.The *u2* 
            argument applies only when *couplingType*=KINEMATIC. 
        u3
            A Boolean specifying if the displacement component in the 3-direction is constrained to 
            the reference node for a kinematic coupling constraint. The default value is ON.The *u3* 
            argument applies only when *couplingType*=KINEMATIC. 
        ur1
            A Boolean specifying if the rotational displacement component about the 1-direction is 
            constrained to the reference node for a kinematic coupling constraint. The default value 
            is ON.The *ur1* argument applies only when *couplingType*=KINEMATIC. 
        ur2
            A Boolean specifying if the rotational displacement component about the 2-direction is 
            constrained to the reference node for a kinematic coupling constraint. The default value 
            is ON.The *ur2* argument applies only when *couplingType*=KINEMATIC. 
        ur3
            A Boolean specifying if the rotational displacement component about the 3-direction is 
            constrained to the reference node for a kinematic coupling constraint. The default value 
            is ON.The *ur3* argument applies only when *couplingType*=KINEMATIC. 
        weightingMethod
            A SymbolicConstant specifying an optional weighting method used for calculating the 
            distributing weight factors. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC. 
            The default value is UNIFORM.The *weightingMethod* argument applies only when 
            *couplingType*=DISTRIBUTING. 

        Returns
        -------
            A Coupling object. 

        Exceptions
        ----------
            None. 
        """
        self.constraints[name] = constraint = Coupling(name, surface, controlPoint, influenceRadius, couplingType,
                                                       adjust, localCsys, u1, u2, u3, ur1, ur2, ur3, weightingMethod)
        return constraint

    def DisplayBody(self, name: str, instance: PartInstance, controlPoints: ModelDotArray) -> DisplayBody:
        """This method creates a DisplayBody object.

        Path
        ----
            - mdb.models[name].DisplayBody

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        instance
            A PartInstance object specifying the part instance that is to be used for display only. 
        controlPoints
            A ModelDotArray object specifying the motion of the PartInstance. The control points may 
            be Vertex, ReferencePoint, or MeshNode objects. Their motion will control the motion of 
            the PartInstance. If this argument is set to an empty sequence, the PartInstance will 
            remain fixed in space during the analysis. The sequence can have either one object or 
            three objects. 

        Returns
        -------
            A DisplayBody object. 

        Exceptions
        ----------
            None. 
        """
        self.constraints[name] = constraint = DisplayBody(name, instance, controlPoints)
        return constraint

    def EmbeddedRegion(self, name: str, embeddedRegion: Region, hostRegion: Region,
                       weightFactorTolerance: float = None, toleranceMethod: SymbolicConstant = BOTH,
                       absoluteTolerance: float = 0, fractionalTolerance: float = 0) -> EmbeddedRegion:
        """This method creates a EmbeddedRegion object.

        Path
        ----
            - mdb.models[name].EmbeddedRegion

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        embeddedRegion
            A Region object specifying the body region to be embedded. 
        hostRegion
            A Region object specifying the host region. A value of None indicates that the host 
            region is the whole model. 
        weightFactorTolerance
            A Float specifying a small value below which the weighting factors will be zeroed out. 
            The default value is 10–6. 
        toleranceMethod
            A SymbolicConstant specifying the method used to determine the embedded element 
            tolerance. Possible values are ABSOLUTE, FRACTIONAL, and BOTH. The default value is 
            BOTH. 
        absoluteTolerance
            A Float specifying the absolute value by which a node on the embedded region may lie 
            outside the host region. If *absoluteTolerance*=0.0, the *fractionalTolerance* value 
            will be used. The default value is 0.0.This argument applies only when 
            *toleranceMethod*=ABSOLUTE or BOTH. 
        fractionalTolerance
            A Float specifying the fractional value by which a node on the embedded region may lie 
            outside the host region. The fractional value is based on the average element size 
            within the host region. The default value is 0.05.If both tolerance arguments are 
            specified, the smaller value will be used.This argument applies only when 
            *toleranceMethod*=FRACTIONAL or BOTH. 

        Returns
        -------
            An EmbeddedRegion object. 

        Exceptions
        ----------
            None. 
        """
        self.constraints[name] = constraint = EmbeddedRegion(name, embeddedRegion, hostRegion, weightFactorTolerance,
                                                             toleranceMethod, absoluteTolerance, fractionalTolerance)
        return constraint

    def Equation(self, name: str, terms: tuple) -> Equation:
        """This method creates an Equation object.

        Path
        ----
            - mdb.models[name].Equation

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        terms
            A sequence of (Float, String, Int, Int) sequences specifying a coefficient, Set name, 
            degree of freedom, and coordinate system ID. The coordinate system ID is optional. 

        Returns
        -------
            An Equation object. 

        Exceptions
        ----------
            - If *terms* does not contain more than one entry: 
              Equation must have two or more terms. 
        """
        self.constraints[name] = constraint = Equation(name, terms)
        return constraint

    def MultipointConstraint(self, name: str, surface: Region, controlPoint: Region, mpcType: SymbolicConstant,
                             csys: str = None, userType: int = 0,
                             userMode: SymbolicConstant = DOF_MODE_MPC) -> MultipointConstraint:
        """This method creates a MultipointConstraint object.

        Path
        ----
            - mdb.models[name].MultipointConstraint

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        surface
            A Region object specifying the surface on which the MultipointConstraint nodes are 
            located. 
        controlPoint
            A Region object specifying the constraint control point. 
        mpcType
            A SymbolicConstant specifying the MPC type of the constraint. Possible values are 
            BEAM_MPC, ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_MPC. 
        csys
            None or a DatumCsys object specifying the initial orientation of the local coordinate 
            system for the MultipointConstraint's degrees of freedom. If *localCsys*=None, the 
            MultipointConstraint is defined in the global coordinate system. The default value is 
            None. 
        userType
            An Int specifying to differentiate between different constraint types in a user-defined 
            MultipointConstraint. The default value is 0.The *userType* argument applies only when 
            *mpcType*=USER_MPC. 
        userMode
            A SymbolicConstant specifying the mode of the constraint when it is user-defined. 
            Possible values are DOF_MODE_MPC and NODE_MODE_MPC. The default value is 
            DOF_MODE_MPC.The *userMode* argument applies only when *mpcType*=USER_MPC. 

        Returns
        -------
            A MultipointConstraint object. 

        Exceptions
        ----------
            None. 
        """
        self.constraints[name] = constraint = MultipointConstraint(name, surface, controlPoint, mpcType, csys, userType,
                                                                   userMode)
        return constraint

    def RigidBody(self, name: str, refPointRegion: Region, bodyRegion: str = None, tieRegion: str = None,
                  pinRegion: str = None, surfaceRegion: str = None, refPointAtCOM: Boolean = OFF,
                  isothermal: Boolean = OFF) -> RigidBody:
        """This method creates a RigidBody object.

        Path
        ----
            - mdb.models[name].RigidBody

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        refPointRegion
            A Region object specifying the reference point. 
        bodyRegion
            None or a Region object specifying the elements constrained to the movement of the 
            reference point. The default value is None. 
        tieRegion
            None or a Region object specifying the nodes tied to the movement of the reference 
            point. The default value is None. 
        pinRegion
            None or a Region object specifying the nodes pinned to the movement of the reference 
            point. The default value is None. 
        surfaceRegion
            None or a Region object specifying the analytic surface constrained to the movement of 
            the reference point. The default value is None. 
        refPointAtCOM
            A Boolean specifying whether the analysis product should recompute the reference point 
            position to be at the center of mass. The default value is OFF. 
        isothermal
            A Boolean specifying whether the temperature degree of freedom should be constrained. 
            The default value is OFF. 

        Returns
        -------
            A RigidBody object. 

        Exceptions
        ----------
            None. 
        """
        self.constraints[name] = constraint = RigidBody(name, refPointRegion, bodyRegion, tieRegion, pinRegion,
                                                        surfaceRegion, refPointAtCOM, isothermal)
        return constraint

    def ShellSolidCoupling(self, name: str, shellEdge: Region, solidFace: Region,
                           positionToleranceMethod: SymbolicConstant = COMPUTED, positionTolerance: float = 0,
                           influenceDistanceMethod: SymbolicConstant = DEFAULT,
                           influenceDistance: float = 0) -> ShellSolidCoupling:
        """This method creates a ShellSolidCoupling object.

        Path
        ----
            - mdb.models[name].ShellSolidCoupling

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        shellEdge
            A Region object specifying the name of the shell edge surface. 
        solidFace
            A Region object specifying the name of the solid surface. 
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance. 
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED. 
        positionTolerance
            A Float specifying the position tolerance. The default value is 0.0.The 
            *positionTolerance* argument applies only when 
            *positionToleranceMethod*=SPECIFIED.Note:Abaqus will not constrain nodes on the solid 
            face region outside the position tolerance. 
        influenceDistanceMethod
            A SymbolicConstant specifying the method used to determine the influence distance. 
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT. 
        influenceDistance
            A Float specifying the influence distance. The *influenceDistance* argument applies only 
            when *influenceDistanceMethod*=SPECIFIED. The default value is 0.0. 

        Returns
        -------
            A ShellSolidCoupling object. 

        Exceptions
        ----------
            None. 
        """
        self.constraints[name] = constraint = ShellSolidCoupling(name, shellEdge, solidFace, positionToleranceMethod,
                                                                 positionTolerance, influenceDistanceMethod,
                                                                 influenceDistance)
        return constraint

    def Tie(self, name: str, main: Region, secondary: Region, adjust: Boolean = ON,
            positionToleranceMethod: SymbolicConstant = COMPUTED, positionTolerance: float = 0,
            tieRotations: Boolean = ON, constraintRatioMethod: SymbolicConstant = DEFAULT,
            constraintRatio: float = 0, constraintEnforcement: SymbolicConstant = SOLVER_DEFAULT,
            thickness: Boolean = ON) -> Tie:
        """This method creates a Tie object.

        Path
        ----
            - mdb.models[name].Tie

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        main
            A Region object specifying the name of the main surface. 
        secondary
            A Region object specifying the name of the secondary surface. 
        adjust
            A Boolean specifying whether initial positions of tied secondary nodes are adjusted to 
            lie on the main surface. The default value is ON. 
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance. 
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED. 
        positionTolerance
            A Float specifying the position tolerance. The *positionTolerance* argument applies only 
            when *positionToleranceMethod*=SPECIFIED. The default value is 0.0. 
        tieRotations
            A Boolean specifying whether rotation degrees of freedom should be tied. The default 
            value is ON. 
        constraintRatioMethod
            A SymbolicConstant specifying the method used to determine the constraint ratio. 
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT. 
        constraintRatio
            A Float specifying the fractional distance between the main reference surface and the 
            secondary node at which the translational constraint should act. The *constraintRatio* 
            argument applies only when *constraintRatioMethod*=SPECIFIED. The default value is 0.0. 
        constraintEnforcement
            A SymbolicConstant specifying the discretization method. Possible values are 
            SOLVER_DEFAULT, NODE_TO_SURFACE, and SURFACE_TO_SURFACE. The default value is 
            SOLVER_DEFAULT. 
        thickness
            A Boolean specifying whether shell element thickness is considered. The default value is 
            ON. 

        Returns
        -------
            A Tie object. 

        Exceptions
        ----------
            None. 
        """
        self.constraints[name] = constraint = Tie(name, main, secondary, adjust, positionToleranceMethod,
                                                  positionTolerance, tieRotations, constraintRatioMethod,
                                                  constraintRatio, constraintEnforcement, thickness)
        return constraint

    def AcousticImpedance(self, name: str, createStepName: str, surface: Region, definition: SymbolicConstant = TABULAR,
                          interactionProperty: str = '', nonreflectingType: SymbolicConstant = PLANE,
                          radius: float = 1, semimajorAxis: float = 1, eccentricity: float = 0,
                          centerCoordinates: tuple = (), directionCosine: tuple = ()) -> AcousticImpedance:
        """This method creates an AcousticImpedance object.

        Path
        ----
            - mdb.models[name].AcousticImpedance

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the AcousticImpedance object is 
            created. 
        surface
            A Region object specifying the acoustic boundary surface. 
        definition
            A SymbolicConstant specifying the type of acoustic impedance to be defined. Possible 
            values are TABULAR and NONREFLECTING. The default value is TABULAR. 
        interactionProperty
            A String specifying the AcousticImpedanceProp object associated with this interaction. 
        nonreflectingType
            A SymbolicConstant specifying the type of nonreflecting geometry to be defined. Possible 
            values are PLANE, IMPROVED, CIRCULAR, SPHERICAL, ELLIPTICAL, and PROLATE. The default 
            value is PLANE.This argument is valid only when *definition*=NONREFLECTING. 
        radius
            A Float specifying the radius of the circle or sphere defining the boundary surface. The 
            default value is 1.0.This argument is valid only when *definition*=NONREFLECTING, and 
            *nonreflectingType*=CIRCULAR or SPHERICAL. 
        semimajorAxis
            A Float specifying the semimajor axis length of the ellipse or prolate spheroid defining 
            the boundary surface. The default value is 1.0.This argument is valid only when 
            *definition*=NONREFLECTING, and *nonreflectingType*=ELLIPTICAL or PROLATE. 
        eccentricity
            A Float specifying the eccentricity of the ellipse or prolate spheroid defining the 
            boundary surface. The default value is 0.0.This argument is valid only when 
            *definition*=NONREFLECTING, and *nonreflectingType*=ELLIPTICAL or PROLATE. 
        centerCoordinates
            A sequence of three Floats specifying the X, Y, and Z coordinates of the center of the 
            ellipse or prolate spheroid defining the boundary surface. The default value is (0, 0, 
            0).This argument is valid only when *definition*=NONREFLECTING, and 
            *nonreflectingType*=ELLIPTICAL or PROLATE. 
        directionCosine
            A sequence of three Floats specifying the X, Y, and Z components of the direction cosine 
            of the major axis of the ellipse or prolate spheroid defining the boundary surface. The 
            default value is (0, 0, 1).This argument is valid only when *definition*=NONREFLECTING, 
            and *nonreflectingType*=ELLIPTICAL or PROLATE. 

        Returns
        -------
            An AcousticImpedance object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = AcousticImpedance(name, createStepName, surface, definition,
                                                                  interactionProperty, nonreflectingType, radius,
                                                                  semimajorAxis, eccentricity, centerCoordinates,
                                                                  directionCosine)
        return interaction

    def AcousticImpedanceProp(self, name: str, tableType: SymbolicConstant, table: tuple,
                              frequencyDependency: Boolean = OFF) -> AcousticImpedanceProp:
        """This method creates an AcousticImpedanceProp object.

        Path
        ----
            - mdb.models[name].AcousticImpedanceProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        tableType
            A SymbolicConstant specifying the type of tabular data to be defined. Possible values 
            are IMPEDANCE and ADMITTANCE. 
        table
            A sequence of sequences of Floats specifying acoustic impedance properties.If 
            *tableType*=IMPEDANCE, each sequence of the table data specifies:The real part of the 
            complex impedance.The imaginary part of the complex impedance.Frequency, if the data 
            depend on frequency.If *tableType*=ADMITTANCE, each sequence of the table data 
            specifies:The real part of the complex admittance.The imaginary part of the complex 
            admittance.Frequency, if the data depend on frequency. 
        frequencyDependency
            A Boolean specifying whether the *table* data depend on frequency. The default value is 
            OFF. 

        Returns
        -------
            An AcousticImpedanceProp object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = AcousticImpedanceProp(name, tableType, table, frequencyDependency)
        return interaction

    def ActuatorSensor(self, name: str, createStepName: str, point: Region, interactionProperty: str,
                       noCoordComponents: int, unsymm: Boolean, noSolutionDepVar: int, userSubUel: str,
                       dof: str, solutionDepVars: tuple) -> ActuatorSensor:
        """This method creates an ActuatorSensor object.

        Path
        ----
            - mdb.models[name].ActuatorSensor

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the actuator/sensor interaction is 
            created. *createStepName* must be set to 'Initial'. 
        point
            A Region object specifying the point at which the constraint is applied. 
        interactionProperty
            A String specifying the ActuatorSensorProp object associated with this interaction. 
        noCoordComponents
            An Int specifying the number of coordinate components supplied to the user subroutine 
            (UEL). 
        unsymm
            A Boolean specifying whether the element matrices are symmetric (ON) or unsymmetric 
            (OFF). The default value is OFF. 
        noSolutionDepVar
            An Int specifying the number of solution-dependent variables. The default value is 0. 
        userSubUel
            A String specifying the name of the user subroutine (UEL) that defines the user element. 
        dof
            A String specifying the degrees of freedom, separated by commas. 
        solutionDepVars
            A sequence of Floats specifying the initial values of the solution-dependent variables. 

        Returns
        -------
            An ActuatorSensor object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = ActuatorSensor(name, createStepName, point, interactionProperty,
                                                               noCoordComponents, unsymm, noSolutionDepVar, userSubUel,
                                                               dof, solutionDepVars)
        return interaction

    def ActuatorSensorProp(self, name: str, realProperties: tuple = (),
                           integerProperties: tuple = ()) -> ActuatorSensorProp:
        """This method creates an ActuatorSensorProp object.

        Path
        ----
            - mdb.models[name].ActuatorSensorProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        realProperties
            A sequence of Floats specifying the PROPS array used by user subroutine UEL. The default 
            value is an empty sequence. 
        integerProperties
            A sequence of Ints specifying the JPROPS array used by user subroutine UEL. The default 
            value is an empty sequence. 

        Returns
        -------
            An ActuatorSensorProp object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = ActuatorSensorProp(name, realProperties, integerProperties)
        return interaction

    def CavityRadiation(self, name: str, createStepName: str, surfaces: RegionArray, surfaceEmissivities: tuple = (),
                        ambientTemp: float = None, blocking: SymbolicConstant = BLOCKING_ALL,
                        blockingSurfaces: RegionArray = None, rangeOfView: float = None,
                        surfaceReflection: Boolean = ON, viewfactorAccurTol: float = 0,
                        minInfinitesimalRatio: float = 64, numPointsPerEdge: int = 3,
                        minLumpedAreaDS: float = 5, cyclicSymmetry: Boolean = OFF, cyclicImages: int = 2,
                        cyclicRotPt: ModelDot = ModelDot(), cyclicRotEndPt: ModelDot = ModelDot(),
                        cyclicSymPt: ModelDot = ModelDot(), periodicSymmetries: int = 0,
                        periodicImages_1: int = 2, periodicImages_2: int = 2, periodicImages_3: int = 2,
                        periodicSymAxis_1: str = '', periodicSymAxis_2: str = '', periodicSymPlane_1: str = '',
                        periodicSymPlane_2: str = '', periodicSymPlane_3: str = '',
                        periodicDistance_1: tuple = (), periodicDistance_2: tuple = (),
                        periodicDistance_3: tuple = (), periodicSymZ: float = None, periodicDistZ: float = None,
                        reflectionSymmetries: int = 0, reflectionSymAxis_1: str = '',
                        reflectionSymAxis_2: str = '', reflectionSymPlane_1: str = '',
                        reflectionSymPlane_2: str = '', reflectionSymPlane_3: str = '',
                        reflectionSymZ: float = None) -> CavityRadiation:
        """This method creates a CavityRadiation object.

        Path
        ----
            - mdb.models[name].CavityRadiation

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the cavity radiation interaction 
            should be created. 
        surfaces
            A RegionArray object specifying the surfaces for which radiation viewfactor control is 
            being specified. 
        surfaceEmissivities
            A sequence of Strings specifying the names of the Cavity Radiation properties containing 
            the surface emissivity data. One name per specified surface. The emissivity data is 
            ignored when *surfaceReflection*=OFF. 
        ambientTemp
            None or a Float specifying the reference ambient temperature value, θ0θ0. Specifying a 
            value indicates an open cavity. The default value is None. 
        blocking
            A SymbolicConstant specifying the blocking checks to be performed in the viewfactor 
            calculations. Possible values are BLOCKING_ALL, NO_BLOCKING, and PARTIAL_BLOCKING. The 
            default value is BLOCKING_ALL. 
        blockingSurfaces
            A RegionArray object specifying the surfaces that provide blocking inside the cavity. 
            This argument applies only when *blocking*=PARTIAL_BLOCKING. 
        rangeOfView
            None or a Float specifying the maximum distance between surface facets at which 
            viewfactors are calculated. More distant facets are deemed too far apart to exchange 
            significant amounts of heat through radiation effects, and the viewfactors between these 
            facets are assumed to be zero. If *rangeOfView*=None, there is no upper limit. The 
            default value is None. 
        surfaceReflection
            A Boolean specifying whether heat reflections are to be included in the cavity radiation 
            calculations. The default value is ON. 
        viewfactorAccurTol
            A Float specifying the acceptable tolerance for the viewfactor calculations. The default 
            value is 0.05. 
        minInfinitesimalRatio
            A Float specifying the facet area ratio above which the infinitesimal-to-finite area 
            approximation is used for viewfactor calculations. The default value is 64.0. 
        numPointsPerEdge
            An Int specifying the number of Gauss integration points to be used along each edge when 
            the numerical integration of contour integrals is used for viewfactor calculations. One 
            to five integration points are allowed. The default value is 3. 
        minLumpedAreaDS
            A Float specifying the nondimensional distance-square value above which the lumped area 
            approximation is used for viewfactor calculations. The default value is 5.0. 
        cyclicSymmetry
            A Boolean specifying whether cyclic symmetry will be applied. This argument cannot be 
            specified for axisymmetric models. The default value is OFF. 
        cyclicImages
            An Int specifying the number of cyclically similar images that compose the cavity formed 
            as a result of this symmetry. This argument applies only when *cyclicSymmetry*=ON. The 
            default value is 2. 
        cyclicRotPt
            A ModelDot object specifying the rotation axis point. This argument applies only when 
            *cyclicSymmetry*=ON. 
        cyclicRotEndPt
            A ModelDot object specifying the rotation axis end point. This argument applies only for 
            three-dimensional models, and only when *cyclicSymmetry*=ON. 
        cyclicSymPt
            A ModelDot object specifying the symmetry axis end point. This argument applies only 
            when *cyclicSymmetry*=ON. 
        periodicSymmetries
            An Int specifying the number of periodic symmetries that will be applied. The default 
            value is 0. 
        periodicImages_1
            An Int specifying the number of repetitions used in the numerical calculation of the 
            cavity viewfactors resulting from the first periodic symmetry. The result of this 
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the 
            value of *periodicImages_1*. This argument applies only when *periodicSymmetries* is 
            greater than zero. The default value is 2. 
        periodicImages_2
            An Int specifying the number of repetitions used in the numerical calculation of the 
            cavity viewfactors resulting from the second periodic symmetry. The result of this 
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the 
            value of *periodicImages_2*. This argument applies only when *periodicSymmetries* is 
            greater than one. The default value is 2. 
        periodicImages_3
            An Int specifying the number of repetitions used in the numerical calculation of the 
            cavity viewfactors resulting from the third periodic symmetry. The result of this 
            symmetry is a cavity composed of the cavity surface defined in the model plus twice the 
            value of *periodicImages_3*. This argument applies only when *periodicSymmetries* = 3. 
            The default value is 2. 
        periodicSymAxis_1
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object 
            indicating the first line of symmetry in two-dimensional models. This argument applies 
            only for 2D models, and when *periodicSymmetries* is greater than zero. 
        periodicSymAxis_2
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object 
            indicating the second line of symmetry in two-dimensional models. This argument applies 
            only for two-dimensional models, and when *periodicSymmetries* = 2. 
        periodicSymPlane_1
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating 
            the first plane of symmetry in three-dimensional models. This argument applies only for 
            three-dimensional models, and when *periodicSymmetries* is greater than zero. 
        periodicSymPlane_2
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating 
            the second plane of symmetry in three-dimensional models. This argument applies only for 
            three-dimensional models, and when *periodicSymmetries* is greater than one. 
        periodicSymPlane_3
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating 
            the third plane of symmetry in three-dimensional models. This argument applies only for 
            three-dimensional models, and when *periodicSymmetries* = 3. 
        periodicDistance_1
            A sequence of sequences of Floats specifying the two points of the vector that describes 
            the periodic distance for the first periodic symmetry. Each point is defined by a tuple 
            of three coordinates indicating its position. This argument applies only when 
            *periodicSymmetries* is greater than zero. The default value is an empty sequence. 
        periodicDistance_2
            A sequence of sequences of Floats specifying the two points of the vector that describes 
            the periodic distance for the second periodic symmetry. Each point is defined by a tuple 
            of three coordinates indicating its position. This argument applies only when 
            *periodicSymmetries* is greater than one. The default value is an empty sequence. 
        periodicDistance_3
            A sequence of sequences of Floats specifying the two points of the vector that describes 
            the periodic distance for the third periodic symmetry. Each point is defined by a tuple 
            of three coordinates indicating its position. This argument applies only when 
            *periodicSymmetries* = 3. The default value is an empty sequence. 
        periodicSymZ
            None or a Float specifying the Z value indicating the symmetry reference line in 
            axisymmetric models. This argument applies only for axisymmetric models, and when 
            *periodicSymmetries* = 1. The default value is None. 
        periodicDistZ
            None or a Float specifying the Z value indicating the periodic distance in axisymmetric 
            models. This argument applies only for axisymmetric models, and when 
            *periodicSymmetries* = 1. The default value is None. 
        reflectionSymmetries
            An Int specifying the number of reflection symmetries will be applied. The default value 
            is 0. 
        reflectionSymAxis_1
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object 
            indicating the first line of symmetry in two-dimensional models. This argument applies 
            only for two-dimensional models, and when *reflectionSymmetries* is greater than zero. 
        reflectionSymAxis_2
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object 
            indicating the second line of symmetry in two-dimensional models. This argument applies 
            only for two-dimensional models, and when *reflectionSymmetries* = 2. 
        reflectionSymPlane_1
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating 
            the first plane of symmetry in three-dimensional models. This argument applies only for 
            three-dimensional models, and when *reflectionSymmetries* is greater than zero. 
        reflectionSymPlane_2
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating 
            the second plane of symmetry in three-dimensional models. This argument applies only for 
            three-dimensional models, and when *reflectionSymmetries* is greater than one. 
        reflectionSymPlane_3
            A planar Face, an ElementFace, or a Datum object representing a datum plane; indicating 
            the third plane of symmetry in three-dimensional models. This argument applies only for 
            three-dimensional models, and when *reflectionSymmetries* = 3. 
        reflectionSymZ
            None or a Float specifying the Z value indicating the symmetry reference line in 
            axisymmetric models. This argument applies only for axisymmetric models, and when 
            *reflectionSymmetries* = 1. The default value is None. 

        Returns
        -------
            A CavityRadiation object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = CavityRadiation(name, createStepName, surfaces, surfaceEmissivities,
                                                                ambientTemp, blocking, blockingSurfaces, rangeOfView,
                                                                surfaceReflection, viewfactorAccurTol,
                                                                minInfinitesimalRatio, numPointsPerEdge,
                                                                minLumpedAreaDS, cyclicSymmetry, cyclicImages,
                                                                cyclicRotPt, cyclicRotEndPt, cyclicSymPt,
                                                                periodicSymmetries, periodicImages_1, periodicImages_2,
                                                                periodicImages_3, periodicSymAxis_1, periodicSymAxis_2,
                                                                periodicSymPlane_1, periodicSymPlane_2,
                                                                periodicSymPlane_3, periodicDistance_1,
                                                                periodicDistance_2, periodicDistance_3, periodicSymZ,
                                                                periodicDistZ, reflectionSymmetries,
                                                                reflectionSymAxis_1, reflectionSymAxis_2,
                                                                reflectionSymPlane_1, reflectionSymPlane_2,
                                                                reflectionSymPlane_3, reflectionSymZ)
        return interaction

    def CavityRadiationProp(self, name: str, temperatureDependency: Boolean = OFF, dependencies: int = 0,
                            property: tuple = ()) -> CavityRadiationProp:
        """This method creates a CavityRadiationProp object.

        Path
        ----
            - mdb.models[name].CavityRadiationProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        property
            A sequence of sequences of Floats specifying the following:The emissivity, 
            ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if 
            the data depend on field variables.Value of the second field variable.Etc. 

        Returns
        -------
            A CavityRadiationProp object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = CavityRadiationProp(name, temperatureDependency, dependencies, property)
        return interaction

    def ConcentratedFilmCondition(self, name: str, createStepName: str, region: Region, definition: SymbolicConstant,
                                  nodalArea: float = 1, explicitRegionType: SymbolicConstant = LAGRANGIAN,
                                  interactionProperty: str = '', field: str = '', sinkTemperature: float = 0,
                                  sinkAmplitude: str = '', filmCoeff: float = 0, filmCoeffAmplitude: str = '',
                                  sinkFieldName: str = '',
                                  sinkDistributionType: SymbolicConstant = UNIFORM) -> ConcentratedFilmCondition:
        """This method creates a ConcentratedFilmCondition object.

        Path
        ----
            - mdb.models[name].ConcentratedFilmCondition

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the ConcentratedFilmCondition object 
            is created. 
        region
            A Region object specifying the region to which the concentrated film condition 
            interaction is applied. The interaction is applied to each node in the region. 
        definition
            A SymbolicConstant specifying how the concentrated film condition is defined. Possible 
            values are EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD. 
        nodalArea
            A Float specifying the area associated with the node where the concentrated film 
            condition is applied. The default value is 1.0. 
        explicitRegionType
            A SymbolicConstant specifying how the concentrated film condition is applied to the 
            boundary of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and 
            EULERIAN. The default value is LAGRANGIAN. This argument applies only during an 
            Abaqus/Explicit analysis. 
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this 
            interaction. The *interactionProperty* argument applies only when 
            *definition*=PROPERTY_REF. The default value is an empty string. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *definition*=FIELD. The default 
            value is an empty string. 
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0. 
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use None in 
            an Abaqus/Standard analysis to specify that the reference sink temperature is applied 
            immediately at the beginning of the step or linearly over the step. Use None in an 
            Abaqus/Explicit analysis to specify that the reference sink temperature is applied 
            throughout the step. 
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The *filmCoeff* argument 
            applies when *definition*=EMBEDDED_COEFF, *definition*=USER_SUB, or *definition*=FIELD. 
            The default value is 0.0. 
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            film coefficient, hh, with time. The default value is an empty string.Note:Use None in 
            an Abaqus/Standard analysis to specify that the reference film coefficient is applied 
            immediately at the beginning of the step or linearly over the step. Use None in an 
            Abaqus/Explicit analysis to specify that the reference film coefficient is applied 
            throughout the step. 
        sinkFieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated 
            with the sink temperature. The *sinkFieldName* argument applies only when 
            *sinkDistributionType*=ANALYTICAL_FIELD or *sinkDistributionType*=DISCRETE_FIELD. The 
            default value is an empty string. 
        sinkDistributionType
            A SymbolicConstant specifying how the sink temperature is distributed. Possible values 
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM. 

        Returns
        -------
            A ConcentratedFilmCondition object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = ConcentratedFilmCondition(name, createStepName, region, definition,
                                                                          nodalArea, explicitRegionType,
                                                                          interactionProperty, field, sinkTemperature,
                                                                          sinkAmplitude, filmCoeff, filmCoeffAmplitude,
                                                                          sinkFieldName, sinkDistributionType)
        return interaction

    def ConcentratedRadiationToAmbient(self, name: str, createStepName: str, region: Region, ambientTemperature: float,
                                       ambientTemperatureAmp: str, emissivity: float, nodalArea: float = 1,
                                       explicitRegionType: SymbolicConstant = LAGRANGIAN, field: str = '',
                                       distributionType: SymbolicConstant = UNIFORM) -> ConcentratedRadiationToAmbient:
        """This method creates a ConcentratedRadiationToAmbient object.

        Path
        ----
            - mdb.models[name].ConcentratedRadiationToAmbient

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the ConcentratedRadiationToAmbient 
            object is created. 
        region
            A Region object specifying the region to which the concentrated radiation interaction is 
            applied. The interaction is applied to each node in the region. 
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0. 
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the 
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify 
            that the reference ambient temperature is applied immediately at the beginning of the 
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that 
            the reference ambient temperature is applied throughout the step. 
        emissivity
            A Float specifying the emissivity, ϵϵ. 
        nodalArea
            A Float specifying the area associated with the node where the concentrated radiation 
            interaction is applied. The default value is 1.0. 
        explicitRegionType
            A SymbolicConstant specifying how the concentrated radiation is applied to the boundary 
            of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and EULERIAN. The 
            default value is LAGRANGIAN.Note:*explicitRegionType* applies only during an 
            Abaqus/Explicit analysis. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *distributionType*=ANALYTICAL_FIELD. 
            The default value is an empty string. 
        distributionType
            A SymbolicConstant specifying how the radiation is defined. Possible values are UNIFORM 
            and ANALYTICAL_FIELD. The default value is UNIFORM. 

        Returns
        -------
            A ConcentratedRadiationToAmbient object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = ConcentratedRadiationToAmbient(name, createStepName, region,
                                                                               ambientTemperature,
                                                                               ambientTemperatureAmp, emissivity,
                                                                               nodalArea, explicitRegionType, field,
                                                                               distributionType)
        return interaction

    def ContactExp(self, name: str, createStepName: str, useAllstar: Boolean = OFF,
                   globalSmoothing: Boolean = ON, includedPairs: RegionPairs = RegionPairs(),
                   excludedPairs: RegionPairs = RegionPairs(),
                   contactPropertyAssignments: ContactPropertyAssignment = ContactPropertyAssignment(),
                   surfaceThicknessAssignments: SurfaceThicknessAssignment = SurfaceThicknessAssignment(),
                   surfaceOffsetAssignments: SurfaceOffsetAssignment = SurfaceOffsetAssignment(),
                   surfaceFeatureAssignments: SurfaceFeatureAssignment = SurfaceFeatureAssignment(),
                   smoothingAssignments: SmoothingAssignment = SmoothingAssignment(),
                   surfaceCrushTriggerAssignments: SurfaceCrushTriggerAssignment = SurfaceCrushTriggerAssignment(),
                   surfaceFrictionAssignments: SurfaceFrictionAssignment = SurfaceFrictionAssignment(),
                   mainSecondaryAssignments: MainSecondaryAssignment = MainSecondaryAssignment(),
                   polarityAssignments: PolarityAssignments = PolarityAssignments()) -> ContactExp:
        """This method creates a ContactExp object.

        Path
        ----
            - mdb.models[name].ContactExp

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which this contact interaction is created. 
        useAllstar
            A Boolean specifying whether the contacting surface pair consists of all exterior faces, 
            shell edges, beam segments, analytical rigid surfaces, and, when applicable, Eulerian 
            material surfaces. 
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically 
            applied to all eligible surfaces. The default value is ON. 
        includedPairs
            A RegionPairs object specifying the domain pairs included in contact. 
        excludedPairs
            A RegionPairs object specifying the domain pairs excluded from contact. 
        contactPropertyAssignments
            A ContactPropertyAssignment object specifying the contact property assignments in the 
            contact domain. 
        surfaceThicknessAssignments
            A SurfaceThicknessAssignment object specifying the surface thickness assignments in the 
            contact domain. 
        surfaceOffsetAssignments
            A SurfaceOffsetAssignment object specifying the surface offset fraction assignments in 
            the contact domain. 
        surfaceFeatureAssignments
            A SurfaceFeatureAssignment object specifying the surface feature angle assignments in 
            the contact domain. 
        smoothingAssignments
            A SmoothingAssignment object specifying the surface smoothing assignments in the contact 
            domain. 
        surfaceCrushTriggerAssignments
            A SurfaceCrushTriggerAssignment object specifying the surface crush trigger assignments 
            in the contact domain. 
        surfaceFrictionAssignments
            A SurfaceFrictionAssignment object specifying the surface friction assignments in the 
            contact domain. 
        mainSecondaryAssignments
            A MainSecondaryAssignment object specifying the main-secondary assignments in the 
            contact domain. 
        polarityAssignments
            A PolarityAssignments object specifying the polarity assignments in the contact domain. 

        Returns
        -------
            A ContactExp object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = ContactExp(name, createStepName, useAllstar, globalSmoothing,
                                                           includedPairs, excludedPairs, contactPropertyAssignments,
                                                           surfaceThicknessAssignments, surfaceOffsetAssignments,
                                                           surfaceFeatureAssignments, smoothingAssignments,
                                                           surfaceCrushTriggerAssignments, surfaceFrictionAssignments,
                                                           mainSecondaryAssignments, polarityAssignments)
        return interaction

    def ContactProperty(self, name: str) -> ContactProperty:
        """This method creates a ContactProperty object.

        Path
        ----
            - mdb.models[name].ContactProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 

        Returns
        -------
            A ContactProperty object. 

        Exceptions
        ----------
            None. 
        """
        self.interactionProperties[name] = interaction = ContactProperty(name)
        return interaction

    def ContactStd(self, name: str, createStepName: str, useAllstar: Boolean = OFF,
                   globalSmoothing: Boolean = ON, includedPairs: RegionPairs = RegionPairs(),
                   excludedPairs: RegionPairs = RegionPairs(),
                   contactPropertyAssignments: ContactPropertyAssignment = ContactPropertyAssignment(),
                   surfaceThicknessAssignments: SurfaceThicknessAssignment = SurfaceThicknessAssignment(),
                   surfaceOffsetAssignments: SurfaceOffsetAssignment = SurfaceOffsetAssignment(),
                   surfaceFeatureAssignments: SurfaceFeatureAssignment = SurfaceFeatureAssignment(),
                   surfaceBeamSmoothingAssignments: SurfaceBeamSmoothingAssignment = SurfaceBeamSmoothingAssignment(),
                   surfaceVertexCriteriaAssignments: SurfaceVertexCriteriaAssignment = SurfaceVertexCriteriaAssignment(),
                   mainSecondaryAssignments: MainSecondaryAssignment = MainSecondaryAssignment(),
                   initializationAssignments: InitializationAssignment = InitializationAssignment(),
                   stabilizationAssignments: StabilizationAssignment = StabilizationAssignment(),
                   smoothingAssignments: SmoothingAssignment = SmoothingAssignment(),
                   slidingTransitionAssignments: SlidingTransitionAssignments = SlidingTransitionAssignments(),
                   slidingFormulationAssignments: SlidingFormulationAssignment = SlidingFormulationAssignment()) -> ContactStd:
        """This method creates a ContactStd object.

        Path
        ----
            - mdb.models[name].ContactStd

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which this contact interaction is created. 
        useAllstar
            A Boolean specifying whether the contacting surface pairs consist of all exterior faces 
            in the model. 
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically 
            applied to all eligible surfaces. The default value is ON. 
        includedPairs
            A RegionPairs object specifying the domain pairs included in contact. 
        excludedPairs
            A RegionPairs object specifying the domain pairs excluded from contact. 
        contactPropertyAssignments
            A ContactPropertyAssignment object specifying the contact property assignments in the 
            contact domain. 
        surfaceThicknessAssignments
            A SurfaceThicknessAssignment object specifying the surface thickness assignments in the 
            contact domain. 
        surfaceOffsetAssignments
            A SurfaceOffsetAssignment object specifying the surface offset fraction assignments in 
            the contact domain. 
        surfaceFeatureAssignments
            A SurfaceFeatureAssignment object specifying the surface feature angle assignments in 
            the contact domain. 
        surfaceBeamSmoothingAssignments
            A SurfaceBeamSmoothingAssignment object specifying the surface beam smoothing 
            assignments in the contact domain. 
        surfaceVertexCriteriaAssignments
            A SurfaceVertexCriteriaAssignment object specifying the surface vertex criteria 
            assignments in the contact domain. 
        mainSecondaryAssignments
            A MainSecondaryAssignment object specifying the main-secondary assignments in the 
            contact domain. 
        initializationAssignments
            An InitializationAssignment object specifying the contact initialization assignments in 
            the contact domain. 
        stabilizationAssignments
            A StabilizationAssignment object specifying the contact stabilization assignments in the 
            contact domain. 
        smoothingAssignments
            A SmoothingAssignment object specifying the surface smoothing assignments in the contact 
            domain. 
        slidingTransitionAssignments
            A SlidingTransitionAssignments object specifying the sliding transition assignments in 
            the contact domain. 
        slidingFormulationAssignments
            A SlidingFormulationAssignment object specifying the sliding formulation assignments in 
            the contact domain. 

        Returns
        -------
            A ContactStd object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = ContactStd(name, createStepName, useAllstar, globalSmoothing,
                                                           includedPairs, excludedPairs, contactPropertyAssignments,
                                                           surfaceThicknessAssignments, surfaceOffsetAssignments,
                                                           surfaceFeatureAssignments, surfaceBeamSmoothingAssignments,
                                                           surfaceVertexCriteriaAssignments, mainSecondaryAssignments,
                                                           initializationAssignments, stabilizationAssignments,
                                                           smoothingAssignments, slidingTransitionAssignments,
                                                           slidingFormulationAssignments)
        return interaction

    def CyclicSymmetry(self, name: str, createStepName: str, main: Region, secondary: Region, repetitiveSectors: int,
                       axisPoint1: Region, axisPoint2: Region,
                       extractedNodalDiameter: SymbolicConstant = ALL_NODAL_DIAMETER,
                       lowestNodalDiameter: int = 0, highestNodalDiameter: int = 0,
                       excitationNodalDiameter: int = 0, adjustTie: Boolean = ON, positionTolerance: float = 0,
                       positionToleranceMethod: SymbolicConstant = COMPUTED_TOLERANCE) -> CyclicSymmetry:
        """This method creates a CyclicSymmetry object.

        Path
        ----
            - mdb.models[name].CyclicSymmetry

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the cyclic symmetry interaction should 
            be created. 
        main
            A Region object specifying the main surface. 
        secondary
            A Region object specifying the secondary surface. 
        repetitiveSectors
            An Int specifying the total number of sectors in the cyclic symmetric model. 
        axisPoint1
            A Region object specifying the first point of the axis of symmetry. The region should 
            contain exactly one mesh node, vertex, interesting point, reference point, or datum 
            point. In a two-dimensional model *axisPoint1* is the only point used to define the axis 
            of symmetry. 
        axisPoint2
            A Region object specifying the second point of the axis of symmetry. The region should 
            contain exactly one mesh node, vertex, interesting point, reference point, or datum 
            point. This point is ignored in a two-dimensional model. 
        extractedNodalDiameter
            A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters 
            or the nodal diameters between the user-specified values for *lowestNodalDiameter* and 
            *highestNodalDiameter*. Possible values are ALL_NODAL_DIAMETER and 
            SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER. 
        lowestNodalDiameter
            An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis. 
            The default value is 0. 
        highestNodalDiameter
            An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis. 
            This argument value should be less than or equal to the half of the total number of 
            sectors (as specified in the *repetitiveSectors* parameter). The default value is 0. 
        excitationNodalDiameter
            An Int specifying the nodal diameter for which the modal-based steady-state dynamic 
            analysis will be performed. This value should be greater than or equal to the lowest 
            nodal diameter (specified in the *lowestNodalDiameter* parameter), and less than or 
            equal to the highest nodal diameter (specified in the *highestNodalDiameter* parameter). 
            The default value is 0. 
        adjustTie
            A Boolean specifying whether or not to adjust the secondary surface of the cyclic 
            symmetry to tie it to the main surface. The default value is ON. 
        positionTolerance
            A Float specifying the position tolerance. The*positionTolerance* argument applies only 
            when *positionToleranceMethod*=SPECIFY_TOLERANCE. The default value is 0.0. 
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance. 
            Possible values are COMPUTED_TOLERANCE and SPECIFY_TOLERANCE. The default value is 
            COMPUTED_TOLERANCE. 

        Returns
        -------
            A CyclicSymmetry object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = CyclicSymmetry(name, createStepName, main, secondary, repetitiveSectors,
                                                               axisPoint1, axisPoint2, extractedNodalDiameter,
                                                               lowestNodalDiameter, highestNodalDiameter,
                                                               excitationNodalDiameter, adjustTie, positionTolerance,
                                                               positionToleranceMethod)
        return interaction

    def ElasticFoundation(self, name: str, createStepName: str, surface: Region, stiffness: float) -> ElasticFoundation:
        """This method creates an ElasticFoundation object.

        Path
        ----
            - mdb.models[name].ElasticFoundation

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the ElasticFoundation object is 
            created. *createStepName* must be set to 'Initial'. 
        surface
            A Region object specifying the surface to which the foundation applies. 
        stiffness
            A Float specifying the foundation stiffness per area (or per length for beams). 

        Returns
        -------
            An ElasticFoundation object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = ElasticFoundation(name, createStepName, surface, stiffness)
        return interaction

    def ExpContactControl(self, name: str, globTrkChoice: SymbolicConstant = DEFAULT, globTrkInc: int = None,
                          fastLocalTrk: Boolean = ON, scalePenalty: float = 1, warpCheckPeriod: int = 20,
                          warpCutoff: float = 20) -> ExpContactControl:
        """This method creates an ExpContactControl object.

        Path
        ----
            - mdb.models[name].ExpContactControl

        Parameters
        ----------
        name
            A String specifying the contact controls repository key. 
        globTrkChoice
            A SymbolicConstant specifying whether or not the default value will be used for the 
            maximum number of increments between global contact searches. Possible values are 
            DEFAULT and SPECIFY. The default value is DEFAULT. 
        globTrkInc
            An Int specifying the maximum number of increments between global contact searches. The 
            *globTrkInc* argument applies only when *globTrkChoice*=SPECIFY. The default value is 
            100 for surface-to-surface contact and 4 for self-contact. 
        fastLocalTrk
            A Boolean specifying whether to use the more computationally efficient local tracking 
            method. The default value is ON. 
        scalePenalty
            A Float specifying the factor by which Abaqus/Explicit will scale the default penalty 
            stiffness to obtain the stiffnesses used for the penalty contact pairs. The default 
            value is 1.0. 
        warpCheckPeriod
            An Int specifying the number of increments between checks for highly warped facets on 
            main surfaces. The default value is 20. 
        warpCutoff
            A Float specifying the out-of-plane warping angle (in degrees), at which a facet will be 
            considered to be highly warped. The default value is 20.0. 

        Returns
        -------
            An ExpContactControl object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.interactions[name] = interaction = ExpContactControl(name, globTrkChoice, globTrkInc, fastLocalTrk,
                                                                  scalePenalty, warpCheckPeriod, warpCutoff)
        return interaction

    def ExpInitialization(self, name: str, overclosureType: SymbolicConstant = ADJUST,
                          interferenceDistance: float = None, clearanceDistance: float = None,
                          openingTolerance: float = None, overclosureTolerance: float = None,
                          adjustNodalCoords: Boolean = True, secondaryNodesetName: str = None,
                          stepFraction: float = 1) -> ExpInitialization:
        """This method creates an ExpInitialization object.

        Path
        ----
            - mdb.models[name].ExpInitialization

        Parameters
        ----------
        name
            A String specifying the contact initialization repository key. 
        overclosureType
            A SymbolicConstant specifying the type of overclosure to be defined. Possible values are 
            ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST. 
        interferenceDistance
            None or a Float specifying the interference distance. This argument is valid only when 
            *overclosureType*=INTERFERENCE. The default value is None. 
        clearanceDistance
            None or a Float specifying the initial clearance distance. This argument is valid only 
            when *overclosureType*=CLEARANCE and must be specified in that case. The default value 
            is None. 
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will 
            undergo strain-free adjustments. This argument is not valid when 
            *overclosureType*=INTERFERENCE unless a value has been specified for 
            *interferenceDistance*. The default value is None. 
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will 
            undergo strain-free adjustments. The default value is None. 
        adjustNodalCoords
            A Boolean specifying whether to resolve clearances/overclosures by adjusting the nodal 
            coordinates without creating strain in the model. *adjustNodalCoords*=True can be used 
            only for clearances/overclosures defined in the first step of an analysis. The default 
            value is True. 
        secondaryNodesetName
            A String specifying the name of the node set containing the secondary nodes to be 
            included in the initial clearance specification. This argument is not valid when 
            *overclosureType*=INTERFERENCE and if *openingTolerance* or *overclosureTolerance* is 
            specified. The default value is None. 
        stepFraction
            A Float specifying the fraction of the step time (between 0.0 and 1.0) in which the 
            interference fit has to be solved. The default value is 1.0. This argument is valid only 
            when *overclosureType*=INTERFERENCE. 

        Returns
        -------
            An ExpInitialization object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.interactions[name] = interaction = ExpInitialization(name, overclosureType, interferenceDistance,
                                                                  clearanceDistance, openingTolerance,
                                                                  overclosureTolerance, adjustNodalCoords,
                                                                  secondaryNodesetName, stepFraction)
        return interaction

    def FilmCondition(self, name: str, createStepName: str, surface: Region, definition: SymbolicConstant,
                      interactionProperty: str = '', sinkTemperature: float = 0, sinkAmplitude: str = '',
                      filmCoeff: float = 0, filmCoeffAmplitude: str = '', field: str = '',
                      sinkFieldName: str = '', sinkDistributionType: SymbolicConstant = UNIFORM) -> FilmCondition:
        """This method creates a FilmCondition object.

        Path
        ----
            - mdb.models[name].FilmCondition

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the FilmCondition object is created. 
        surface
            A Region object specifying the name of the surface to which the film condition 
            interaction is applied. 
        definition
            A SymbolicConstant specifying how the film condition is defined. Possible values are 
            EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD. 
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this 
            interaction. The *interactionProperty* argument applies only when 
            *definition*=PROPERTY_REF. The default value is an empty string. 
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0. 
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use empty 
            string in an Abaqus/Standard analysis to specify that the reference sink temperature is 
            applied immediately at the beginning of the step or linearly over the step. Use empty 
            string in an Abaqus/Explicit analysis to specify that the reference sink temperature is 
            applied throughout the step. 
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The *filmCoeff* argument 
            applies when *definition*=EMBEDDED_COEFF, *definition*=USER_SUB, or *definition*=FIELD. 
            The default value is 0.0. 
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            film coefficient, hh, with time. The default value is an empty string. Note: Use empty 
            string in an Abaqus/Standard analysis to specify that the reference film coefficient is 
            applied immediately at the beginning of the step or linearly over the step. Use empty 
            string in an Abaqus/Explicit analysis to specify that the reference film coefficient is 
            applied throughout the step. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *definition*=FIELD. The default 
            value is an empty string. 
        sinkFieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated 
            with the sink temperature. The *sinkFieldName* argument applies only when 
            *sinkDistributionType*=ANALYTICAL_FIELD or *sinkDistributionType*=DISCRETE_FIELD. The 
            default value is an empty string. 
        sinkDistributionType
            A SymbolicConstant specifying how the sink temperature is distributed. Possible values 
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM. 

        Returns
        -------
            A FilmCondition object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = FilmCondition(name, createStepName, surface, definition,
                                                              interactionProperty, sinkTemperature, sinkAmplitude,
                                                              filmCoeff, filmCoeffAmplitude, field, sinkFieldName,
                                                              sinkDistributionType)
        return interaction

    def FilmConditionProp(self, name: str, temperatureDependency: Boolean = OFF, dependencies: int = 0,
                          property: tuple = ()) -> FilmConditionProp:
        """This method creates a FilmConditionProp object.

        Path
        ----
            - mdb.models[name].FilmConditionProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        property
            A sequence of sequences of Floats specifying the following: 
            - The film coefficient, hh. 
            - Temperature, if the data depend on temperature. 
            - Value of the first field variable, if the data depend on field variables. 
            - Value of the second field variable. 
            - Etc. 

        Returns
        -------
            A FilmConditionProp object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = FilmConditionProp(name, temperatureDependency, dependencies, property)
        return interaction

    def FluidCavity(self, name: str, createStepName: str, cavityPoint: Region, cavitySurface: Region,
                    interactionProperty: str, ambientPressure: float = 0, thickness: float = 1,
                    useAdiabatic: Boolean = OFF, checkNormals: Boolean = ON) -> FluidCavity:
        """This method creates an FluidCavity object.

        Path
        ----
            - mdb.models[name].FluidCavity

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the FluidCavity object is created. 
        cavityPoint
            A Region object specifying the fluid cavity reference point. 
        cavitySurface
            A Region object specifying the surface forming the boundary of the fluid cavity. 
        interactionProperty
            A String specifying the FluidCavityProperty object associated with this interaction. 
        ambientPressure
            A Float specifying the magnitude of the ambient pressure. The default value is 0.0. 
        thickness
            A Float specifying the out-of-plane thickness of the surface for two-dimensional models. 
            This argument is valid only when using two-dimensional models. The default value is 1.0. 
        useAdiabatic
            A Boolean specifying whether adiabatic behavior is assumed for the ideal gas. This 
            argument is valid only when *interactionProperty* specifies a pneumatic definition. The 
            default value is OFF. 
        checkNormals
            A Boolean specifying whether the analysis will check the consistency of the surface 
            normals. The default value is ON. 

        Returns
        -------
            A FluidCavity object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = FluidCavity(name, createStepName, cavityPoint, cavitySurface,
                                                            interactionProperty, ambientPressure, thickness,
                                                            useAdiabatic, checkNormals)
        return interaction

    def FluidCavityProperty(self, name: str, definition: SymbolicConstant = HYDRAULIC, fluidDensity: float = None,
                            molecularWeight: float = None, useExpansion: Boolean = OFF,
                            expansionTempDep: Boolean = OFF, expansionDependencies: int = 0,
                            referenceTemperature: float = 0, expansionTable: tuple = (),
                            useBulkModulus: Boolean = OFF, bulkModulusTempDep: Boolean = OFF,
                            bulkModulusDependencies: int = 0, bulkModulusTable: tuple = (),
                            useCapacity: Boolean = OFF, capacityType: SymbolicConstant = POLYNOMIAL,
                            capacityTempDep: Boolean = OFF, capacityDependencies: int = 0,
                            capacityTable: tuple = ()) -> FluidCavityProperty:
        """This method creates a FluidCavityProperty object.

        Path
        ----
            - mdb.models[name].FluidCavityProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        definition
            A SymbolicConstant specifying the type of fluid cavity property to be defined. Possible 
            values are HYDRAULIC and PNEUMATIC. The default value is HYDRAULIC. 
        fluidDensity
            None or a Float specifying the reference fluid density. This argument is applicable only 
            when *definition*=HYDRAULIC, and is required in that case. The default value is None. 
        molecularWeight
            None or a Float specifying the molecular weight of the ideal gas species. This argument 
            is applicable only when *definition*=PNEUMATIC, and is required in that case. The 
            default value is None. 
        useExpansion
            A Boolean specifying whether thermal expansion coefficients will be defined. This 
            argument is applicable only when *definition*=HYDRAULIC. The default value is OFF. 
        expansionTempDep
            A Boolean specifying whether the thermal fluid expansion data will have temperature 
            dependency. This argument is applicable only when *definition*=HYDRAULIC and when 
            *useExpansion*=True. The default value is OFF. 
        expansionDependencies
            An Int specifying the number of field variable dependencies in the thermal fluid 
            expansion data. This argument is applicable only when *definition*=HYDRAULIC and when 
            *useExpansion*=True. The default value is 0. 
        referenceTemperature
            A Float specifying the reference temperature for the coefficient of thermal expansion. 
            This argument is applicable only when *definition*=HYDRAULIC, when *useExpansion*=True, 
            and when either *expansionTempDep*=True or when *expansionDependencies* is greater than 
            0. The default value is 0.0. 
        expansionTable
            A sequence of sequences of Floats specifying the thermal expansion coefficients. This 
            argument is applicable only when *definition*=HYDRAULIC and when *useExpansion*=True. 
            Each sequence contains the following data: 
            - The mean coefficient of thermal expansion. 
            - Temperature, if the data depend on temperature. 
            - Value of the first field variable, if the data depend on field variables. 
            - Value of the second field variable. 
            - Etc. 
        useBulkModulus
            A Boolean specifying whether fluid bulk modulus values will be defined. This argument is 
            applicable only when *definition*=HYDRAULIC. The default value is OFF. 
        bulkModulusTempDep
            A Boolean specifying whether the fluid bulk modulus data will have temperature 
            dependency. This argument is applicable only when *definition*=HYDRAULIC and when 
            *useBulkModulus*=True. The default value is OFF. 
        bulkModulusDependencies
            An Int specifying the number of field variable dependencies in the fluid bulk modulus 
            data. This argument is applicable only when *definition*=HYDRAULIC and when 
            *useBulkModulus*=True. The default value is 0. 
        bulkModulusTable
            A sequence of sequences of Floats specifying the fluid bulk modulus values. This 
            argument is applicable only when *definition*=HYDRAULIC and when *useBulkModulus*=True. 
            Each sequence contains the following data: 
            - The fluid bulk modulus. 
            - Temperature, if the data depend on temperature. 
            - Value of the first field variable, if the data depend on field variables. 
            - Value of the second field variable. 
            - Etc. 
        useCapacity
            A Boolean specifying whether molar heat capacity values will be defined. This argument 
            is applicable only when *definition*=PNEUMATIC. The default value is OFF. 
        capacityType
            A SymbolicConstant specifying the method to define the molar heat capacity. Possible 
            values are POLYNOMIAL and TABULAR. The default value is POLYNOMIAL. 
        capacityTempDep
            A Boolean specifying whether the molar heat capacity data will have temperature 
            dependency. This argument is applicable only when *definition*=PNEUMATIC, when 
            *useCapacity*=True, and when *capacityType*=TABULAR. The default value is OFF. 
        capacityDependencies
            An Int specifying the number of field variable dependencies in the molar heat capacity 
            data. This argument is applicable only when *definition*=PNEUMATIC, when 
            *useCapacity*=True, and when *capacityType*=TABULAR. The default value is 0. 
        capacityTable
            A sequence of sequences of Floats specifying the molar heat capacity values in the form 
            of a polynomial expression. This argument is applicable only when 
            *definition*=PNEUMATIC, when *useCapacity*=True, and when *capacityType*=POLYNOMIAL. In 
            this form, only one sequence is specified and that sequence contains the following data: 
            - The first molar heat capacity coefficient. 
            - The second molar heat capacity coefficient. 
            - The third molar heat capacity coefficient. 
            - The fourth molar heat capacity coefficient. 
            - The fifth molar heat capacity coefficient. 
            Alternatively, the sequence data may specify the molar heat capacity values at constant 
            pressure for an ideal gas species. This argument is applicable only when 
            *definition*=PNEUMATIC, when *useCapacity*=True, and when *capacityType*=TABULAR. Each 
            sequence contains the following data: 
            - The molar heat capacity at constant pressure. 
            - Temperature, if the data depend on temperature. 
            - Value of the first field variable, if the data depend on field variables. 
            - Value of the second field variable. 
            - Etc. 

        Returns
        -------
            A FluidCavityProperty object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = FluidCavityProperty(name, definition, fluidDensity, molecularWeight,
                                                                    useExpansion, expansionTempDep,
                                                                    expansionDependencies, referenceTemperature,
                                                                    expansionTable, useBulkModulus, bulkModulusTempDep,
                                                                    bulkModulusDependencies, bulkModulusTable,
                                                                    useCapacity, capacityType, capacityTempDep,
                                                                    capacityDependencies, capacityTable)
        return interaction

    def FluidExchange(self, name: str, createStepName: str, firstCavity: str, interactionProperty: str,
                      definition: SymbolicConstant = TO_ENVIRONMENT, secondCavity: str = '',
                      exchangeArea: float = 1) -> FluidExchange:
        """This method creates an FluidExchange object.

        Path
        ----
            - mdb.models[name].FluidExchange

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the FluidExchange object is created. 
        firstCavity
            A String specifying the first FluidCavity object associated with this interaction. This 
            will be the only cavity specified if *definition*=TO_ENVIRONMENT. 
        interactionProperty
            A String specifying the FluidExchangeProperty object associated with this interaction. 
        definition
            A SymbolicConstant specifying the type of fluid exchange to be defined. Possible values 
            are TO_ENVIRONMENT and BETWEEN_CAVITIES. The default value is TO_ENVIRONMENT. 
        secondCavity
            A String specifying the second FluidCavity object associated with this interaction. This 
            argument is applicable only when *definition*=BETWEEN_CAVITIES. 
        exchangeArea
            A Float specifying the effective exchange area. The default value is 1.0. 

        Returns
        -------
            A FluidExchange object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = FluidExchange(name, createStepName, firstCavity, interactionProperty,
                                                              definition, secondCavity, exchangeArea)
        return interaction

    def FluidExchangeProperty(self, name: str, dataTable: tuple, definition: SymbolicConstant = BULK_VISCOSITY,
                              pressureDependency: Boolean = OFF, temperatureDependency: Boolean = OFF,
                              fieldDependencies: int = 0) -> FluidExchangeProperty:
        """This method creates a FluidExchangeProperty object.

        Path
        ----
            - mdb.models[name].FluidExchangeProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        dataTable
            A sequence of sequences of Floats specifying the viscous and hydrodynamic resistance 
            coefficients when *definition*=BULK_VISCOSITY. Each sequence contains the following 
            data: 
            - The viscous resistance coefficient. 
            - The hydrodynamic resistance coefficient. 
            - The average absolute pressure, if the data depend on pressure. 
            - The average temperature, if the data depend on temperature. 
            - The value of the first field variable, if the data depend on field variables. 
            - The value of the second field variable. 
            - Etc. 
            Alternatively, the sequence data may specify the mass flow rate. This is applicable only 
            when *definition*=MASS_FLUX. In this form, only one sequence is specified and that 
            sequence contains the following data: 
            - The mass flow rate per unit area. 
            Alternatively, the sequence data may specify the mass rate leakage. This is applicable 
            only when *definition*=MASS_RATE_LEAK. Each sequence contains the following data: 
            - The absolute value of the mass flow rate per unit area. (The first tabular value 
            entered must always be zero.) 
            - The absolute value of the pressure difference. (The first tabular value entered must 
            always be zero.) 
            - The average absolute pressure, if the data depend on pressure. 
            - The average temperature, if the data depend on temperature. 
            - The value of the first field variable, if the data depend on field variables. 
            - The value of the second field variable. 
            - Etc. 
            Alternatively, the sequence data may specify the volume flow rate. This is applicable 
            only when *definition*=VOL_FLUX. In this form, only one sequence is specified and that 
            sequence contains the following data: 
            - The volumetric flow rate per unit area. 
            Alternatively, the sequence data may specify the volume rate leakage. This is applicable 
            only when *definition*=VOL_RATE_LEAK. Each sequence contains the following data: 
            - The absolute value of the volumetric flow rate per unit area. (The first tabular value 
            entered must always be zero.) 
            - The absolute value of the pressure difference. (The first tabular value entered must 
            always be zero.) 
            - The average absolute pressure, if the data depend on pressure. 
            - The average temperature, if the data depend on temperature. 
            - The value of the first field variable, if the data depend on field variables. 
            - The value of the second field variable. 
            - Etc. 
        definition
            A SymbolicConstant specifying the type of fluid exchange property to be defined. 
            Possible values are BULK_VISCOSITY, MASS_FLUX, MASS_RATE_LEAK, VOL_FLUX, and 
            VOL_RATE_LEAK. The default value is BULK_VISCOSITY. 
        pressureDependency
            A Boolean specifying whether the data will have pressure dependency. This argument is 
            applicable only when *definition*=BULK_VISCOSITY, or when *definition*=MASS_RATE_LEAK, 
            or when *definition*=VOL_RATE_LEAK. The default value is OFF. 
        temperatureDependency
            A Boolean specifying whether the data will have temperature dependency. This argument is 
            applicable only when *definition*=BULK_VISCOSITY, or when *definition*=MASS_RATE_LEAK, 
            or when *definition*=VOL_RATE_LEAK. The default value is OFF. 
        fieldDependencies
            An Int specifying the number of field variable dependencies in the data. This argument 
            is applicable only when *definition*=BULK_VISCOSITY, or when 
            *definition*=MASS_RATE_LEAK, or when *definition*=VOL_RATE_LEAK. The default value is 0. 

        Returns
        -------
            A FluidExchangeProperty object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = FluidExchangeProperty(name, dataTable, definition, pressureDependency,
                                                                      temperatureDependency, fieldDependencies)
        return interaction

    def FluidInflator(self, name: str, createStepName: str, cavity: str, interactionProperty: str,
                      inflationTimeAmplitude: str = '', massFlowAmplitude: str = '') -> FluidInflator:
        """This method creates a FluidInflator object.

        Path
        ----
            - mdb.models[name].FluidInflator

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the FluidInflator object is created. 
        cavity
            A String specifying the first FluidCavity object associated with this interaction. 
        interactionProperty
            A String specifying the FluidInflatorProperty object associated with this interaction. 
        inflationTimeAmplitude
            A string specifying the name of the amplitude curve defining a mapping between the 
            inflation time and the actual time. 
        massFlowAmplitude
            A string specifying the name of the amplitude curve by which to modify the mass flow 
            rate. 

        Returns
        -------
            A FluidInflator object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = FluidInflator(name, createStepName, cavity, interactionProperty,
                                                              inflationTimeAmplitude, massFlowAmplitude)
        return interaction

    def FluidInflatorProperty(self, name: str, definition: str, effectiveArea: float, tankVolume: float,
                              dischargeCoefficient: float = None, dataTable: tuple = (), numFluids: int = None,
                              mixtureType: str = '', inflationTime: tuple = (), fluidbehaviorName: tuple = (),
                              massFraction: tuple = ()) -> FluidInflatorProperty:
        """This method creates a FluidInflatorProperty object.

        Path
        ----
            - mdb.models[name].FluidInflatorProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        definition
            A Symbolic constant specifying the method used for modeling the flow characteristics of 
            inflators. The default value is *definition*=DUAL PRESSURE. The possible values are DUAL 
            PRESSURE, PRESSURE AND MASS, TANK TEST, and TEMPERATURE AND MASS. 
        effectiveArea
            A Float specifying the total inflator orifice area. This argument is applicable only if 
            *definition*=DUAL PRESSURE or *definition*=PRESSURE AND MASS. 
        tankVolume
            A Float specifying the tank volume. This argument is applicable only if 
            *definition*=DUAL PRESSURE or *definition*=TANK TEST. 
        dischargeCoefficient
            A Float specifying the discharge coefficient. This argument is applicable only if 
            *definition*=DUAL PRESSURE or *definition*=PRESSURE AND MASS. 
        dataTable
            A sequence of sequences of Floats specifying the items described in the "Table data" 
            section below. 
        numFluids
            An Int specifying the number of gas species used for this inflator. 
        mixtureType
            A Symbolic constant specifying whether to use mass fraction or the molar fraction for a 
            mixture of ideal gases. The default value is MASS FRACTION. The possible values are MASS 
            FRACTION or MOLAR FRACTION. 
        inflationTime
            A sequence of sequences of Floats specifying the inflation time. 
        fluidbehaviorName
            A sequence of sequences of Strings specifying fluid behavior names. 
        massFraction
            A sequence of sequences of Floats specifying the mass fraction or the molar fraction 
            corresponding to entered fluid behavior. 

        Returns
        -------
            A FluidInflatorProperty object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = FluidInflatorProperty(name, definition, effectiveArea, tankVolume,
                                                                      dischargeCoefficient, dataTable, numFluids,
                                                                      mixtureType, inflationTime, fluidbehaviorName,
                                                                      massFraction)
        return interaction

    def IncidentWave(self, name: str, createStepName: str, sourcePoint: Region, standoffPoint: Region,
                     surface: Region, interactionProperty: str, definition: SymbolicConstant = PRESSURE,
                     amplitude: str = '', imaginaryAmplitude: str = '', surfaceNormal: tuple = (),
                     initialDepth: float = None, referenceMagnitude: float = None,
                     detonationTime: float = None, magnitudeFactor: float = 1) -> IncidentWave:
        """This method creates an IncidentWave object.

        Path
        ----
            - mdb.models[name].IncidentWave

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the IncidentWave object is created. 
        sourcePoint
            A Region object specifying the incident wave source point. 
        standoffPoint
            A Region object specifying the incident wave standoff point.This argument is not valid 
            when *definition*=CONWEP. 
        surface
            A Region object specifying the surface defining the incident wave interaction. In 
            problems involving fluid/surface boundaries, both the fluid surface and the solid 
            surface comprising the boundary must have an incident wave interaction specified. 
        interactionProperty
            A String specifying the IncidentWaveProperty object associated with this interaction. 
        definition
            A SymbolicConstant specifying the type of incident wave to be defined. The value must be 
            PRESSURE for linear perturbation steps. An Explicit step is required when the value is 
            set to CONWEP. Possible values are PRESSURE, ACCELERATION, UNDEX, and CONWEP. The 
            default value is PRESSURE. 
        amplitude
            A String specifying the name of the Amplitude object that defines the fluid pressure 
            time history at the standoff point, if *definition*=PRESSURE. If 
            *definition*=ACCELERATION, then this string specifies the name of the Amplitude object 
            that defines the fluid particle acceleration time history at the standoff point. This 
            member can be specified only if *definition*=PRESSURE or ACCELERATION. The default value 
            is an empty string. 
        imaginaryAmplitude
            A String specifying the name of the Amplitude object that defines the imaginary 
            component of the fluid pressure time history at the standoff point. This member is 
            applicable only for linear perturbation steps and if *definition*=PRESSURE. The default 
            value is an empty string. 
        surfaceNormal
            A sequence of three Floats specifying the X, Y, and Z components of the direction cosine 
            of the fluid surface normal.This argument is valid only when *definition*=UNDEX. 
        initialDepth
            None or a Float specifying the initial depth of the UNDEX bubble. The default value is 
            None.This argument is valid only when *definition*=UNDEX. 
        referenceMagnitude
            A Float specifying the reference magnitude.This argument is not valid when 
            *definition*=CONWEP. 
        detonationTime
            A Float specifying the time of detonation, given in total time.This argument is valid 
            only when *definition*=CONWEP. 
        magnitudeFactor
            A Float specifying the magnitude scale factor. The default value is 1.0.This argument is 
            valid only when *definition*=CONWEP. 

        Returns
        -------
            An IncidentWave object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = IncidentWave(name, createStepName, sourcePoint, standoffPoint, surface,
                                                             interactionProperty, definition, amplitude,
                                                             imaginaryAmplitude, surfaceNormal, initialDepth,
                                                             referenceMagnitude, detonationTime, magnitudeFactor)
        return interaction

    def IncidentWaveProperty(self, name: str, definition: SymbolicConstant = PLANAR,
                             propagationModel: SymbolicConstant = ACOUSTIC, soundSpeed: float = None,
                             fluidDensity: float = None, specificHeatRatio: float = None, gravity: float = None,
                             atmosphericPressure: float = None, dragCoefficient: float = None,
                             dragExponent: float = 2, waveEffects: Boolean = ON, chargeDensity: float = None,
                             chargeMass: float = None, constantK1: float = None, constantK2: float = None,
                             constantA: float = None, constantB: float = None, constantKc: float = None,
                             duration: float = None, maximumSteps: int = 1500, relativeStepControl: float = None,
                             absoluteStepControl: float = None, stepControlExponent: float = 0, genDecayA: float = 0,
                             genDecayB: float = 0, genDecayC: float = 0, seedNumber: int = None,
                             massTNT: float = None, massFactor: float = 1, lengthFactor: float = 1,
                             timeFactor: float = 1, pressureFactor: float = 1) -> IncidentWaveProperty:
        """This method creates an IncidentWaveProperty object.

        Path
        ----
            - mdb.models[name].IncidentWaveProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        definition
            A SymbolicConstant specifying the type of wave to be defined. Possible values are 
            PLANAR, SPHERICAL, DIFFUSE, AIR_BLAST, and SURFACE_BLAST. The default value is PLANAR. 
        propagationModel
            A SymbolicConstant specifying the spherical propagation model. Possible values are 
            ACOUSTIC, UNDEX_CHARGE, and GENERALIZED_DECAY. The default value is ACOUSTIC.This 
            argument is valid only when *definition*=SPHERICAL. 
        soundSpeed
            A Float specifying the speed of sound in the fluid.This argument is not valid when 
            *definition*=AIR_BLAST or when *definition*=SURFACE_BLAST. 
        fluidDensity
            A Float specifying the fluid mass density.This argument is not valid when 
            *definition*=AIR_BLAST or when *definition*=SURFACE_BLAST. 
        specificHeatRatio
            None or a Float specifying the ratio of specific heats for gas. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        gravity
            None or a Float specifying the acceleration due to gravity. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        atmosphericPressure
            None or a Float specifying the atmospheric pressure. The default value is None.This 
            argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE. 
        dragCoefficient
            None or a Float specifying the fluid drag coefficient. The default value is None.This 
            argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE. 
        dragExponent
            A Float specifying the fluid drag exponent. The default value is 2.0.This argument is 
            valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE. 
        waveEffects
            A Boolean specifying whether or not to include wave effects in the fluid and gas. The 
            default value is ON.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        chargeDensity
            None or a Float specifying the density of the charge material. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        chargeMass
            None or a Float specifying the mass of the charge material. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        constantK1
            None or a Float specifying the charge material constant K. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        constantK2
            None or a Float specifying the charge material constant k. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        constantA
            None or a Float specifying the charge material constant A. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        constantB
            None or a Float specifying the charge material constant B. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        constantKc
            None or a Float specifying the charge material constant Kc. The default value is 
            None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        duration
            None or a Float specifying the time duration for the bubble simulation. The default 
            value is None.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        maximumSteps
            An Int specifying the maximum number of time steps for the bubble simulation. The 
            default value is 1500.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        relativeStepControl
            A Float specifying the relative step size control parameter. The default value is 
            1×10–11.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        absoluteStepControl
            A Float specifying the absolute step size control parameter. The default value is 
            1×10–11.This argument is valid only when *definition*=SPHERICAL and 
            *propagationModel*=UNDEX_CHARGE. 
        stepControlExponent
            A Float specifying the step size control exponent. The default value is 0.2.This 
            argument is valid only when *definition*=SPHERICAL and *propagationModel*=UNDEX_CHARGE. 
        genDecayA
            A Float specifying the constant A associated with the generalized decay propagation 
            model. The default value is 0.0.This argument is valid only when *definition*=SPHERICAL 
            and *propagationModel*=GENERALIZED_DECAY. 
        genDecayB
            A Float specifying the constant B associated with the generalized decay propagation 
            model. The default value is 0.0.This argument is valid only when *definition*=SPHERICAL 
            and *propagationModel*=GENERALIZED_DECAY. 
        genDecayC
            A Float specifying the constant C associated with the generalized decay propagation 
            model. The default value is 0.0.This argument is valid only when *definition*=SPHERICAL 
            and *propagationModel*=GENERALIZED_DECAY. 
        seedNumber
            An Int specifying the seed number (N) for the diffuse source calculation. N2 sources 
            will be used in the simulation.This argument is valid only when *definition*=DIFFUSE. 
        massTNT
            A Float specifying the equivalent mass of TNT, in any preferred mass unit.This argument 
            is valid only when *definition*=AIR_BLAST or *definition*=SURFACE_BLAST. 
        massFactor
            A Float specifying the multiplication factor to convert from the preferred mass unit to 
            kilograms. The default value is 1.0.This argument is valid only when 
            *definition*=AIR_BLAST or *definition*=SURFACE_BLAST. 
        lengthFactor
            A Float specifying the multiplication factor to convert from the analysis length unit to 
            meters. The default value is 1.0.This argument is valid only when *definition*=AIR_BLAST 
            or *definition*=SURFACE_BLAST. 
        timeFactor
            A Float specifying the multiplication factor to convert from the analysis time unit to 
            seconds. The default value is 1.0.This argument is valid only when 
            *definition*=AIR_BLAST or *definition*=SURFACE_BLAST. 
        pressureFactor
            A Float specifying the multiplication factor to convert from the analysis pressure unit 
            to pascals. The default value is 1.0.This argument is valid only when 
            *definition*=AIR_BLAST or *definition*=SURFACE_BLAST. 

        Returns
        -------
            An IncidentWaveProperty object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = IncidentWaveProperty(name, definition, propagationModel, soundSpeed,
                                                                     fluidDensity, specificHeatRatio, gravity,
                                                                     atmosphericPressure, dragCoefficient, dragExponent,
                                                                     waveEffects, chargeDensity, chargeMass, constantK1,
                                                                     constantK2, constantA, constantB, constantKc,
                                                                     duration, maximumSteps, relativeStepControl,
                                                                     absoluteStepControl, stepControlExponent,
                                                                     genDecayA, genDecayB, genDecayC, seedNumber,
                                                                     massTNT, massFactor, lengthFactor, timeFactor,
                                                                     pressureFactor)
        return interaction

    def ModelChange(self, name: str, createStepName: str, isRestart: Boolean = OFF,
                    regionType: SymbolicConstant = GEOMETRY, region: Region = Region(),
                    activeInStep: Boolean = OFF, includeStrain: Boolean = OFF) -> ModelChange:
        """This method creates a ModelChange object.

        Path
        ----
            - mdb.models[name].ModelChange

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the ModelChange object is created. 
        isRestart
            A Boolean specifying whether this interaction is being used solely to indicate that 
            model change may be required in a subsequent restart analysis (either for elements or 
            contact pairs). The default value is OFF. 
        regionType
            A SymbolicConstant specifying the region selection type. This argument is valid only 
            when *isRestart*=False. Possible values are GEOMETRY, SKINS, STRINGERS, and ELEMENTS. 
            The default value is GEOMETRY. 
        region
            A Region object specifying the elements to be removed or reactivated. This argument is 
            valid only when *isRestart*=False. 
        activeInStep
            A Boolean specifying whether elements are being removed or reactivated. This argument is 
            valid only when *isRestart*=False. The default value is OFF. 
        includeStrain
            A Boolean specifying whether stress/displacement elements are reactivated with strain. 
            This argument is valid only when *isRestart*=False and when *activeInStep*=True. The 
            default value is OFF. 

        Returns
        -------
            A ModelChange object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = ModelChange(name, createStepName, isRestart, regionType, region,
                                                            activeInStep, includeStrain)
        return interaction

    def PressurePenetration(self, name: str, createStepName: str, contactInteraction: str, mainPoints: RegionArray,
                            secondaryPoints: RegionArray, penetrationPressure: float, criticalPressure: float,
                            amplitude: str = UNSET, penetrationTime: float = 0) -> PressurePenetration:
        """This method creates a PressurePenetration object.

        Path
        ----
            - mdb.models[name].PressurePenetration

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the PressurePenetration object is 
            created. 
        contactInteraction
            A String specifying the name of the Surface-to-surface contact (Standard) interaction. 
        mainPoints
            A RegionArray object specifying the points on the main surface that are exposed to the 
            fluid. 
        secondaryPoints
            A RegionArray object specifying the points on the secondary surface that are exposed to 
            the fluid. 
        penetrationPressure
            A tuple of Floats specifying the fluid pressure magnitude. For steady state dynamic 
            analyses, a tuple of Complexes specifying the fluid pressure magnitude. 
        criticalPressure
            A tuple of Floats specifying the critical contact pressure below which fluid penetration 
            starts to occur. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        penetrationTime
            A Float specifying the fraction of the current step time over which the fluid pressure 
            on newly penetrated contact surface segments is ramped up to the current magnitude. The 
            default value is 0.001. 

        Returns
        -------
            A PressurePenetration object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = PressurePenetration(name, createStepName, contactInteraction,
                                                                    mainPoints, secondaryPoints, penetrationPressure,
                                                                    criticalPressure, amplitude, penetrationTime)
        return interaction

    def RadiationToAmbient(self, name: str, createStepName: str, surface: Region, emissivity: float, field: str = '',
                           distributionType: SymbolicConstant = UNIFORM, radiationType: SymbolicConstant = AMBIENT,
                           ambientTemperature: float = 0, ambientTemperatureAmp: str = '') -> RadiationToAmbient:
        """This method creates a RadiationToAmbient object.

        Path
        ----
            - mdb.models[name].RadiationToAmbient

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the RadiationToAmbient object is 
            created. 
        surface
            A Region object specifying the surface to which the radiation interaction is applied. 
        emissivity
            A Float specifying the emissivity, ϵϵ. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *distributionType*=ANALYTICAL_FIELD. 
            The default value is an empty string. 
        distributionType
            A SymbolicConstant specifying how the radiation is distributed. This argument applies 
            only when *radiationType*=AMBIENT. Possible values are UNIFORM and ANALYTICAL_FIELD. The 
            default value is UNIFORM. 
        radiationType
            A SymbolicConstant specifying whether to use the default surface radiation behavior, or 
            the cavity radiation approximation. Possible values are AMBIENT and CAVITY. The default 
            value is AMBIENT. 
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0. This argument applies only 
            when *radiationType*=AMBIENT. The default value is 0.0. 
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the 
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify 
            that the reference ambient temperature is applied immediately at the beginning of the 
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that 
            the reference ambient temperature is applied throughout the step. This argument applies 
            only when *radiationType*=AMBIENT. 

        Returns
        -------
            A RadiationToAmbient object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = RadiationToAmbient(name, createStepName, surface, emissivity, field,
                                                                   distributionType, radiationType, ambientTemperature,
                                                                   ambientTemperatureAmp)
        return interaction

    def SelfContactExp(self, name: str, createStepName: str, surface: Region, interactionProperty: str,
                       mechanicalConstraint: SymbolicConstant = KINEMATIC, contactControls: str = '') -> SelfContactExp:
        """This method creates a SelfContactExp object.

        Path
        ----
            - mdb.models[name].SelfContactExp

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the SelfContactExp object is created. 
        surface
            A Region object specifying the surface where self-contact is defined. 
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this 
            interaction. 
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are 
            KINEMATIC and PENALTY. The default value is KINEMATIC. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 

        Returns
        -------
            A SelfContactExp object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = SelfContactExp(name, createStepName, surface, interactionProperty,
                                                               mechanicalConstraint, contactControls)
        return interaction

    def SelfContactStd(self, name: str, createStepName: str, surface: Region, interactionProperty: str,
                       enforcement: SymbolicConstant = SURFACE_TO_SURFACE, thickness: Boolean = ON,
                       smooth: float = 0, contactControls: str = '') -> SelfContactStd:
        """This method creates a SelfContactStd object.

        Path
        ----
            - mdb.models[name].SelfContactStd

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the SelfContactStd object is created. 
        surface
            A Region object specifying the surface where self-contact is defined. 
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this 
            interaction. 
        enforcement
            A SymbolicConstant specifying the discretization method. Possible values are 
            NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE. 
        thickness
            A Boolean specifying whether shell/membrane element thickness is considered. The default 
            value is ON.This argument in valid only when *enforcement*=SURFACE_TO_SURFACE. 
        smooth
            A Float specifying the degree of smoothing used for deformable or rigid main surfaces 
            involved when *enforcement*=NODE_TO_SURFACE. The value given must lie between 0.0 and 
            0.5. The default value is 0.2. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 

        Returns
        -------
            A SelfContactStd object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = SelfContactStd(name, createStepName, surface, interactionProperty,
                                                               enforcement, thickness, smooth, contactControls)
        return interaction

    def StdContactControl(self, name: str, stiffnessScaleFactor: float = 1,
                          penetrationTolChoice: SymbolicConstant = RELATIVE,
                          relativePenetrationTolerance: float = None, absolutePenetrationTolerance: float = None,
                          frictionOnset: SymbolicConstant = None, automaticTolerances: Boolean = OFF,
                          maxchp: int = 0, perrmx: float = 0, uerrmx: float = 0,
                          stabilizeChoice: SymbolicConstant = NONE, dampFactor: float = 1, dampCoef: float = 0,
                          tangFraction: float = 1, eosFraction: float = 0,
                          zeroDampingChoice: SymbolicConstant = COMPUTE, zeroDamping: float = None,
                          enforceWithLagrangeMultipliers: SymbolicConstant = DEFAULT) -> StdContactControl:
        """This method creates an StdContactControl object.

        Path
        ----
            - mdb.models[name].StdContactControl

        Parameters
        ----------
        name
            A String specifying the contact controls repository key. 
        stiffnessScaleFactor
            A Float specifying the factor by which Abaqus/Standard will scale the default penalty 
            stiffness to obtain the stiffnesses used for the contact pairs. Only contact 
            interactions defined with augmented Lagrangian surface behavior will be affected by this 
            argument. The default value is 1.0. 
        penetrationTolChoice
            A SymbolicConstant specifying whether the allowable penetration is an absolute value or 
            a value relative to the characteristic contact surface face dimension. Only contact 
            interactions defined with augmented Lagrangian surface behavior will be affected by this 
            argument. Possible values are RELATIVE and ABSOLUTE. The default value is RELATIVE. 
        relativePenetrationTolerance
            A Float specifying the ratio of the allowable penetration to the characteristic contact 
            surface face dimension. The float values represent percentages (e.g.: 0.001=0.1%). Only 
            contact interactions defined with augmented Lagrangian surface behavior will be affected 
            by this argument. The default value is 10–3.The *relativePenetrationTolerance* argument 
            applies only when *penetrationTolChoice*=RELATIVE. The *relativePenetrationTolerance* 
            and *absolutePenetrationTolerance* arguments are mutually exclusive. 
        absolutePenetrationTolerance
            None or a Float specifying the allowable penetration. Only contact interactions defined 
            with augmented Lagrangian surface behavior will be affected by this argument. The 
            *absolutePenetrationTolerance* argument applies only when 
            *penetrationTolChoice*=ABSOLUTE. The *relativePenetrationTolerance* and 
            *absolutePenetrationTolerance* arguments are mutually exclusive. The default value is 
            None. 
        frictionOnset
            A SymbolicConstant specifying when the application of friction occurs. Possible values 
            are: 
            - IMMEDIATE, specifying the friction is included in the increment when contact occurs. 
            - DELAYED, specifying the application of friction is delayed until the increment after 
            contact occurs. 
        automaticTolerances
            A Boolean specifying whether Abaqus/Standard should automatically compute an overclosure 
            tolerance and a separation tolerance to prevent chattering in contact. The default value 
            is OFF.The *automaticTolerances* argument cannot be used with the *maxchp*, *perrmx*, 
            and *uerrmx* arguments. 
        maxchp
            An Int specifying the maximum number of points that are permitted to violate contact 
            conditions in any increment. The default value is 0.Either the *perrmx* or the *uerrmx* 
            argument must be specified in conjunction with the *maxchp* argument. 
        perrmx
            A Float specifying the maximum value of tensile stress (tensile force in GAP- or 
            ITT-type contact elements) allowed to be transmitted at a contact point. The default 
            value is 0.0.The *perrmx* argument must be specified in conjunction with the *maxchp* 
            argument. 
        uerrmx
            A Float specifying the maximum overclosure distance allowed at a secondary node that is 
            considered to be open. The default value is 0.0.The *uerrmx* argument must be specified 
            in conjunction with the *maxchp* argument. 
        stabilizeChoice
            A SymbolicConstant specifying whether or not viscous damping will be specified, and if 
            so, how it will be specified. Possible values are NONE, AUTOMATIC, and COEFFICIENT. The 
            default value is NONE. 
        dampFactor
            A Float specifying the value of the damping factor. This value is multiplied by the 
            calculated damping coefficient. The default value is 1.0.This argument is only valid 
            when *stabilizeChoice*=AUTOMATIC. 
        dampCoef
            A Float specifying the damping coefficient. The default value is 0.0.This argument is 
            only valid when *stabilizeChoice*=COEFFICIENT. 
        tangFraction
            A Float specifying the tangential stabilization as a fraction of the normal 
            stabilization (damping). The default value is 1.0.This argument is valid only if 
            *stabilizeChoice* = AUTOMATIC or COEFFICIENT. 
        eosFraction
            A Float specifying the fraction of the damping that remains at the end of the step. The 
            default value is 0.0.This argument is valid only if *stabilizeChoice* = AUTOMATIC or 
            COEFFICIENT. 
        zeroDampingChoice
            A SymbolicConstant specifying how the zero-damping clearance will be specified. Possible 
            values are COMPUTE and SPECIFY. The default value is COMPUTE.This argument is valid only 
            if *stabilizeChoice* = AUTOMATIC or COEFFICIENT. 
        zeroDamping
            None or a Float specifying the clearance at which damping becomes zero. This argument is 
            valid only when *zeroDampingChoice*=SPECIFY. This argument is valid only if 
            *stabilizeChoice* = AUTOMATIC or COEFFICIENT. The default value is None. 
        enforceWithLagrangeMultipliers
            A SymbolicConstant specifying whether to enforce the contact constraints with Lagrange 
            multipliers. Possible values are DEFAULT, ENFORCEMENT_OFF, and ENFORCEMENT_ON. The 
            default value is DEFAULT. 

        Returns
        -------
            A StdContactControl object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.interactions[name] = interaction = StdContactControl(name, stiffnessScaleFactor, penetrationTolChoice,
                                                                  relativePenetrationTolerance,
                                                                  absolutePenetrationTolerance, frictionOnset,
                                                                  automaticTolerances, maxchp, perrmx, uerrmx,
                                                                  stabilizeChoice, dampFactor, dampCoef, tangFraction,
                                                                  eosFraction, zeroDampingChoice, zeroDamping,
                                                                  enforceWithLagrangeMultipliers)
        return interaction

    def StdInitialization(self, name: str, overclosureType: SymbolicConstant = ADJUST,
                          interferenceDistance: float = None, clearanceDistance: float = None,
                          openingTolerance: float = None, overclosureTolerance: float = None) -> StdInitialization:
        """This method creates a StdInitialization object.

        Path
        ----
            - mdb.models[name].StdInitialization

        Parameters
        ----------
        name
            A String specifying the contact initialization repository key. 
        overclosureType
            A SymbolicConstant specifying the type of overclosure to be defined. Possible values are 
            ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST. 
        interferenceDistance
            None or a Float specifying the interference distance. This argument is valid only when 
            *overclosureType*=INTERFERENCE. The default value is None. 
        clearanceDistance
            None or a Float specifying the initial clearance distance. This argument is valid only 
            when *overclosureType*=CLEARANCE, and must be specified in that case. The default value 
            is None. 
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will 
            undergo strain-free adjustments. This argument is not valid when 
            *overclosureType*=INTERFERENCE unless a value has been specified for 
            *interferenceDistance*. The default value is None. 
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will 
            undergo strain-free adjustments.. The default value is None. 

        Returns
        -------
            A StdInitialization object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.interactions[name] = interaction = StdInitialization(name, overclosureType, interferenceDistance,
                                                                  clearanceDistance, openingTolerance,
                                                                  overclosureTolerance)
        return interaction

    def StdStabilization(self, name: str, zeroDistance: float = None, reductionFactor: float = 0,
                         scaleFactor: float = 1, tangentialFactor: float = 0, amplitude: str = '',
                         reset: Boolean = OFF) -> StdStabilization:
        """This method creates a StdStabilization object.

        Path
        ----
            - mdb.models[name].StdStabilization

        Parameters
        ----------
        name
            A String specifying the contact stabilization repository key. 
        zeroDistance
            None or a Float specifying the clearance distance at which the stabilization becomes 
            zero. The default value is None. 
        reductionFactor
            A Float specifying the factor by which the analysis will reduce the contact 
            stabilization coefficient per increment. The default value is 0.1. 
        scaleFactor
            A Float specifying the factor by which the analysis will scale the contact stabilization 
            coefficient. The default value is 1.0. 
        tangentialFactor
            A Float specifying the factor that scales the contact stabilization coefficient in the 
            tangential direction. The default value is 0.0. 
        amplitude
            A String specifying the name of the Amplitude object that defines a time-dependent scale 
            factor for contact stabilization over the step. The default value is an empty string. 
        reset
            A Boolean specifying whether to cancel carryover effects from contact stabilization 
            specifications involving nondefault amplitudes that appeared in previous steps. The 
            default value is OFF. 

        Returns
        -------
            A StdStabilization object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.interactions[name] = interaction = StdStabilization(name, zeroDistance, reductionFactor, scaleFactor,
                                                                 tangentialFactor, amplitude, reset)
        return interaction

    def StdXplCosimulation(self, name: str, createStepName: str, region: Region,
                           incrementation: SymbolicConstant = ALLOW_SUBCYCLING, stepSize: float = 0,
                           stepSizeDefinition: SymbolicConstant = DEFAULT) -> StdXplCosimulation:
        """This method creates a StdXplCosimulation object.

        Path
        ----
            - mdb.models[name].StdXplCosimulation

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the StdXplCosimulation object is 
            created. 
        region
            A Region object specifying the import and export region upon which the co-simulation 
            exchanges data with the coupled analysis program. 
        incrementation
            A SymbolicConstant specifying whether the analysis programs use the same time increments 
            or one is allowed to use more time increments than the other before exchanging data. 
            Possible values are ALLOW_SUBCYCLING and LOCKSTEP. The default value is 
            ALLOW_SUBCYCLING. 
        stepSize
            A Float specifying the size of the increments to be used by Abaqus/Standard and 
            Abaqus/Explicit. The default value is 0.0. 
        stepSizeDefinition
            A SymbolicConstant specifying whether the increment size is the analysis default or a 
            supplied variable. Possible values are DEFAULT and SPECIFIED. The default value is 
            DEFAULT. 

        Returns
        -------
            A StdXplCosimulation object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = StdXplCosimulation(name, createStepName, region, incrementation,
                                                                   stepSize, stepSizeDefinition)
        return interaction

    def SurfaceToSurfaceContactExp(self, name: str, createStepName: str, main: Region, secondary: Region,
                                   sliding: SymbolicConstant, interactionProperty: str,
                                   mechanicalConstraint: SymbolicConstant = KINEMATIC,
                                   weightingFactorType: SymbolicConstant = DEFAULT, weightingFactor: float = 0,
                                   contactControls: str = '',
                                   initialClearance: typing.Union[SymbolicConstant, float] = OMIT,
                                   halfThreadAngle: str = None, pitch: str = None,
                                   majorBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
                                   meanBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
                                   datumAxis: DatumAxis = DatumAxis(), useReverseDatumAxis: Boolean = OFF,
                                   clearanceRegion: Region = Region()) -> SurfaceToSurfaceContactExp:
        """This method creates a SurfaceToSurfaceContactExp object.

        Path
        ----
            - mdb.models[name].SurfaceToSurfaceContactExp

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the SurfaceToSurfaceContactExp object 
            is created. 
        main
            A Region object specifying the main surface. 
        secondary
            A Region object specifying the secondary surface. 
        sliding
            A SymbolicConstant specifying the contact formulation. Possible values are FINITE and 
            SMALL. 
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this 
            interaction. 
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are 
            KINEMATIC and PENALTY. The default value is KINEMATIC. 
        weightingFactorType
            A SymbolicConstant specifying the weighting for node-to-face contact. Possible values 
            are DEFAULT and SPECIFIED. The default value is DEFAULT. 
        weightingFactor
            A Float specifying the weighting factor for the contact surfaces when 
            *weightingFactorType*=SPECIFIED. The default value is 0.0. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 
        initialClearance
            A SymbolicConstant or a Float specifying the initial clearance at regions of contact. 
            Possible values are OMIT and COMPUTED. The default value is OMIT. 
        halfThreadAngle
            None or a sequence of Floats specifying the half thread angle used for bolt clearance. 
            The default value is None. 
        pitch
            None or a sequence of Floats specifying the pitch used for bolt clearance. The default 
            value is None. 
        majorBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used 
            for bolt clearance. The default value is COMPUTED. 
        meanBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used 
            for bolt clearance. The default value is COMPUTED. 
        datumAxis
            A DatumAxis object specifying the orientation of the bolt hole when specifying bolt 
            clearance. 
        useReverseDatumAxis
            A Boolean specifying whether to reverse the bolt clearance direction given by the datum 
            axis. The default value is OFF. 
        clearanceRegion
            A Region object specifying the contact region for which clearance is specified. 

        Returns
        -------
            A SurfaceToSurfaceContactExp object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = SurfaceToSurfaceContactExp(name, createStepName, main, secondary,
                                                                           sliding, interactionProperty,
                                                                           mechanicalConstraint, weightingFactorType,
                                                                           weightingFactor, contactControls,
                                                                           initialClearance, halfThreadAngle, pitch,
                                                                           majorBoltDiameter, meanBoltDiameter,
                                                                           datumAxis, useReverseDatumAxis,
                                                                           clearanceRegion)
        return interaction

    def SurfaceToSurfaceContactStd(self, name: str, createStepName: str, master: Region, slave: Region,
                                   sliding: SymbolicConstant, interactionProperty: str,
                                   interferenceType: SymbolicConstant = NONE, overclosure: float = 0,
                                   interferenceDirectionType: SymbolicConstant = COMPUTED, direction: tuple = (),
                                   amplitude: str = '', smooth: float = 0, hcrit: float = 0, extensionZone: float = 0,
                                   adjustMethod: SymbolicConstant = NONE, adjustTolerance: float = 0,
                                   adjustSet: Region = Region(), enforcement: SymbolicConstant = SURFACE_TO_SURFACE,
                                   thickness: Boolean = ON, contactControls: str = '', tied: Boolean = OFF,
                                   initialClearance: typing.Union[SymbolicConstant, float] = OMIT,
                                   halfThreadAngle: str = None, pitch: str = None,
                                   majorBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
                                   meanBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
                                   datumAxis: DatumAxis = DatumAxis(), useReverseDatumAxis: Boolean = OFF,
                                   clearanceRegion: Region = Region(), surfaceSmoothing: SymbolicConstant = NONE,
                                   bondingSet: Region = Region(), handedness: SymbolicConstant = RIGHT,
                                   normalAdjustment: SymbolicConstant = None) -> SurfaceToSurfaceContactStd:
        """This method creates a SurfaceToSurfaceContactStd object.

        Path
        ----
            - mdb.models[name].SurfaceToSurfaceContactStd

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the SurfaceToSurfaceContactStd object 
            is created. 
        master
            A Region object specifying the main surface. 
        slave
            A Region object specifying the secondary surface. 
        sliding
            A SymbolicConstant specifying the contact formulation. Possible values are FINITE and 
            SMALL. 
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this 
            interaction. 
        interferenceType
            A SymbolicConstant specifying the type of time-dependent allowable interference for 
            contact pairs and contact elements. Possible values are: 
            - NONE, specifying no allowable contact interference. 
            - SHRINK_FIT. 
            - UNIFORM. 
            The default value is NONE. 
        overclosure
            A Float specifying the maximum overclosure distance allowed. This argument applies only 
            when *interferenceType*=UNIFORM. The default value is 0.0. 
        interferenceDirectionType
            A SymbolicConstant specifying the method used to determine the interference direction. 
            Possible values are COMPUTED and DIRECTION_COSINE. The default value is COMPUTED. 
        direction
            A sequence of three Floats specifying the following: 
            - XX-direction cosine of the interference direction vector. 
            - YY-direction cosine of the interference direction vector. 
            - ZZ-direction cosine of the interference direction vector. 
            This argument is required only when *interferenceDirectionType*=DIRECTION_COSINE. 
        amplitude
            A String specifying the name of the amplitude curve that defines the magnitude of the 
            prescribed interference during the step. Use None to specify that the prescribed 
            interference is applied immediately at the beginning of the step and ramped down to zero 
            linearly over the step. 
        smooth
            A Float specifying the degree of smoothing used for deformable or rigid main surfaces 
            involved when *enforcement*=NODE_TO_SURFACE. The value given must lie between 0.0 and 
            0.5. The default value is 0.2. 
        hcrit
            A Float specifying the distance by which a secondary node must penetrate the main 
            surface before Abaqus/Standard abandons the current increment and tries again with a 
            smaller increment. The default value is 0.0. 
        extensionZone
            A Float specifying a fraction of the end segment or facet edge length by which the main 
            surface is to be extended to avoid numerical round-off errors associated with contact 
            modeling. The value given must lie between 0.0 and 0.2. The default value is 0.1. 
        adjustMethod
            A SymbolicConstant specifying the adjust method. Possible values are NONE, OVERCLOSED, 
            TOLERANCE, and SET. The default value is NONE. 
        adjustTolerance
            A Float specifying the adjust tolerance. The default value is 0.0. 
        adjustSet
            A Region object specifying the Set object to which the adjustment is to be applied. 
        enforcement
            A SymbolicConstant specifying the discretization method. Possible values are 
            NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE. 
        thickness
            A Boolean specifying whether shell/membrane element thickness is considered. The default 
            value is ON.This argument is not valid when *sliding*=FINITE and 
            *enforcement*=NODE_TO_SURFACE. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. The empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 
        tied
            A Boolean specifying whether the surfaces are to be "tied" together for the duration of 
            the simulation. The default value is OFF. 
        initialClearance
            A SymbolicConstant or a Float specifying the initial clearance at regions of contact. 
            Possible values are OMIT and COMPUTED. The default value is OMIT. 
        halfThreadAngle
            None or a sequence of Floats specifying the half thread angle used for bolt clearance. 
            The default value is None. 
        pitch
            None or a sequence of Floats specifying the pitch used for bolt clearance. The default 
            value is None. 
        majorBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used 
            for bolt clearance. The default value is COMPUTED. 
        meanBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used 
            for bolt clearance. The default value is COMPUTED. 
        datumAxis
            A DatumAxis object specifying the orientation of the bolt hole when specifying bolt 
            clearance. 
        useReverseDatumAxis
            A Boolean specifying whether to reverse the bolt clearance direction given by the datum 
            axis. The default value is OFF. 
        clearanceRegion
            A Region object specifying the contact region for which clearance is specified. 
        surfaceSmoothing
            A SymbolicConstant specifying whether to use surface smoothing for geometric surfaces in 
            SurfaceToSurfaceContactStd interactions. Possible values are AUTOMATIC and NONE. The 
            default value is NONE. 
        bondingSet
            A Region object specifying the secondary node sub-set for bonding, used only when the 
            contact property CohesiveBehavior option specifies use. 
        handedness
            A SymbolicConstant specifying the bolt handedness formulation. Possible values are RIGHT 
            and LEFT. The default value is RIGHT. 
        normalAdjustment
            A SymbolicConstant specifying the bolt normal adjustment formulation for all secondary 
            nodes. Possible values are UNIFORM AXIAL COMPONENT and LOCATION DEPENDENT. The default 
            value is UNIFORM AXIAL COMPONENT. 

        Returns
        -------
            A SurfaceToSurfaceContactStd object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = SurfaceToSurfaceContactStd(name, createStepName, master, slave, sliding,
                                                                           interactionProperty, interferenceType,
                                                                           overclosure, interferenceDirectionType,
                                                                           direction, amplitude, smooth, hcrit,
                                                                           extensionZone, adjustMethod, adjustTolerance,
                                                                           adjustSet, enforcement, thickness,
                                                                           contactControls, tied, initialClearance,
                                                                           halfThreadAngle, pitch, majorBoltDiameter,
                                                                           meanBoltDiameter, datumAxis,
                                                                           useReverseDatumAxis, clearanceRegion,
                                                                           surfaceSmoothing, bondingSet, handedness,
                                                                           normalAdjustment)
        return interaction

    def XFEMCrackGrowth(self, name: str, createStepName: str, crackName: str,
                        allowGrowth: Boolean = ON) -> XFEMCrackGrowth:
        """This method creates an XFEMCrackGrowth object.

        Path
        ----
            - mdb.models[name].XFEMCrackGrowth

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the XFEMCrackGrowth object is created. 
        crackName
            A String specifying the XFEMCrack object associated with this interaction. 
        allowGrowth
            A Boolean specifying whether the crack is allowed to grow (propagate) during this 
            analysis step. The default value is ON. 

        Returns
        -------
            A XFEMCrackGrowth object. 

        Exceptions
        ----------
            None. 
        """
        self.interactions[name] = interaction = XFEMCrackGrowth(name, createStepName, crackName, allowGrowth)
        return interaction

    def BodyCharge(self, name: str, createStepName: str, region: Region, magnitude: float,
                   amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM, field: str = '') -> BodyCharge:
        """This method creates a BodyCharge object.

        Path
        ----
            - mdb.models[name].BodyCharge

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 

        Returns
        -------
            A BodyCharge object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = BodyCharge(name, createStepName, region, magnitude, amplitude, distributionType,
                                             field)
        return load

    def BodyConcentrationFlux(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                              distributionType: SymbolicConstant = UNIFORM,
                              amplitude: str = UNSET) -> BodyConcentrationFlux:
        """This method creates a BodyConcentrationFlux object.

        Path
        ----
            - mdb.models[name].BodyConcentrationFlux

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the body concentration flux magnitude. *magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        distributionType
            A SymbolicConstant specifying how the body concentration flux is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A BodyConcentrationFlux object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = BodyConcentrationFlux(name, createStepName, region, magnitude, field,
                                                        distributionType, amplitude)
        return load

    def BodyCurrent(self, name: str, createStepName: str, region: Region, magnitude: float,
                    amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM,
                    field: str = '') -> BodyCurrent:
        """This method creates a BodyCurrent object.

        Path
        ----
            - mdb.models[name].BodyCurrent

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 

        Returns
        -------
            A BodyCurrent object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = BodyCurrent(name, createStepName, region, magnitude, amplitude, distributionType,
                                              field)
        return load

    def BodyCurrentDensity(self, name: str, createStepName: str, region: Region, comp1: str, comp2: str, comp3: str,
                           amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM) -> BodyCurrentDensity:
        """This method creates a BodyCurrentDensity object.

        Path
        ----
            - mdb.models[name].BodyCurrentDensity

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        comp1
            A Complex specifying the first component of the load. 
        comp2
            A Complex specifying the second component of the load. 
        comp3
            A Complex specifying the third component of the load. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and USER_DEFINED. The default value is UNIFORM. 

        Returns
        -------
            A BodyCurrentDensity object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = BodyCurrentDensity(name, createStepName, region, comp1, comp2, comp3, amplitude,
                                                     distributionType)
        return load

    def BodyForce(self, name: str, createStepName: str, region: Region, field: str = '',
                  distributionType: SymbolicConstant = UNIFORM, comp1: float = None, comp2: float = None,
                  comp3: float = None, amplitude: str = UNSET) -> BodyForce:
        """This method creates a BodyForce object.

        Path
        ----
            - mdb.models[name].BodyForce

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        comp1
            A Float or a Complex specifying the body force component in the 
            1-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least 
            one of them must be nonzero unless *distributionType*=USER_DEFINED. 
        comp2
            A Float or a Complex specifying the body force component in the 2-direction. 
        comp3
            A Float or a Complex specifying the body force component in the 3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A BodyForce object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = BodyForce(name, createStepName, region, field, distributionType, comp1, comp2, comp3,
                                            amplitude)
        return load

    def BodyHeatFlux(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                     distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET) -> BodyHeatFlux:
        """This method creates a BodyHeatFlux object.

        Path
        ----
            - mdb.models[name].BodyHeatFlux

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the body heat flux magnitude. *magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        distributionType
            A SymbolicConstant specifying how the body heat flux is distributed spatially. Possible 
            values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A BodyHeatFlux object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = BodyHeatFlux(name, createStepName, region, magnitude, field, distributionType,
                                               amplitude)
        return load

    def BoltLoad(self, name: str, createStepName: str, region: Region, magnitude: float,
                 boltMethod: SymbolicConstant = APPLY_FORCE, datumAxis: DatumAxis = DatumAxis(),
                 amplitude: str = UNSET, preTenSecPartLevel: Boolean = False) -> BoltLoad:
        """This method creates a BoltLoad object.

        Path
        ----
            - mdb.models[name].BoltLoad

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the bolt load magnitude. 
        boltMethod
            A SymbolicConstant specifying the method of applying the bolt load. Possible values are 
            APPLY_FORCE and ADJUST_LENGTH. The default value is APPLY_FORCE. 
        datumAxis
            A DatumAxis object specifying the orientation of the pre-tension section normal.Note: 
            *datumAxis* is applicable only for Solid and Shell regions; it has no meaning for Wire 
            regions. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        preTenSecPartLevel
            A Boolean specifying whether the pre-tension section is to be defined at the part level. 
            The default value is False. You should provide the *preTenSecPartLevel* argument only if 
            the selected region belongs to a dependent part instance. A pre-tension section cannot 
            be defined at the part level for independent and model instances. 

        Returns
        -------
            A BoltLoad object. 

        Exceptions
        ----------
            TextError. 
        """
        self.loads[name] = load = BoltLoad(name, createStepName, region, magnitude, boltMethod, datumAxis, amplitude,
                                           preTenSecPartLevel)
        return load

    def ConcCharge(self, name: str, createStepName: str, region: Region, magnitude: float,
                   distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET) -> ConcCharge:
        """This method creates a ConcCharge object.

        Path
        ----
            - mdb.models[name].ConcCharge

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A ConcCharge object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ConcCharge(name, createStepName, region, magnitude, distributionType, field,
                                             amplitude)
        return load

    def ConcConcFlux(self, name: str, createStepName: str, region: Region, magnitude: float,
                     distributionType: SymbolicConstant = UNIFORM, field: str = '',
                     amplitude: str = UNSET) -> ConcConcFlux:
        """This method creates a ConcConcFlux object.

        Path
        ----
            - mdb.models[name].ConcConcFlux

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A ConcConcFlux object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ConcConcFlux(name, createStepName, region, magnitude, distributionType, field,
                                               amplitude)
        return load

    def ConcCurrent(self, name: str, createStepName: str, region: Region, magnitude: float,
                    distributionType: SymbolicConstant = UNIFORM, field: str = '',
                    amplitude: str = UNSET) -> ConcCurrent:
        """This method creates a ConcCurrent object.

        Path
        ----
            - mdb.models[name].ConcCurrent

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A ConcCurrent object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ConcCurrent(name, createStepName, region, magnitude, distributionType, field,
                                              amplitude)
        return load

    def ConcentratedForce(self, name: str, createStepName: str, region: Region,
                          distributionType: SymbolicConstant = UNIFORM, field: str = '', cf1: float = None,
                          cf2: float = None, cf3: float = None, amplitude: str = UNSET, follower: Boolean = OFF,
                          localCsys: int = None) -> ConcentratedForce:
        """This method creates a ConcentratedForce object.

        Path
        ----
            - mdb.models[name].ConcentratedForce

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        cf1
            A Float or a Complex specifying the concentrated force component in the 1-direction. 
            Although *cf1*, *cf2*, and *cf3* are optional arguments, at least one of them must be 
            nonzero. 
        cf2
            A Float or a Complex specifying the concentrated force component in the 2-direction. 
        cf3
            A Float or a Complex specifying the concentrated force component in the 3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        follower
            A Boolean specifying whether the direction of the force rotates with the rotation at 
            each node of the region. You should provide the *follower* argument only if it is valid 
            for the specified step. The default value is OFF. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the load's degrees 
            of freedom. If *localCsys*=None, the degrees of freedom are defined in the global 
            coordinate system. When this member is queried, it returns an Int. The default value is 
            None. 

        Returns
        -------
            A ConcentratedForce object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ConcentratedForce(name, createStepName, region, distributionType, field, cf1, cf2,
                                                    cf3, amplitude, follower, localCsys)
        return load

    def ConcentratedHeatFlux(self, name: str, createStepName: str, region: Region, magnitude: float,
                             distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET,
                             dof: int = 11) -> ConcentratedHeatFlux:
        """This method creates a ConcentratedHeatFlux object.

        Path
        ----
            - mdb.models[name].ConcentratedHeatFlux

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        dof
            An Int specifying the degree of freedom of the node, to which the concentrated heat flux 
            should be applied. The default value is 11. 

        Returns
        -------
            A ConcentratedHeatFlux object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ConcentratedHeatFlux(name, createStepName, region, magnitude, distributionType, field,
                                                       amplitude, dof)
        return load

    def ConcPoreFluid(self, name: str, createStepName: str, region: Region, magnitude: float,
                      distributionType: SymbolicConstant = UNIFORM, field: str = '',
                      amplitude: str = UNSET) -> ConcPoreFluid:
        """This method creates a ConcPoreFluid object.

        Path
        ----
            - mdb.models[name].ConcPoreFluid

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A ConcPoreFluid object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ConcPoreFluid(name, createStepName, region, magnitude, distributionType, field,
                                                amplitude)
        return load

    def ConnectorForce(self, name: str, createStepName: str, region: str = '', fastenerName: str = '',
                       fastenerSetName: str = '', f1: float = None, f2: float = None, f3: float = None,
                       amplitude: str = UNSET) -> ConnectorForce:
        """This method creates a ConnectorForce object on a wire region. Alternatively, the load
        may also be applied to a wire set referenced from an assembled fastener template model.

        Path
        ----
            - mdb.models[name].ConnectorForce

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            The wire region to which the load is applied. This argument is not valid when 
            *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the load will be 
            applied. This argument is not valid when *region* is specified. When this argument is 
            specified, *fastenerSetName* must also be specified. The default value is an empty 
            string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the load will be 
            applied. This argument is not valid when *region* is specified. When this argument is 
            specified, *fastenerName* must also be specified. The default value is an empty string. 
        f1
            A Float or a Complex specifying the connector force component in the connector's local 
            1-direction.Note:Although *f1*, *f2*, and *f3* are optional arguments, at least one of 
            them must be nonzero. 
        f2
            A Float or a Complex specifying the connector force component in the connector's local 
            2-direction. 
        f3
            A Float or a Complex specifying the connector force component in the connector's local 
            3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A ConnectorForce object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ConnectorForce(name, createStepName, region, fastenerName, fastenerSetName, f1, f2,
                                                 f3, amplitude)
        return load

    def ConnectorMoment(self, name: str, createStepName: str, region: str = '', fastenerName: str = '',
                        fastenerSetName: str = '', m1: float = None, m2: float = None, m3: float = None,
                        amplitude: str = UNSET) -> ConnectorMoment:
        """This method creates a ConnectorMoment object on a wire region. Alternatively, the load
        may also be applied to a wire set referenced from an assembled fastener template model.

        Path
        ----
            - mdb.models[name].ConnectorMoment

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            The wire region to which the load is applied. This argument is not valid when 
            *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the load will be 
            applied. This argument is not valid when *region* is specified. When this argument is 
            specified, *fastenerSetName* must also be specified. The default value is an empty 
            string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the load will be 
            applied. This argument is not valid when *region* is specified. When this argument is 
            specified, *fastenerName* must also be specified. The default value is an empty string. 
        m1
            A Float or a Complex specifying the moment component in the connector's local 
            4-direction. 
        m2
            A Float or a Complex specifying the moment component in the connector's local 
            5-direction. 
        m3
            A Float or a Complex specifying the moment component in the connector's local 
            6-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A ConnectorMoment object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ConnectorMoment(name, createStepName, region, fastenerName, fastenerSetName, m1, m2,
                                                  m3, amplitude)
        return load

    def CoriolisForce(self, name: str, createStepName: str, region: Region, magnitude: float, point1: tuple,
                      point2: tuple, amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM,
                      field: str = '') -> CoriolisForce:
        """This method creates a CoriolisForce object.

        Path
        ----
            - mdb.models[name].CoriolisForce

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        point1
            A sequence of Floats specifying the first point on the axis of rotation for the load. 
        point2
            A sequence of Floats specifying the second point on the axis of rotation for the load. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 

        Returns
        -------
            A CoriolisForce object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = CoriolisForce(name, createStepName, region, magnitude, point1, point2, amplitude,
                                                distributionType, field)
        return load

    def Gravity(self, name: str, createStepName: str, distributionType: SymbolicConstant = UNIFORM,
                field: str = '', region: Region = Region(), comp1: float = None, comp2: float = None,
                comp3: float = None, amplitude: str = UNSET) -> Gravity:
        """This method creates a Gravity object.

        Path
        ----
            - mdb.models[name].Gravity

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        region
            A Region object specifying the region to which the load is applied. 
        comp1
            A Float or a Complex specifying the component of the load in the 
            1-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least 
            one of them must be nonzero. 
        comp2
            A Float or a Complex specifying the component of the load in the 2-direction. 
        comp3
            A Float or a Complex specifying the component of the load in the 3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A Gravity object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = Gravity(name, createStepName, distributionType, field, region, comp1, comp2, comp3,
                                          amplitude)
        return load

    def InertiaRelief(self, name: str, createStepName: str, u1: Boolean = OFF, u2: Boolean = OFF, u3: Boolean = OFF,
                      ur1: Boolean = OFF, ur2: Boolean = OFF, ur3: Boolean = OFF, referencePoint: tuple = (),
                      localCoordinates: int = None) -> InertiaRelief:
        """This method creates an InertiaRelief object.

        Path
        ----
            - mdb.models[name].InertiaRelief

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        u1
            A Boolean specifying the 1-direction as a free direction.Note:Although *u1*, *u2*, *u3*, 
            *ur1*, *ur2*, and *ur3* are optional arguments, at least one of them must be specified. 
            Further, any specified set of free directions cannot include only two rotational degrees 
            of freedom. 
        u2
            A Boolean specifying the 2-direction as a free direction. 
        u3
            A Boolean specifying the 3-direction as a free direction. 
        ur1
            A Boolean specifying the rotation about the 1–direction as a free direction. 
        ur2
            A Boolean specifying the rotation about the 2–direction as a free direction. 
        ur3
            A Boolean specifying the rotation about the 3–direction as a free direction. 
        referencePoint
            A sequence of Floats specifying the *X*, *Y* and *Z*-coordinates of a fixed rotation 
            point or a point on the rotation axis or a point on the symmetry line, about which 
            rotations are defined. Such a point must be specified only for certain combinations of 
            free directions. 
        localCoordinates
            None or a DatumCsys object specifying the local coordinate system of the rigid body 
            degrees of freedom for the inertia relief load. If *localCoordinates*=None, the free 
            directions are defined in the global coordinate system. When this member is queried, it 
            returns an Int. The default value is None. 

        Returns
        -------
            An InertiaRelief object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = InertiaRelief(name, createStepName, u1, u2, u3, ur1, ur2, ur3, referencePoint,
                                                localCoordinates)
        return load

    def InwardVolAccel(self, name: str, createStepName: str, region: Region, magnitude: float,
                       distributionType: SymbolicConstant = UNIFORM, field: str = '',
                       amplitude: str = UNSET) -> InwardVolAccel:
        """This method creates a InwardVolAccel object.

        Path
        ----
            - mdb.models[name].InwardVolAccel

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            name of the first analysis step. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            An InwardVolAccel object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = InwardVolAccel(name, createStepName, region, magnitude, distributionType, field,
                                                 amplitude)
        return load

    def LineLoad(self, name: str, createStepName: str, region: Region,
                 distributionType: SymbolicConstant = UNIFORM, field: str = '', comp1: float = None,
                 comp2: float = None, comp3: float = None, amplitude: str = UNSET,
                 system: SymbolicConstant = GLOBAL) -> LineLoad:
        """This method creates a LineLoad object.

        Path
        ----
            - mdb.models[name].LineLoad

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        comp1
            A Float or a Complex specifying the component of the load in the global or the beam 
            local 1-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at 
            least one of them must be nonzero unless *distributionType*=USER_DEFINED. 
        comp2
            A Float or a Complex specifying the component of the load in the global or the beam 
            local 2-direction. 
        comp3
            A Float or a Complex specifying the component of the load in the global 3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        system
            A SymbolicConstant specifying whether the load is applied in a global or the beam local 
            frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL. 

        Returns
        -------
            A LineLoad object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = LineLoad(name, createStepName, region, distributionType, field, comp1, comp2, comp3,
                                           amplitude, system)
        return load

    def LoadCase(self, name: str, boundaryConditions: tuple = (), loads: tuple = (),
                 includeActiveBaseStateBC: Boolean = ON) -> LoadCase:
        """This method creates a load case in a step.

        Path
        ----
            - mdb.models[name].steps[name].LoadCase

        Parameters
        ----------
        name
            A String specifying the name of the object. 
        boundaryConditions
            A sequence of (String, Float) sequences specifying the name of a BoundaryCondition 
            followed by a nonzero Float scaling factor. The default value is an empty sequence. 
        loads
            A sequence of (String, Float) sequences specifying the name of a Load followed by a 
            nonzero Float specifying a scale factor. The default value is an empty sequence. 
        includeActiveBaseStateBC
            A Boolean specifying whether to include all active boundary conditions propagated or 
            modified from the base state. The default value is ON. 

        Returns
        -------
            A LoadCase object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.loads[name] = load = LoadCase(name, boundaryConditions, loads, includeActiveBaseStateBC)
        return load

    def Moment(self, name: str, createStepName: str, region: Region, cm1: float = None, cm2: float = None,
               cm3: float = None, amplitude: str = UNSET, follower: Boolean = OFF,
               localCsys: int = None, distributionType: SymbolicConstant = UNIFORM, field: str = '') -> Moment:
        """This method creates a Moment object.

        Path
        ----
            - mdb.models[name].Moment

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        cm1
            A Float or a Complex specifying the load component in the 4-direction.Note:Although 
            *comp1*, *comp2*, and *comp3* are optional arguments, at least one of them must be 
            nonzero. 
        cm2
            A Float or a Complex specifying the load component in the 5- direction. 
        cm3
            A Float or a Complex specifying the load component in the 6-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        follower
            A Boolean specifying whether the direction of the force rotates with the rotation of the 
            node. You should provide the *follower* argument only if it is valid for the specified 
            step. The default value is OFF. 
        localCsys
            None or a DatumCsys object specifying the ID of the Datum coordinate system used as the 
            local coordinate system of the load. If *localCsys*=None, the load is defined in the 
            global coordinate system. When this member is queried, it returns an Int. The default 
            value is None. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 

        Returns
        -------
            A Moment object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = Moment(name, createStepName, region, cm1, cm2, cm3, amplitude, follower, localCsys,
                                         distributionType, field)
        return load

    def PEGLoad(self, name: str, createStepName: str, region: Region,
                distributionType: SymbolicConstant = UNIFORM, field: str = '', comp1: float = None,
                comp2: float = None, comp3: float = None, amplitude: str = UNSET) -> PEGLoad:
        """This method creates a PEGLoad object.

        Path
        ----
            - mdb.models[name].PEGLoad

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        comp1
            A Float or a Complex specifying the load component at dof 1 of reference node 
            1.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least one of 
            them must be nonzero. 
        comp2
            A Float or a Complex specifying the load component at dof 1 of reference node 2. 
        comp3
            A Float or a Complex specifying the load component at dof 2 of reference node 2. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A PEGLoad object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = PEGLoad(name, createStepName, region, distributionType, field, comp1, comp2, comp3,
                                          amplitude)
        return load

    def PipePressure(self, name: str, createStepName: str, region: Region, magnitude: float, diameter: float,
                     hZero: float, hReference: float, field: str = '', amplitude: str = UNSET,
                     distributionType: SymbolicConstant = UNIFORM, side: SymbolicConstant = INTERNAL) -> PipePressure:
        """This method creates a Pressure object.

        Path
        ----
            - mdb.models[name].PipePressure

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the pressure is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the pressure magnitude.Note:*magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        diameter
            A Float specifying the effective inner or outer diameter. 
        hZero
            A Float specifying the height of the zero pressure level when 
            *distributionType*=HYDROSTATIC. 
        hReference
            A Float specifying the height of the reference pressure level when 
            *distributionType*=HYDROSTATIC. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM, 
            HYDROSTATIC, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        side
            A SymbolicConstant specifying whether the pressure is applied internally or externally. 
            Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL. 

        Returns
        -------
            A PipePressure object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = PipePressure(name, createStepName, region, magnitude, diameter, hZero, hReference,
                                               field, amplitude, distributionType, side)
        return load

    def Pressure(self, name: str, createStepName: str, region: Region, magnitude: float = 0.0, hZero: float = 0.0,
                 hReference: float = 0.0, field: str = '', refPoint: str = '',
                 distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET) -> Pressure:
        """This method creates a Pressure object.

        Path
        ----
            - mdb.models[name].Pressure

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the pressure is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float or a Complex specifying the pressure magnitude.Note:*magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        hZero
            A Float specifying the height of the zero pressure level when 
            *distributionType*=HYDROSTATIC. 
        hReference
            A Float specifying the height of the reference pressure level when 
            *distributionType*=HYDROSTATIC. 
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated 
            with this load. The *field* argument applies only when *distributionType*=FIELD or 
            *distributionType*=DISCRETE_FIELD. The default value is an empty string. 
        refPoint
            A Region specifying the reference point from which the relative velocity is determined 
            when *distributionType*=STAGNATION or VISCOUS. 
        distributionType
            A SymbolicConstant specifying how the pressure is distributed spatially. Possible values 
            are UNIFORM, USER_DEFINED, FIELD, HYDROSTATIC, STAGNATION, VISCOUS, TOTAL_FORCE, and 
            DISCRETE_FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A Pressure object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = Pressure(name, createStepName, region, magnitude, hZero, hReference, field, refPoint,
                                           distributionType, amplitude)
        return load

    def RotationalBodyForce(self, name: str, createStepName: str, region: Region, magnitude: float, point1: tuple,
                            point2: tuple, distributionType: SymbolicConstant = UNIFORM, field: str = '',
                            centrifugal: Boolean = OFF, rotaryAcceleration: Boolean = OFF,
                            amplitude: str = UNSET) -> RotationalBodyForce:
        """This method creates a RotationalBodyForce object.

        Path
        ----
            - mdb.models[name].RotationalBodyForce

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        point1
            A sequence of Floats specifying the first point on the axis of rotation for the load. 
        point2
            A sequence of Floats specifying the second point on the axis of rotation for the load. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        centrifugal
            A Boolean specifying whether or not the effect of the load is centrifugal. The default 
            value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be 
            specified and only one must have the value ON. 
        rotaryAcceleration
            A Boolean specifying whether or not the effect of the load is rotary acceleration. The 
            default value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be 
            specified and only one must have the value ON. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A RotationalBodyForce object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = RotationalBodyForce(name, createStepName, region, magnitude, point1, point2,
                                                      distributionType, field, centrifugal, rotaryAcceleration,
                                                      amplitude)
        return load

    def ShellEdgeLoad(self, name: str, createStepName: str, region: Region, magnitude: float,
                      distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET,
                      angle: float = 0, axis: SymbolicConstant = AXIS_1, localCsys: int = GENERAL,
                      userCsys: str = GENERAL, directionVector: tuple = (), follower: Boolean = ON,
                      resultant: Boolean = OFF, traction: SymbolicConstant = NORMAL) -> ShellEdgeLoad:
        """This method creates a ShellEdgeLoad object.

        Path
        ----
            - mdb.models[name].ShellEdgeLoad

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float or Complex specifying the load magnitude. *magnitude* is optional if 
            *distributionType*=USER_DEFINED 
        distributionType
            A SymbolicConstant specifying how the shell edge load is distributed spatially. Possible 
            values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        angle
            A Float specifying an additional rotation of *directionVector* about an axis. The 
            default value is 0.This parameter is available only if *traction* is GENERAL. 
        axis
            A SymbolicConstant specifying the axis about which to apply an additional rotation of 
            *directionVector*. Possible values are AXIS_1, AXIS_2, AXIS_3. The default value is 
            AXIS_1.This parameter is available only if *traction* is GENERAL. 
        localCsys
            A DatumCsys object specifying the local coordinate system of the load's degrees of 
            freedom. The default value is None, indicating that the degrees of freedom are defined 
            in the global coordinate system or by the *userCsys* parameter if defined. This 
            parameter is available only if *traction* is GENERAL. When this member is queried, it 
            returns an Int. 
        userCsys
            A String specifying a CSYS defined by a user-subroutine. The default value is None, 
            indicating that the degrees of freedom are defined in the global coordinate system or by 
            the *localCsys* parameter if defined. This parameter is available only if *traction* is 
            GENERAL. 
        directionVector
            A tuple of two points specifying the direction of the load. Each point is specified as a 
            point region or a tuple of coordinates. If *traction* is SHEAR, then *directionVector* 
            will be projected onto the region surface. This parameter is available only if 
            *traction* is GENERAL. 
        follower
            A Boolean specifying whether the direction of the force changes with rotation. The 
            default value is ON. This parameter may be modified only if *traction* is GENERAL. You 
            should provide the *follower* argument only if it is valid for the specified step. 
        resultant
            A Boolean specifying whether to maintain a constant resultant force by defining traction 
            per unit undeformed area. If *resultant* is OFF, traction is defined per unit deformed 
            area. The default value is OFF. You should provide the *resultant* argument only if it 
            is valid for the specified step. 
        traction
            A SymbolicConstant specifying how to apply surface traction. Possible values are NORMAL, 
            TRANSVERSE, SHEAR, MOMENT and GENERAL. The default value is NORMAL. 

        Returns
        -------
            A ShellEdgeLoad object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = ShellEdgeLoad(name, createStepName, region, magnitude, distributionType, field,
                                                amplitude, angle, axis, localCsys, userCsys, directionVector, follower,
                                                resultant, traction)
        return load

    def SubmodelSB(self, name: str, createStepName: str, region: Region, globalStep: str,
                   globalDrivingRegion: str = '', absoluteExteriorTolerance: float = None,
                   exteriorTolerance: float = 0, globalIncrement: int = 0) -> SubmodelSB:
        """This method creates a SubmodelSB object.

        Path
        ----
            - mdb.models[name].SubmodelSB

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        globalStep
            A String specifying the step in the global model from which Abaqus reads the values of 
            the variables that will drive the submodel analysis. The String indicates the position 
            of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates 
            the first step. 
        globalDrivingRegion
            A String specifying the element set in the global model that will be searched for 
            elements whose responses will be used to drive the submodel. An empty string indicates 
            that the entire global model will be searched. The default value is an empty string. 
        absoluteExteriorTolerance
            None or a Float specifying the absolute value by which a driven node of the submodel can 
            lie outside the region of the elements of the global model. The default value is None. 
        exteriorTolerance
            None or a Float specifying the fraction of the average element size in the global model 
            by which a driven node of the submodel can lie outside the region of the elements of the 
            global model. The default value is 0.05. 
        globalIncrement
            An Int specifying the increment number in the global model step from which the solution 
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the 
            solution from the last increment will be used. The *globalIncrement* argument is 
            applicable only for linear perturbation steps. The default value is 0. 

        Returns
        -------
            A SubmodelSB object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SubmodelSB(name, createStepName, region, globalStep, globalDrivingRegion,
                                             absoluteExteriorTolerance, exteriorTolerance, globalIncrement)
        return load

    def SubstructureLoad(self, name: str, createStepName: str, region: Region, loadCaseNames: str, magnitude: float,
                         amplitude: str = UNSET) -> SubstructureLoad:
        """This method creates a SubstructureLoad object.

        Path
        ----
            - mdb.models[name].SubstructureLoad

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the substructure load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        loadCaseNames
            A list of names of the load cases that should be activated by this substructure load. 
        magnitude
            A Float specifying the multiplier for the load case magnitude. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A SubstructureLoad object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SubstructureLoad(name, createStepName, region, loadCaseNames, magnitude, amplitude)
        return load

    def SurfaceCharge(self, name: str, createStepName: str, region: Region, magnitude: float,
                      distributionType: SymbolicConstant = UNIFORM, field: str = '',
                      amplitude: str = UNSET) -> SurfaceCharge:
        """This method creates a SurfaceCharge object.

        Path
        ----
            - mdb.models[name].SurfaceCharge

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A SurfaceCharge object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SurfaceCharge(name, createStepName, region, magnitude, distributionType, field,
                                                amplitude)
        return load

    def SurfaceConcentrationFlux(self, name: str, createStepName: str, region: Region, magnitude: float,
                                 field: str = '',
                                 distributionType: SymbolicConstant = UNIFORM,
                                 amplitude: str = UNSET) -> SurfaceConcentrationFlux:
        """This method creates a SurfaceConcentrationFlux object.

        Path
        ----
            - mdb.models[name].SurfaceConcentrationFlux

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the surface concentration flux magnitude. *magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        distributionType
            A SymbolicConstant specifying how the surface concentration flux is distributed 
            spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is 
            UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A SurfaceConcentrationFlux object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SurfaceConcentrationFlux(name, createStepName, region, magnitude, field,
                                                           distributionType, amplitude)
        return load

    def SurfaceCurrent(self, name: str, createStepName: str, region: Region, magnitude: float,
                       distributionType: SymbolicConstant = UNIFORM, field: str = '',
                       amplitude: str = UNSET) -> SurfaceCurrent:
        """This method creates a SurfaceCurrent object.

        Path
        ----
            - mdb.models[name].SurfaceCurrent

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A SurfaceCurrent object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SurfaceCurrent(name, createStepName, region, magnitude, distributionType, field,
                                                 amplitude)
        return load

    def SurfaceCurrentDensity(self, name: str, createStepName: str, region: Region, comp1: str, comp2: str, comp3: str,
                              distributionType: SymbolicConstant = UNIFORM,
                              amplitude: str = UNSET) -> SurfaceCurrentDensity:
        """This method creates a SurfaceCurrentDensity object.

        Path
        ----
            - mdb.models[name].SurfaceCurrentDensity

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        comp1
            A Complex specifying the first component of the load. 
        comp2
            A Complex specifying the second component of the load. 
        comp3
            A Complex specifying the third component of the load. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and USER_DEFINED. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A SurfaceCurrentDensity object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SurfaceCurrentDensity(name, createStepName, region, comp1, comp2, comp3,
                                                        distributionType, amplitude)
        return load

    def SurfaceHeatFlux(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                        distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET) -> SurfaceHeatFlux:
        """This method creates a SurfaceHeatFlux object.

        Path
        ----
            - mdb.models[name].SurfaceHeatFlux

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the surface heat flux magnitude. *magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        distributionType
            A SymbolicConstant specifying how the surface heat flux is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A SurfaceHeatFlux object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SurfaceHeatFlux(name, createStepName, region, magnitude, field, distributionType,
                                                  amplitude)
        return load

    def SurfacePoreFluid(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                         distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET) -> SurfacePoreFluid:
        """This method creates a SurfacePoreFluid object.

        Path
        ----
            - mdb.models[name].SurfacePoreFluid

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the surface pore fluid flow magnitude. *magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM, 
            USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A SurfacePoreFluid object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SurfacePoreFluid(name, createStepName, region, magnitude, field, distributionType,
                                                   amplitude)
        return load

    def SurfaceTraction(self, name: str, createStepName: str, region: Region, magnitude: float,
                        distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET,
                        angle: float = 0, axis: SymbolicConstant = AXIS_1, localCsys: int = None,
                        userCsys: str = '', directionVector: tuple = (), follower: Boolean = ON,
                        resultant: Boolean = OFF, traction: SymbolicConstant = SHEAR) -> SurfaceTraction:
        """This method creates a SurfaceTraction object.

        Path
        ----
            - mdb.models[name].SurfaceTraction

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float or Complex specifying the load magnitude. *magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        distributionType
            A SymbolicConstant specifying how the surface traction is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        angle
            A Float specifying an additional rotation of *directionVector* about an axis. The 
            default value is 0.0. 
        axis
            A SymbolicConstant specifying the axis about which to apply an additional rotation of 
            *directionVector*. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is 
            AXIS_1. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the load's degrees 
            of freedom. If *localCsys*=None, the degrees of freedom are defined in the global 
            coordinate system or by the *userCsys* parameter if defined. When this member is 
            queried, it returns an Int. The default value is None. 
        userCsys
            A String specifying a CSYS defined by a user-subroutine. If *userCsys*=None, the degrees 
            of freedom are defined in the global coordinate system or by the *localCsys* parameter 
            if defined. The default value is "None". 
        directionVector
            A VertexArray object of length 2 specifying the direction of the load. Instead of 
            through a Vertex, each point may be specified through a tuple of coordinates. If 
            *traction* is SHEAR, then *directionVector* will be projected onto the region surface. 
            This parameter is available only if *traction* is GENERAL or SHEAR. 
        follower
            A Boolean specifying whether the direction of the force changes with rotation. The 
            default value is ON.This parameter may be modified only if *traction* is GENERAL. You 
            should provide the *follower* argument only if it is valid for the specified step. 
        resultant
            A Boolean specifying whether the to maintain a constant resultant force by defining 
            traction per unit undeformed area. If *resultant* is OFF, traction is defined per unit 
            deformed area. The default value is OFF.You should provide the *resultant* argument only 
            if it is valid for the specified step. 
        traction
            A SymbolicConstant specifying how to apply surface traction. Possible values are SHEAR 
            and GENERAL. The default value is SHEAR. 

        Returns
        -------
            A SurfaceTraction object. 

        Exceptions
        ----------
            None. 
        """
        self.loads[name] = load = SurfaceTraction(name, createStepName, region, magnitude, distributionType, field,
                                                  amplitude, angle, axis, localCsys, userCsys, directionVector,
                                                  follower, resultant, traction)
        return load

    def AnnealStep(self, name: str, previous: str, description: str = '', refTemp: float = None,
                   maintainAttributes: Boolean = False) -> AnnealStep:
        """This method creates an AnnealStep object.

        Path
        ----
            - mdb.models[name].AnnealStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        refTemp
            A Float specifying the post-anneal reference temperature. The default value is the 
            current temperature at all nodes in the model after the annealing has completed. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 

        Returns
        -------
            An AnnealStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = AnnealStep(name, previous, description, refTemp, maintainAttributes)
        return step

    def BuckleStep(self, name: str, previous: str, numEigen: int, description: str = '',
                   eigensolver: SymbolicConstant = SUBSPACE, minEigen: float = None,
                   maxEigen: float = None, vectors: int = None, maxIterations: int = 30,
                   blockSize: SymbolicConstant = DEFAULT, maxBlocks: SymbolicConstant = DEFAULT,
                   matrixStorage: SymbolicConstant = SOLVER_DEFAULT, maintainAttributes: Boolean = False) -> BuckleStep:
        """This method creates a BuckleStep object.

        Path
        ----
            - mdb.models[name].BuckleStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        numEigen
            An Int specifying the number of eigenvalues to be estimated. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        eigensolver
            A SymbolicConstant specifying the eigensolver. Possible values are SUBSPACE and LANCZOS. 
            The default value is SUBSPACE. 
        minEigen
            None or a Float specifying the minimum eigenvalue of interest. The default value is 
            None. 
        maxEigen
            None or a Float specifying the maximum eigenvalue of interest. The default value is 
            None. 
        vectors
            An Int specifying the number of vectors used in the iteration. The default value is the 
            minimum of (2*n*, *n* + 8), where *n* is the number of eigenvalues requested. 
        maxIterations
            An Int specifying the maximum number of iterations. The default value is 30. 
        blockSize
            The SymbolicConstant DEFAULT or an Int specifying the size of the Lanczos block steps. 
            The default value is DEFAULT. 
        maxBlocks
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of Lanczos block 
            steps within each Lanczos run. The default value is DEFAULT.Note:*minEigen*, 
            *blockSize*, and *maxBlocks* are ignored unless *eigensolver*=LANCZOS. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 

        Returns
        -------
            A BuckleStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = BuckleStep(name, previous, numEigen, description, eigensolver, minEigen, maxEigen,
                                             vectors, maxIterations, blockSize, maxBlocks, matrixStorage,
                                             maintainAttributes)
        return step

    def ComplexFrequencyStep(self, name: str, previous: str, numEigen: SymbolicConstant = ALL, description: str = '',
                             shift: float = None, frictionDamping: Boolean = OFF,
                             matrixStorage: SymbolicConstant = SOLVER_DEFAULT, maintainAttributes: Boolean = False,
                             minEigen: float = None, maxEigen: float = None,
                             propertyEvaluationFrequency: float = None) -> ComplexFrequencyStep:
        """This method creates a ComplexFrequencyStep object.

        Path
        ----
            - mdb.models[name].ComplexFrequencyStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        numEigen
            The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be 
            calculated or a SymbolicConstant ALL. The default value is ALL. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        shift
            None or a Float specifying the shift point in cycles per time. The default value is 
            None. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        minEigen
            None or a Float specifying the minimum frequency of interest in cycles per time. The 
            default value is None. 
        maxEigen
            None or a Float specifying the maximum frequency of interest in cycles per time. The 
            default value is None. 
        propertyEvaluationFrequency
            None or a Float specifying the frequency at which to evaluate frequency-dependent 
            properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. 
            If the value is None, the analysis product will evaluate the stiffness associated with 
            frequency-dependent springs and dashpots at zero frequency and will not consider the 
            stiffness contributions from frequency-domain viscoelasticity in the step. The default 
            value is None. 

        Returns
        -------
            A ComplexFrequencyStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = ComplexFrequencyStep(name, previous, numEigen, description, shift, frictionDamping,
                                                       matrixStorage, maintainAttributes, minEigen, maxEigen,
                                                       propertyEvaluationFrequency)
        return step

    def CoupledTempDisplacementStep(self, name: str, previous: str, description: str = '',
                                    response: SymbolicConstant = TRANSIENT,
                                    timePeriod: float = 1, nlgeom: Boolean = OFF,
                                    stabilizationMethod: SymbolicConstant = NONE, stabilizationMagnitude: float = None,
                                    timeIncrementationMethod: SymbolicConstant = AUTOMATIC, maxNumInc: int = 100,
                                    initialInc: float = None, minInc: float = None, maxInc: float = None,
                                    deltmx: float = 0,
                                    cetol: float = 0, creepIntegration: SymbolicConstant = IMPLICIT,
                                    solutionTechnique: SymbolicConstant = FULL_NEWTON,
                                    matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                                    amplitude: SymbolicConstant = STEP,
                                    extrapolation: SymbolicConstant = LINEAR, maintainAttributes: Boolean = False,
                                    convertSDI: SymbolicConstant = PROPAGATED, adaptiveDampingRatio: float = 0,
                                    continueDampingFactors: Boolean = OFF) -> CoupledTempDisplacementStep:
        """This method creates a CoupledTempDisplacementStep object.

        Path
        ----
            - mdb.models[name].CoupledTempDisplacementStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and 
            TRANSIENT. The default value is TRANSIENT. 
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0. 
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the 
            step. The default value is OFF. 
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE, 
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE. 
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the 
            problem is expected to be unstable and *stabilizationMethod*≠NONE. The default value is 
            2×10–4. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10−5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step. 
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a 
            transient analysis. The default value is 0.0. 
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from 
            the creep strain rates at the beginning and end of the increment. The default value is 
            0.0. 
        creepIntegration
            A SymbolicConstant specifying the type of integration to be used for creep and swelling 
            effects throughout the step. Possible values are IMPLICIT, EXPLICIT, and NONE. The 
            default value is IMPLICIT. 
        solutionTechnique
            A SymbolicConstant specifying the type of solution technique. Possible values are 
            FULL_NEWTON and SEPARATED. The default value is FULL_NEWTON. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. The default value is STEP. Possible values are STEP and RAMP. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total 
            strain energy and can be used only if *stabilizationMethod* is not NONE. The default 
            value is 0.05. 
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the 
            results of the preceding general step. This parameter must be used in conjunction with 
            the *adaptiveDampingRatio* parameter. The default value is OFF. 

        Returns
        -------
            A CoupledTempDisplacementStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = CoupledTempDisplacementStep(name, previous, description, response, timePeriod, nlgeom,
                                                              stabilizationMethod, stabilizationMagnitude,
                                                              timeIncrementationMethod, maxNumInc, initialInc, minInc,
                                                              maxInc, deltmx, cetol, creepIntegration,
                                                              solutionTechnique, matrixStorage, amplitude,
                                                              extrapolation, maintainAttributes, convertSDI,
                                                              adaptiveDampingRatio, continueDampingFactors)
        return step

    def CoupledThermalElectricalStructuralStep(self, name: str, previous: str, description: str = '',
                                               response: SymbolicConstant = TRANSIENT,
                                               timePeriod: float = 1, nlgeom: Boolean = OFF,
                                               stabilizationMethod: SymbolicConstant = NONE,
                                               stabilizationMagnitude: float = None,
                                               timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
                                               maxNumInc: int = 100,
                                               initialInc: float = None, minInc: float = None, maxInc: float = None,
                                               deltmx: float = 0,
                                               cetol: float = 0, creepIntegration: SymbolicConstant = IMPLICIT,
                                               matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                                               amplitude: SymbolicConstant = STEP,
                                               extrapolation: SymbolicConstant = LINEAR,
                                               maintainAttributes: Boolean = False,
                                               convertSDI: SymbolicConstant = PROPAGATED,
                                               adaptiveDampingRatio: float = 0,
                                               continueDampingFactors: Boolean = OFF) -> CoupledThermalElectricalStructuralStep:
        """This method creates a CoupledThermalElectricalStructuralStep object.

        Path
        ----
            - mdb.models[name].CoupledThermalElectricalStructuralStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and 
            TRANSIENT. The default value is TRANSIENT. 
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0. 
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the 
            step. The default value is OFF. 
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE, 
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE. 
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the 
            problem is expected to be unstable and *stabilizationMethod*≠NONE. The default value is 
            2×10–4. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10−5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step. 
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a 
            transient analysis. The default value is 0.0. 
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from 
            the creep strain rates at the beginning and end of the increment. The default value is 
            0.0. 
        creepIntegration
            A SymbolicConstant specifying the type of integration to be used for creep and swelling 
            effects throughout the step. Possible values are IMPLICIT, EXPLICIT, and NONE. The 
            default value is IMPLICIT. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. The default value is STEP. Possible values are STEP and RAMP. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total 
            strain energy and can be used only if *stabilizationMethod* is not NONE. The default 
            value is 0.05. 
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the 
            results of the preceding general step. This parameter must be used in conjunction with 
            the *adaptiveDampingRatio* parameter. The default value is OFF. 

        Returns
        -------
            A CoupledThermalElectricalStructuralStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = CoupledThermalElectricalStructuralStep(name, previous, description, response,
                                                                         timePeriod, nlgeom, stabilizationMethod,
                                                                         stabilizationMagnitude,
                                                                         timeIncrementationMethod, maxNumInc,
                                                                         initialInc, minInc, maxInc, deltmx, cetol,
                                                                         creepIntegration, matrixStorage, amplitude,
                                                                         extrapolation, maintainAttributes, convertSDI,
                                                                         adaptiveDampingRatio, continueDampingFactors)
        return step

    def CoupledThermalElectricStep(self, name: str, previous: str, description: str = '',
                                   response: SymbolicConstant = TRANSIENT,
                                   timePeriod: float = 1, timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
                                   maxNumInc: int = 100, initialInc: float = None, minInc: float = None,
                                   maxInc: float = None, end: SymbolicConstant = PERIOD, deltmx: float = 0,
                                   mxdem: float = 0, solutionTechnique: SymbolicConstant = FULL_NEWTON,
                                   matrixStorage: SymbolicConstant = SOLVER_DEFAULT, amplitude: SymbolicConstant = STEP,
                                   extrapolation: SymbolicConstant = LINEAR, maintainAttributes: Boolean = False,
                                   convertSDI: SymbolicConstant = PROPAGATED) -> CoupledThermalElectricStep:
        """This method creates a CoupledThermalElectricStep object.

        Path
        ----
            - mdb.models[name].CoupledThermalElectricStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and 
            TRANSIENT. The default value is TRANSIENT. 
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10−5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step. 
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis. 
            Possible values are PERIOD and SS. The default value is PERIOD. 
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment in a 
            transient analysis. The default value is 0.0. 
        mxdem
            A Float specifying the maximum allowable emissivity change with temperature and field 
            variables during an increment. The default value is 0.1. 
        solutionTechnique
            A SymbolicConstant specifying the type of solution technique. Possible values are 
            FULL_NEWTON and SEPARATED. The default value is FULL_NEWTON. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. The default value is STEP. Possible values are STEP and RAMP. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 

        Returns
        -------
            A CoupledThermalElectricStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = CoupledThermalElectricStep(name, previous, description, response, timePeriod,
                                                             timeIncrementationMethod, maxNumInc, initialInc, minInc,
                                                             maxInc, end, deltmx, mxdem, solutionTechnique,
                                                             matrixStorage, amplitude, extrapolation,
                                                             maintainAttributes, convertSDI)
        return step

    def DirectCyclicStep(self, name: str, previous: str, description: str = '', timePeriod: float = 1,
                         timeIncrementationMethod: SymbolicConstant = AUTOMATIC, maxNumInc: int = 100,
                         initialInc: float = None, minInc: float = None, maxInc: float = None,
                         maxNumIterations: int = 200, initialTerms: int = 11, maxTerms: int = 25,
                         termsIncrement: int = 5, deltmx: float = 0, cetol: float = 0, timePoints: str = NONE,
                         fatigue: Boolean = OFF, continueAnalysis: Boolean = OFF, minCycleInc: int = 100,
                         maxCycleInc: int = 1000, maxNumCycles: SymbolicConstant = DEFAULT,
                         damageExtrapolationTolerance: float = 1,
                         matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                         extrapolation: SymbolicConstant = LINEAR, maintainAttributes: Boolean = False,
                         convertSDI: SymbolicConstant = PROPAGATED) -> DirectCyclicStep:
        """This method creates a DirectCyclicStep object.

        Path
        ----
            - mdb.models[name].DirectCyclicStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        timePeriod
            A Float specifying the time of single loading cycle. The default value is 1.0. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10−5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step. 
        maxNumIterations
            An Int specifying the maximum number of iterations in a step. The default value is 200. 
        initialTerms
            An Int specifying the initial number of terms in the Fourier series. The default value 
            is 11. 
        maxTerms
            An Int specifying the maximum number of terms in the Fourier series. The default value 
            is 25. 
        termsIncrement
            An Int specifying the increment in number of terms in the Fourier series. The default 
            value is 5. 
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment. The 
            default value is 0.0. 
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from 
            the creep strain rates at the beginning and end of the increment. The default value is 
            0.0. 
        timePoints
            None or a String specifying a String specifying the name of a time point object used to 
            determine at which times the response of the structure will be evaluated. The default 
            value is NONE. 
        fatigue
            A Boolean specifying whether to include low-cycle fatigue analysis. The default value is 
            OFF. 
        continueAnalysis
            A Boolean specifying whether the displacement solution in the Fourier series obtained in 
            the previous direct cyclic step is used as the starting values for the current step. The 
            default value is OFF. 
        minCycleInc
            An Int specifying the minimum number of cycles over which the damage is extrapolated 
            forward. The default value is 100. 
        maxCycleInc
            An Int specifying the maximum number of cycles over which the damage is extrapolated 
            forward. The default value is 1000. 
        maxNumCycles
            The SymbolicConstant DEFAULT or an Int specifying the maximum number of cycles allowed 
            in a step or DEFAULT. A value of 1 plus half of the maximum number of cycles will be 
            used if DEFAULT is specified. The default value is DEFAULT. 
        damageExtrapolationTolerance
            A Float specifying the maximum extrapolated damage increment. The default value is 1.0. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 

        Returns
        -------
            A DirectCyclicStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = DirectCyclicStep(name, previous, description, timePeriod, timeIncrementationMethod,
                                                   maxNumInc, initialInc, minInc, maxInc, maxNumIterations,
                                                   initialTerms, maxTerms, termsIncrement, deltmx, cetol, timePoints,
                                                   fatigue, continueAnalysis, minCycleInc, maxCycleInc, maxNumCycles,
                                                   damageExtrapolationTolerance, matrixStorage, extrapolation,
                                                   maintainAttributes, convertSDI)
        return step

    def EmagTimeHarmonicStep(self, name: str, previous: str, frequencyRange: EmagTimeHarmonicFrequencyArray,
                             description: str = '', factorization: SymbolicConstant = COMPLEX) -> EmagTimeHarmonicStep:
        """This method creates a EmagTimeHarmonicStep object.

        Path
        ----
            - mdb.models[name].EmagTimeHarmonicStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        frequencyRange
            An EmagTimeHarmonicFrequencyArray object. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        factorization
            A SymbolicConstant specifying whether damping terms are to be ignored so that a real, 
            rather than a complex, system matrix is factored. Possible values are REAL_ONLY and 
            COMPLEX. The default value is COMPLEX. 

        Returns
        -------
            An EmagTimeHarmonicStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = EmagTimeHarmonicStep(name, previous, frequencyRange, description, factorization)
        return step

    def ExplicitDynamicsStep(self, name: str, previous: str, description: str = '', timePeriod: float = 1,
                             nlgeom: Boolean = ON, adiabatic: Boolean = OFF,
                             timeIncrementationMethod: SymbolicConstant = AUTOMATIC_GLOBAL,
                             maxIncrement: float = None, scaleFactor: float = 1,
                             massScaling: MassScalingArray = PREVIOUS_STEP, linearBulkViscosity: float = 0,
                             quadBulkViscosity: float = 1, userDefinedInc: float = None,
                             maintainAttributes: Boolean = False,
                             improvedDtMethod: Boolean = ON) -> ExplicitDynamicsStep:
        """This method creates an ExplicitDynamicsStep object.

        Path
        ----
            - mdb.models[name].ExplicitDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0. 
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the 
            step. The default value is ON. 
        adiabatic
            A Boolean specifying that an adiabatic stress analysis is to be performed. The default 
            value is OFF. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default 
            value is AUTOMATIC_GLOBAL. 
        maxIncrement
            None or a Float specifying the maximum time increment. If there is no upper limit, 
            *maxIncrement*=None. This argument is required only when 
            *timeIncrementationMethod*=AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None. 
        scaleFactor
            A Float specifying the factor that is used to scale the time increment. This argument is 
            required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or 
            FIXED_EBE. The default value is 1.0. 
        massScaling
            A MassScalingArray object specifying mass scaling controls. The default value is 
            PREVIOUS_STEP. 
        linearBulkViscosity
            A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06. 
        quadBulkViscosity
            A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is 
            1.2. 
        userDefinedInc
            None or a Float specifying the user-defined time increment. This argument is required 
            only when *timeIncrementationMethod*=FIXED_USER_DEFINED_INC. The default value is None. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        improvedDtMethod
            A Boolean specifying whether to use the "improved" (*improvedDtMethod*=ON) or 
            "conservative" (*improvedDtMethod*=OFF) method to estimate the element stable time 
            increment for three-dimensional continuum elements and elements with plane stress 
            formulations (shell, membrane, and two-dimensional plane stress elements). The default 
            value is ON. 

        Returns
        -------
            An ExplicitDynamicsStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = ExplicitDynamicsStep(name, previous, description, timePeriod, nlgeom, adiabatic,
                                                       timeIncrementationMethod, maxIncrement, scaleFactor, massScaling,
                                                       linearBulkViscosity, quadBulkViscosity, userDefinedInc,
                                                       maintainAttributes, improvedDtMethod)
        return step

    def FrequencyStep(self, name: str, previous: str, eigensolver: SymbolicConstant,
                      numEigen: SymbolicConstant = ALL, description: str = '', shift: float = 0,
                      minEigen: float = None, maxEigen: float = None, vectors: int = None,
                      maxIterations: int = 30, blockSize: SymbolicConstant = DEFAULT,
                      maxBlocks: SymbolicConstant = DEFAULT, normalization: SymbolicConstant = DISPLACEMENT,
                      propertyEvaluationFrequency: float = None, projectDamping: Boolean = ON,
                      acousticCoupling: SymbolicConstant = AC_ON, acousticRangeFactor: float = 1,
                      frictionDamping: Boolean = OFF, matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                      maintainAttributes: Boolean = False, simLinearDynamics: Boolean = OFF,
                      residualModes: Boolean = OFF, substructureCutoffMultiplier: float = 5,
                      firstCutoffMultiplier: float = 1, secondCutoffMultiplier: float = 1,
                      residualModeRegion: str = None, residualModeDof: str = None,
                      limitSavedEigenvectorRegion: SymbolicConstant = None) -> FrequencyStep:
        """This method creates a FrequencyStep object.

        Path
        ----
            - mdb.models[name].FrequencyStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        eigensolver
            A SymbolicConstant specifying the eigensolver. Possible values are LANCZOS, SUBSPACE, 
            and AMS.The following optional arguments are ignored unless *eigensolver*=LANCZOS: 
            *blockSize*, *maxBlocks*, *normalization*, *propertyEvaluationFrequency*.The following 
            optional arguments are ignored unless *eigensolver*=LANCZOS or AMS: *minEigen*, 
            *maxEigen*, and *acousticCoupling*.The following optional arguments are ignored unless 
            *eigensolver*=AMS: *projectDamping*, *acousticRangeFactor*, 
            *substructureCutoffMultiplier*, *firstCutoffMultiplier*, *secondCutoffMultiplier*, 
            *residualModeRegion*, *regionalModeDof*, and *limitSavedEigenvectorRegion*. 
        numEigen
            The SymbolicConstant ALL or an Int specifying the number of eigenvalues to be calculated 
            or ALL. The default value is ALL. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        shift
            A Float specifying the shift point in cycles per time. The default value is 0.0. 
        minEigen
            None or a Float specifying the minimum frequency of interest in cycles per time. The 
            default value is None. 
        maxEigen
            None or a Float specifying the maximum frequency of interest in cycles per time. The 
            default value is None. 
        vectors
            None or an Int specifying the number of vectors used in the iteration. The default is 
            the minimum of (2*n*, *n* + 8), where *n* is the number of eigenvalues requested. The 
            default value is None. 
        maxIterations
            An Int specifying the maximum number of iterations. The default value is 30. 
        blockSize
            A SymbolicConstant specifying the size of the Lanczos block steps. The default value is 
            DEFAULT. 
        maxBlocks
            A SymbolicConstant specifying the maximum number of Lanczos block steps within each 
            Lanczos run. The default value is DEFAULT. 
        normalization
            A SymbolicConstant specifying the method for normalizing eigenvectors. Possible values 
            are DISPLACEMENT and MASS. The default value is DISPLACEMENT.A value of DISPLACEMENT 
            indicates normalizing the eigenvectors so that the largest displacement entry in each 
            vector is unity. A value of MASS indicates normalizing the eigenvectors with respect to 
            the structure's mass matrix, which results in scaling the eigenvectors so that the 
            generalized mass for each vector is unity. 
        propertyEvaluationFrequency
            None or a Float specifying the frequency at which to evaluate frequency-dependent 
            properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. 
            If the value is None, the analysis product will evaluate the stiffness associated with 
            frequency-dependent springs and dashpots at zero frequency and will not consider the 
            stiffness contributions from frequency-domain viscoelasticity in the step. The default 
            value is None. 
        projectDamping
            A Boolean specifying whether to include projection of viscous and structural damping 
            operators during *AMS* eigenvalue extraction. Valid only when *eigenSolver*=AMS. The 
            default value is ON. 
        acousticCoupling
            A SymbolicConstant specifying the type of acoustic-structural coupling in models with 
            acoustic and structural elements coupled using the TIE option or in models with ASI-type 
            elements. Possible values are AC_ON, AC_OFF, and AC_PROJECTION. The default value is 
            AC_ON. 
        acousticRangeFactor
            A Float specifying the ratio of the maximum acoustic frequency to the maximum structural 
            frequency. The default value is 1.0. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        simLinearDynamics
            A Boolean specifying whether to activate the SIM-based linear dynamics procedures. The 
            default value is OFF. 
        residualModes
            A Boolean specifying whether to include residual modes from an immediately preceding 
            Static, Linear Perturbation step. The default value is OFF. 
        substructureCutoffMultiplier
            A Float specifying the cutoff frequency for substructure eigenproblems, defined as a 
            multiplier of the maximum frequency of interest. The default value is 5.0. 
        firstCutoffMultiplier
            A Float specifying the first cutoff frequency for a reduced eigenproblem, defined as a 
            multiplier of the maximum frequency of interest. The default value is 1.7. 
        secondCutoffMultiplier
            A Float specifying the second cutoff frequency for a reduced eigenproblem defined as a 
            multiplier of the maximum frequency of interest. The default value is 1.1. 
        residualModeRegion
            None or a sequence of Strings specifying the name of a region for which residual modes 
            are requested. The default value is None. 
        residualModeDof
            None or a sequence of Ints specifying the degree of freedom for which residual modes are 
            requested. The default value is None. 
        limitSavedEigenvectorRegion
            None or a Region object specifying a region for which eigenvectors should be saved or 
            the SymbolicConstant None representing the whole model. The default value is None. 

        Returns
        -------
            A FrequencyStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = FrequencyStep(name, previous, eigensolver, numEigen, description, shift, minEigen,
                                                maxEigen, vectors, maxIterations, blockSize, maxBlocks, normalization,
                                                propertyEvaluationFrequency, projectDamping, acousticCoupling,
                                                acousticRangeFactor, frictionDamping, matrixStorage, maintainAttributes,
                                                simLinearDynamics, residualModes, substructureCutoffMultiplier,
                                                firstCutoffMultiplier, secondCutoffMultiplier, residualModeRegion,
                                                residualModeDof, limitSavedEigenvectorRegion)
        return step

    def GeostaticStep(self, name: str, previous: str, description: str = '', nlgeom: Boolean = OFF,
                      matrixSolver: SymbolicConstant = DIRECT,
                      matrixStorage: SymbolicConstant = SOLVER_DEFAULT, maintainAttributes: Boolean = False,
                      solutionTechnique: SymbolicConstant = FULL_NEWTON, reformKernel: int = 8,
                      convertSDI: SymbolicConstant = PROPAGATED, utol: float = None, timePeriod: float = 1,
                      timeIncrementationMethod: SymbolicConstant = AUTOMATIC, maxNumInc: int = 100,
                      initialInc: float = None, minInc: float = None, maxInc: float = None) -> GeostaticStep:
        """This method creates a GeostaticStep object.

        Path
        ----
            - mdb.models[name].GeostaticStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the 
            step. The default value is OFF. 
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and 
            ITERATIVE. The default value is DIRECT. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations. 
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON. 
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix 
            is reformed.. The default value is 8. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 
        utol
            None or a Float specifying the tolerance for maximum change of displacements. The 
            default value is None. 
        timePeriod
            A Float specifying the total time period. The default value is 1.0.Note:This parameter 
            is ignored unless *timeIncrementationMethod*=AUTOMATIC. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step.Note:This parameter is ignored unless 
            *timeIncrementationMethod*=AUTOMATIC. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10−5 times the total time period.Note:This 
            parameter is ignored unless *timeIncrementationMethod*=AUTOMATIC. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step.Note:This parameter is ignored unless 
            *timeIncrementationMethod*=AUTOMATIC. 

        Returns
        -------
            A GeostaticStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = GeostaticStep(name, previous, description, nlgeom, matrixSolver, matrixStorage,
                                                maintainAttributes, solutionTechnique, reformKernel, convertSDI, utol,
                                                timePeriod, timeIncrementationMethod, maxNumInc, initialInc, minInc,
                                                maxInc)
        return step

    def HeatTransferStep(self, name: str, previous: str, description: str = '', response: SymbolicConstant = TRANSIENT,
                         timePeriod: float = 1, timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
                         maxNumInc: int = 100, initialInc: float = None, minInc: float = None,
                         maxInc: float = None, end: float = None, deltmx: float = 0, mxdem: float = 0,
                         amplitude: SymbolicConstant = STEP, extrapolation: SymbolicConstant = LINEAR,
                         matrixSolver: SymbolicConstant = DIRECT,
                         matrixStorage: SymbolicConstant = SOLVER_DEFAULT, maintainAttributes: Boolean = False,
                         solutionTechnique: SymbolicConstant = FULL_NEWTON, reformKernel: int = 8,
                         convertSDI: SymbolicConstant = PROPAGATED) -> HeatTransferStep:
        """This method creates a HeatTransferStep object.

        Path
        ----
            - mdb.models[name].HeatTransferStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and 
            TRANSIENT. The default value is TRANSIENT. 
        timePeriod
            A Float specifying the total time period. The default value is 1.0. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of 0.8 times the initial time increment or 10−5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step. 
        end
            None or a Float specifying the temperature change rate (temperature per time) used to 
            define steady state. When all nodal temperatures are changing at less than this rate, 
            the solution terminates. The default value is None.Note:This parameter is ignored unless 
            *response*=STEADY_STATE. 
        deltmx
            A Float specifying the maximum temperature change to be allowed in an increment during a 
            transient heat transfer analysis. The default value is 0.0. 
        mxdem
            A Float specifying the maximum allowable emissivity change with temperature and field 
            variables during an increment. The default value is 0.1. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. The default is STEP. Possible values are STEP and RAMP. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and 
            ITERATIVE. The default value is DIRECT. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations. 
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON. 
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix 
            is reformed.. The default value is 8. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 

        Returns
        -------
            A HeatTransferStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = HeatTransferStep(name, previous, description, response, timePeriod,
                                                   timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc, end,
                                                   deltmx, mxdem, amplitude, extrapolation, matrixSolver, matrixStorage,
                                                   maintainAttributes, solutionTechnique, reformKernel, convertSDI)
        return step

    def ImplicitDynamicsStep(self, name: str, previous: str, description: str = '', timePeriod: float = 1,
                             nlgeom: Boolean = OFF, matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                             application: SymbolicConstant = ANALYSIS_PRODUCT_DEFAULT, adiabatic: Boolean = OFF,
                             timeIncrementationMethod: SymbolicConstant = AUTOMATIC, maxNumInc: int = 100,
                             initialInc: float = None, minInc: float = None,
                             maxInc: typing.Union[SymbolicConstant, float] = DEFAULT,
                             hafTolMethod: SymbolicConstant = VALUE, haftol: float = None,
                             halfIncScaleFactor: float = None, nohaf: Boolean = OFF,
                             amplitude: SymbolicConstant = STEP,
                             alpha: typing.Union[SymbolicConstant, float] = DEFAULT,
                             initialConditions: SymbolicConstant = DEFAULT,
                             extrapolation: SymbolicConstant = ANALYSIS_PRODUCT_DEFAULT, noStop: Boolean = OFF,
                             maintainAttributes: Boolean = False, solutionTechnique: SymbolicConstant = FULL_NEWTON,
                             reformKernel: int = 8, convertSDI: SymbolicConstant = PROPAGATED) -> ImplicitDynamicsStep:
        """This method creates an ImplicitDynamicsStep object.

        Path
        ----
            - mdb.models[name].ImplicitDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        timePeriod
            A Float specifying the total time period of the step. The default value is 1.0. 
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the 
            step. The default value is based on the previous step. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        application
            A SymbolicConstant specifying the application type of the step. Possible values are 
            ANALYSIS_PRODUCT_DEFAULT, TRANSIENT_FIDELITY, MODERATE_DISSIPATION, and QUASI_STATIC. 
            The default value is ANALYSIS_PRODUCT_DEFAULT. 
        adiabatic
            A Boolean specifying whether an adiabatic stress analysis is to be performed. The 
            default value is OFF. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10−5 times the total time period. 
        maxInc
            The SymbolicConstant DEFAULT or a Float specifying the maximum time increment allowed. 
        hafTolMethod
            A SymbolicConstant specifying the way of specifying half-increment residual tolerance 
            with the automatic time incrementation scheme. Possible values are 
            ANALYSIS_PRODUCT_DEFAULT, VALUE, and SCALE. The default value is VALUE. 
        haftol
            None or a Float specifying the half-increment residual tolerance to be used with the 
            automatic time incrementation scheme. The default value is None. 
        halfIncScaleFactor
            None or a Float specifying the half-increment residual tolerance scale factor to be used 
            with the automatic time incrementation scheme. The default value is None. 
        nohaf
            A Boolean specifying whether to suppress calculation of the half-increment residual. The 
            default value is OFF. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. Possible values are STEP and RAMP. The default value is STEP. 
        alpha
            The SymbolicConstant DEFAULT or a Float specifying the nondefault value of the numerical 
            (artificial) damping control parameter, αα, in the implicit operator. Possible values 
            are −.333 <α<<α< 0. The default value is DEFAULT. 
        initialConditions
            A SymbolicConstant specifying whether accelerations should be calculated or recalculated 
            at the beginning of the step. Possible values are DEFAULT, BYPASS, and ALLOW. The 
            default value is DEFAULT. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, 
            PARABOLIC, VELOCITY_PARABOLIC, and ANALYSIS_PRODUCT_DEFAULT. The default value is 
            ANALYSIS_PRODUCT_DEFAULT. 
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum 
            number of iterations allowed have been completed, even if the equilibrium tolerances are 
            not satisfied. The default value is OFF.Warning:You should set *noStop*=OFF only in 
            special cases when you have a thorough understanding of how to interpret the results. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations. 
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON. 
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix 
            is reformed.. The default value is 8. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 

        Returns
        -------
            An ImplicitDynamicsStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = ImplicitDynamicsStep(name, previous, description, timePeriod, nlgeom, matrixStorage,
                                                       application, adiabatic, timeIncrementationMethod, maxNumInc,
                                                       initialInc, minInc, maxInc, hafTolMethod, haftol,
                                                       halfIncScaleFactor, nohaf, amplitude, alpha, initialConditions,
                                                       extrapolation, noStop, maintainAttributes, solutionTechnique,
                                                       reformKernel, convertSDI)
        return step

    def MassDiffusionStep(self, name: str, previous: str, description: str = '', response: SymbolicConstant = TRANSIENT,
                          timePeriod: float = 1, timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
                          maxNumInc: int = 100, initialInc: float = None, minInc: float = None,
                          maxInc: float = None, end: SymbolicConstant = PERIOD, dcmax: float = 0,
                          amplitude: SymbolicConstant = STEP, extrapolation: SymbolicConstant = LINEAR,
                          maintainAttributes: Boolean = False,
                          convertSDI: SymbolicConstant = PROPAGATED) -> MassDiffusionStep:
        """This method creates a MassDiffusionStep object.

        Path
        ----
            - mdb.models[name].MassDiffusionStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and 
            TRANSIENT. The default value is TRANSIENT. 
        timePeriod
            A Float specifying the total time period. The default value is 1.0. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of 0.8 times the initial time increment or 10−5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step. 
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis. 
            Possible values are PERIOD and SS. The default value is PERIOD. 
        dcmax
            A Float specifying the maximum normalized concentration change to be allowed in an 
            increment. The default value is 0.0. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. The default is STEP. Possible values are STEP and RAMP. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 

        Returns
        -------
            A MassDiffusionStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = MassDiffusionStep(name, previous, description, response, timePeriod,
                                                    timeIncrementationMethod, maxNumInc, initialInc, minInc, maxInc,
                                                    end, dcmax, amplitude, extrapolation, maintainAttributes,
                                                    convertSDI)
        return step

    def ModalDynamicsStep(self, name: str, previous: str, description: str = '', continueAnalysis: Boolean = OFF,
                          timePeriod: float = 1, incSize: float = 1,
                          directDamping: DirectDamping = DirectDamping(),
                          compositeDamping: CompositeDamping = CompositeDamping(),
                          rayleighDamping: RayleighDamping = RayleighDamping(),
                          amplitude: SymbolicConstant = STEP, maintainAttributes: Boolean = False,
                          directDampingByFrequency: DirectDampingByFrequency = DirectDampingByFrequency(),
                          rayleighDampingByFrequency: RayleighDampingByFrequency = RayleighDampingByFrequency()) -> ModalDynamicsStep:
        """This method creates a ModalDynamicsStep object.

        Path
        ----
            - mdb.models[name].ModalDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        continueAnalysis
            A Boolean specifying that the step starts with zero initial conditions. The default 
            value is OFF. 
        timePeriod
            A Float specifying the total time period. The default value is 1.0. 
        incSize
            A Float specifying the time increment to be used. The default value is 1.0. 
        directDamping
            A DirectDamping object. 
        compositeDamping
            A CompositeDamping object. 
        rayleighDamping
            A RayleighDamping object. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. Possible values are STEP and RAMP. The default value is STEP. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        directDampingByFrequency
            A DirectDampingByFrequency object. 
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object. 

        Returns
        -------
            A ModalDynamicsStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = ModalDynamicsStep(name, previous, description, continueAnalysis, timePeriod, incSize,
                                                    directDamping, compositeDamping, rayleighDamping, amplitude,
                                                    maintainAttributes, directDampingByFrequency,
                                                    rayleighDampingByFrequency)
        return step

    def RandomResponseStep(self, name: str, previous: str, freq: RandomResponseFrequencyArray, description: str = '',
                           scale: SymbolicConstant = LOG, directDamping: DirectDamping = DirectDamping(),
                           compositeDamping: CompositeDamping = CompositeDamping(),
                           rayleighDamping: RayleighDamping = RayleighDamping(),
                           structuralDamping: StructuralDamping = StructuralDamping(),
                           directDampingByFrequency: DirectDampingByFrequency = DirectDampingByFrequency(),
                           rayleighDampingByFrequency: RayleighDampingByFrequency = RayleighDampingByFrequency(),
                           structuralDampingByFrequency: StructuralDampingByFrequency = StructuralDampingByFrequency(),
                           maintainAttributes: Boolean = False) -> RandomResponseStep:
        """This method creates a RandomResponseStep object.

        Path
        ----
            - mdb.models[name].RandomResponseStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        freq
            A RandomResponseFrequencyArray object specifying frequencies over ranges of modes. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        scale
            A SymbolicConstant specifying the frequency scale. Possible values are LINEAR and LOG. 
            The default value is LOG. 
        directDamping
            A DirectDamping object. 
        compositeDamping
            A CompositeDamping object. 
        rayleighDamping
            A RayleighDamping object. 
        structuralDamping
            A StructuralDamping object. 
        directDampingByFrequency
            A DirectDampingByFrequency object. 
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object. 
        structuralDampingByFrequency
            A StructuralDampingByFrequency object. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 

        Returns
        -------
            A RandomResponseStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = RandomResponseStep(name, previous, freq, description, scale, directDamping,
                                                     compositeDamping, rayleighDamping, structuralDamping,
                                                     directDampingByFrequency, rayleighDampingByFrequency,
                                                     structuralDampingByFrequency, maintainAttributes)
        return step

    def ResponseSpectrumStep(self, name: str, previous: str, components: ResponseSpectrumComponentArray,
                             description: str = '', comp: SymbolicConstant = SINGLE_DIRECTION,
                             sum: SymbolicConstant = ABS, directDamping: DirectDamping = DirectDamping(),
                             compositeDamping: CompositeDamping = CompositeDamping(),
                             rayleighDamping: RayleighDamping = RayleighDamping(),
                             directDampingByFrequency: DirectDampingByFrequency = DirectDampingByFrequency(),
                             rayleighDampingByFrequency: RayleighDampingByFrequency = RayleighDampingByFrequency(),
                             maintainAttributes: Boolean = False) -> ResponseSpectrumStep:
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
        self.steps[name] = step = ResponseSpectrumStep(name, previous, components, description, comp, sum,
                                                       directDamping, compositeDamping, rayleighDamping,
                                                       directDampingByFrequency, rayleighDampingByFrequency,
                                                       maintainAttributes)
        return step

    def SoilsStep(self, name: str, previous: str, description: str = '', response: SymbolicConstant = TRANSIENT,
                  timePeriod: float = 1, nlgeom: Boolean = OFF,
                  stabilizationMethod: SymbolicConstant = NONE, stabilizationMagnitude: float = None,
                  creep: Boolean = ON, timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
                  initialInc: float = None, minInc: float = None, maxInc: float = None,
                  maxNumInc: int = 100, end: SymbolicConstant = PERIOD, utol: float = None,
                  cetol: float = 0, amplitude: SymbolicConstant = STEP,
                  extrapolation: SymbolicConstant = LINEAR, matrixSolver: SymbolicConstant = DIRECT,
                  matrixStorage: SymbolicConstant = SOLVER_DEFAULT, maintainAttributes: Boolean = False,
                  solutionTechnique: SymbolicConstant = FULL_NEWTON, reformKernel: int = 8,
                  convertSDI: SymbolicConstant = PROPAGATED, adaptiveDampingRatio: float = 0,
                  continueDampingFactors: Boolean = OFF) -> SoilsStep:
        """This method creates a SoilsStep object.

        Path
        ----
            - mdb.models[name].SoilsStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        response
            A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and 
            TRANSIENT. The default value is TRANSIENT. 
        timePeriod
            A Float specifying the total time period. The default value is 1.0. 
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the 
            step. The default value is OFF. 
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE, 
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE. 
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the 
            problem is expected to be unstable, and *stabilizationMethod* is not NONE. The default 
            value is 2×10–4. 
        creep
            A Boolean specifying whether a creep response occurs during this step. The default value 
            is ON. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10−5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        end
            A SymbolicConstant specifying the time period to be analyzed in a transient analysis. 
            Possible values are PERIOD and SS. The default value is PERIOD. 
        utol
            None or a Float specifying the maximum pore pressure change permitted in any increment 
            (in pressure units) in a transient consolidation analysis. The default value is None. 
        cetol
            A Float specifying the maximum allowable difference in the creep strain increment 
            calculated from the creep strain rates at the beginning and end of the increment. The 
            default value is 0.0. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. The default value is STEP. Possible values are STEP and RAMP. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and 
            ITERATIVE. The default value is DIRECT. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations. 
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON. 
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix 
            is reformed.. The default value is 8. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total 
            strain energy and can be used only if *stabilizationMethod* is not NONE. The default 
            value is 0.05. 
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the 
            results of the preceding general step. This parameter must be used in conjunction with 
            the *adaptiveDampingRatio* parameter. The default value is OFF. 

        Returns
        -------
            A SoilsStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = SoilsStep(name, previous, description, response, timePeriod, nlgeom,
                                            stabilizationMethod, stabilizationMagnitude, creep,
                                            timeIncrementationMethod, initialInc, minInc, maxInc, maxNumInc, end, utol,
                                            cetol, amplitude, extrapolation, matrixSolver, matrixStorage,
                                            maintainAttributes, solutionTechnique, reformKernel, convertSDI,
                                            adaptiveDampingRatio, continueDampingFactors)
        return step

    def StaticLinearPerturbationStep(self, name: str, previous: str, description: str = '',
                                     matrixSolver: SymbolicConstant = DIRECT,
                                     matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                                     maintainAttributes: Boolean = False) -> StaticLinearPerturbationStep:
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
        self.steps[name] = step = StaticLinearPerturbationStep(name, previous, description, matrixSolver, matrixStorage,
                                                               maintainAttributes)
        return step

    def StaticRiksStep(self, name: str, previous: str, description: str = '', nlgeom: Boolean = OFF,
                       adiabatic: Boolean = OFF, maxLPF: float = None, nodeOn: Boolean = OFF,
                       maximumDisplacement: float = 0, dof: int = 0, region: Region = Region(),
                       timeIncrementationMethod: SymbolicConstant = AUTOMATIC, maxNumInc: int = 100,
                       totalArcLength: float = 1, initialArcInc: float = None, minArcInc: float = None,
                       maxArcInc: float = None, matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                       extrapolation: SymbolicConstant = LINEAR, fullyPlastic: str = '', noStop: Boolean = OFF,
                       maintainAttributes: Boolean = False, useLongTermSolution: Boolean = OFF,
                       convertSDI: SymbolicConstant = PROPAGATED) -> StaticRiksStep:
        """This method creates a StaticRiksStep object.

        Path
        ----
            - mdb.models[name].StaticRiksStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is 
            OFF. 
        adiabatic
            A Boolean specifying whether to perform an adiabatic stress analysis. The default value 
            is OFF. 
        maxLPF
            None or a Float specifying the maximum value of the load proportionality factor. The 
            default value is None. 
        nodeOn
            A Boolean specifying whether to monitor the finishing displacement value at a node. The 
            default value is OFF. 
        maximumDisplacement
            A Float specifying the value of the total displacement (or rotation) at the node and 
            degree of freedom that, if crossed during an increment, ends the step at the current 
            increment. This argument is required when *nodeOn*=ON. The default value is 0.0. 
        dof
            An Int specifying the degree of freedom being monitored. This argument is required when 
            *nodeOn*=ON. The default value is 0. 
        region
            A Region object specifying the vertex at which the finishing displacement value is being 
            monitored. This argument is required when *nodeOn*=ON. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        totalArcLength
            A Float specifying the total load proportionality factor associated with the load in 
            this step. The default value is 1.0. 
        initialArcInc
            A Float specifying the initial load proportionality factor. The default value is the 
            total load proportionality factor for the step. 
        minArcInc
            A Float specifying the minimum arc length increment allowed. The default value is the 
            smaller of the suggested initial load proportionality factor or 10−5 times the total 
            load proportionality factor for the step. 
        maxArcInc
            A Float specifying the maximum arc length increment allowed. The default value is the 
            total load proportionality factor for the step. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        fullyPlastic
            A String specifying the name of the region being monitored for fully plastic behavior. 
            The default value is an empty string. 
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum 
            number of iterations allowed have been completed, even if the equilibrium tolerances are 
            not satisfied. The default value is OFF.Warning:You should set *noStop*=ON only in 
            special cases when you have a thorough understanding of how to interpret the results. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        useLongTermSolution
            A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with 
            time-domain viscoelasticity or the long-term elastic-plastic solution for two-layer 
            viscoplasticity. The default value is OFF. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 

        Returns
        -------
            A StaticRiksStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = StaticRiksStep(name, previous, description, nlgeom, adiabatic, maxLPF, nodeOn,
                                                 maximumDisplacement, dof, region, timeIncrementationMethod, maxNumInc,
                                                 totalArcLength, initialArcInc, minArcInc, maxArcInc, matrixStorage,
                                                 extrapolation, fullyPlastic, noStop, maintainAttributes,
                                                 useLongTermSolution, convertSDI)
        return step

    def StaticStep(self, name: str, previous: str, description: str = '', timePeriod: float = 1,
                   nlgeom: Boolean = OFF, stabilizationMethod: SymbolicConstant = NONE,
                   stabilizationMagnitude: float = None, adiabatic: Boolean = OFF,
                   timeIncrementationMethod: SymbolicConstant = AUTOMATIC, maxNumInc: int = 100,
                   initialInc: float = None, minInc: float = None, maxInc: float = None,
                   matrixSolver: SymbolicConstant = DIRECT,
                   matrixStorage: SymbolicConstant = SOLVER_DEFAULT, amplitude: SymbolicConstant = RAMP,
                   extrapolation: SymbolicConstant = LINEAR, fullyPlastic: str = '', noStop: Boolean = OFF,
                   maintainAttributes: Boolean = False, useLongTermSolution: Boolean = OFF,
                   solutionTechnique: SymbolicConstant = FULL_NEWTON, reformKernel: int = 8,
                   convertSDI: SymbolicConstant = PROPAGATED, adaptiveDampingRatio: float = 0,
                   continueDampingFactors: Boolean = OFF) -> StaticStep:
        """This method creates a StaticStep object.

        Path
        ----
            - mdb.models[name].StaticStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        timePeriod
            A Float specifying the total time period. The default value is 1.0. 
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is 
            OFF. 
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE, 
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE. 
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the 
            problem is expected to be unstable, and *stabilizationMethod* is not NONE. The default 
            value is 2×10–4. 
        adiabatic
            A Boolean specifying whether to perform an adiabatic stress analysis. The default value 
            is OFF. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10–5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default value is the total 
            time period for the step. 
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and 
            ITERATIVE. The default value is DIRECT. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. Possible values are STEP and RAMP. The default value is RAMP. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        fullyPlastic
            A String specifying the region being monitored for fully plastic behavior. The default 
            value is an empty string. 
        noStop
            A Boolean specifying whether to accept the solution to an increment after the maximum 
            number of iterations allowed has been completed, even if the equilibrium tolerances are 
            not satisfied. The default value is OFF.Warning:You should set *noStop*=ON only in 
            special cases when you have a thorough understanding of how to interpret the results. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        useLongTermSolution
            A Boolean specifying wether to obtain the fully relaxed long-term elastic solution with 
            time-domain viscoelasticity or the long-term elastic-plastic solution for two-layer 
            viscoplasticity. The default value is OFF. 
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations. 
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON. 
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix 
            is reformed.. The default value is 8. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total 
            strain energy and can be used only if *stabilizationMethod* is not NONE. The default 
            value is 0.05. 
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the 
            results of the preceding general step. This parameter must be used in conjunction with 
            the *adaptiveDampingRatio* parameter. The default value is OFF. 

        Returns
        -------
            A StaticStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = StaticStep(name, previous, description, timePeriod, nlgeom, stabilizationMethod,
                                             stabilizationMagnitude, adiabatic, timeIncrementationMethod, maxNumInc,
                                             initialInc, minInc, maxInc, matrixSolver, matrixStorage, amplitude,
                                             extrapolation, fullyPlastic, noStop, maintainAttributes,
                                             useLongTermSolution, solutionTechnique, reformKernel, convertSDI,
                                             adaptiveDampingRatio, continueDampingFactors)
        return step

    def SteadyStateDirectStep(self, name: str, previous: str, frequencyRange: SteadyStateDirectFrequencyArray,
                              description: str = '', factorization: SymbolicConstant = COMPLEX,
                              scale: SymbolicConstant = LOGARITHMIC, matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                              maintainAttributes: Boolean = False, subdivideUsingEigenfrequencies: Boolean = OFF,
                              frictionDamping: Boolean = OFF) -> SteadyStateDirectStep:
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
        self.steps[name] = step = SteadyStateDirectStep(name, previous, frequencyRange, description, factorization,
                                                        scale, matrixStorage, maintainAttributes,
                                                        subdivideUsingEigenfrequencies, frictionDamping)
        return step

    def SteadyStateModalStep(self, name: str, previous: str, frequencyRange: SteadyStateModalFrequencyArray,
                             description: str = '', scale: SymbolicConstant = LOGARITHMIC,
                             directDamping: DirectDamping = DirectDamping(),
                             compositeDamping: CompositeDamping = CompositeDamping(),
                             rayleighDamping: RayleighDamping = RayleighDamping(),
                             structuralDamping: StructuralDamping = StructuralDamping(),
                             directDampingByFrequency: DirectDampingByFrequency = DirectDampingByFrequency(),
                             rayleighDampingByFrequency: RayleighDampingByFrequency = RayleighDampingByFrequency(),
                             structuralDampingByFrequency: StructuralDampingByFrequency = StructuralDampingByFrequency(),
                             maintainAttributes: Boolean = False,
                             subdivideUsingEigenfrequencies: Boolean = ON) -> SteadyStateModalStep:
        """This method creates a SteadyStateModalStep object.

        Path
        ----
            - mdb.models[name].SteadyStateModalStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        frequencyRange
            A SteadyStateModalFrequencyArray object. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        scale
            A SymbolicConstant specifying whether a logarithmic or linear scale is used for output. 
            Possible values are LOGARITHMIC and LINEAR. The default value is LOGARITHMIC. 
        directDamping
            A DirectDamping object. 
        compositeDamping
            A CompositeDamping object. 
        rayleighDamping
            A RayleighDamping object. 
        structuralDamping
            A StructuralDamping object. 
        directDampingByFrequency
            A DirectDampingByFrequency object. 
        rayleighDampingByFrequency
            A RayleighDampingByFrequency object. 
        structuralDampingByFrequency
            A StructuralDampingByFrequency object. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        subdivideUsingEigenfrequencies
            A Boolean specifying whether to subdivide each frequency range using the 
            eigenfrequencies of the system. The default value is ON. 

        Returns
        -------
            A SteadyStateModalStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = SteadyStateModalStep(name, previous, frequencyRange, description, scale,
                                                       directDamping, compositeDamping, rayleighDamping,
                                                       structuralDamping, directDampingByFrequency,
                                                       rayleighDampingByFrequency, structuralDampingByFrequency,
                                                       maintainAttributes, subdivideUsingEigenfrequencies)
        return step

    def SteadyStateSubspaceStep(self, name: str, previous: str, frequencyRange: SteadyStateSubspaceFrequencyArray,
                                description: str = '', factorization: SymbolicConstant = COMPLEX,
                                scale: SymbolicConstant = LOGARITHMIC, matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                                maintainAttributes: Boolean = False, subdivideUsingEigenfrequencies: Boolean = ON,
                                projection: SymbolicConstant = ALL_FREQUENCIES, maxDampingChange: float = 0,
                                maxStiffnessChange: float = 0,
                                frictionDamping: Boolean = OFF) -> SteadyStateSubspaceStep:
        """This method creates a SteadyStateSubspaceStep object.

        Path
        ----
            - mdb.models[name].SteadyStateSubspaceStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        frequencyRange
            A SteadyStateSubspaceFrequencyArray object. 
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
            eigenfrequencies of the system. The default value is ON. 
        projection
            A SymbolicConstant specifying how often to perform subspace projections onto the modal 
            subspace. Possible values are ALL_FREQUENCIES, CONSTANT, EIGENFREQUENCY, 
            PROPERTY_CHANGE, and RANGE. The default value is ALL_FREQUENCIES. 
        maxDampingChange
            A Float specifying the maximum relative change in damping material properties before a 
            new projection is to be performed. The default value is 0.1. 
        maxStiffnessChange
            A Float specifying the maximum relative change in stiffness material properties before a 
            new projection is to be performed. The default value is 0.1. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 

        Returns
        -------
            A SteadyStateSubspaceStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = SteadyStateSubspaceStep(name, previous, frequencyRange, description, factorization,
                                                          scale, matrixStorage, maintainAttributes,
                                                          subdivideUsingEigenfrequencies, projection, maxDampingChange,
                                                          maxStiffnessChange, frictionDamping)
        return step

    def SubspaceDynamicsStep(self, name: str, previous: str, description: str = '', timePeriod: float = 1,
                             vectors: SymbolicConstant = ALL, nlgeom: Boolean = OFF, maxNumInc: int = 100,
                             incSize: float = 0, amplitude: SymbolicConstant = STEP,
                             maintainAttributes: Boolean = False) -> SubspaceDynamicsStep:
        """This method creates a SubspaceDynamicsStep object.

        Path
        ----
            - mdb.models[name].SubspaceDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        timePeriod
            A Float specifying the total time period of the step. The default value is 1.0. 
        vectors
            The SymbolicConstant ALL or an Int specifying the number of modes to be used for 
            subspace projection. The possible value for the SymbolicConstant is ALL. The default 
            value is ALL. 
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is 
            OFF. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        incSize
            A Float specifying the suggested time increment. The default value is 0.0. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. Possible values are STEP and RAMP. The default value is STEP. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 

        Returns
        -------
            A SubspaceDynamicsStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = SubspaceDynamicsStep(name, previous, description, timePeriod, vectors, nlgeom,
                                                       maxNumInc, incSize, amplitude, maintainAttributes)
        return step

    def SubstructureGenerateStep(self, name: str, previous: str, substructureIdentifier: int, description: str = '',
                                 recoveryMatrix: SymbolicConstant = WHOLE_MODEL, recoveryRegion: Region = Region(),
                                 computeGravityLoadVectors: Boolean = False, computeReducedMassMatrix: Boolean = False,
                                 computeReducedStructuralDampingMatrix: Boolean = False,
                                 computeReducedViscousDampingMatrix: Boolean = False,
                                 evaluateFrequencyDependentProperties: Boolean = False, frequency: float = 0,
                                 retainedEigenmodesMethod: SymbolicConstant = NONE,
                                 modeRange: SubstructureGenerateModesArray = None,
                                 frequencyRange: SubstructureGenerateFrequencyArray = None,
                                 globalDampingField: SymbolicConstant = NONE, alphaDampingRatio: float = 0,
                                 betaDampingRatio: float = 0, structuralDampingRatio: float = 0,
                                 viscousDampingControl: SymbolicConstant = NONE,
                                 structuralDampingControl: SymbolicConstant = NONE) -> SubstructureGenerateStep:
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
        self.steps[name] = step = SubstructureGenerateStep(name, previous, substructureIdentifier, description,
                                                           recoveryMatrix, recoveryRegion, computeGravityLoadVectors,
                                                           computeReducedMassMatrix,
                                                           computeReducedStructuralDampingMatrix,
                                                           computeReducedViscousDampingMatrix,
                                                           evaluateFrequencyDependentProperties, frequency,
                                                           retainedEigenmodesMethod, modeRange, frequencyRange,
                                                           globalDampingField, alphaDampingRatio, betaDampingRatio,
                                                           structuralDampingRatio, viscousDampingControl,
                                                           structuralDampingControl)
        return step

    def TempDisplacementDynamicsStep(self, name: str, previous: str, description: str = '', timePeriod: float = 1,
                                     nlgeom: Boolean = OFF,
                                     timeIncrementationMethod: SymbolicConstant = AUTOMATIC_GLOBAL,
                                     maxIncrement: float = None, scaleFactor: float = 1, userDefinedInc: float = None,
                                     massScaling: MassScalingArray = PREVIOUS_STEP, linearBulkViscosity: float = 0,
                                     quadBulkViscosity: float = 1, maintainAttributes: Boolean = False,
                                     improvedDtMethod: Boolean = ON) -> TempDisplacementDynamicsStep:
        """This method creates a TempDisplacementDynamicsStep object.

        Path
        ----
            - mdb.models[name].TempDisplacementDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        timePeriod
            A Float specifying the time period of the step. The default value is 1.0. 
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the 
            step. The default value is OFF. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default 
            value is AUTOMATIC_GLOBAL. 
        maxIncrement
            None or a Float specifying the maximum time increment allowed. If there is no upper 
            limit, *maxIncrement*=None. The default value is None. 
        scaleFactor
            A Float specifying the factor that is used to scale the time increment. This argument is 
            required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or 
            FIXED_EBE. The default value is 1.0. 
        userDefinedInc
            None or a Float specifying the user-defined time increment. The default value is None. 
        massScaling
            A MassScalingArray object specifying mass scaling controls. The default value is 
            PREVIOUS_STEP. 
        linearBulkViscosity
            A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06. 
        quadBulkViscosity
            A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is 
            1.2. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        improvedDtMethod
            A Boolean specifying whether to use the "improved" (*improvedDtMethod*=ON) or 
            "conservative" (*improvedDtMethod*=OFF) method to estimate the element stable time 
            increment for three-dimensional continuum elements and elements with plane stress 
            formulations (shell, membrane, and two-dimensional plane stress elements). The default 
            value is ON. 

        Returns
        -------
            A TempDisplacementDynamicsStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = TempDisplacementDynamicsStep(name, previous, description, timePeriod, nlgeom,
                                                               timeIncrementationMethod, maxIncrement, scaleFactor,
                                                               userDefinedInc, massScaling, linearBulkViscosity,
                                                               quadBulkViscosity, maintainAttributes, improvedDtMethod)
        return step

    def ViscoStep(self, name: str, previous: str, description: str = '', timePeriod: float = 1,
                  nlgeom: Boolean = OFF, stabilizationMethod: SymbolicConstant = NONE,
                  stabilizationMagnitude: float = None,
                  timeIncrementationMethod: SymbolicConstant = AUTOMATIC,
                  matrixSolver: SymbolicConstant = DIRECT,
                  matrixStorage: SymbolicConstant = SOLVER_DEFAULT, initialInc: float = None,
                  maxNumInc: int = 100, minInc: float = None, maxInc: float = 1,
                  integration: SymbolicConstant = IMPLICIT_EXPLICIT, cetol: float = 0,
                  amplitude: SymbolicConstant = STEP, extrapolation: SymbolicConstant = LINEAR,
                  maintainAttributes: Boolean = False, solutionTechnique: SymbolicConstant = FULL_NEWTON,
                  reformKernel: int = 8, convertSDI: SymbolicConstant = PROPAGATED,
                  adaptiveDampingRatio: float = 0, continueDampingFactors: Boolean = OFF) -> ViscoStep:
        """This method creates a ViscoStep object.

        Path
        ----
            - mdb.models[name].ViscoStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        timePeriod
            A Float specifying the total time period. The default value is 1.0. 
        nlgeom
            A Boolean specifying whether to allow for geometric nonlinearity. The default value is 
            OFF. 
        stabilizationMethod
            A SymbolicConstant specifying the stabilization type. Possible values are NONE, 
            DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE. 
        stabilizationMagnitude
            A Float specifying the damping intensity of the automatic damping algorithm if the 
            problem is expected to be unstable, and *stabilizationMethod* is not NONE. The default 
            value is 2×10–4. 
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values 
            are FIXED and AUTOMATIC. The default value is AUTOMATIC. 
        matrixSolver
            A SymbolicConstant specifying the type of solver. Possible values are DIRECT and 
            ITERATIVE. The default value is DIRECT. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        initialInc
            A Float specifying the initial time increment. The default value is the total time 
            period for the step. 
        maxNumInc
            An Int specifying the maximum number of increments in a step. The default value is 100. 
        minInc
            A Float specifying the minimum time increment allowed. The default value is the smaller 
            of the suggested initial time increment or 10−5 times the total time period. 
        maxInc
            A Float specifying the maximum time increment allowed. The default is the total time 
            period for the step. The default value is 1.0. 
        integration
            A SymbolicConstant specifying which type of integration to use throughout the step. 
            Possible values are IMPLICIT_EXPLICIT and EXPLICIT_ONLY. The default value is 
            IMPLICIT_EXPLICIT. 
        cetol
            A Float specifying the maximum difference in the creep strain increment calculated from 
            the creep strain rates at the beginning and end of the increment. The default value is 
            0.0. 
        amplitude
            A SymbolicConstant specifying the amplitude variation for loading magnitudes during the 
            step. Possible values are STEP and RAMP. The default value is STEP. 
        extrapolation
            A SymbolicConstant specifying the type of extrapolation to use in determining the 
            incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and 
            PARABOLIC. The default value is LINEAR. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        solutionTechnique
            A SymbolicConstant specifying the technique used to for solving nonlinear equations. 
            Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON. 
        reformKernel
            An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix 
            is reformed.. The default value is 8. 
        convertSDI
            A SymbolicConstant specifying whether to force a new iteration if severe discontinuities 
            occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and 
            CONVERT_SDI_ON. The default value is PROPAGATED. 
        adaptiveDampingRatio
            A Float specifying the maximum allowable ratio of the stabilization energy to the total 
            strain energy and can be used only if *stabilizationMethod* is not NONE. The default 
            value is 0.05. 
        continueDampingFactors
            A Boolean specifying whether this step will carry over the damping factors from the 
            results of the preceding general step. This parameter must be used in conjunction with 
            the *adaptiveDampingRatio* parameter. The default value is OFF. 

        Returns
        -------
            A ViscoStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        self.steps[name] = step = ViscoStep(name, previous, description, timePeriod, nlgeom, stabilizationMethod,
                                            stabilizationMagnitude, timeIncrementationMethod, matrixSolver,
                                            matrixStorage, initialInc, maxNumInc, minInc, maxInc, integration, cetol,
                                            amplitude, extrapolation, maintainAttributes, solutionTechnique,
                                            reformKernel, convertSDI, adaptiveDampingRatio, continueDampingFactors)
        return step

    def AcousticInfiniteSection(self, name: str, material: str, thickness: float = 1,
                                order: int = 10) -> AcousticInfiniteSection:
        """This method creates an AcousticInfiniteSection object.

        Path
        ----
            - mdb.models[name].AcousticInfiniteSection
            - session.odbs[name].AcousticInfiniteSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        material
            A String specifying the name of the material. 
        thickness
            A Float specifying the thickness of the section. Possible values are *thickness* >> 0.0. 
            The default value is 1.0. 
        order
            An Int specifying the number of ninth-order polynomials that will be used to resolve the 
            variation of the acoustic field in the infinite direction. Possible values are 0 << 
            *order* ≤≤ 10. The default value is 10. 

        Returns
        -------
            An AcousticInfiniteSection object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.sections[name] = section = AcousticInfiniteSection(name, material, thickness, order)
        return section

    def AcousticInterfaceSection(self, name: str, thickness: float = 1) -> AcousticInterfaceSection:
        """This method creates an AcousticInterfaceSection object.

        Path
        ----
            - mdb.models[name].AcousticInterfaceSection
            - session.odbs[name].AcousticInterfaceSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        thickness
            A Float specifying the thickness of the section. Possible values are *thickness* >> 0.0. 
            The default value is 1.0. 

        Returns
        -------
            An AcousticInterfaceSection object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.sections[name] = section = AcousticInterfaceSection(name, thickness)
        return section

    def BeamSection(self, name: str, integration: SymbolicConstant, profile: str, poissonRatio: float = 0,
                    thermalExpansion: Boolean = OFF, temperatureDependency: Boolean = OFF,
                    dependencies: int = 0, density: float = None, referenceTemperature: float = None,
                    temperatureVar: SymbolicConstant = LINEAR, alphaDamping: float = 0,
                    betaDamping: float = 0, compositeDamping: float = 0, useFluidInertia: Boolean = OFF,
                    submerged: SymbolicConstant = FULLY, fluidMassDensity: float = None,
                    crossSectionRadius: float = None, lateralMassCoef: float = 1, axialMassCoef: float = 0,
                    massOffsetX: float = 0, massOffsetY: float = 0, beamShape: SymbolicConstant = CONSTANT,
                    material: str = '', table: tuple = (), outputPts: tuple = (),
                    centroid: tuple[float] = (), shearCenter: tuple[float] = (), profileEnd: str = '') -> BeamSection:
        """This method creates a BeamSection object.

        Path
        ----
            - mdb.models[name].BeamSection
            - session.odbs[name].BeamSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        integration
            A SymbolicConstant specifying the integration method for the section. Possible values 
            are BEFORE_ANALYSIS and DURING_ANALYSIS. 
        profile
            A String specifying the name of the profile. This argument represents the start profile 
            in case of *beamShape*=TAPERED. 
        poissonRatio
            A Float specifying the Poisson's ratio of the section. The default value is 0.0. 
        thermalExpansion
            A Boolean specifying whether to use thermal expansion data. The default value is OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        density
            None or a Float specifying the density of the section. The default value is None. 
        referenceTemperature
            None or a Float specifying the reference temperature of the section. The default value 
            is None. 
        temperatureVar
            A SymbolicConstant specifying the temperature variation for the section. Possible values 
            are LINEAR and INTERPOLATED. The default value is LINEAR. 
        alphaDamping
            A Float specifying the αRαR factor to create mass proportional damping in 
            direct-integration dynamics. The default value is 0.0. 
        betaDamping
            A Float specifying the βRβR factor to create stiffness proportional damping in 
            direct-integration dynamics. The default value is 0.0. 
        compositeDamping
            A Float specifying the fraction of critical damping to be used in calculating composite 
            damping factors for the modes (for use in modal dynamics). The default value is 0.0. 
        useFluidInertia
            A Boolean specifying whether added mass effects will be simulated. The default value is 
            OFF. 
        submerged
            A SymbolicConstant specifying whether the section is either full submerged or half 
            submerged. This argument applies only when *useFluidInertia* = True. Possible values are 
            FULLY and HALF. The default value is FULLY. 
        fluidMassDensity
            None or a Float specifying the mass density of the fluid. This argument applies only 
            when *useFluidInertia* = True and must be specified in that case. The default value is 
            None. 
        crossSectionRadius
            None or a Float specifying the radius of the cylindrical cross-section. This argument 
            applies only when *useFluidInertia* = True and must be specified in that case. The 
            default value is None. 
        lateralMassCoef
            A Float specifying the added mass coefficient, CACA, for lateral motions of the beam. 
            This argument applies only when*useFluidInertia* = True. The default value is 1.0. 
        axialMassCoef
            A Float specifying the added mass coefficient, C(A−E)C(A-E), for motions along the axis 
            of the beam. This argument affects only the term added to the free end(s) of the beam, 
            and applies only when *useFluidInertia* = True. The default value is 0.0. 
        massOffsetX
            A Float specifying the local 1-coordinate of the center of the cylindrical cross-section 
            with respect to the beam cross-section. This argument applies only when 
            *useFluidInertia* = True. The default value is 0.0. 
        massOffsetY
            A Float specifying the local 2-coordinate of the center of the cylindrical cross-section 
            with respect to the beam cross-section. This argument applies only when 
            *useFluidInertia* = True. The default value is 0.0. 
        beamShape
            A SymbolicConstant specifying the change in cross-section of the beam along length. 
            Possible values are CONSTANT and TAPERED. The default value is CONSTANT. This parameter 
            is available for manipulating the model database but not for the ODB API. 
        material
            A String specifying the name of the material. The default value is an empty string. The 
            material is required when *integration* is "DURING_ANALYSIS". 
        table
            A sequence of sequences of Floats specifying the items described below. The default 
            value is an empty sequence. 
        outputPts
            A sequence of pairs of Floats specifying the positions at which output is requested. The 
            default value is an empty sequence. 
        centroid
            A pair of Floats specifying the *X–Y* coordinates of the centroid. The default value is 
            (0.0, 0.0). 
        shearCenter
            A pair of Floats specifying the *X–Y* coordinates of the shear center. The default value 
            is (0.0, 0.0). 
        profileEnd
            A String specifying the name of the end profile. The type of the end profile must be 
            same as that of the start profile. This argument is valid only when *beamShape*=TAPERED. 
            The default value is an empty string. This parameter is available for manipulating the 
            model database but not for the ODB API. 

        Returns
        -------
            A BeamSection object. 

        Exceptions
        ----------
            None. 
        """
        self.sections[name] = section = BeamSection(name, integration, profile, poissonRatio, thermalExpansion,
                                                    temperatureDependency, dependencies, density, referenceTemperature,
                                                    temperatureVar, alphaDamping, betaDamping, compositeDamping,
                                                    useFluidInertia, submerged, fluidMassDensity, crossSectionRadius,
                                                    lateralMassCoef, axialMassCoef, massOffsetX, massOffsetY, beamShape,
                                                    material, table, outputPts, centroid, shearCenter, profileEnd)
        return section

    def CohesiveSection(self, name: str, response: SymbolicConstant, material: str,
                        initialThicknessType: SymbolicConstant = SOLVER_DEFAULT, initialThickness: float = 1,
                        outOfPlaneThickness: float = None) -> CohesiveSection:
        """This method creates a CohesiveSection object.

        Path
        ----
            - mdb.models[name].CohesiveSection
            - session.odbs[name].CohesiveSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        response
            A SymbolicConstant specifying the geometric assumption that defines the constitutive 
            behavior of the cohesive elements. Possible values are TRACTION_SEPARATION, CONTINUUM, 
            and GASKET. 
        material
            A String specifying the name of the material. 
        initialThicknessType
            A SymbolicConstant specifying the method used to compute the initial thickness. Possible 
            values are:SOLVER_DEFAULT, specifying that Abaqus will use the analysis product 
            defaultGEOMETRY, specifying that Abaqus will compute the thickness from the nodal 
            coordinates of the elements.SPECIFY, specifying that Abaqus will use the value given for 
            *initialThickness*The default value is SOLVER_DEFAULT. 
        initialThickness
            A Float specifying the initial thickness for the section. The *initialThickness* 
            argument applies only when *initialThicknessType*=SPECIFY. The default value is 1.0. 
        outOfPlaneThickness
            None or a Float specifying the out-of-plane thickness for the section. The default value 
            is None. 

        Returns
        -------
            A CohesiveSection object. 

        Exceptions
        ----------
            RangeError and InvalidNameError. 
        """
        self.sections[name] = section = CohesiveSection(name, response, material, initialThicknessType,
                                                        initialThickness, outOfPlaneThickness)
        return section

    def CompositeShellSection(self, name: str, layup: SectionLayerArray, symmetric: Boolean = OFF,
                              thicknessType: SymbolicConstant = UNIFORM, preIntegrate: Boolean = OFF,
                              poissonDefinition: SymbolicConstant = DEFAULT, poisson: float = 0,
                              integrationRule: SymbolicConstant = SIMPSON, temperature: SymbolicConstant = GRADIENT,
                              idealization: SymbolicConstant = NO_IDEALIZATION, nTemp: int = None,
                              thicknessModulus: float = None, useDensity: Boolean = OFF, density: float = 0,
                              layupName: str = '', thicknessField: str = '',
                              nodalThicknessField: str = '') -> CompositeShellSection:
        """This method creates a CompositeShellSection object.

        Path
        ----
            - mdb.models[name].parts[name].compositeLayups[i].CompositeShellSection
            - mdb.models[name].CompositeShellSection
            - session.odbs[name].CompositeShellSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        layup
            A SectionLayerArray object specifying the shell cross-section. 
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis. 
            The default value is OFF. 
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the 
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, DISCRETE_FIELD, 
            NODAL_ANALYTICAL_FIELD, and NODAL_DISCRETE_FIELD. The default value is UNIFORM. 
        preIntegrate
            A Boolean specifying whether the shell section properties are specified by the user 
            prior to the analysis (ON) or integrated during the analysis (OFF). The default value is 
            OFF. 
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. 
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio 
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an 
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis 
            is the value provided in *poisson*.The default value is DEFAULT. 
        poisson
            A Float specifying the Poisson's ratio. Possible values are −1.0 ≤≤ *poisson* ≤≤ 0.5. 
            This argument is valid only when *poissonDefinition*=VALUE. The default value is 0.5. 
        integrationRule
            A SymbolicConstant specifying the shell section integration rule. Possible values are 
            SIMPSON and GAUSS. The default value is SIMPSON. 
        temperature
            A SymbolicConstant specifying the mode used for temperature and field variable input 
            across the section thickness. Possible values are GRADIENT and POINTWISE. The default 
            value is GRADIENT. 
        idealization
            A SymbolicConstant specifying the mechanical idealization used for the section 
            calculations. This member is only applicable when *preIntegrate* is set to ON. Possible 
            values are NO_IDEALIZATION, SMEAR_ALL_LAYERS, MEMBRANE, and BENDING. The default value 
            is NO_IDEALIZATION. 
        nTemp
            None or an Int specifying the number of temperature points to be input. This argument is 
            valid only when *temperature*=POINTWISE. The default value is None. 
        thicknessModulus
            None or a Float specifying the effective thickness modulus. This argument is relevant 
            only for continuum shells and must be used in conjunction with the argument *poisson*. 
            The default value is None. 
        useDensity
            A Boolean specifying whether or not to use the value of *density*. The default value is 
            OFF. 
        density
            A Float specifying the value of density to apply to this section. The default value is 
            0.0. 
        layupName
            A String specifying the layup name for this section. The default value is an empty 
            string. 
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to 
            define the thickness of the shell elements. The *thicknessField* argument applies only 
            when *thicknessType*=ANALYTICAL_FIELD or *thicknessType*=DISCRETE_FIELD. The default 
            value is an empty string. 
        nodalThicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to 
            define the thickness of the shell elements at each node. The *nodalThicknessField* 
            argument applies only when *thicknessType*=NODAL_ANALYTICAL_FIELD or 
            *thicknessType*=NODAL_DISCRETE_FIELD. The default value is an empty string. 

        Returns
        -------
            A CompositeShellSection object. 

        Exceptions
        ----------
            None. 
        """
        self.sections[name] = section = CompositeShellSection(name, layup, symmetric, thicknessType, preIntegrate,
                                                              poissonDefinition, poisson, integrationRule, temperature,
                                                              idealization, nTemp, thicknessModulus, useDensity,
                                                              density, layupName, thicknessField, nodalThicknessField)
        return section

    def CompositeSolidSection(self, name: str, layup: SectionLayerArray, symmetric: Boolean = OFF,
                              layupName: str = '') -> CompositeSolidSection:
        """This method creates a CompositeSolidSection object.

        Path
        ----
            - mdb.models[name].CompositeSolidSection
            - session.odbs[name].CompositeSolidSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        layup
            A SectionLayerArray object specifying the solid cross-section. 
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis. 
            The default value is OFF. 
        layupName
            A String specifying the layup name for this section. The default value is an empty 
            string. 

        Returns
        -------
            A CompositeSolidSection object. 

        Exceptions
        ----------
            None. 
        """
        self.sections[name] = section = CompositeSolidSection(name, layup, symmetric, layupName)
        return section

    def ConnectorSection(self, name: str, assembledType: SymbolicConstant = NONE,
                         rotationalType: SymbolicConstant = NONE, translationalType: SymbolicConstant = NONE,
                         integration: SymbolicConstant = UNSPECIFIED, u1ReferenceLength: float = None,
                         u2ReferenceLength: float = None, u3ReferenceLength: float = None,
                         ur1ReferenceAngle: float = None, ur2ReferenceAngle: float = None,
                         ur3ReferenceAngle: float = None, massPerLength: float = None,
                         contactAngle: float = None, materialFlowFactor: float = 1, regularize: Boolean = ON,
                         defaultTolerance: Boolean = ON, regularization: float = 0,
                         extrapolation: SymbolicConstant = CONSTANT,
                         behaviorOptions: ConnectorBehaviorOptionArray = None) -> ConnectorSection:
        """This method creates a ConnectorSection object.

        Path
        ----
            - mdb.models[name].ConnectorSection
            - session.odbs[name].ConnectorSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        assembledType
            A SymbolicConstant specifying the assembled connection type. Possible values 
            are:NONEBEAMBUSHINGCVJOINTCYLINDRICALHINGEPLANARRETRACTORSLIPRINGTRANSLATORUJOINTWELDThe 
            default value is NONE.You cannot include the *assembledType* argument if 
            *translationalType* or *rotationalType* are given a value other than NONE. At least one 
            of the arguments *assembledType*, *translationalType*, or *rotationalType* must be given 
            a value other than NONE. 
        rotationalType
            A SymbolicConstant specifying the basic rotational connection type. Possible values 
            are:NONEALIGNCARDANCONSTANT_VELOCITYEULERFLEXION_TORSIONFLOW_CONVERTERPROJECTION_FLEXION_TORSIONREVOLUTEROTATIONROTATION_ACCELEROMETERUNIVERSALThe 
            default value is NONE.You cannot include the *rotationalType* argument if 
            *assembledType* is given a value other than NONE. At least one of the arguments 
            *assembledType*, *translationalType*, or *rotationalType* must be given an value other 
            than NONE. 
        translationalType
            A SymbolicConstant specifying the basic translational connection type. Possible values 
            are:NONEACCELEROMETERAXIALCARTESIANJOINLINKPROJECTION_CARTESIANRADIAL_THRUSTSLIDE_PLANESLOTThe 
            default value is NONE.You cannot include the *translationalType* argument if 
            *assembledType* is given a value other than NONE. At least one of the arguments 
            *assembledType*, *translationalType*, or *rotationalType* must be given an value other 
            than NONE. 
        integration
            A SymbolicConstant specifying the time integration scheme to use for analysis. This 
            argument is applicable only to an Abaqus/Explicit analysis. Possible values are 
            UNSPECIFIED, IMPLICIT, and EXPLICIT. The default value is UNSPECIFIED. 
        u1ReferenceLength
            None or a Float specifying the reference length associated with constitutive response 
            for the first component of relative motion. The default value is None. 
        u2ReferenceLength
            None or a Float specifying the reference length associated with constitutive response 
            for the second component of relative motion. The default value is None. 
        u3ReferenceLength
            None or a Float specifying the reference length associated with constitutive response 
            for the third component of relative motion. The default value is None. 
        ur1ReferenceAngle
            None or a Float specifying the reference angle in degrees associated with constitutive 
            response for the fourth component of relative motion. The default value is None. 
        ur2ReferenceAngle
            None or a Float specifying the reference angle in degrees associated with constitutive 
            response for the fifth component of relative motion. The default value is None. 
        ur3ReferenceAngle
            None or a Float specifying the reference angle in degrees associated with constitutive 
            response for the sixth component of relative motion. The default value is None. 
        massPerLength
            None or a Float specifying the mass per unit reference length of belt material. This 
            argument is applicable only when *assembledType*=SLIPRING, and must be specified in that 
            case. The default value is None. 
        contactAngle
            None or a Float specifying the contact angle made by the belt wrapping around node b. 
            This argument is applicable only to an Abaqus/Explicit analysis, and only when 
            *assembledType*=SLIPRING. The default value is None. 
        materialFlowFactor
            A Float specifying the scaling factor for material flow at node b. This argument is 
            applicable only when *assembledType*=RETRACTOR or *rotationalType*=FLOW_CONVERTER. The 
            default value is 1.0. 
        regularize
            A Boolean specifying whether or not all tabular data associated with the 
            *behaviorOptions* will be regularized. This argument is applicable only for an 
            Abaqus/Explicit analysis. The default value is ON. 
        defaultTolerance
            A Boolean specifying whether or not the default regularization tolerance will be used 
            for all tabular data associated with the *behaviorOptions*. This argument is applicable 
            only for an Abaqus/Explicit analysis and only if *regularize*=ON. The default value is 
            ON. 
        regularization
            A Float specifying the regularization increment to be used for all tabular data 
            associated with the *behaviorOptions*. This argument is applicable only for an 
            Abaqus/Explicit analysis and only if *regularize*=ON and *defaultTolerance*=OFF. The 
            default value is 0.03. 
        extrapolation
            A SymbolicConstant specifying the extrapolation technique to be used for all tabular 
            data associated with the *behaviorOptions*. Possible values are CONSTANT and LINEAR. The 
            default value is CONSTANT. 
        behaviorOptions
            A ConnectorBehaviorOptionArray object. 

        Returns
        -------
            A ConnectorSection object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.sections[name] = section = ConnectorSection(name, assembledType, rotationalType, translationalType,
                                                         integration, u1ReferenceLength, u2ReferenceLength,
                                                         u3ReferenceLength, ur1ReferenceAngle, ur2ReferenceAngle,
                                                         ur3ReferenceAngle, massPerLength, contactAngle,
                                                         materialFlowFactor, regularize, defaultTolerance,
                                                         regularization, extrapolation, behaviorOptions)
        return section

    def EulerianSection(self, name: str, data: str) -> EulerianSection:
        """This method creates a EulerianSection object.

        Path
        ----
            - mdb.models[name].EulerianSection
            - session.odbs[name].EulerianSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        data
            A String-to-String Dictionary specifying a dictionary mapping Material instance names to 
            Material names. Internally the specified mapping gets sorted on Material instance name. 

        Returns
        -------
            An EulerianSection object. 

        Exceptions
        ----------
            None. 
        """
        self.sections[name] = section = EulerianSection(name, data)
        return section

    def GasketSection(self, name: str, material: str, crossSection: float = 1, initialGap: float = 0,
                      initialThickness: typing.Union[SymbolicConstant, float] = DEFAULT,
                      initialVoid: float = 0,
                      stabilizationStiffness: typing.Union[SymbolicConstant, float] = DEFAULT) -> GasketSection:
        """This method creates a GasketSection object.

        Path
        ----
            - mdb.models[name].GasketSection
            - session.odbs[name].GasketSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        material
            A String specifying the name of the material of which the gasket is made or material 
            that defines gasket behavior. 
        crossSection
            A Float specifying the cross-sectional area, width, or out-of-plane thickness, if 
            applicable, depending on the gasket element type. The default value is 1.0. 
        initialGap
            A Float specifying the initial gap. The default value is 0.0. 
        initialThickness
            The SymbolicConstant DEFAULT or a Float specifying the initial gasket thickness. If 
            DEFAULT is specified, the initial thickness is determined using nodal coordinates. The 
            default value is DEFAULT. 
        initialVoid
            A Float specifying the initial void. The default value is 0.0. 
        stabilizationStiffness
            The SymbolicConstant DEFAULT or a Float specifying the default stabilization stiffness 
            used in all but link elements to stabilize gasket elements that are not supported at all 
            nodes, such as those that extend outside neighboring components. If DEFAULT is 
            specified, a value is used equal to 10–9 times the initial compressive stiffness in the 
            thickness direction. The default value is DEFAULT. 

        Returns
        -------
            A GasketSection object. 

        Exceptions
        ----------
            InvalidNameError and ValueError. 
        """
        self.sections[name] = section = GasketSection(name, material, crossSection, initialGap, initialThickness,
                                                      initialVoid, stabilizationStiffness)
        return section

    def GeneralStiffnessSection(self, name: str, stiffnessMatrix: tuple, referenceTemperature: float = None,
                                applyThermalStress: Boolean = OFF, temperatureDependency: Boolean = OFF,
                                dependencies: int = 0, poissonDefinition: SymbolicConstant = DEFAULT,
                                poisson: float = 0, useDensity: Boolean = OFF, density: float = 0,
                                thermalStresses: tuple = (), scalingData: tuple = ()) -> GeneralStiffnessSection:
        """This method creates a GeneralStiffnessSection object.

        Path
        ----
            - mdb.models[name].GeneralStiffnessSection
            - session.odbs[name].GeneralStiffnessSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        stiffnessMatrix
            A sequence of Floats specifying the stiffness matrix for the section in the order D11, 
            D12, D22, D13, D23, D33, ...., D66. Twenty-one entries must be given. 
        referenceTemperature
            None or a Float specifying the reference temperature for thermal expansion. The default 
            value is None. 
        applyThermalStress
            A Boolean specifying whether or not the section stiffness varies with thermal stresses. 
            The default value is OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. 
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio 
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an 
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis 
            is the value provided in *poisson*.The default value is DEFAULT. 
        poisson
            A Float specifying the Poisson's ratio. Possible values are −1.0 ≤≤ *poisson* ≤≤ 0.5. 
            This argument is valid only when *poissonDefinition*=VALUE. The default value is 0.5. 
        useDensity
            A Boolean specifying whether or not to use the value of *density*. The default value is 
            OFF. 
        density
            A Float specifying the value of density to apply to this section. The default value is 
            0.0. 
        thermalStresses
            A sequence of Floats specifying the generalized stress values caused by a unit 
            temperature rise. Six entries must be given if the value of *applyThermalStress* is set 
            to True. The default value is (""). 
        scalingData
            A sequence of sequences of Floats specifying the scaling factors for given temperatures 
            and/or field data. Each row should contain (Y, alpha, T, F1,...,Fn). The default value 
            is an empty sequence. 

        Returns
        -------
            A GeneralStiffnessSection object. 

        Exceptions
        ----------
            None. 
        """
        self.sections[name] = section = GeneralStiffnessSection(name, stiffnessMatrix, referenceTemperature,
                                                                applyThermalStress, temperatureDependency, dependencies,
                                                                poissonDefinition, poisson, useDensity, density,
                                                                thermalStresses, scalingData)
        return section

    def HomogeneousShellSection(self, name: str, material: str, thickness: float = 0, numIntPts: int = 5,
                                thicknessType: SymbolicConstant = UNIFORM, preIntegrate: Boolean = OFF,
                                poissonDefinition: SymbolicConstant = DEFAULT, poisson: float = 0,
                                integrationRule: SymbolicConstant = SIMPSON, temperature: SymbolicConstant = GRADIENT,
                                idealization: SymbolicConstant = NO_IDEALIZATION, nTemp: int = None,
                                thicknessModulus: float = None, useDensity: Boolean = OFF, density: float = 0,
                                thicknessField: str = '', nodalThicknessField: str = '') -> HomogeneousShellSection:
        """This method creates a HomogeneousShellSection object.

        Path
        ----
            - mdb.models[name].parts[name].compositeLayups[i]\
            - .HomogeneousShellSection
            - mdb.models[name].HomogeneousShellSection
            - session.odbs[name].HomogeneousShellSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        material
            A String specifying the name of the section material. 
        thickness
            A Float specifying the thickness of the section. The *thickness* argument applies only 
            when *thicknessType*=UNIFORM. The default value is 0.0. 
        numIntPts
            An Int specifying the number of integration points to be used through the section. 
            Possible values are *numIntPts* >> 0. The default value is 5.To use the default settings 
            of the analysis products, set *numIntPts* to 5 if *integrationRule*=SIMPSON or set 
            *numIntPts* to 7 if *integrationRule*=GAUSS. 
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the 
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, DISCRETE_FIELD, 
            NODAL_ANALYTICAL_FIELD, and NODAL_DISCRETE_FIELD. The default value is UNIFORM. 
        preIntegrate
            A Boolean specifying whether the shell section properties are specified by the user 
            prior to the analysis (ON) or integrated during the analysis (OFF). The default value is 
            OFF. 
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. 
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio 
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an 
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis 
            is the value provided in *poisson*.The default value is DEFAULT. 
        poisson
            A Float specifying the Poisson's ratio. Possible values are −1.0 ≤≤ *poisson* ≤≤ 0.5. 
            This argument is valid only when *poissonDefinition*=VALUE. The default value is 0.5. 
        integrationRule
            A SymbolicConstant specifying the shell section integration rule. Possible values are 
            SIMPSON and GAUSS. The default value is SIMPSON. 
        temperature
            A SymbolicConstant specifying the mode used for temperature and field variable input 
            across the section thickness. Possible values are GRADIENT and POINTWISE. The default 
            value is GRADIENT. 
        idealization
            A SymbolicConstant specifying the mechanical idealization used for the section 
            calculations. This member is only applicable when *preIntegrate* is set to ON. Possible 
            values are NO_IDEALIZATION, SMEAR_ALL_LAYERS, MEMBRANE, and BENDING. The default value 
            is NO_IDEALIZATION. 
        nTemp
            None or an Int specifying the number of temperature points to be input. This argument is 
            valid only when *temperature*=POINTWISE. The default value is None. 
        thicknessModulus
            None or a Float specifying the effective thickness modulus. This argument is relevant 
            only for continuum shells and must be used in conjunction with the argument *poisson*. 
            The default value is None. 
        useDensity
            A Boolean specifying whether or not to use the value of *density*. The default value is 
            OFF. 
        density
            A Float specifying the value of density to apply to this section. The default value is 
            0.0. 
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to 
            define the thickness of the shell elements. The *thicknessField* argument applies only 
            when *thicknessType*=ANALYTICAL_FIELD or *thicknessType*=DISCRETE_FIELD. The default 
            value is an empty string. 
        nodalThicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to 
            define the thickness of the shell elements at each node. The *nodalThicknessField* 
            argument applies only when *thicknessType*=NODAL_ANALYTICAL_FIELD or 
            *thicknessType*=NODAL_DISCRETE_FIELD. The default value is an empty string. 

        Returns
        -------
            A HomogeneousShellSection object. 

        Exceptions
        ----------
            None. 
        """
        self.sections[name] = section = HomogeneousShellSection(name, material, thickness, numIntPts, thicknessType,
                                                                preIntegrate, poissonDefinition, poisson,
                                                                integrationRule, temperature, idealization, nTemp,
                                                                thicknessModulus, useDensity, density, thicknessField,
                                                                nodalThicknessField)
        return section

    def HomogeneousSolidSection(self, name: str, material: str, thickness: float = 1) -> HomogeneousSolidSection:
        """This method creates a HomogeneousSolidSection object.

        Path
        ----
            - mdb.models[name].HomogeneousSolidSection
            - session.odbs[name].HomogeneousSolidSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        material
            A String specifying the name of the material. 
        thickness
            A Float specifying the thickness of the section. Possible values are None or greater 
            than zero. The default value is 1.0. 

        Returns
        -------
            A HomogeneousSolidSection object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.sections[name] = section = HomogeneousSolidSection(name, material, thickness)
        return section

    def MembraneSection(self, name: str, material: str, thickness: float = 1,
                        thicknessType: SymbolicConstant = UNIFORM,
                        poissonDefinition: SymbolicConstant = DEFAULT, poisson: float = 0,
                        thicknessField: str = '') -> MembraneSection:
        """This method creates a MembraneSection object.

        Path
        ----
            - mdb.models[name].MembraneSection
            - session.odbs[name].MembraneSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        material
            A String specifying the name of the material. 
        thickness
            A Float specifying the thickness for the section. Possible values are *thickness* >> 
            0.0. The default value is 1.0. 
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the 
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default 
            value is UNIFORM. 
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. 
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio 
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an 
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis 
            is the value provided in *poisson*.The default value is DEFAULT. 
        poisson
            A Float specifying the section Poisson's ratio. Possible values are −1.0 ≤≤ *poisson* ≤≤ 
            0.5. This argument is valid only when *poissonDefinition*=VALUE. The default value is 
            0.5. 
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to 
            define the thickness of the shell elements. The *thicknessField* argument applies only 
            when *thicknessType*=ANALYTICAL_FIELD or *thicknessType*=DISCRETE_FIELD. The default 
            value is an empty string. 

        Returns
        -------
            A MembraneSection object. 

        Exceptions
        ----------
            RangeError and InvalidNameError. 
        """
        self.sections[name] = section = MembraneSection(name, material, thickness, thicknessType, poissonDefinition,
                                                        poisson, thicknessField)
        return section

    def MPCSection(self, name: str, mpcType: SymbolicConstant, userMode: SymbolicConstant = DOF_MODE,
                   userType: int = 0) -> MPCSection:
        """This method creates a MPCSection object.

        Path
        ----
            - mdb.models[name].MPCSection
            - session.odbs[name].MPCSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        mpcType
            A SymbolicConstant specifying the MPC type of the section. Possible values are BEAM_MPC, 
            ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_DEFINED. 
        userMode
            A SymbolicConstant specifying the mode of the MPC when it is user-defined. Possible 
            values are DOF_MODE and NODE_MODE. The default value is DOF_MODE.The *userMode* argument 
            applies only when *mpcType*=USER_DEFINED. 
        userType
            An Int specifying to differentiate between different constraint types in a user-defined 
            MPCSection. The default value is 0.The *userType* argument applies only when 
            *mpcType*=USER_DEFINED. 

        Returns
        -------
            A MPCSection object. 

        Exceptions
        ----------
            RangeError and InvalidNameError. 
        """
        self.sections[name] = section = MPCSection(name, mpcType, userMode, userType)
        return section

    def PEGSection(self, name: str, material: str, thickness: float = 1, wedgeAngle1: float = 0,
                   wedgeAngle2: float = 0) -> PEGSection:
        """This method creates a PEGSection object.

        Path
        ----
            - mdb.models[name].PEGSection
            - session.odbs[name].PEGSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        material
            A String specifying the name of the material. 
        thickness
            A Float specifying the thickness of the section. Possible values are *thickness* >> 0.0. 
            The default value is 1.0. 
        wedgeAngle1
            A Float specifying the value of the x component of the angle between the bounding 
            planes, ΔϕxΔ⁢ϕx. The default value is 0.0. 
        wedgeAngle2
            A Float specifying the value of the y component of the angle between the bounding 
            planes, ΔϕyΔ⁢ϕy. The default value is 0.0. 

        Returns
        -------
            A PEGSection object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        self.sections[name] = section = PEGSection(name, material, thickness, wedgeAngle1, wedgeAngle2)
        return section

    def SurfaceSection(self, name: str, useDensity: Boolean = OFF, density: float = 0) -> SurfaceSection:
        """This method creates a SurfaceSection object.

        Path
        ----
            - mdb.models[name].SurfaceSection
            - session.odbs[name].SurfaceSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        useDensity
            A Boolean specifying whether or not to use the value of *density*. The default value is 
            OFF. 
        density
            A Float specifying the value of density to apply to this section. The default value is 
            0.0. 

        Returns
        -------
            A SurfaceSection object. 

        Exceptions
        ----------
            RangeError and InvalidNameError. 
        """
        self.sections[name] = section = SurfaceSection(name, useDensity, density)
        return section

    def TrussSection(self, name: str, material: str, area: float = 1) -> TrussSection:
        """This method creates a TrussSection object.

        Path
        ----
            - mdb.models[name].TrussSection
            - session.odbs[name].TrussSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        material
            A String specifying the name of the material. 
        area
            A Float specifying the cross-sectional area for the section. Possible values are *area* 
            >> 0. The default value is 1.0. 

        Returns
        -------
            A TrussSection object. 

        Exceptions
        ----------
            RangeError and InvalidNameError. 
        """
        self.sections[name] = section = TrussSection(name, material, area)
        return section

    def ConstrainedSketch(self, name: str, sheetSize: float, gridSpacing: float = None,
                          transform: tuple = ()) -> ConstrainedSketch:
        """This method creates a ConstrainedSketch object. If the sketch cannot be created, the
        method returns None.

        Path
        ----
            - mdb.models[name].ConstrainedSketch

        Parameters
        ----------
        name
            A String specifying the repository key. 
        sheetSize
            A Float specifying the sheet size. 
        gridSpacing
            A Float specifying the spacing between gridlines. Possible values are Floats >> 0. The 
            default value is approximately 2 percent of *sheetSize*. 
        transform
            A sequence of sequences of Floats specifying the three-dimensional orientation of the 
            sketch. The sequence is a 3 × 4 transformation matrix specifying the axis of rotation 
            and the translation vector. Possible values are any Floats.The default value for the 
            axis of rotation is the identity matrix`(1.0, 0.0, 0.0),  (0.0, 1.0, 0.0),  (0.0, 0.0, 
            1.0)`The default value for the translation vector is`(0.0, 0.0, 0.0)`The default values 
            position the sketch on the *X–Y* plane centered at the origin. 

        Returns
        -------
            A ConstrainedSketch object. 

        Exceptions
        ----------
            None. 
        """
        self.sketches[name] = sketch = ConstrainedSketch(name, sheetSize, gridSpacing, transform)
        return sketch

    def Field(self, name: str, createStepName: str, region: Region, outputVariable: str = '',
              fieldVariableNum: int = None, distributionType: SymbolicConstant = UNIFORM,
              crossSectionDistribution: SymbolicConstant = CONSTANT_THROUGH_THICKNESS,
              field: str = '', amplitude: str = UNSET, fileName: str = '',
              beginStep: SymbolicConstant = None, beginIncrement: SymbolicConstant = None,
              endStep: SymbolicConstant = None, endIncrement: SymbolicConstant = None,
              interpolate: SymbolicConstant = OFF, magnitudes: str = '') -> Field:
        """This method creates a Field object.

        Path
        ----
            - mdb.models[name].Field

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the predefined field is created. 
        region
            A Region object specifying the region to which the predefined field is applied. *Region* 
            is ignored if the predefined field has a *distributionType* member available, and 
            *distributionType*=FROM_FILE. 
        outputVariable
            A String specifying the scalar nodal output variable that will be read from an output 
            database and used to initialize a specified predefined field. This argument is a 
            required argument if *distributionType*=FROM_FILE or 
            *distributionType*=FROM_FILE_AND_USER_DEFINED. 
        fieldVariableNum
            An Int specifying the field variable number. 
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values 
            are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and 
            DISCRETE_FIELD. The default value is UNIFORM. 
        crossSectionDistribution
            A SymbolicConstant specifying how the predefined field is distributed over the 
            cross-section of the region. Possible values are 
            - CONSTANT_THROUGH_THICKNESS 
            - GRADIENTS_THROUGH_SHELL_CS 
            - GRADIENTS_THROUGH_BEAM_CS 
            - POINTS_THROUGH_SECTION 
            The default value is CONSTANT_THROUGH_THICKNESS. 
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated 
            with this predefined field. The *field* argument applies only when 
            *distributionType*=FIELD or *distributionType*=DISCRETE_FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the predefined field has no amplitude reference. The default 
            value is UNSET.Note:*amplitude* should be given only if it is valid for the specified 
            step. 
        fileName
            A String specifying the name of the file from which the Field values are to be read when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. 
        beginStep
            An Int specifying the first step from which Field values are to be read or the 
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The 
            default value is None. 
        beginIncrement
            An Int specifying the first increment of the step set in *beginStep* or the 
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The 
            default value is None. 
        endStep
            An Int specifying the last step from which Field values are to be read or the 
            SymbolicConstants FIRST_STEP and LAST_STEP. This argument is valid only when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The 
            default value is None. 
        endIncrement
            An Int specifying the last increment of the step set in *endStep* or the 
            SymbolicConstants STEP_START and STEP_END. This argument is valid only when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The 
            default value is None. 
        interpolate
            A SymbolicConstant specifying whether to interpolate a field read from an output 
            database or results file. Possible values are OFF, ON, or MIDSIDE_ONLY. The default 
            value is OFF. 
        magnitudes
            A Sequence of Doubles specifying the Field values when *distributionType*=UNIFORM or 
            FIELD. The value of the *magnitudes* argument is a function of the 
            *crossSectionDistribution* argument, as shown in the following list: 
            - If *crossSectionDistribution*=CONSTANT_THROUGH_THICKNESS, *magnitudes* is a Double 
            specifying the Field. 
            - If *crossSectionDistribution*=GRADIENTS_THROUGH_SHELL_CS, *magnitudes* is a sequence 
            of Doubles specifying the mean value and the gradient in the thickness direction. 
            - If *crossSectionDistribution*=GRADIENTS_THROUGH_BEAM_CS, *magnitudes* is a sequence of 
            Doubles specifying the mean value, the gradient in the N1 direction, and the gradient in 
            the N2 direction. 
            - If *crossSectionDistribution*=POINTS_THROUGH_SECTION, *magnitudes* is a sequence of 
            Doubles specifying the Field at each point. 

        Returns
        -------
            A Field object. 

        Exceptions
        ----------
            None. 
        """
        self.predefinedFields[name] = predefinedField = Field(name, createStepName, region, outputVariable,
                                                              fieldVariableNum, distributionType,
                                                              crossSectionDistribution, field, amplitude, fileName,
                                                              beginStep, beginIncrement, endStep, endIncrement,
                                                              interpolate, magnitudes)
        return predefinedField

    def FluidCavityPressure(self, name: str, fluidCavity: str, fluidPressure: float) -> FluidCavityPressure:
        """This method creates a FluidCavityPressure object.

        Path
        ----
            - mdb.models[name].FluidCavityPressure

        Parameters
        ----------
        name
            A String specifying the repository key. 
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction. 
        fluidPressure
            A Float specifying the initial fluid pressure. 

        Returns
        -------
            A FluidCavityPressure object. 

        Exceptions
        ----------
            None. 
        """
        self.predefinedFields[name] = predefinedField = FluidCavityPressure(name, fluidCavity, fluidPressure)
        return predefinedField

    def InitialState(self, name: str, instances: PartInstanceArray, fileName: str,
                     endStep: SymbolicConstant = LAST_STEP, endIncrement: SymbolicConstant = STEP_END,
                     updateReferenceConfiguration: Boolean = OFF) -> InitialState:
        """This method creates an InitialState predefined field object.

        Path
        ----
            - mdb.models[name].InitialState

        Parameters
        ----------
        name
            A String specifying the repository key. 
        instances
            A PartInstanceArray object specifying the instances to which the predefined field is 
            applied. 
        fileName
            A String specifying the name of the job that generated the initial state data. 
        endStep
            The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial 
            state values are to be read or the SymbolicConstant LAST_STEP. The default value is 
            LAST_STEP. 
        endIncrement
            The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration 
            of the step set in *endStep* or the SymbolicConstant STEP_END. The default value is 
            STEP_END. 
        updateReferenceConfiguration
            A Boolean specifying whether to update the reference configuration based on the import 
            data. The default value is OFF. 

        Returns
        -------
            An InitialState object. 

        Exceptions
        ----------
            None. 
        """
        self.predefinedFields[name] = predefinedField = InitialState(name, instances, fileName, endStep, endIncrement,
                                                                     updateReferenceConfiguration)
        return predefinedField

    def KinematicHardening(self, name: str, region: Region, numBackStress: int = 1, equivPlasticStrain: tuple = (),
                           backStress: tuple = (), sectPtNum: tuple = (),
                           definition: SymbolicConstant = KINEMATIC_HARDENING, rebarLayerNames: tuple = (),
                           distributionType: SymbolicConstant = MAGNITUDE) -> KinematicHardening:
        """This method creates a KinematicHardening object.

        Path
        ----
            - mdb.models[name].KinematicHardening

        Parameters
        ----------
        name
            A String specifying the repository key. 
        region
            A Region object specifying the region to which the predefined field is applied. 
        numBackStress
            An Int specifying the number of backstresses. The default value is 1. 
        equivPlasticStrain
            A sequence of Floats specifying the initial equivalent plastic strain. 
        backStress
            A sequence of sequences of Floats specifying the initial backstress tensor for kinematic 
            hardening models. The default value is an empty sequence. 
        sectPtNum
            A sequence of Ints specifying section point numbers. This argument is valid only when 
            *definition*=SECTION_PTS. 
        definition
            A SymbolicConstant specifying different types of kinematic hardening. Possible values 
            are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The 
            default value is KINEMATIC_HARDENING. 
        rebarLayerNames
            A sequence of Strings specifying rebar layer names. This argument is valid only when 
            *definition*=REBAR. 
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE 
            and ANALYTICAL_FIELD. The default value is MAGNITUDE. 

        Returns
        -------
            A KinematicHardening object. 

        Exceptions
        ----------
            None. 
        """
        self.predefinedFields[name] = predefinedField = KinematicHardening(name, region, numBackStress,
                                                                           equivPlasticStrain, backStress, sectPtNum,
                                                                           definition, rebarLayerNames,
                                                                           distributionType)
        return predefinedField

    def MaterialAssignment(self, name: str, instanceList: PartInstanceArray, useFields: Boolean = OFF,
                           assignmentList: tuple = (), fieldList: tuple = (),
                           colorList: tuple = ()) -> MaterialAssignment:
        """This method creates a MaterialAssignment predefined field object.

        Path
        ----
            - mdb.models[name].MaterialAssignment

        Parameters
        ----------
        name
            A String specifying the repository key. 
        instanceList
            A PartInstanceArray object specifying the part instances to which the predefined field 
            is applied. All instances must be assigned the same Eulerian section. 
        useFields
            A Boolean specifying whether the volume fraction data will be uniform or defined by 
            discrete fields. The default value is OFF. 
        assignmentList
            A sequence of tuples specifying the uniform volume fractions to be assigned. This 
            argument is valid only when *useFields*=FALSE. Each tuple contains two entries:A Region 
            object.A tuple of Floats specifying the uniform volume fraction values. The length of 
            the tuple must match the number of material instance names specified in the Eulerain 
            section assigned to part instances specified by *instanceList*. 
        fieldList
            A sequence of tuples specifying the discrete volume fractions to be assigned. This 
            argument is valid only when *useFields*=TRUE. Each tuple contains two entries:A Region 
            object.A tuple of Strings specifying Discrete Field names. The length of the tuple must 
            match the number of material instance names specified in the Eulerain section assigned 
            to part instances specified by *instanceList*. 
        colorList
            A sequence of three Ints specifying colors used to display the material instance 
            assignments. This is a sequence of R,G,B colors, where the values are represented by 
            integers between 0 and 255. The default value is an empty sequence. 

        Returns
        -------
            A MaterialAssignment object. 

        Exceptions
        ----------
            None. 
        """
        self.predefinedFields[name] = predefinedField = MaterialAssignment(name, instanceList, useFields,
                                                                           assignmentList, fieldList, colorList)
        return predefinedField

    def Stress(self, name: str, region: Region, distributionType: SymbolicConstant = UNIFORM,
               sigma11: float = None, sigma22: float = None, sigma33: float = None,
               sigma12: float = None, sigma13: float = None, sigma23: float = None) -> Stress:
        """This method creates a Stress predefined field object.

        Path
        ----
            - mdb.models[name].Stress

        Parameters
        ----------
        name
            A String specifying the repository key. 
        region
            A Region object specifying the region to which the predefined field is applied. Region 
            is ignored if the predefined field has *distributionType*=FROM_FILE. 
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM 
            and FROM_FILE. The default value is UNIFORM. 
        sigma11
            A Float specifying the first principal component of the stress. 
        sigma22
            A Float specifying the second principal component of the stress. 
        sigma33
            A Float specifying the third principal component of the stress. 
        sigma12
            A Float specifying the first shear component of the stress. 
        sigma13
            A Float specifying the second shear component of the stress. 
        sigma23
            A Float specifying the third shear component of the stress. 

        Returns
        -------
            A Stress object. 

        Exceptions
        ----------
            None. 
        """
        self.predefinedFields[name] = predefinedField = Stress(name, region, distributionType, sigma11, sigma22,
                                                               sigma33, sigma12, sigma13, sigma23)
        return predefinedField

    def Temperature(self, name: str, createStepName: str, region: Region,
                    distributionType: SymbolicConstant = UNIFORM,
                    crossSectionDistribution: SymbolicConstant = CONSTANT_THROUGH_THICKNESS,
                    field: str = '', amplitude: str = UNSET, fileName: str = '',
                    beginStep: SymbolicConstant = None, beginIncrement: SymbolicConstant = None,
                    endStep: SymbolicConstant = None, endIncrement: SymbolicConstant = None,
                    interpolate: SymbolicConstant = OFF, magnitudes: str = '',
                    absoluteExteriorTolerance: float = 0, exteriorTolerance: float = 0) -> Temperature:
        """This method creates a Temperature object.

        Path
        ----
            - mdb.models[name].Temperature

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the predefined field is created. 
        region
            A Region object specifying the region to which the predefined field is applied. *Region* 
            is ignored if the predefined field has a *distributionType* member available, and 
            *distributionType*=FROM_FILE . 
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values 
            are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and 
            DISCRETE_FIELD. The default value is UNIFORM. 
        crossSectionDistribution
            A SymbolicConstant specifying how the predefined field is distributed over the cross 
            section of the region. Possible values are 
            - CONSTANT_THROUGH_THICKNESS 
            - GRADIENTS_THROUGH_SHELL_CS 
            - GRADIENTS_THROUGH_BEAM_CS 
            - POINTS_THROUGH_SECTION 
            The default value is CONSTANT_THROUGH_THICKNESS. 
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated 
            with this predefined field. The *field* argument applies only when 
            *distributionType*=FIELD or *distributionType*=DISCRETE_FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the predefined field has no amplitude reference. The default 
            value is UNSET.Note:*amplitude* should be given only if it is valid for the specified 
            step. 
        fileName
            A String specifying the name of the file from which the temperature values are to be 
            read when *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. 
        beginStep
            An Int specifying the first step from which temperature values are to be read or the 
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The 
            default value is None. 
        beginIncrement
            An Int specifying the first increment of the step set in *beginStep* or the 
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The 
            default value is None. 
        endStep
            An Int specifying the last step from which temperature values are to be read or the 
            SymbolicConstants FIRST_STEP and LAST_STEP. This argument is valid only when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The 
            default value is None. 
        endIncrement
            An Int specifying the last increment of the step set in *endStep* or the 
            SymbolicConstants STEP_START and STEP_END. This argument is valid only when 
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The 
            default value is None. 
        interpolate
            A SymbolicConstant specifying whether to interpolate a field read from an output 
            database or results file. Possible values are OFF, ON or MIDSIDE_ONLY. The default value 
            is OFF. 
        magnitudes
            A Sequence of Doubles specifying the temperature values when *distributionType*=UNIFORM 
            or FIELD. The value of the *magnitudes* argument is a function of the 
            *crossSectionDistribution* argument, as shown in the following list: 
            - If *crossSectionDistribution*=CONSTANT_THROUGH_THICKNESS then *magnitudes* is a Double 
            specifying the temperature. 
            - If *crossSectionDistribution*=GRADIENTS_THROUGH_SHELL_CS then *magnitudes* is a 
            sequence of Doubles specifying the mean value and the gradient in the thickness 
            direction. 
            - If *crossSectionDistribution*=GRADIENTS_THROUGH_BEAM_CS then *magnitudes* is a 
            sequence of Doubles specifying the mean value, the gradient in the N1 direction, and the 
            gradient in the N2 direction. 
            - If *crossSectionDistribution*=POINTS_THROUGH_SECTION then *magnitudes* is a sequence 
            of Doubles specifying the temperature at each point. 
        absoluteExteriorTolerance
            A Float specifying the absolute value by which a driven node of the field can lie 
            outside the region of the elements of the global model. The default value is 0.0. This 
            argument cannot be used with *midside*. 
        exteriorTolerance
            A Float specifying the fraction of the average element size in the global model by which 
            a driven node of the field can lie outside the region of the elements of the global 
            model. The default value is 0.0. This argument cannot be used with *midside*. 

        Returns
        -------
            A Temperature object. 

        Exceptions
        ----------
            None. 
        """
        self.predefinedFields[name] = predefinedField = Temperature(name, createStepName, region, distributionType,
                                                                    crossSectionDistribution, field, amplitude,
                                                                    fileName, beginStep, beginIncrement, endStep,
                                                                    endIncrement, interpolate, magnitudes,
                                                                    absoluteExteriorTolerance, exteriorTolerance)
        return predefinedField

    def Velocity(self, name: str, region: Region, velocity1: float, velocity2: float, velocity3: float,
                 omega: float, axisBegin: tuple, axisEnd: tuple, field: str = '',
                 distributionType: SymbolicConstant = MAGNITUDE) -> Velocity:
        """This method creates a Velocity predefined field object.

        Path
        ----
            - mdb.models[name].Velocity

        Parameters
        ----------
        name
            A String specifying the repository key. 
        region
            A Region object specifying the region to which the predefined field is applied. 
        velocity1
            A Float specifying the first component of the velocity. 
        velocity2
            A Float specifying the second component of the velocity. 
        velocity3
            A Float specifying the third component of the velocity. 
        omega
            A Float specifying the angular velocity. 
        axisBegin
            A sequence of Floats specifying the *X-*, *Y-*, and *Z*- coordinates of the starting 
            point of the axis about which *omega* is defined. 
        axisEnd
            A sequence of Floats specifying the *X-*, *Y-*, and *Z*- coordinates of the end point of 
            the axis about which *omega* is defined. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            predefined field. The *field* argument applies only when 
            *distributionType*=FIELD_ANALYTICAL. The default value is an empty string. 
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE 
            and FIELD_ANALYTICAL. The default value is MAGNITUDE. 

        Returns
        -------
            A Velocity object. 

        Exceptions
        ----------
            None. 
        """
        self.predefinedFields[name] = predefinedField = Velocity(name, region, velocity1, velocity2, velocity3, omega,
                                                                 axisBegin, axisEnd, field, distributionType)
        return predefinedField

    def Part(self, name: str, dimensionality: SymbolicConstant, type: SymbolicConstant,
             twist: Boolean = OFF):
        """This method creates a Part object and places it in the parts repository.

        Path
        ----
            - mdb.models[name].Part

        Parameters
        ----------
        name
            A String specifying the repository key.
        dimensionality
            A SymbolicConstant specifying the dimensionality of the part. Possible values are
            THREE_D, TWO_D_PLANAR, and AXISYMMETRIC.
        type
            A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE_BODY,
            EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE.
        twist
            A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only
            available when *dimensionality*=AXISYMMETRIC and *type*=DEFORMABLE_BODY). The default
            value is OFF.

        Returns
        -------
            A Part object.

        Exceptions
        ----------
            InvalidNameError.
        """
        self.parts[name] = Part(name, dimensionality, type, twist)
        return self.parts[name]

    def Material(self, name: str, description: str = '', materialIdentifier: str = ''):
        """This method creates a Material object.

        Path
        ----
            - mdb.models[name].Material
            - session.odbs[name].Material

        Parameters
        ----------
        name
            A String specifying the name of the new material.
        description
            A String specifying user description of the material. The default value is an empty
            string.
        materialIdentifier
            A String specifying material identifier for customer use. The default value is an empty
            string.

        Returns
        -------
            A Material object.

        Exceptions
        ----------
            InvalidNameError.
        """
        self.materials[name] = material = Material(name, description, materialIdentifier)
        return material

    def FieldOutputRequest(self, name: str, createStepName: str, region: SymbolicConstant = MODEL,
                           variables: SymbolicConstant = PRESELECT, frequency: SymbolicConstant = 1,
                           modes: SymbolicConstant = ALL,
                           timeInterval: typing.Union[SymbolicConstant, float] = EVERY_TIME_INCREMENT,
                           numIntervals: int = 20, timeMarks: Boolean = OFF, boltLoad: str = '',
                           sectionPoints: SymbolicConstant = DEFAULT, interactions: str = None,
                           rebar: SymbolicConstant = EXCLUDE, filter: SymbolicConstant = None,
                           directions: Boolean = ON, fasteners: str = '', assembledFastener: str = '',
                           assembledFastenerSet: str = '', exteriorOnly: Boolean = OFF, layupNames: str = '',
                           layupLocationMethod: str = SPECIFIED, outputAtPlyTop: Boolean = False,
                           outputAtPlyMid: Boolean = True, outputAtPlyBottom: Boolean = False,
                           position: SymbolicConstant = INTEGRATION_POINTS):
        """This method creates a FieldOutputRequest object.

        Path
        ----
            - mdb.models[name].FieldOutputRequest

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the object is created.
        region
            The SymbolicConstant MODEL or a Region object specifying the region from which output is
            requested. The SymbolicConstant MODEL represents the whole model. The default value is
            MODEL.
        variables
            A sequence of Strings specifying output request variable or component names, or the
            SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
            the given step. ALL represents all valid output variables. The default value is
            PRESELECT.
        frequency
            The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in
            increments. The default value is 1.
        modes
            The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
            output is desired. The default value is ALL.
        timeInterval
            The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at
            which the output states are to be written. The default value is EVERY_TIME_INCREMENT.
        numIntervals
            An Int specifying the number of intervals during the step at which output database
            states are to be written. The default value is 20.
        timeMarks
            A Boolean specifying when to write results to the output database. OFF indicates that
            output is written immediately after the time dictated by the specified number of
            intervals. ON indicates that output is written at the exact times dictated by the
            specified number of intervals. The default value is OFF.
        boltLoad
            A String specifying a bolt load from which output is requested.
        sectionPoints
            The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
            which output requested. The default is DEFAULT.
        interactions
            None or a sequence of Strings specifying the interaction names. The default value is
            None.The sequence can contain only one String.
        rebar
            A SymbolicConstant specifying whether output is requested for rebar. Possible values are
            EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.
        filter
            The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
            object. The default value is None.
        directions
            A Boolean specifying whether to output directions of the local material coordinate
            system. The default value is ON.
        fasteners
            A String specifying the fastener name. The default value is an empty string.
        assembledFastener
            A String specifying the assembled fastener name. The default value is an empty string.
        assembledFastenerSet
            A String specifying the set name from the model referenced by the assembled fastener,
            *assembledFastener*. The default value is an empty string.
        exteriorOnly
            A Boolean specifying whether the output domain is restricted to the exterior of the
            model. This argument is only valid if *region*=MODEL. The default value is OFF.
        layupNames
            A List of Composite Layer Names.
        layupLocationMethod
            A Symbolic constant specifying the method used to indicate the output locations for
            composite layups. Possible values are ALL_LOCATIONS, SPECIFIED and TYPED_IN. The default
            value is SPECIFIED.
        outputAtPlyTop
            A Boolean specifying whether to output at the ply top section point. The default value
            is False.
        outputAtPlyMid
            A Boolean specifying whether to output at the ply mid section point. The default value
            is True.
        outputAtPlyBottom
            A Boolean specifying whether to output at the ply bottom section point. The default
            value is False.
        position
            A SymbolicConstant specifying the position on an element where output needs to be
            written. Possible values are INTEGRATION_POINTS, AVERAGED_AT_NODES, CENTROIDAL, and
            NODES. The default value is INTEGRATION_POINTS.

        Returns
        -------
            A FieldOutputRequest object.

        Exceptions
        ----------
            None.
        """
        self.fieldOutputRequests[name] = FieldOutputRequest(name, createStepName, region, variables, frequency, modes,
                                                            timeInterval, numIntervals, timeMarks, boltLoad,
                                                            sectionPoints, interactions, rebar, filter, directions,
                                                            fasteners, assembledFastener, assembledFastenerSet,
                                                            exteriorOnly, layupNames, layupLocationMethod,
                                                            outputAtPlyTop, outputAtPlyMid, outputAtPlyBottom, position)
        return self.fieldOutputRequests[name]

    def HistoryOutputRequest(self, name: str, createStepName: str, region: SymbolicConstant = MODEL,
                             variables: SymbolicConstant = PRESELECT, frequency: SymbolicConstant = 1,
                             modes: SymbolicConstant = ALL,
                             timeInterval: typing.Union[SymbolicConstant, float] = EVERY_TIME_INCREMENT,
                             numIntervals: int = 20, boltLoad: str = '', sectionPoints: SymbolicConstant = DEFAULT,
                             stepName: str = '', interactions: str = None, contourIntegral: str = None,
                             numberOfContours: int = 0, stressInitializationStep: str = None,
                             contourType: SymbolicConstant = J_INTEGRAL, kFactorDirection: SymbolicConstant = MTS,
                             rebar: SymbolicConstant = EXCLUDE, integratedOutputSection: str = '',
                             springs: tuple = None, filter: SymbolicConstant = None, fasteners: str = '',
                             assembledFastener: str = '', assembledFastenerSet: str = '', sensor: Boolean = OFF,
                             useGlobal: Boolean = True):
        """This method creates a HistoryOutputRequest object.

        Path
        ----
            - mdb.models[name].HistoryOutputRequest

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the object is created.
        region
            The SymbolicConstant MODEL or a Region object specifying the region from which output is
            requested. The SymbolicConstant MODEL represents the whole model. The default value is
            MODEL.If the region is a surface region, the surface must lie within the general contact
            surface domain.
        variables
            A sequence of Strings specifying output request variable or component names, or the
            SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
            the given step. ALL represents all valid output variables. The default value is
            PRESELECT.
        frequency
            The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in
            increments. The default value is 1.
        modes
            The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
            output is desired. The default value is ALL.
        timeInterval
            The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at
            which the output states are to be written. The default value is EVERY_TIME_INCREMENT.
        numIntervals
            An Int specifying the number of intervals during the step at which output database
            states are to be written. The default value is 20.
        boltLoad
            A String specifying a bolt load from which output is requested. The default value is an
            empty string.
        sectionPoints
            The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
            which output is requested. The default value is DEFAULT.
        stepName
            A String specifying the name of the step. The default value is an empty string.
        interactions
            None or a sequence of Strings specifying the interaction names. The default value is
            None.The sequence can contain only one String.
        contourIntegral
            A String specifying the contour integral name. The default value is None.
        numberOfContours
            An Int specifying the number of contour integrals to output for the contour integral
            object. The default value is 0.
        stressInitializationStep
            A String specifying the name of the stress initialization step. The default value is
            None.
        contourType
            A SymbolicConstant specifying the type of contour integral. Possible values are
            J_INTEGRAL, C_INTEGRAL, T_STRESS, and K_FACTORS. The default value is J_INTEGRAL.
        kFactorDirection
            A SymbolicConstant specifying the stress intensity factor direction. Possible values are
            MTS, MERR, and K110. The *kFactorDirection* argument is valid only if
            *contourType*=K_FACTORS. The default value is MTS.
        rebar
            A SymbolicConstant specifying whether output is requested for rebar. Possible values are
            EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.
        integratedOutputSection
            A String specifying the integrated output section. The default value is an empty string.
        springs
            A sequence of Strings specifying the springs/dashpots names. The default value is None.
            The sequence can contain only one String.
        filter
            The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
            object. The default value is None.
        fasteners
            A String specifying the fastener name. The default value is an empty string.
        assembledFastener
            A String specifying the assembled fastener name. The default value is an empty string.
        assembledFastenerSet
            A String specifying the set name from the model referenced by the assembled fastener,
            *assembledFastener*. The default value is an empty string.
        sensor
            A Boolean specifying whether to associate the output request with a sensor definition.
            The default value is OFF.
        useGlobal
            A Boolean specifying whether to output vector-valued nodal variables in the global
            directions. The default value is True.

        Returns
        -------
            A HistoryOutputRequest object.

        Exceptions
        ----------
            None.
        """
        self.historyOutputRequests[name] = HistoryOutputRequest(name, createStepName, region, variables, frequency,
                                                                modes, timeInterval, numIntervals, boltLoad,
                                                                sectionPoints, stepName, interactions, contourIntegral,
                                                                numberOfContours, stressInitializationStep, contourType,
                                                                kFactorDirection, rebar, integratedOutputSection,
                                                                springs, filter, fasteners, assembledFastener,
                                                                assembledFastenerSet, sensor, useGlobal)
        return self.historyOutputRequests[name]
