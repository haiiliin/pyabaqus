from ..UtilityAndView.Repository import Repository
from .OdbAnalysisError import OdbAnalysisError
from .OdbAnalysisWarning import OdbAnalysisWarning
from .OdbDiagnosticStep import OdbDiagnosticStep
from .OdbJobTime import OdbJobTime
from .OdbNumericalProblemSummary import OdbNumericalProblemSummary
from abaqusConstants import *

class OdbDiagnosticData:

    """The OdbDiagnosticData object. 

    Access
    ------
        - import visualization
        - session.odbData[name].diagnosticData

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A repository of OdbAnalysisError objects. 
    analysisErrors: Repository[str, OdbAnalysisError] = None

    # A repository of OdbAnalysisWarning objects. 
    analysisWarnings: Repository[str, OdbAnalysisWarning] = None

    # A repository of OdbDiagnosticStep objects. 
    steps: Repository[str, OdbDiagnosticStep] = None

    # An OdbJobTime object. 
    jobTime: OdbJobTime = None

    # An OdbNumericalProblemSummary object. 
    numericalProblemSummary: OdbNumericalProblemSummary = None

    # A boolean specifying whether or not double precision is used for the analysis. This 
    # attribute is read-only. 
    isXplDoublePrecision: Boolean = OFF

    # A String specifying the job status after the analysis. This attribute is read-only. 
    jobStatus: str = ''

    # An int specifying the number of domains. This attribute is read-only. 
    numDomains: str = ''

    # An int specifying the number of analysis errors encountered. This attribute is 
    # read-only. 
    numberOfAnalysisErrors: str = ''

    # An int specifying the number of analysis warnings encountered. This attribute is 
    # read-only. 
    numberOfAnalysisWarnings: str = ''

    # An int specifying the number of steps present in the analysis. This attribute is 
    # read-only. 
    numberOfSteps: str = ''

