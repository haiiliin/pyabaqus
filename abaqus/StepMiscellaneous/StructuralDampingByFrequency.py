from .StructuralDampingByFrequencyComponentArray import StructuralDampingByFrequencyComponentArray

class StructuralDampingByFrequency:

    """A StructuralDampingByFrequency object contains structural damping parameters. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].structuralDampingByFrequency

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A StructuralDampingByFrequencyComponentArray object. 
    components: StructuralDampingByFrequencyComponentArray = None

