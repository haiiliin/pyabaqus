from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.FaceArray import FaceArray
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshNodeArray import MeshNodeArray
from abaqusConstants import *

class Surface:

    """The Surface object stores surfaces selected from the assembly. A surface is comprised of 
    geometric or discrete entities but not both. An instance of a Surface object is 
    available from the *surface* member of the Assembly object. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].allInternalSurfaces[name]
        - mdb.models[name].parts[name].allSurfaces[name]
        - mdb.models[name].parts[name].surfaces[name]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].surfaces[name]
        - mdb.models[name].rootAssembly.allInternalSurfaces[name]
        - mdb.models[name].rootAssembly.allSurfaces[name]
        - mdb.models[name].rootAssembly.instances[name].surfaces[name]
        - mdb.models[name].rootAssembly.modelInstances[i].surfaces[name]
        - mdb.models[name].rootAssembly.surfaces[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An EdgeArray object. 
    edges: EdgeArray = None

    # A FaceArray object. 
    faces: FaceArray = None

    # A MeshElementArray object. 
    elements: MeshElementArray = None

    # A MeshNodeArray object. 
    nodes: MeshNodeArray = None

    # A tuple of SymbolicConstants specifying the sides; for example, (SIDE1, SIDE2). 
    sides: SymbolicConstant = None

    # A tuple of Ints specifying the instances. This member is not applicable for a Surface 
    # object on an output database. 
    instances: int = None

    def __init__(self, name: str, objectToCopy: 'Surface'):
        """This method copies a surface from an existing surface.

        Path
        ----
            - mdb.models[*name*].parts[*name*].Surface
            - mdb.models[*name*].rootAssembly.Surface

        Parameters
        ----------
        name
            A String specifying the name of the surface. 
        objectToCopy
            A Surface object to be copied. 

        Returns
        -------
            A Surface object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def SurfaceByBoolean(self, name: str, surfaces: tuple[Surface], operation: SymbolicConstant = UNION):
        """This method creates a surface by performing a boolean operation on two or more input
        surfaces.

        Path
        ----
            - mdb.models[*name*].parts[*name*].SurfaceByBoolean
            - mdb.models[*name*].rootAssembly.SurfaceByBoolean

        Parameters
        ----------
        name
            A String specifying the repository key. 
        surfaces
            A sequence of Surface objects. 
        operation
            A SymbolicConstant specifying the boolean operation to perform. Possible values are 
            UNION, INTERSECTION, andDIFFERENCE. The default value is UNION. Note that if DIFFERENCE 
            is specified, the order of the given input surfaces is important; All surfaces specified 
            after the first one are subtracted from the first one. 

        Returns
        -------
            A Surface object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def SurfaceFromElsets(self, name: str, elementSetSeq: tuple):
        """This method creates a surface from a sequence of element sets in a model database.

        Path
        ----
            - mdb.models[*name*].rootAssembly.SurfaceFromElsets

        Parameters
        ----------
        name
            A String specifying the repository key. 
        elementSetSeq
            A sequence of element sets. For example,`elementSetSeq=((elset1, S1),(elset2, S2))`where 
            `elset1=mdb.models[name].rootAssembly.sets['Clutch']` and `S1` and `S2` indicate the 
            side of the element set. 

        Returns
        -------
            A Surface object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

