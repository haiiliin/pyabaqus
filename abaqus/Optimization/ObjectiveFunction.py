from abaqusConstants import *
from .OptimizationObjectiveArray import OptimizationObjectiveArray


class ObjectiveFunction:
    """The ObjectiveFunction object defines the objective of the optimization.

    Notes
    -----
        This object can be accessed by:
        - import optimization
        - mdb.models[name].optimizationTasks[name].objectiveFunctions[name]

    """
    # Optimization objectives
    objectives: OptimizationObjectiveArray = OptimizationObjectiveArray()

    def __init__(self, name: str, objectives: OptimizationObjectiveArray, target: SymbolicConstant = MINIMIZE):
        """This method creates an ObjectiveFunction object.

        Notes
        -----
            This function can be accessed by:
            -           mdb.models[name].optimizationTasks[name].ObjectiveFunction

        Parameters
        ----------
        name
            A String specifying the objective function repository key. 
        objectives
            An OptimizationObjectiveArray object. 
        target
            A SymbolicConstant specifying the target of the objective function. Possible values are 
            MINIMIZE, MAXIMIZE, and MINIMIZE_MAXIMUM. The default value is MINIMIZE. 

        Returns
        -------
            An ObjectiveFunction object.  and RangeError. 
        """
        pass

    def setValues(self, target: SymbolicConstant = MINIMIZE):
        """This method modifies the ObjectiveFunction object.

        Parameters
        ----------
        target
            A SymbolicConstant specifying the target of the objective function. Possible values are 
            MINIMIZE, MAXIMIZE, and MINIMIZE_MAXIMUM. The default value is MINIMIZE.

        Raises
        ------
            RangeError. 
        """
        pass
