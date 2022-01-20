class CompositeDampingComponent:
    """A CompositeDampingComponent object is used to define composite damping over a range of
    modes. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].compositeDamping.components[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the mode number of the lowest mode of a range. 
    start: int = None

    # An Int specifying the mode number of the highest mode of a range. 
    end: int = None
