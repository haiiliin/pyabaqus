from ..UtilityAndView.Repository import Repository
from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .StopCondition import StopCondition
from abaqusConstants import *

class OptimizationTask:

    """The OptimizationTask object is the abstract base type for other OptimizationTask 
    objects. The OptimizationTask object has no explicit constructor. The methods and 
    members of the OptimizationTask object are common to all objects derived from 
    OptimizationTask. 

    Access
    ------
        - import optimization
        - mdb.models[name].optimizationTasks[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the optimization task repository key. 
    name: str = ''

    # The SymbolicConstant MODEL or a Region object specifying the region to which the 
    # optimization task is applied. The default value is MODEL. 
    region: SymbolicConstant = MODEL

    # A repository of DesignResponse objects. 
    designResponses: Repository[str, DesignResponse] = None

    # A repository of ObjectiveFunction objects. 
    objectiveFunctions: Repository[str, ObjectiveFunction] = None

    # A repository of OptimizationConstraint objects. 
    optimizationConstraints: Repository[str, OptimizationConstraint] = None

    # A repository of GeometricRestriction objects. 
    geometricRestrictions: Repository[str, GeometricRestriction] = None

    # A repository of StopCondition objects. 
    stopConditions: Repository[str, StopCondition] = None

