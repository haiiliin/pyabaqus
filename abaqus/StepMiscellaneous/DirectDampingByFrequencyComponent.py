class DirectDampingByFrequencyComponent:
    """A DirectDampingByFrequencyComponent object is used to define direct damping over a range
    of frequencies. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].directDampingByFrequency.components[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Float specifying the frequency value in cycles/time. 
    frequency: float = None

    # A Float specifying the fraction of critical damping. 
    fraction: float = None
