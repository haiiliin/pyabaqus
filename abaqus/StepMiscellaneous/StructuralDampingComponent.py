class StructuralDampingComponent:
    """A StructuralDampingComponent object is used to define structural damping over a range of
    modes. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].structuralDamping.components[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the mode number of the lowest mode of a range. 
    start: int = None

    # An Int specifying the mode number of the highest mode of a range. 
    end: int = None

    # A Float specifying the damping factor, s. 
    factor: float = None
