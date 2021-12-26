from abaqusConstants import *
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.VertexArray import VertexArray
from ..Datum.Datum import Datum
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshNodeArray import MeshNodeArray
from ..Model.Model import Model
from ..Region.Set import Set
from ..Region.Surface import Surface
from ..UtilityAndView.Repository import Repository


class ModelInstance:

    """A ModelInstance object is an instance of a Model. 

    Access
    ------
        - import assembly
        - mdb.models[name].rootAssembly.modelInstances[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A repository of Set objects specifying the sets created on the assembly. For more 
    # information, see [Region 
    # commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all). 
    sets: Repository[str, Set] = None

    # A repository of Surface objects specifying the surfaces created on the assembly. For 
    # more information, see [Region 
    # commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all). 
    surfaces: Repository[str, Surface] = None

    # A VertexArray object. 
    vertices: VertexArray = None

    # An EdgeArray object. 
    edges: EdgeArray = None

    # A MeshElementArray object. 
    elements: MeshElementArray = None

    # A MeshNodeArray object. 
    nodes: MeshNodeArray = None

    # A repository of Datum objects. 
    datums: Repository[str, Datum] = None

    # A repository of ReferencePoint objects. 
    referencePoints: Repository[str, ReferencePoint] = None

    def Instance(self, name: str, model: Model, autoOffset: Boolean = OFF):
        """This method creates a ModelInstance object and puts it into the instances repository.

        Path
        ----
            - mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            The repository key. The name must be a valid Abaqus object name. 
        model
            A Model object to be instanced. If the model does not exist, no ModelInstance object is 
            created. 
        autoOffset
            A Boolean specifying whether to apply an auto offset to the new instance that will 
            offset it from existing instances. The default value is OFF. 

        Returns
        -------
            A ModelInstance object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def ConvertConstraints(self):
        """This method converts the position constraints of an instance to absolute positions. The
        method deletes the constraint features on the instance but preserves the position in
        space.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getPosition(self):
        """This method prints the sum of the translations and rotations applied to the
        ModelInstance object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def replace(self, instanceOf: Model, applyConstraints: Boolean = True):
        """This method replaces one instance with an instance of another model.

        Parameters
        ----------
        instanceOf
            A Model object to be instanced. If the model does not exist, no ModelInstance object is 
            created. 
        applyConstraints
            A Boolean specifying whether to apply existing constraints on the new instance or to 
            position the new instance in the same place as the original instance. The default value 
            is True. A value of False indicates that constraints applies to the instance are deleted 
            will be deleted from the feature list. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def translate(self, vector: tuple):
        """This method translates an instance by the specified amount.

        Parameters
        ----------
        vector
            A sequence of three Floats specifying a translation vector. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

