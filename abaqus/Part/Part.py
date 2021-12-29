from abaqusConstants import *
from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.Face import Face
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.Vertex import Vertex
from ..EditMesh.Part import Part as EditMeshPart
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshNode import MeshNode
from ..Mesh.Part import Part as MeshPart
from ..Property.SectionAssignment import SectionAssignment
from ..Region.Part import Part as RegionPart
from ..Region.Region import Region
from ..Region.Set import Set
from ..Region.Surface import Surface


class Part(EditMeshPart, MeshPart, RegionPart):

    def Surface(self, side1Faces: tuple[Face] = None, side2Faces: tuple[Face] = None, side12Faces: tuple[Face] = None,
                end1Edges: tuple[Face] = None, end2Edges: tuple[Face] = None, circumEdges: tuple[Face] = None,
                side1Edges: tuple[Face] = None, side2Edges: tuple[Face] = None, face1Elements: tuple[Face] = None,
                face2Elements: tuple[Face] = None, face3Elements: tuple[Face] = None, face4Elements: tuple[Face] = None,
                face5Elements: tuple[Face] = None, face6Elements: tuple[Face] = None, side1Elements: tuple[Face] = None,
                side2Elements: tuple[Face] = None, side12Elements: tuple[Face] = None, end1Elements: tuple[Face] = None,
                end2Elements: tuple[Face] = None, circumElements: tuple[Face] = None, name: str = ''):
        """This method creates a surface from a sequence of objects in a model database. The
        surface will apply to the sides specified by the arguments.For example
        surface=mdb.models['Model-1'].parts['Part-1'].Surface(side1Faces=side1Faces,
        name='Surf-1')

        Path
        ----
            - mdb.models[*name*].parts[*name*].Surface
            - mdb.models[*name*].rootAssembly.Surface

        Parameters
        ----------
                side1Faces
                side2Faces
                side12Faces
            On three-dimensional wire edges, you can use the following arguments:
                end1Edges
                end2Edges
                circumEdges
            On three-dimensional or two-dimensional or axisymmetric edges, you can use the following arguments:
                side1Edges
                side2Edges
            On two-dimensional or axisymmetric shell elements, you can use the following arguments:
                face1Elements
                face2Elements
                face3Elements
                face4Elements
                face5Elements
                face6Elements
            On three-dimensional shell elements, you can use the following arguments:
                side1Elements
                side2Elements
                side12Elements
            On three-dimensional wire elements, you can use the following arguments:
                end1Elements
                end2Elements
                circumElements
            On two-dimensional or axisymmetric wire elements, you can use the following arguments:
        name
            A String specifying the repository key. The default value is an empty string.

        Returns
        -------
            A Surface object.

        Exceptions
        ----------
            InvalidNameError.
        """
        surface = Surface(side1Faces, side2Faces, side12Faces, end1Edges, end2Edges, circumEdges, side1Edges,
                          side2Edges, face1Elements, face2Elements, face3Elements, face4Elements, face5Elements,
                          face6Elements, side1Elements, side2Elements, side12Elements, end1Elements, end2Elements,
                          circumElements, name)
        self.surfaces[name] = surface
        self.allSurfaces[name] = surface
        return surface

    def Set(self, name: str, nodes: tuple[MeshNode] = None, elements: tuple[MeshElement] = None,
            region: Region = None, vertices: tuple[Vertex] = None, edges: tuple[Edge] = None,
            faces: tuple[Face] = None, cells: tuple[Cell] = None, xVertices: tuple[Vertex] = None,
            xEdges: tuple[Edge] = None, xFaces: tuple[Face] = None,
            referencePoints: tuple[ReferencePoint] = (), skinFaces: tuple = (),
            skinEdges: tuple = (), stringerEdges: tuple = ()):
        """This method creates a set from a sequence of objects in a model database.

        Path
        ----
            - mdb.models[*name*].parts[*name*].Set
            - mdb.models[*name*].rootAssembly.Set

        Parameters
        ----------
        name
            A String specifying the repository key.
        nodes
            A sequence of MeshNode objects. The default value is None.
        elements
            A sequence of MeshElement objects. The default value is None.
        region
            A Region object specifying other objects to be included in the set. The default value is
            None.
        vertices
            A sequence of ConstrainedSketchVertex objects. The default value is None.
        edges
            A sequence of Edge objects. The default value is None.
        faces
            A sequence of Face objects. The default value is None.
        cells
            A sequence of Cell objects. The default value is None.
        xVertices
            A sequence of ConstrainedSketchVertex objects that excludes specific vertices from the set. The default
            value is None.
        xEdges
            A sequence of Edge objects that excludes specific edges from the set. The default value
            is None.
        xFaces
            A sequence of Face objects that excludes specific faces from the set. The default value
            is None.
        referencePoints
            A sequence of ReferencePoint objects. The default value is an empty sequence.
        skinFaces
            A tuple of tuples specifying a skin name and the sequence of faces associated with this
            skin. Valid only for geometric regions on 3D and 2D parts.
        skinEdges
            A tuple of tuples specifying a skin name and the sequence of edges associated with this
            skin. Valid only for geometric regions on Axisymmetric parts.
        stringerEdges
            A tuple of tuples specifying a stringer name and the sequence of edges associated with
            this stringer. Valid only for geometric regions on 3D and 2D parts.

        Returns
        -------
            A Set object.

        Exceptions
        ----------
            InvalidNameError.
        """
        aSet = Set(name, nodes, elements, region, vertices, edges, faces, cells, xVertices, xEdges, xFaces,
                   referencePoints, skinFaces, skinEdges, stringerEdges)
        self.sets[name] = aSet
        self.allSets[name] = aSet
        return aSet

    def SectionAssignment(self, region: Set, sectionName: str, thicknessAssignment: SymbolicConstant = FROM_SECTION,
                          offset: float = 0, offsetType: SymbolicConstant = SINGLE_VALUE, offsetField: str = ''):
        """This method creates a SectionAssignment object.

        Path
        ----
            - mdb.models[*name*].parts[*name*].SectionAssignment
            - mdb.models[*name*].rootAssembly.SectionAssignment

        Parameters
        ----------
        region
            A Set object specifying the region to which the section is assigned.
        sectionName
            A String specifying the name of the section.
        thicknessAssignment
            A SymbolicConstant specifying section thickness assignment method. Possible values are
            FROM_SECTION and FROM_GEOMETRY. The default value is FROM_SECTION.
        offset
            A Float specifying the offset of the shell section. The default value is 0.0.
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If
            *offsetType* is set to OFFSET_FIELD the *offsetField* must have a value. Possible values
            are SINGLE_VALUE, MIDDLE_SURFACE, TOP_SURFACE, BOTTOM_SURFACE, FROM_GEOMETRY, and
            OFFSET_FIELD. The default value is SINGLE_VALUE.
        offsetField
            A String specifying the name of the field specifying the offset. The default value is
            "".

        Returns
        -------
            A SectionAssignment object.

        Exceptions
        ----------
            None.
        """
        sectionAssignment = SectionAssignment(region, sectionName, thicknessAssignment, offset, offsetType, offsetField)
        self.sectionAssignments.append(sectionAssignment)
        return sectionAssignment

