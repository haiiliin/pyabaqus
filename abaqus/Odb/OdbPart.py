import typing

from abaqusConstants import *
from .AnalyticSurface import AnalyticSurface
from .AnalyticSurfaceSegment import AnalyticSurfaceSegment
from .BeamOrientationArray import BeamOrientationArray
from .OdbDatumCsys import OdbDatumCsys
from .OdbMeshElementArray import OdbMeshElementArray
from .OdbMeshNodeArray import OdbMeshNodeArray
from .OdbRigidBodyArray import OdbRigidBodyArray
from .OdbSet import OdbSet
from .RebarOrientationArray import RebarOrientationArray
from .SectionCategory import SectionCategory
from ..Property.MaterialOrientationArray import MaterialOrientationArray
from ..Property.SectionAssignmentArray import SectionAssignmentArray
from ..UtilityAndView.Repository import Repository


class OdbPart:

    """The OdbPart object is similar to the kernel Part object and contains nodes and elements, 
    but not geometry. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].parts[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An OdbMeshNodeArray object. 
    nodes: OdbMeshNodeArray = OdbMeshNodeArray()

    # An OdbMeshElementArray object. 
    elements: OdbMeshElementArray = OdbMeshElementArray()

    # A repository of OdbSet objects specifying node sets. 
    nodeSets: Repository[str, OdbSet] = Repository[str, OdbSet]()

    # A repository of OdbSet objects specifying element sets. 
    elementSets: Repository[str, OdbSet] = Repository[str, OdbSet]()

    # A repository of OdbSet objects specifying surfaces. 
    surfaces: Repository[str, OdbSet] = Repository[str, OdbSet]()

    # A SectionAssignmentArray object. 
    sectionAssignments: SectionAssignmentArray = SectionAssignmentArray()

    # A BeamOrientationArray object. 
    beamOrientations: BeamOrientationArray = BeamOrientationArray()

    # A MaterialOrientationArray object. 
    materialOrientations: MaterialOrientationArray = MaterialOrientationArray()

    # A RebarOrientationArray object. 
    rebarOrientations: RebarOrientationArray = RebarOrientationArray()

    # An OdbRigidBodyArray object. 
    rigidBodies: OdbRigidBodyArray = OdbRigidBodyArray()

    # An AnalyticSurface object specifying analytic Surface defined on the instance. 
    analyticSurface: AnalyticSurface = AnalyticSurface()

    def Part(self, name: str, embeddedSpace: SymbolicConstant, type: SymbolicConstant):
        """This method creates an OdbPart object. Nodes and elements are added to this object at a
        later stage.

        Path
        ----
            - session.odbs[name].Part

        Parameters
        ----------
        name
            A String specifying the part name. 
        embeddedSpace
            A SymbolicConstant specifying the dimensionality of the Part object. Possible values are 
            THREE_D, TWO_D_PLANAR, and AXISYMMETRIC. 
        type
            A SymbolicConstant specifying the type of the Part object. Possible values are 
            DEFORMABLE_BODY and ANALYTIC_RIGID_SURFACE. 

        Returns
        -------
            An OdbPart object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def addElements(self, labels: tuple, connectivity: tuple, type: str, elementSetName: str = '', 
                    sectionCategory: SectionCategory = SectionCategory()):
        """This method adds elements to an OdbPart object using element labels and nodal
        connectivity.
        Warning:Adding elements not in ascending order of their labels may cause Abaqus/Viewer
        to plot contours incorrectly.

        Parameters
        ----------
        labels
            A sequence of Ints specifying the element labels. 
        connectivity
            A sequence of sequences of Ints specifying the nodal connectivity. 
        type
            A String specifying the element type. 
        elementSetName
            A String specifying a name for this element set. The default value is the empty string. 
        sectionCategory
            A SectionCategory object for this element set. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def addElements(self, elementData: tuple, type: str, elementSetName: str = None, 
                    sectionCategory: SectionCategory = SectionCategory()):
        """This method adds elements to an OdbPart object using a sequence of element labels and
        nodal connectivity.
        Warning:Adding elements not in ascending order of their labels may cause Abaqus/Viewer
        to plot contours incorrectly.

        Parameters
        ----------
        elementData
            A sequence of sequences of Ints specifying the element labels and nodal connectivity, in 
            the form ((*label*, *c1*, *c2*, *c3*, *c4*), (*label*, *c1*, *c2*, *c3*, *c4*), ...). 
        type
            A String specifying the element type. The value can be user defined. 
        elementSetName
            A String specifying a name for this element set. The default value is None. 
        sectionCategory
            A SectionCategory object for this element set. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def addElements(self, *args, **kwargs):
        pass

    @typing.overload
    def addNodes(self, labels: tuple, coordinates: tuple, nodeSetName: str = None):
        """This method adds nodes to an OdbPart object using node labels and coordinates.
        Warning:Adding nodes not in ascending order of their labels may cause Abaqus/Viewer to
        plot contours incorrectly.

        Parameters
        ----------
        labels
            A sequence of Ints specifying the node labels. 
        coordinates
            A sequence of sequences of Floats specifying the nodal coordinates. 
        nodeSetName
            A String specifying a name for this node set. The default value is None. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def addNodes(self, nodeData: tuple, nodeSetName: str = None):
        """This method adds nodes to an OdbPart object using a sequence of node labels and
        coordinates.
        Warning:Adding nodes not in ascending order of their labels may cause Abaqus/Viewer to
        plot contours incorrectly.

        Parameters
        ----------
        nodeData
            A sequence of tuples specifying the node labels and coordinates, in the form ((*label*, 
            *x*, *y*, *z*), (*label*, *x*, *y*, *z*), ...). 
        nodeSetName
            A String specifying a name for this node set. The default value is None. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def addNodes(self, *args, **kwargs):
        pass

    def assignBeamOrientation(self, region: str, method: SymbolicConstant, vector: tuple):
        """This method assigns a beam section orientation to a region of a part instance.

        Parameters
        ----------
        region
            An OdbSet specifying a region on an instance. 
        method
            A SymbolicConstant specifying the assignment method. Only a value of N1_COSINES is 
            currently supported. 
        vector
            A sequence of three Floats specifying the approximate local  n1n1 -direction of the beam 
            cross-section. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def assignMaterialOrientation(self, region: str, localCSys: OdbDatumCsys, axis: SymbolicConstant = AXIS_1, angle: float = 0, 
                                  stackDirection: SymbolicConstant = STACK_3):
        """This method assigns a material orientation to a region of a part instance.

        Parameters
        ----------
        region
            An OdbSet specifying a region on an instance. 
        localCSys
            An OdbDatumCsys object specifying the local coordinate system or None, indicating the 
            global coordinate system. 
        axis
            A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate 
            system about which an additional rotation is applied. For shells this axis is also the 
            shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is 
            AXIS_1. 
        angle
            A Float specifying the angle of the additional rotation. The default value is 0.0. 
        stackDirection
            A SymbolicConstant specifying the stack or thickness direction of the material. Possible 
            values are STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is 
            STACK_3. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def assignRebarOrientation(self, region: str, localCsys: OdbDatumCsys, axis: SymbolicConstant = AXIS_1, angle: float = 0):
        """This method assigns a rebar reference orientation to a region of a part instance.

        Parameters
        ----------
        region
            An OdbSet specifying a region on an instance. 
        localCsys
            An OdbDatumCsys object specifying the local coordinate system or None, indicating the 
            global coordinate system. 
        axis
            A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate 
            system about which an additional rotation is applied. For shells this axis is also the 
            shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is 
            AXIS_1. 
        angle
            A Float specifying the angle of the additional rotation. The default value is 0.0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getElementFromLabel(self, label: int):
        """This method is used to retrieved an element with a specific label from a part object.

        Parameters
        ----------
        label
            An Int specifying the element label. 

        Returns
        -------
            An OdbMeshElement object. 

        Exceptions
        ----------
            - If no element with the specified label exists: 
              OdbError: Invalid element label 
        """
        pass

    def getNodeFromLabel(self, label: int):
        """This method is used to retrieved a node with a specific label from a part object.

        Parameters
        ----------
        label
            An Int specifying the node label. 

        Returns
        -------
            An OdbMeshNode object. 

        Exceptions
        ----------
            - If no node with the specified label exists: 
              OdbError: Invalid node label 
        """
        pass

    def AnalyticRigidSurf2DPlanar(self, name: str, profile: tuple[AnalyticSurfaceSegment], filletRadius: str = 0):
        """This method is used to define a two-dimensional AnalyticSurface object on the part
        object.

        Parameters
        ----------
        name
            The name of the analytic surface. 
        profile
            A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment 
            object. 
        filletRadius
            A Double specifying the radius of curvature to smooth discontinuities between adjoining 
            segments. The default value is 0.0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            - If OdbPart is of type THREE_D: 
              OdbError: 2D-Planar Analytic Rigid Surface can be defined only if the part is of type 
            TWO_D_PLANAR or AXISYMMETRIC. 
        """
        pass

    def AnalyticRigidSurfExtrude(self, name: str, profile: tuple[AnalyticSurfaceSegment], filletRadius: str = 0):
        """This method is used to define a three-dimensional cylindrical AnalyticSurface on the
        part object.

        Parameters
        ----------
        name
            The name of the analytic surface. 
        profile
            A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment 
            object. 
        filletRadius
            A Double specifying the radius of curvature to smooth discontinuities between adjoining 
            segments. The default value is 0.0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            - If OdbPart is not of type THREE_D: 
              OdbError: Analytic Rigid Surface of type CYLINDER can be defined only if the part is 
            of type THREE_D. 
        """
        pass

    def AnalyticRigidSurfRevolve(self, name: str, profile: tuple[AnalyticSurfaceSegment], filletRadius: str = 0):
        """This method is used to define a three-dimensional AnalyticSurface of revolution on the
        part object.

        Parameters
        ----------
        name
            The name of the analytic surface. 
        profile
            A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment 
            object. 
        filletRadius
            A Double specifying the radius of curvature to smooth discontinuities between adjoining 
            segments. The default value is 0.0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            - If OdbPart is not of type THREE_D: 
              OdbError: Analytic Rigid Surface of type REVOLUTION can be defined only if the part is 
            of type THREE_D. 
        """
        pass

    def RigidBody(self, referenceNode: str, position: str = INPUT, isothermal: Boolean = OFF, elset: str = '', 
                  pinNodes: str = '', tieNodes: str = '', analyticSurface: str = ''):
        """This method defines an OdbRigidBody on the part object.

        Parameters
        ----------
        referenceNode
            An OdbSet specifying the reference node assigned to the rigid body. 
        position
            A symbolic constant specify if the location of the reference node is to be defined by 
            the user. Possible values are INPUT and CENTER_OF_MASS. The default value is INPUT. 
        isothermal
            A Boolean specifying an isothermal rigid body. The default value is OFF. This parameter 
            is used only for a fully-coupled thermal stress analysis. 
        elset
            An OdbSet specifying an element set assigned to the rigid body. 
        pinNodes
            An OdbSet specifying pin-type nodes assigned to the rigid body. 
        tieNodes
            An OdbSet specifying tie-type nodes assigned to the rigid body. 
        analyticSurface
            An AnalyticSurface specifying the Analytic Rigid Surface assigned to the rigid body. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            - If *referenceNode* is not a node set: 
              OdbError: Rigid body definition requires a node set. 
        """
        pass

