from .DirectDampingComponentArray import DirectDampingComponentArray

class DirectDamping:

    """A DirectDamping object contains direct modal damping parameters. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].directDamping

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A DirectDampingComponentArray object. 
    components: DirectDampingComponentArray = DirectDampingComponentArray()

