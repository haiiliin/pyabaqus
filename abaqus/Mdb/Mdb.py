from ..Adaptivity.AdaptivityProcess import AdaptivityProcess
from ..Annotation.Annotation import Annotation
from ..CustomKernel.RepositorySupport import RepositorySupport
from ..EditMesh.MeshEditOptions import MeshEditOptions
from ..Job.Coexecution import Coexecution
from ..Job.Job import Job
from ..Job.OptimizationProcess import OptimizationProcess
from ..Model.Model import Model
from ..UtilityAndView.Repository import Repository
from abaqusConstants import *

class Mdb:

    """The Mdb object is the high-level Abaqus model database. A model database stores models 
    and analysis controls. 

    Access
    ------
        - mdb

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the release number of the Mdb object in memory. 
    version: int = None

    # A Float specifying the value of a counter associated with the Mdb object. The counter 
    # indicates when the Mdb object was last changed. 
    lastChangedCount: float = None

    # A repository of Job objects. 
    jobs: Repository[str, Job] = None

    # A repository of AdaptivityProcess objects. 
    adaptivityProcesses: Repository[str, AdaptivityProcess] = None

    # A repository of Coexecution objects. 
    coexecutions: Repository[str, Coexecution] = None

    # A repository of OptimizationProcess objects. 
    optimizationProcesses: Repository[str, OptimizationProcess] = None

    # A MeshEditOptions object specifying the undo/redo behavior when editing meshes on parts 
    # or part instances. 
    meshEditOptions: MeshEditOptions = None

    # A repository of Model objects. 
    models: Repository[str, Model] = None

    # A RepositorySupport object. 
    customData: RepositorySupport = None

    # A repository of Annotation objects. 
    annotations: Repository[str, Annotation] = None

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
            A Mdb object. 

        Exceptions
        ----------
            None. 
        """
        pass

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
            A Mdb object. 

        Exceptions
        ----------
            None. 
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

        Exceptions
        ----------
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

    def openAcis(self, fileName: str, scaleFromFile: Boolean = OFF):
        """This method creates an AcisFile object from a file containing ACIS-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        Path
        ----
            - openAcis

        Parameters
        ----------
        fileName
            A String specifying the path to the ACIS file to open. 
        scaleFromFile
            A Boolean specifying whether to scale, rotate, and translate the part using the 
            transform read from the ACIS file. The default value is OFF. 

        Returns
        -------
            An AcisFile object. 

        Exceptions
        ----------
            - File is from a newer version of ACIS than the CAE kernel. 
              Texterror: ACIS File version exceeds Kernel. 
            - The data in the ACIS file are corrupted. 
              Texterror: Failed to read ACIS file. 
        """
        pass

    def openCatia(self, fileName: str, topology: SymbolicConstant = SOLID, convertUnits: SymbolicConstant = OFF, 
                  combineBodies: Boolean = OFF):
        """This method creates an AcisFile object from a file containing CATIA V5–format geometry.
        This object is subsequently used by the PartFromGeometryFile method.

        Path
        ----
            - openCatia

        Parameters
        ----------
        fileName
            A String specifying the path to the CATIA file to open. 
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of 
            the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, 
            Abaqus/CAE attempts to attach cells to create a solid. If *topology*=SHELL, Abaqus/CAE 
            builds the body as a shell entity and not as a solid entity. The default value is SOLID. 
        convertUnits
            A SymbolicConstant specifying whether the original units should be retained. Possible 
            values are ON and OFF. The default value is OFF. 
        combineBodies
            A Boolean specifying whether to combine the bodies in the CATPart file. If the bodies to 
            be combined touch or overlap, invalid entities would result. For CATProduct files, this 
            option will be ignored. 

        Returns
        -------
            An AcisFile object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def openEnf(self, fileName: str, fileType: str, topology: SymbolicConstant = SOLID, 
                convertUnits: Boolean = OFF):
        """This method creates anAcisFile object from a file containing Elysium Neutral File-format
        geometry that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object is
        subsequently used by the PartFromGeometryFile method.

        Path
        ----
            - openEnf

        Parameters
        ----------
        fileName
            A String specifying the path to the Elysium Neutral File that was created by I-DEAS, 
            Pro/ENGINEER, or CATIA V5. 
        fileType
            A String specifying the type of CAD system that created the file. Possible values are 
            “ideas”, “proe”, or “catiav5”. 
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of 
            the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, 
            Abaqus/CAE attempts to attach cells to create a solid. If *topology*=SHELL, Abaqus/CAE 
            builds the body as a shell entity and not as a solid entity. The default value is SOLID. 
        convertUnits
            A Boolean specifying if the dimensions of the part should be converted to millimeters. 
            The default value is OFF. 

        Returns
        -------
            An AcisFile object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def openIges(self, fileName: str, trimCurve: SymbolicConstant = DEFAULT, 
                 scaleFromFile: SymbolicConstant = OFF, msbo: Boolean = False, 
                 includedLayers: tuple = (), topology: SymbolicConstant = SOLID, 
                 uniteWires: SymbolicConstant = ON):
        """This method creates an AcisFile object from a file containing IGES-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        Path
        ----
            - openIges

        Parameters
        ----------
        fileName
            A String specifying the path to the IGES file to open. 
        trimCurve
            A SymbolicConstant specifying the method used to define the trim curves that bound 
            parametric surfaces. Possible values are:DEFAULT, use either of the following as 
            specified by the contents of the IGES file.PARAMETRIC_DATA, use the parameter space of 
            the surface being trimmed.THREED_DATA, use real space—the coordinate system of the part 
            along with an indication that the trim curve lies on the parametric surface.The default 
            value is DEFAULT. 
        scaleFromFile
            A SymbolicConstant specifying whether the imported geometry needs to be scaled using the 
            units information available in the IGES file. Possible values are ON and OFF. The 
            default value is OFF. When the argument is set to ON, the geometry is scaled to 
            millimeters with respect to the unit system specified in the IGES file. 
        msbo
            A Boolean specifying if the IGES file contains MSBO (Manifold Solid B-Rep Object) 
            entities. The default value is False. 
        includedLayers
            A sequence of Ints specifying the levels or layers of entities that will be translated 
            from the IGES file to build the part. The default is to include all the layers. 
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of 
            the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, 
            Abaqus/CAE attempts to attach cells to create a solid. If *topology*=SHELL, Abaqus/CAE 
            builds the body as a shell entity and not as a solid entity. The default value is SOLID. 
        uniteWires
            A SymbolicConstant specifying whether the imported wires need to be united or not. 
            Possible values are ON andOFF. The default value is ON. When importing a sketch, this 
            value is set to OFF. 

        Returns
        -------
            An AcisFile object. 

        Exceptions
        ----------
            - The data in the IGES file are corrupted. 
              Texterror: Failed to read IGES file. 
        """
        pass

    def openParasolid(self, fileName: str, topology: SymbolicConstant = SOLID):
        """This method creates anAcisFile object from a file containing Parasolid-format geometry.
        This object is subsequently used by the PartFromGeometryFile method.

        Path
        ----
            - openParasolid

        Parameters
        ----------
        fileName
            A String specifying the path to the Parasolid file to open. 
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of 
            the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, 
            Abaqus/CAE attempts to attach cells to create a solid. If *topology*=SHELL, Abaqus/CAE 
            builds the body as a shell entity and not as a solid entity. The default value is SOLID. 

        Returns
        -------
            An AcisFile object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def openStep(self, fileName: str, scale: float = 1):
        """This method creates an AcisFile object from a file containing STEP-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        Path
        ----
            - openStep

        Parameters
        ----------
        fileName
            A String specifying the path to the STEP file to open. 
        scale
            A Float specifying the scaling factor to apply to the imported geometric entities. The 
            default value is 1.0. 

        Returns
        -------
            An AcisFile object. 

        Exceptions
        ----------
            - The data in the STEP file are corrupted. 
              Texterror: Failed to read STEP file. 
        """
        pass

    def openVda(self, fileName: str):
        """This method creates an AcisFile object from a file containing VDA-FS-format geometry.
        This object is subsequently used by the PartFromGeometryFile method.

        Path
        ----
            - openVda

        Parameters
        ----------
        fileName
            A String specifying the path to the VDA-FS file to open. 

        Returns
        -------
            An AcisFile object. 

        Exceptions
        ----------
            - The data in the VDA-FS file are corrupted. 
              Texterror: Failed to read VDA file. 
        """
        pass

    def openSolidworks(self, fileName: str, topology: SymbolicConstant = SOLID):
        """This method creates an AcisFile object from a file containing Solidworks format
        geometry. This object is subsequently used by the PartFromGeometryFile method.

        Path
        ----
            - openSolidworks

        Parameters
        ----------
        fileName
            A String specifying the path to the Solidworks file to open. 
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of 
            the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, 
            Abaqus/CAE attempts to attach cells to create a solid entity. If *topology*=SHELL, 
            Abaqus/CAE builds the body as a shell entity, not as a solid entity. The default value 
            is SOLID. 

        Returns
        -------
            An AcisFile object. 

        Exceptions
        ----------
            - The data in the Solidworks file are corrupted. 
              Texterror: Failed to read Solidworks file. 
        """
        pass

    def close(self):
        """This method closes an open Mdb object but does not save the Mdb object to disk. After
        closing the Mdb object, this method creates a new unnamed empty Mdb object.

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

    def save(self):
        """This method saves an Mdb object to disk at the location specified by *pathName*
        (*pathName* is a member of the Mdb object).

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
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

        Returns
        -------
            None. 

        Exceptions
        ----------
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

        Returns
        -------
            None. 

        Exceptions
        ----------
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

        Exceptions
        ----------
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

        Exceptions
        ----------
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

        Returns
        -------
            None. 

        Exceptions
        ----------
            - If the auxiliary Mdb was not opened earlier. 
              MdbError: The auxiliary Mdb was not opened. 
            - If the model fromName does not exist in the auxiliary Mdb. 
              KeyError: fromName does not exist. 
        """
        pass

