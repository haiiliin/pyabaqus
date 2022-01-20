from abaqusConstants import *
from .TransverseShearBeam import TransverseShearBeam
from .TransverseShearShell import TransverseShearShell
from ..Connector.ConnectorBehaviorOptionArray import ConnectorBehaviorOptionArray


class SectionBase:
    """The Section object defines the properties of a section. The Section object is the
    abstract base type for other Section objects. The Section object has no explicit 
    constructor. The methods and members of the Section object are common to all objects 
    derived from the Section. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name]
        - import odbSection
        - session.odbs[name].sections[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A ConnectorBehaviorOptionArray object.
    behaviorOptions: ConnectorBehaviorOptionArray = ConnectorBehaviorOptionArray()

    # A String specifying the repository key. 
    name: str = ''

    # A TransverseShearBeam object.
    beamTransverseShear: TransverseShearBeam = TransverseShearBeam(ANALYSIS_DEFAULT)

    # A TransverseShearShell object.
    transverseShear: TransverseShearShell = TransverseShearShell(0, 0, 0)

    def sectionsFromOdb(self, fileName: str):
        """This method creates Section objects by reading an output database. The new sections are
        placed in the sections repository.

        Path
        ----
            - mdb.models[*name*].sectionsFromOdb

        Parameters
        ----------
        fileName
            A String specifying the name of the output database file (including the .odb extension) 
            to be read. This String can also be the full path to the output database file if it is 
            located in another directory. 

        Returns
        -------
            A list of Section objects. 

        Exceptions
        ----------
            None. 
        """
        pass
