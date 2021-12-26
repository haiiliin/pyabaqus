import typing

from abaqusConstants import *
from .HistoryOutput import HistoryOutput
from .HistoryPoint import HistoryPoint
from ..UtilityAndView.Repository import Repository


class HistoryRegion:

    """The HistoryRegion object contains history data for a single location in the model. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].steps[name].historyRegions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the position of the history output. Possible values are 
    # NODAL, INTEGRATION_POINT, WHOLE_ELEMENT, WHOLE_REGION, and WHOLE_MODEL. 
    position: SymbolicConstant = None

    # A repository of HistoryOutput objects. 
    historyOutputs: Repository[str, HistoryOutput] = Repository[str, HistoryOutput]()

    def __init__(self, name: str, description: str, point: HistoryPoint, loadCase: str = None):
        """This method creates a HistoryRegion object.

        Path
        ----
            - session.odbs[name].steps[name].HistoryRegion

        Parameters
        ----------
        name
            A String specifying the name of the HistoryRegion object. 
        description
            A String specifying the description of the HistoryRegion object. 
        point
            A HistoryPoint object specifying the point to which the history data refer. 
        loadCase
            None or an OdbLoadCase object specifying the load case associated with the HistoryRegion 
            object. The default value is None. 

        Returns
        -------
            A HistoryRegion object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def getSubset(self, variableName: str):
        """This method returns a subset of the data in the HistoryRegion object.

        Parameters
        ----------
        variableName
            A String specifying the name of the output variable to return. 

        Returns
        -------
            A HistoryRegion object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def getSubset(self, start: float):
        """This method returns a subset of the data in the HistoryRegion object.

        Parameters
        ----------
        start
            A Float specifying the start of the subset. This is the same as the first item in the 
            data array member of the HistoryOutput object. 

        Returns
        -------
            A HistoryRegion object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def getSubset(self, start: float, end: float):
        """This method returns a subset of the data in the HistoryRegion object.

        Parameters
        ----------
        start
            A Float specifying the start of the subset. This is the same as the first item in the 
            data array member of the HistoryOutput object. 
        end
            A Float specifying the end of the subset. 

        Returns
        -------
            A HistoryRegion object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getSubset(self, *args, **kwargs):
        pass

