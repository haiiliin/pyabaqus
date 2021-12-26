from .RuleResult import RuleResult
from ..UtilityAndView.Repository import Repository


class AdaptivityIteration:

    """The AdaptivityIteration object contains information about a given iteration of the 
    varying topology adaptivity process (adaptive remeshing). 

    Access
    ------
        - import job
        - mdb.adaptivityProcesses[name].iterations[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A repository of RuleResult objects specifying the calculated results from sizing 
    # functions corresponding to the RemeshingRule objects for this iteration of an adaptivity 
    # process. 
    ruleResults: Repository[str, RuleResult] = None

    def __init__(self, iteration: str, jobName: str, modelName: str, odbPath: str, remeshingErrors: int):
        """This method creates an AdaptivityIteration object.

        Path
        ----
            - mdb.adaptivityProcesses[name].AdaptivityIteration

        Parameters
        ----------
        iteration
            An Int specifying the sequence number for this iteration in the adaptivity process. 
        jobName
            A String specifying the name of the job that was run for this iteration. 
        modelName
            A String specifying the name of the model that was analyzed and remeshed in this 
            iteration. 
        odbPath
            A String specifying the path to the ODB file that was created for this iteration. 
        remeshingErrors
            An Int specifying the number of part instances which generated errors while remeshing 
            the model in this iteration of the adaptivity process. 

        Returns
        -------
            An AdaptivityIteration object. 

        Exceptions
        ----------
            None. 
        """
        pass

