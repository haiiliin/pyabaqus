from .StructuralDampingByFrequencyComponentArray import StructuralDampingByFrequencyComponentArray


class StructuralDampingByFrequency:
    """A StructuralDampingByFrequency object contains structural damping parameters.

    Attributes
    ----------
    components: StructuralDampingByFrequencyComponentArray
        A StructuralDampingByFrequencyComponentArray object.

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name].structuralDampingByFrequency

    """

    # A StructuralDampingByFrequencyComponentArray object. 
    components: StructuralDampingByFrequencyComponentArray = StructuralDampingByFrequencyComponentArray()
