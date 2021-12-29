from abaqusConstants import *
from ..Job.ModelJob import ModelJob
from .MdbBase import MdbBase
from ..Model.Model import Model


class Mdb(MdbBase):

    def Model(self, name: str, description: str = '', stefanBoltzmann: float = None,
              absoluteZero: float = None, waveFormulation: SymbolicConstant = NOT_SET,
              modelType: SymbolicConstant = STANDARD_EXPLICIT, universalGas: float = None,
              copyConstraints: Boolean = ON, copyConnectors: Boolean = ON,
              copyInteractions: Boolean = ON) -> Model:
        """This method creates a Model object.

        Path
        ----
            - mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        description
            A String specifying the purpose and contents of the Model object. The default value is
            an empty string.
        stefanBoltzmann
            None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
        absoluteZero
            None or a Float specifying the absolute zero constant. The default value is None.
        waveFormulation
            A SymbolicConstant specifying the type of incident wave formulation to be used in
            acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
            is NOT_SET.
        modelType
            A SymbolicConstant specifying the analysis model type. Possible values are
            STANDARD_EXPLICIT and ELECTROMAGNETIC. The default is STANDARD_EXPLICIT.
        universalGas
            None or a Float specifying the universal gas constant. The default value is None.
        copyConstraints
            A boolean specifying whether to copy the constraints created in the model to the model
            that instances this model. The default value is ON.
        copyConnectors
            A boolean specifying whether to copy the connectors created in the model to the model
            that instances this model. The default value is ON.
        copyInteractions
            A boolean specifying whether to copy the interactions created in the model to the model
            that instances this model. The default value is ON.

        Returns
        -------
            A Model object.

        Exceptions
        ----------
            None.
        """
        self.models[name] = model = Model(name, description, stefanBoltzmann, absoluteZero, waveFormulation, modelType,
                                          universalGas, copyConstraints, copyConnectors, copyInteractions)
        return model

    def Job(self, name: str, model: str, description: str = '', type: SymbolicConstant = ANALYSIS,
            queue: str = '', waitHours: int = 0, waitMinutes: int = 0, atTime: str = '',
            echoPrint: Boolean = OFF, contactPrint: Boolean = OFF, modelPrint: Boolean = OFF,
            historyPrint: Boolean = OFF, scratch: str = '', userSubroutine: str = '',
            numCpus: int = 1, memory: int = 90, memoryUnits: SymbolicConstant = PERCENTAGE,
            explicitPrecision: SymbolicConstant = SINGLE,
            nodalOutputPrecision: SymbolicConstant = SINGLE,
            parallelizationMethodExplicit: SymbolicConstant = DOMAIN, numDomains: int = 1,
            activateLoadBalancing: Boolean = OFF, multiprocessingMode: SymbolicConstant = DEFAULT,
            licenseType: SymbolicConstant = DEFAULT, *args, **kwargs) -> ModelJob:
        """This method creates an analysis job using a model on a model database (MDB) for the
        model definition.

        Path
        ----
            - mdb.Job

        Parameters
        ----------
        name
            A String specifying the name of the new job. The name must be a valid Abaqus/CAE object
            name.
        model
            A String specifying the name of the model to be analyzed or a Model object specifying
            the model to be analyzed.
        description
            A String specifying a description of the job.
        type
            A SymbolicConstant specifying the type of job. Possible values are ANALYSIS,
            SYNTAXCHECK, RECOVER, and RESTART. The default value is ANALYSIS.If the object has the
            type JobFromInputFile, *type*=RESTART is not available.
        queue
            A String specifying the name of the queue to which to submit the job. The default value
            is an empty string.Note:You can use the *queue* argument when creating a Job object on a
            Windows workstation; however, remote queues are available only on Linux platforms.
        waitHours
            An Int specifying the number of hours to wait before submitting the job. This argument
            is ignored if *queue* is set. The default value is 0.This argument works in conjunction
            with *waitMinutes*. *waitHours* and *atTime* are mutually exclusive.
        waitMinutes
            An Int specifying the number of minutes to wait before submitting the job. This argument
            is ignored if *queue* is set. The default value is 0.This argument works in conjunction
            with *waitHours*. *waitMinutes* and *atTime* are mutually exclusive.
        atTime
            A String specifying the time at which to submit the job. If *queue* is empty, the string
            syntax must be valid for the Linux `at` command. If *queue* is set, the syntax must be
            valid according to the system administrator. The default value is an empty
            string.Note:You can use the *atTime* argument when creating a Job object on a Windows
            workstation; however, the `at` command is available only on Linux platforms.
        echoPrint
            A Boolean specifying whether an echo of the input data is printed. The default value is
            OFF.
        contactPrint
            A Boolean specifying whether contact constraint data are printed. The default value is
            OFF.
        modelPrint
            A Boolean specifying whether model definition data are printed. The default value is
            OFF.
        historyPrint
            A Boolean specifying whether history data are printed. The default value is OFF.
        scratch
            A String specifying the location of the scratch directory. The default value is an empty
            string.
        userSubroutine
            A String specifying the file containing the user's subroutine definitions. The default
            value is an empty string.
        numCpus
            An Int specifying the number of CPUs to use for this analysis if parallel processing is
            available. Possible values are *numCpus* >> 0. The default value is 1.
        memory
            An Int specifying the amount of memory available to Abaqus analysis. The value should be
            expressed in the units supplied in *memoryUnits*. The default value is 90.
        memoryUnits
            A SymbolicConstant specifying the units for the amount of memory used in an Abaqus
            analysis. Possible values are PERCENTAGE, MEGA_BYTES, and GIGA_BYTES. The default value
            is PERCENTAGE.
        explicitPrecision
            A SymbolicConstant specifying whether to use the double precision version of
            Abaqus/Explicit. Possible values are SINGLE, FORCE_SINGLE, DOUBLE,
            DOUBLE_CONSTRAINT_ONLY, and DOUBLE_PLUS_PACK. The default value is SINGLE.
        nodalOutputPrecision
            A SymbolicConstant specifying the precision of the nodal output written to the output
            database. Possible values are SINGLE and FULL. The default value is SINGLE.
        parallelizationMethodExplicit
            A SymbolicConstant specifying the parallelization method for Abaqus/Explicit. This value
            is ignored for Abaqus/Standard. Possible values are DOMAIN and LOOP. The default value
            is DOMAIN.
        numDomains
            An Int specifying the number of domains for parallel execution in Abaqus/Explicit. When
            *parallelizationMethodExplicit*=DOMAIN, *numDomains* must be a multiple of *numCpus*.
            The default value is 1.
        activateLoadBalancing
            A Boolean specifying whether to activate dyanmic load balancing for jobs running on
            multiple processors with multiple domains in Abaqus/Explicit. The default value is OFF.
        multiprocessingMode
            A SymbolicConstant specifying whether an analysis is decomposed into threads or into
            multiple processes that communicate through a message passing interface (MPI). Possible
            values are DEFAULT, THREADS, and MPI. The default value is DEFAULT.
        licenseType
            A SymbolicConstant specifying the type of license type being used in the case of the
            DSLS SimUnit license model. Possible values are DEFAULT, TOKEN, and CREDIT. The default
            value is DEFAULT.If the license model is not the DSLS SimUnit, the licenseType is not
            available.

        Returns
        -------
            A ModelJob object.

        Exceptions
        ----------
            AbaqusException.
        """
        self.jobs[name] = job = ModelJob(name, model, description, type, queue, waitHours, waitMinutes, atTime,
                                         echoPrint, contactPrint, modelPrint, historyPrint, scratch, userSubroutine,
                                         numCpus, memory, memoryUnits, explicitPrecision, nodalOutputPrecision,
                                         parallelizationMethodExplicit, numDomains, activateLoadBalancing,
                                         multiprocessingMode, licenseType, *args, **kwargs)
        return job
