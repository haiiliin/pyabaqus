

class RayleighDampingByFrequencyComponent:

    """A RayleighDampingByFrequencyComponent object is used to define Rayleigh damping over a 
    range of frequencies. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].rayleighDampingByFrequency.components[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Float specifying the frequency value in cycles/time. 
    frequency: float = None

    # A Float specifying the mass proportional damping, αM. 
    alpha: float = None

    # A Float specifying the stiffness proportional damping, βM. 
    beta: float = None

