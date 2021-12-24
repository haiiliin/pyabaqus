

class StructuralDampingByFrequencyComponent:

    """A StructuralDampingByFrequencyComponent object is used to define structural damping over 
    a range of frequencies. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].structuralDampingByFrequency.components[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Float specifying the frequency value in cycles/time. 
    frequency: float = None

    # A Float specifying the damping factor, s. 
    factor: float = None

