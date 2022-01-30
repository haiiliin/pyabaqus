from .DirectDampingByFrequencyComponentArray import DirectDampingByFrequencyComponentArray


class DirectDampingByFrequency:
    """A DirectDampingByFrequency object contains direct damping parameters.

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name].directDampingByFrequency

    """

    # A DirectDampingByFrequencyComponentArray object. 
    components: DirectDampingByFrequencyComponentArray = DirectDampingByFrequencyComponentArray()
