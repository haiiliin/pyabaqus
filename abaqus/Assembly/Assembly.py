from ..EditMesh.Assembly import Assembly as EditMeshAssembly
from ..Mesh.Assembly import Assembly as MeshAssembly
from ..Region.Assembly import Assembly as RegionAssembly


class Assembly(EditMeshAssembly, MeshAssembly, RegionAssembly):
    pass
