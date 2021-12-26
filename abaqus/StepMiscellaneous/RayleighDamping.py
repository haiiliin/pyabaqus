from .RayleighDampingComponentArray import RayleighDampingComponentArray

class RayleighDamping:

    """A RayleighDamping object contains Rayleigh Damping parameters. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].rayleighDamping

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A RayleighDampingComponentArray object. 
    components: RayleighDampingComponentArray = RayleighDampingComponentArray()

