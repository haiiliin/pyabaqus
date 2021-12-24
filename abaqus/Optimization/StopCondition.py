from abaqusConstants import *

class StopCondition:

    """The StopCondition object is the abstract base type for other StopCondition objects. The 
    StopCondition object has no explicit constructor. The methods and members of the 
    StopCondition object are common to all objects derived from StopCondition. 

    Access
    ------
        - import optimization
        - mdb.models[name].optimizationTasks[name].stopConditions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the stop condition repository key. 
    name: str = ''

    # The SymbolicConstant MODEL or a Region object specifying the region to which the stop 
    # condition is applied. The default value is MODEL. 
    region: SymbolicConstant = MODEL

