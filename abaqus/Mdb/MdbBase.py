from ..Adaptivity.AdaptivityProcess import AdaptivityProcess
from ..Annotation.Annotation import Annotation
from ..CustomKernel.RepositorySupport import RepositorySupport
from ..EditMesh.MeshEditOptions import MeshEditOptions
from ..Job.Coexecution import Coexecution
from ..Job.Job import Job
from ..Job.OptimizationProcess import OptimizationProcess
from ..Model.Model import Model


class MdbBase:
    """The Mdb object is the high-level Abaqus model database. A model database stores models
    and analysis controls. 

    Notes
    -----
        This object can be accessed by:
        - mdb

    """

    # An Int specifying the release number of the Mdb object in memory. 
    version: int = None

    # A Float specifying the value of a counter associated with the Mdb object. The counter 
    # indicates when the Mdb object was last changed. 
    lastChangedCount: float = None

    # A repository of Job objects. 
    jobs: dict[str, Job] = dict[str, Job]()

    # A repository of AdaptivityProcess objects. 
    adaptivityProcesses: dict[str, AdaptivityProcess] = dict[str, AdaptivityProcess]()

    # A repository of Coexecution objects. 
    coexecutions: dict[str, Coexecution] = dict[str, Coexecution]()

    # A repository of OptimizationProcess objects. 
    optimizationProcesses: dict[str, OptimizationProcess] = dict[str, OptimizationProcess]()

    # A MeshEditOptions object specifying the undo/redo behavior when editing meshes on parts 
    # or part instances. 
    meshEditOptions: MeshEditOptions = MeshEditOptions()

    # A repository of Model objects. 
    models: dict[str, Model] = dict[str, Model]()

    # A RepositorySupport object. 
    customData: RepositorySupport = RepositorySupport()

    # A repository of Annotation objects. 
    annotations: dict[str, Annotation] = dict[str, Annotation]()

    def __init__(self, pathName: str = ''):
        """This constructor creates an empty Mdb object.

        Path
        ----
            - Mdb

        Parameters
        ----------
        pathName
            A String specifying the path to be used when the model database is saved to a file. If 
            you do not provide a file extension, .cae is appended automatically to the path. The 
            default value is an empty string. 

        Returns
        -------
            A Mdb object. . 
        """
        self.pathName = pathName
        self.models['Model-1'] = Model('Model-1')
        self.models['Model-1'].FieldOutputRequest('F-Output-1', 'Initial')

    def importDxf(self, fileName: str):
        """This method creates a ConstrainedSketch object from a file containing dxf-format
        (AutoCAD) geometry. Only a limited number of entities are supported. This format should
        be used only if no other formats are available.

        Path
        ----
            - importDxf

        Parameters
        ----------
        fileName
            A String specifying the path to the dxf file to open. 

        Returns
        -------
            A Mdb object. . 
        """
        pass

    def openMdb(self, pathName: str):
        """This method opens an existing model database file.

        Path
        ----
            - openMdb

        Parameters
        ----------
        pathName
            A String specifying the path to the model database file to open. If you do not provide a 
            file extension, Abaqus/CAE attempts to open the file with .cae appended to the path. 

        Returns
        -------
            An Mdb object. 

        Raises
        ------
            - If the file is an invalid model database: 
              MdbError: invalid model database. 
            - If the file contains a model database from an Abaqus release other than the Abaqus 
            release you are currently running: 
              MdbError: incompatible release number, expected *<Abaqus release>*, got *<earlier or 
            later Abaqus release>* 
            - If the model database file is already opened in write mode: 
              MdbError: cannot open file: May be in use by another CAE session 
            - If the command fails to open the model database file for reasons not mentioned above: 
              MdbError: cannot open file... 
        """
        pass

    def close(self):
        """This method closes an open Mdb object but does not save the Mdb object to disk. After
        closing the Mdb object, this method creates a new unnamed empty Mdb object.

        Parameters
        ----------
        """
        pass

    def save(self):
        """This method saves an Mdb object to disk at the location specified by *pathName*
        (*pathName* is a member of the Mdb object).

        Parameters
        ----------

        Returns
        -------
            None. 

        Raises
        ------
            - If *pathName* is empty: 
              MdbError: cannot save file: pathname member is empty 
            - If *pathName* is abaqus.cae: 
              MdbError: “abaqus.cae” is an invalid CAE filename. 
            - If the command fails to save the Mdb object to disk for reasons not mentioned above: 
              MdbError: cannot save file... 
        """
        pass

    def saveAs(self, pathName: str):
        """This method saves an Mdb object to disk at the specified location.

        Parameters
        ----------
        pathName
            A String specifying the path to be used when the model database is saved to a file. If 
            you do not provide a file extension, .cae is appended automatically to the path.

        Raises
        ------
            - If *pathName* is abaqus.cae: 
              MdbError: “abaqus.cae” is an invalid CAE filename. 
            - If the command fails to save the Mdb object to disk for reasons not mentioned above: 
              MdbError: cannot save file... 
        """
        pass

    def openAuxMdb(self, pathName: str):
        """This method opens an auxiliary Mdb object on the disk at the specified location. This
        enables models from the auxiliary Mdb object to be copied into the current Mdb.

        Parameters
        ----------
        pathName
            A String specifying the path to the auxiliary Mdb which is to be opened. If you do not 
            provide a file extension, .cae is appended automatically to the path.

        Raises
        ------
            - If the file is an invalid model database: 
              MdbError: invalid model database. 
            - If the file contains a model database from an Abaqus release other than the Abaqus 
            release you are currently running: 
              MdbError: incompatible release number, expected *<Abaqus release>*, got *<earlier or 
            later Abaqus release>*. 
            - If the command fails to open the model database file for reasons not mentioned above: 
              MdbError: cannot open file... 
        """
        pass

    def closeAuxMdb(self):
        """This method closes the auxiliary Mdb which had been opened earlier using the openAuxMdb
        command.

        Parameters
        ----------

        Returns
        -------
            None. 

        Raises
        ------
            - If the auxiliary Mdb was not opened earlier. 
              MdbError: The auxiliary Mdb was not opened.. 
        """
        pass

    def getAuxMdbModelNames(self):
        """This method returns a list of model names present in the auxiliary Mdb which had been
        opened earlier using the openAuxMdb command.

        Parameters
        ----------

        Returns
        -------
            A list of model names present in the auxiliaryMdb 

        Raises
        ------
            - If the auxiliary Mdb was not opened earlier. 
              MdbError: The auxiliary Mdb was not opened.. 
        """
        pass

    def copyAuxMdbModel(self, fromName: str, toName: str = ''):
        """This method copies a specified model from the auxiliary Mdb which had been opened
        earlier using the openAuxMdb command.

        Parameters
        ----------
        fromName
            A String specifying the model name in the auxiliary Mdb which is to be copied. 
        toName
            A String specifying the name to be given to the model after it is copied into the Mdb. 
            If this argument is not specified *toName* is assumed to be the same as *fromName*. If a 
            model with name *toName* already exists in Mdb, it is overwritten.

        Raises
        ------
            - If the auxiliary Mdb was not opened earlier. 
              MdbError: The auxiliary Mdb was not opened. 
            - If the model fromName does not exist in the auxiliary Mdb. 
              KeyError: fromName does not exist. 
        """
        pass
