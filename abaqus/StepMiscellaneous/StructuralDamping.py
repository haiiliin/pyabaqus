from .StructuralDampingComponentArray import StructuralDampingComponentArray

class StructuralDamping:

    """A StructuralDamping object contains structural damping parameters. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].structuralDamping

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A StructuralDampingComponentArray object. 
    components: StructuralDampingComponentArray = StructuralDampingComponentArray()

