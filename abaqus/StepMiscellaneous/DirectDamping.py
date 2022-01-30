from .DirectDampingComponentArray import DirectDampingComponentArray


class DirectDamping:
    """A DirectDamping object contains direct modal damping parameters.

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name].directDamping

    """

    # A DirectDampingComponentArray object. 
    components: DirectDampingComponentArray = DirectDampingComponentArray()
