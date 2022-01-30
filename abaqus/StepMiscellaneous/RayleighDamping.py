from .RayleighDampingComponentArray import RayleighDampingComponentArray


class RayleighDamping:
    """A RayleighDamping object contains Rayleigh Damping parameters.

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name].rayleighDamping

    """

    # A RayleighDampingComponentArray object. 
    components: RayleighDampingComponentArray = RayleighDampingComponentArray()
