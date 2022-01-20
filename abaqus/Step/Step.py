from ..Adaptivity.AdaptivityStep import AdaptivityStep
from ..StepOutput.OutputStep import OutputStep
from ..TableCollection.TableCollectionStep import TableCollectionStep


class Step(AdaptivityStep, OutputStep, TableCollectionStep):
    pass
