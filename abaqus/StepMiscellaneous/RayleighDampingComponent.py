class RayleighDampingComponent:
    """A RayleighDampingComponent object is used to define Rayleigh damping over a range of
    modes. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].rayleighDamping.components[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the mode number of the lowest mode of a range. 
    start: int = None

    # An Int specifying the mode number of the highest mode of a range. 
    end: int = None

    # A Float specifying the mass proportional damping, αM. 
    alpha: float = None

    # A Float specifying the stiffness proportional damping, βM. 
    beta: float = None
