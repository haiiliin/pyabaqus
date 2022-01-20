from abaqusConstants import *
from .OdbAnalysisError import OdbAnalysisError
from .OdbAnalysisWarning import OdbAnalysisWarning
from .OdbDiagnosticStep import OdbDiagnosticStep
from .OdbJobTime import OdbJobTime
from .OdbNumericalProblemSummary import OdbNumericalProblemSummary
from ..UtilityAndView.Repository import Repository


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
    analysisErrors: Repository[str, OdbAnalysisError] = Repository[str, OdbAnalysisError]()

    # A repository of OdbAnalysisWarning objects. 
    analysisWarnings: Repository[str, OdbAnalysisWarning] = Repository[str, OdbAnalysisWarning]()

    # A repository of OdbDiagnosticStep objects. 
    steps: Repository[str, OdbDiagnosticStep] = Repository[str, OdbDiagnosticStep]()

    # An OdbJobTime object. 
    jobTime: OdbJobTime = OdbJobTime()

    # An OdbNumericalProblemSummary object. 
    numericalProblemSummary: OdbNumericalProblemSummary = OdbNumericalProblemSummary()

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
