from .OdbMeshNode import OdbMeshNode
from .OdbSet import OdbSet


class OdbPretensionSection:
    """The pretension section object is used to define an assembly load. It associates a
    pretension node with a pretension section. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].rootAssembly.pretensionSections[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An OdbSet object specifying the node set containing the pretension node. 
    node: OdbSet = OdbSet('set', tuple[OdbMeshNode]())

    # An OdbSet object specifying the element set that defines the pretension section. 
    element: OdbSet = OdbSet('set', tuple[OdbMeshNode]())

    # An OdbSet object specifying the surface set that defines the pretension section. 
    surface: OdbSet = OdbSet('set', tuple[OdbMeshNode]())

    # A tuple of Floats specifying the components of the normal to the pretension section. 
    normal: float = None
