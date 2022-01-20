from ..EditMesh.MeshEditPart import MeshEditPart
from ..Mesh.MeshPart import MeshPart
from ..Property.PropertyPart import PropertyPart
from ..Region.RegionPart import RegionPart


class Part(MeshEditPart, MeshPart, PropertyPart, RegionPart):
    pass
