from .RayleighDampingByFrequencyComponentArray import RayleighDampingByFrequencyComponentArray


class RayleighDampingByFrequency:
    """A RayleighDampingByFrequency object contains Rayleigh Damping parameters.

    Attributes
    ----------
    components: RayleighDampingByFrequencyComponentArray
        A RayleighDampingByFrequencyComponentArray object.

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name].rayleighDampingByFrequency

    """

    # A RayleighDampingByFrequencyComponentArray object. 
    components: RayleighDampingByFrequencyComponentArray = RayleighDampingByFrequencyComponentArray()
