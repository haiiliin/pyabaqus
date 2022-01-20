class OdbJobTime:
    """The OdbJobTime object stores the analysis time of a job.

    Access
    ------
        - import visualization
        - session.odbData[name].diagnosticData.jobTime

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A float specifying the systemtime for the analysis. This attribute is read-only. 
    systemTime: str = ''

    # A float specifying the usertime for the analysis. This attribute is read-only. 
    userTime: str = ''

    # A float specifying the wallclocktime for the analysis. This attribute is read-only. 
    wallclockTime: str = ''
