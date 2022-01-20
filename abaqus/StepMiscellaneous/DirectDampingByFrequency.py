from .DirectDampingByFrequencyComponentArray import DirectDampingByFrequencyComponentArray


class DirectDampingByFrequency:
    """A DirectDampingByFrequency object contains direct damping parameters.

    Access
    ------
        - import step
        - mdb.models[name].steps[name].directDampingByFrequency

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A DirectDampingByFrequencyComponentArray object. 
    components: DirectDampingByFrequencyComponentArray = DirectDampingByFrequencyComponentArray()
