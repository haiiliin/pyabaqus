from ..Assembly.AssemblyModel import AssemblyModel
from ..Amplitude.AmplitudeModel import AmplitudeModel
from ..BoundaryCondition.BoundaryConditionModel import BoundaryConditionModel
from ..Constraint.ConstraintModel import ConstraintModel
from ..Interaction.InteractionModel import InteractionModel
from ..LoadAndLoadCase.LoadModel import LoadModel
from ..Material.MaterialModel import MaterialModel
from ..PredefinedField.PredefinedFieldModel import PredefinedFieldModel
from ..Part.PartModel import PartModel
from ..Section.SectionModel import SectionModel
from ..Sketcher.SketchModel import SketchModel
from ..Step.StepModel import StepModel
from ..StepOutput.OutputModel import OutputModel


class PolarityAssignments:
    pass


class Model(AssemblyModel, AmplitudeModel, BoundaryConditionModel, ConstraintModel, InteractionModel, LoadModel,
            MaterialModel, PredefinedFieldModel, PartModel, SectionModel, SketchModel, StepModel, OutputModel):
    pass
