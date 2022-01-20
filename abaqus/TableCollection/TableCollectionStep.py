from abaqus.Step.StepBase import StepBase
from abaqus.TableCollection.ActivateElements import ActivateElements


class TableCollectionStep(StepBase):

    def ActivateElements(self, tableCollection: str, activation: str, eigenTimeConst: str = '',
                         expansionTimeConstant: str = '') -> ActivateElements:
        """This method creates an ActivateElements object.

        Path
        ----
            - mdb.models[name].ActivateElements

        Parameters
        ----------
        tableCollection
            A String specifying the name of the tableCollection object.
        activation
            A string specifying the name of progressive element activation.
        eigenTimeConst
            A Double specifying the time constant used to ramp up the eigenstrains at element
            activation.
        expansionTimeConstant
            A Double specifying the time constant used to ramp up the thermal strains at element
            activation.

        Returns
        -------
            An ActivateElements object.

        Exceptions
        ----------
            RangeError.
        """
        self.activateElements['activation'] = activateElements = ActivateElements(tableCollection, activation,
                                                                                  eigenTimeConst, expansionTimeConstant)
        return activateElements
