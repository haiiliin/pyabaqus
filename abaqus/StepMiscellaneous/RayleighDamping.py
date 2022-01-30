from .RayleighDampingComponentArray import RayleighDampingComponentArray


class RayleighDamping:
    """A RayleighDamping object contains Rayleigh Damping parameters.

    Attributes
    ----------
    components: RayleighDampingComponentArray
        A RayleighDampingComponentArray object.

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name].rayleighDamping

    """

    # A RayleighDampingComponentArray object. 
    components: RayleighDampingComponentArray = RayleighDampingComponentArray()
