from abaqusConstants import *
from .OdbDiagnosticAttempt import OdbDiagnosticAttempt
from ..UtilityAndView.Repository import Repository


class OdbDiagnosticIncrement:

    """The OdbDiagnosticIncrement object. 

    Access
    ------
        - import visualization
        - session.odbData[name].diagnosticData.steps[i].increments[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A repository of OdbDiagnosticAttempt objects. 
    attempts: Repository[str, OdbDiagnosticAttempt] = None

    # A float specifying the size of the initial increment. This attribute is read-only. 
    initialSize: str = ''

    # A boolean specifying whether the solution converged for the particular increment. This 
    # attribute is read-only. 
    isConverged: Boolean = OFF

    # An int specifying the number of attempts for the particular increment. This attribute is 
    # read-only. 
    numberOfAttempts: str = ''

    # An int specifying the number of element diagnostics encountered for the particular 
    # increment. This attribute is read-only. 
    numberOfElementDiagnostics: str = ''

    # A float specifying the size of the particular increment. This attribute is read-only. 
    size: str = ''

    # A float specifying the amount of step time completed in the particular increment. This 
    # attribute is read-only. 
    stepTimeCompleted: str = ''

