from .StructuralDampingComponentArray import StructuralDampingComponentArray


class StructuralDamping:
    """A StructuralDamping object contains structural damping parameters.

    Attributes
    ----------
    components: StructuralDampingComponentArray
        A StructuralDampingComponentArray object.

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name].structuralDamping

    """

    # A StructuralDampingComponentArray object. 
    components: StructuralDampingComponentArray = StructuralDampingComponentArray()
